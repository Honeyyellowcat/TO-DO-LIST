#pip install Flask
from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    name = data.get('name')
    if name:
        new_task = {'name': name, 'completed': False}
        tasks.append(new_task)
        return jsonify(new_task), 201
    else:
        return jsonify({'error': 'Name is required'}), 400

@app.route('/tasks/<int:index>', methods=['PUT'])
def update_task(index):
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = not tasks[index]['completed']
        return jsonify(tasks[index])
    else:
        return jsonify({'error': 'Task index out of range'}), 404

@app.route('/tasks/<int:index>', methods=['DELETE'])
def delete_task(index):
    if 0 <= index < len(tasks):
        deleted_task = tasks.pop(index)
        return jsonify(deleted_task)
    else:
        return jsonify({'error': 'Task index out of range'}), 404

if __name__ == '__main__':
    app.run(debug=True)
