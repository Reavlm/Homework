from flask import Flask, request, jsonify

app = Flask(__name__)

books = []

@app.route('/books', methods=['POST'])
def create_book():
    data = request.json
    book = {
        'id': len(books) + 1,
        'book_name': data['book_name'],
        'author': data['author'],
        'publisher': data['publisher']
    }
    books.append(book)
    return jsonify({'message': 'Book created', 'id': book['id']}), 201

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books), 200

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = next((b for b in books if b['id'] == id), None)
    return jsonify(book) if book else ('', 404)

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.json
    book = next((b for b in books if b['id'] == id), None)
    if book:
        book.update(data)
        return jsonify({'message': 'Book updated', 'id': id}), 200
    return ('', 404)

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = next((b for b in books if b['id'] == id), None)
    if book:
        books.remove(book)
        return ('', 204)
    return ('', 404)

if __name__ == '__main__':
    app.run(debug=True)