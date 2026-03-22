# 📚 The Digital Shelf — Online Bookstore (Short README)

## 📌 Overview

A full-stack **Flask-based web app** for browsing, buying, and renting books. It uses **SQLite** for storage and a dynamic frontend for displaying books.

---

## 🚀 Features

* View books with price, stock, and ratings ⭐
* Buy (reduces stock) or Rent (hourly cost)
* Checkout page with payment form
* REST API for book operations
* Responsive and animated UI

---

## 🛠️ Tech Stack

* **Backend:** Flask, SQLAlchemy, Flask-CORS
* **Database:** SQLite
* **Frontend:** HTML, CSS, JavaScript

---

## ▶️ Run Project

```bash
pip install flask flask-cors flask-sqlalchemy
python app.py
```

Open: `http://127.0.0.1:5000/`

---

## 🔌 API

* `GET /api/books` → Get all books
* `POST /api/add_book` → Add book
* `POST /api/transaction/<id>` → Buy/Rent

---

## 🔮 Future Scope

* Authentication
* Payment gateway
* Admin panel
* Search & filters

---

🚀 *A beginner-friendly full-stack project for learning Flask and web development.*
