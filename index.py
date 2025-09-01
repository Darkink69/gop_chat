from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def handle_request():
    name = request.args.get('name', default='')
    chat_id = request.args.get('id', default='0')
    item = request.args.get('item', default='')
    return 'ok'


if __name__ == '__main__':
    app.run(debug=True)