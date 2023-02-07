from flask import Flask, request, jsonify
from flask_cors import CORS
from time import strftime
import os

from lib.utils import transcribe_audio, is_extension_file_allowed
from lib.cohere import get_client
from lib.whisper import get_model
from lib.log import get_logger

ALLOW_CORS = os.getenv('CORS')
PORT = os.getenv('PORT') or 8080

app = Flask(__name__)
CORS(app, origins=[ALLOW_CORS])

@app.route('/api/status', methods=['GET'])
def status():
    return 'Everything is ok!'

@app.route('/api/summarize', methods=['POST'])
def summarize():
    try:
        file = request.files.get('audio', None)

        if file is None:
            return jsonify({
                "message": 'No audio file was included'
            }), 400

        if (not is_extension_file_allowed(file.filename)):
            return jsonify({
                "message": "{} has invalid extension. Extensions allowed are: ['.wav', '.mp3', '.mp4']".format(file.filename)
            }), 400

        text = transcribe_audio(file, model)
        summary = cohere_client.generate(prompt=text, max_tokens=200)

        return jsonify({
            "transcribe": text,
            "summary": summary.generations[0].text
        }), 200

    except Exception as err:
        print(err)
        return jsonify({ "message": "An error occurs when we try to summarize an audio."}), 500


@app.after_request
def after_request(response):
     timestamp = strftime('[%Y-%b-%d %H:%M]')
     logger.error('%s %s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status)
     return response

if __name__ == '__main__':
    from waitress import serve

    cohere_client = get_client()
    model = get_model()
    logger = get_logger()

    serve(app, host="0.0.0.0", port=PORT)
