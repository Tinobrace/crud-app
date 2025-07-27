from flask import Flask, jsonify, request
from models import Item

app = Flask(__name__)

items = []

# 🎉 API Status Message - By Dreamfyre
print("\n🔥 CRUD-App API is Live! 🔥")
print("Powered by Dreamfyre 💻🚀")
print("Test your endpoints and let the coding magic happen!\n")

# Root route to confirm API is running
@app.route('/')
def home():
    return """
    <h1>🔥 CRUD-App API by Dreamfyre is Live! 🚀</h1>
    <p>Use the <code>/items</code> endpoint to interact.</p>
    """

@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    new_item = Item(id=len(items) + 1, name=data['name'])
    items.append(new_item)
    return jsonify(new_item.__dict__), 201

@app.route('/items', methods=['GET'])
def read_items():
    return jsonify([item.__dict__ for item in items]), 200

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    for item in items:
        if item.id == item_id:
            item.name = data['name']
            return jsonify(item.__dict__), 200
    return jsonify({'message': 'Item not found'}), 404

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item.id != item_id]
    return jsonify({'message': 'Item deleted'}), 204

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
