from app import app, db, Book

new_books = [
    {"title": "Sapiens: A Brief History of Humankind", "author": "Yuval Noah Harari", "rating": 4.3},
    {"title": "Educated: A Memoir", "author": "Tara Westover", "rating": 4.5},
    {"title": "Atomic Habits", "author": "James Clear", "rating": 4.3},
    {"title": "The Devil in the White City", "author": "Erik Larson", "rating": 4.0},
    {"title": "Becoming", "author": "Michelle Obama", "rating": 4.5},
    {"title": "The Tipping Point", "author": "Malcolm Gladwell", "rating": 4.0},
    {"title": "Quiet: The Power of Introverts", "author": "Susan Cain", "rating": 4.1},
    {"title": "The Immortal Life of Henrietta Lacks", "author": "Rebecca Skloot", "rating": 4.1},
    {"title": "Thinking, Fast and Slow", "author": "Daniel Kahneman", "rating": 4.2},
    {"title": "Just Mercy", "author": "Bryan Stevenson", "rating": 4.6},
    {"title": "The Emperor of All Maladies", "author": "Siddhartha Mukherjee", "rating": 4.3},
    {"title": "The Sixth Extinction", "author": "Elizabeth Kolbert", "rating": 4.1},
    {"title": "A Brief History of Time", "author": "Stephen Hawking", "rating": 4.2},
    {"title": "The Wager", "author": "David Grann", "rating": 4.3},
    {"title": "In Cold Blood", "author": "Truman Capote", "rating": 4.1}
]

with app.app_context():
    # 1. This completely drops the old tables (removes the outdated structure)
    db.drop_all()
    
    # 2. This recreates the tables with your NEW structure (including 'rating')
    db.create_all()
    
    # 3. Now we add the books
    for b in new_books:
        book = Book(
            title=b["title"],
            author=b["author"],
            category="Non-Fiction",
            buy_price=500.0,      
            hourly_rate=50.0,     
            stock=5,              
            rating=b["rating"]
        )
        db.session.add(book)
        
    db.session.commit()
    print(f"Successfully added {len(new_books)} books to the database!")