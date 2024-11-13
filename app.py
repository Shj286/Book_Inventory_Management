from flask import Flask, request, jsonify, render_template, redirect, url_for, send_file
from flask_sqlalchemy import SQLAlchemy
import csv
import io

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Model
class Inventory(db.Model):
    entry_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    publication_date = db.Column(db.String(10))  # Storing date as a string for simplicity
    isbn = db.Column(db.String(13), unique=True, nullable=False)

# Route to add a new book
@app.route('/add', methods=['POST'])
def add_book():
    data = request.form
    new_book = Inventory(
        title=data['title'],
        author=data['author'],
        genre=data['genre'],
        publication_date=data['publication_date'],
        isbn=data['isbn']
    )
    db.session.add(new_book)
    db.session.commit()
    return redirect(url_for('home'))

# Route to filter books
@app.route('/filter', methods=['GET'])
def filter_books():
    title = request.args.get('title', '')
    author = request.args.get('author', '')
    genre = request.args.get('genre', '')

    books = Inventory.query.filter(
        Inventory.title.contains(title),
        Inventory.author.contains(author),
        Inventory.genre.contains(genre)
    ).all()
    return render_template('frontend.html', books=books)

# Route to export books data
@app.route('/export', methods=['GET'])
def export_books():
    export_format = request.args.get('format', 'csv')
    books = Inventory.query.all()

    output = io.StringIO()
    if export_format == 'csv':
        writer = csv.writer(output)
        writer.writerow(['Entry ID', 'Title', 'Author', 'Genre', 'Publication Date', 'ISBN'])
        for book in books:
            writer.writerow([book.entry_id, book.title, book.author, book.genre, book.publication_date, book.isbn])
        output.seek(0)
        return send_file(io.BytesIO(output.getvalue().encode()), mimetype='text/csv', as_attachment=True, download_name='books.csv')

    return jsonify([book.to_dict() for book in books])

# Route to render the home page
@app.route('/')
def home():
    books = Inventory.query.all()
    return render_template('frontend.html', books=books)

if __name__ == '__main__':
    # Ensure the database tables are created within an application context
    with app.app_context():
        db.create_all()  # This will create the database tables
    app.run(debug=True)
