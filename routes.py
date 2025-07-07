from flask import Flask, request, jsonify
from models import Item

app = Flask(__name__)

items = []

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
    return jsonify({'error': 'Item not found'}), 404

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item.id != item_id]
    return jsonify({'result': 'Item deleted'}), 204

def set_routes(app):
    app.add_url_rule('/items', view_func=create_item, methods=['POST'])
    app.add_url_rule('/items', view_func=read_items, methods=['GET'])
    app.add_url_rule('/items/<int:item_id>', view_func=update_item, methods=['PUT'])
    app.add_url_rule('/items/<int:item_id>', view_func=delete_item, methods=['DELETE'])