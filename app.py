from flask import Flask, request, jsonify, render_template
from flask_cors import CORS # <--- ADD THIS LINE
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)
# For a live website, change this to your PostgreSQL/MySQL cloud database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookstore.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    buy_price = db.Column(db.Float, nullable=False)
    hourly_rate = db.Column(db.Float, default=50.0)
    stock = db.Column(db.Integer, default=1)
    rating = db.Column(db.Float, default=0.0) # <--- NEW LINE

# Initialize Database
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

# --- This is the ONLY get_books route now, including the rating ---
@app.route('/api/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    output = []
    for book in books:
        output.append({
            'id': book.id, 'title': book.title, 'author': book.author,
            'category': book.category, 'buy_price': book.buy_price,
            'hourly_rate': book.hourly_rate, 'stock': book.stock,
            'rating': book.rating
        })
    return jsonify(output)

@app.route('/api/add_book', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Book(
        title=data['title'], author=data['author'], category=data['category'],
        buy_price=data['buy_price'], hourly_rate=data.get('hourly_rate', 50.0),
        stock=data.get('stock', 1)
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book added successfully!'})

@app.route('/api/transaction/<int:book_id>', methods=['POST'])
def handle_transaction(book_id):
    data = request.get_json()
    action = data.get('action') # 'buy' or 'rent'
    
    book = Book.query.get_or_404(book_id)
    
    if book.stock > 0:
        if action == 'buy':
            book.stock -= 1
            db.session.commit()
            return jsonify({'message': f'Successfully bought {book.title}! Stock updated.'})
        elif action == 'rent':
            hours = data.get('hours', 1)
            cost = hours * book.hourly_rate
            # Logic to track who rented it goes here
            return jsonify({'message': f'Rented {book.title} for {hours} hour(s). Total: {cost} Rs.'})
    
    return jsonify({'error': 'Book out of stock'}), 400
@app.route('/checkout/<int:book_id>/<action>')
def checkout(book_id, action):
    # Find the book in the database
    book = Book.query.get_or_404(book_id)
    
    # Determine the price
    if action == 'buy':
        price = book.buy_price
        action_text = "Buy"
    else:
        price = book.hourly_rate
        action_text = "Rent (1 Hour)"
        
    return render_template('checkout.html', book=book, action=action_text, price=price)
if __name__ == '__main__':
    app.run(debug=True)
