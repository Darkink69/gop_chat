from flask import Flask, request, jsonify
import gop

app = Flask(__name__)

@app.route('/')
def handle_request():
    name = request.args.get('name', default='qqqq')
    chat_id = request.args.get('id', default='0')
    item = request.args.get('item', default='')
    return 'ok'

@app.route('/123')
def test():
    res = gop.get_gop()

    return res


if __name__ == '__main__':
    app.run(debug=True)