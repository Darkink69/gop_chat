from flask import Flask, request, jsonify
import gop
import banana
import whisper

app = Flask(__name__)

@app.route('/')
def handle_request():
    name = request.args.get('name', default='qqqq')
    chat_id = request.args.get('id', default='0')
    item = request.args.get('item', default='')
    return 'ok'


@app.route('/123')
def test():
    prompt = request.args.get('prompt', default='')
    res = gop.get_gop(prompt)

    return res


@app.route('/456')
def get_banana():
    prompt = request.args.get('prompt', default='')
    res = banana.get_banana(prompt)

    return (res

@app.route('/whisper'))
def get_transcribe_whisper():
    audio = request.args.get('audio', default='')
    res = whisper.get_transcribe(audio)

    return res


if __name__ == '__main__':
    app.run(debug=True)