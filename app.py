from flask import Flask, request, jsonify
import sqlite3
from utils import generate_token, verify_token  
from models import create_tables  

app = Flask(__name__)

def require_auth(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")
        username = request.headers.get("Username")
        if not token or not username or not verify_token(token, username):
            return jsonify({"error": "Unauthorized"}), 401
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__  
    return wrapper


@app.route('/books', methods=['POST'])
@require_auth
def add_book():
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    published_date = data.get('published_date')

    if not title or not author:
        return jsonify({"error": "Title and author are required"}), 400

    connection = sqlite3.connect('library.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO books (title, author, published_date) VALUES (?, ?, ?)",
                   (title, author, published_date))
    connection.commit()
    connection.close()

    return jsonify({"message": "Book added successfully"}), 201

@app.route('/books', methods=['GET'])
@require_auth
def get_books():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 5))

    connection = sqlite3.connect('library.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    connection.close()

    start = (page - 1) * per_page
    end = start + per_page
    paginated_books = books[start:end]

    return jsonify({"books": [{"id": b[0], "title": b[1], "author": b[2], "published_date": b[3]} for b in paginated_books]}), 200


@app.route('/books/<int:book_id>', methods=['PUT'])
@require_auth
def update_book(book_id):
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    published_date = data.get('published_date')

    connection = sqlite3.connect('library.db')
    cursor = connection.cursor()
    cursor.execute("UPDATE books SET title = ?, author = ?, published_date = ? WHERE id = ?",
                   (title, author, published_date, book_id))
    connection.commit()
    connection.close()

    return jsonify({"message": "Book updated successfully"}), 200


@app.route('/books/<int:book_id>', methods=['DELETE'])
@require_auth
def delete_book(book_id):
    connection = sqlite3.connect('library.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    connection.commit()
    connection.close()

    return jsonify({"message": "Book deleted successfully"}), 200


@app.route('/books/search', methods=['GET'])
@require_auth
def search_books():
    query = request.args.get('query', '').lower()
    connection = sqlite3.connect('library.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books WHERE LOWER(title) LIKE ? OR LOWER(author) LIKE ?",
                   (f"%{query}%", f"%{query}%"))
    books = cursor.fetchall()
    connection.close()

    return jsonify({"books": [{"id": b[0], "title": b[1], "author": b[2], "published_date": b[3]} for b in books]}), 200


@app.route('/members', methods=['POST'])
@require_auth
def add_member():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({"error": "Name and email are required"}), 400

    connection = sqlite3.connect('library.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO members (name, email) VALUES (?, ?)", (name, email))
    connection.commit()
    connection.close()

    return jsonify({"message": "Member added successfully"}), 201


if __name__ == '__main__':
    create_tables()  
    app.run(debug=True)
