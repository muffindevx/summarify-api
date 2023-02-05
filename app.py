from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import whisper
import cohere

API_TRIAL_KEY = os.getenv('API_TRIAL_KEY')
ALLOW_CORS = os.getenv('CORS')
UPLOAD_EXTENSIONS = ['.mp3', '.mp4', '.wav']

app = Flask(__name__)
CORS(app, origins=[ALLOW_CORS])

# Allow to get model for transcribe audio with Whisper AI
model = whisper.load_model("base")
cohere_client = cohere.Client(API_TRIAL_KEY)

def transcribe_audio(file):
    file.save("audio")
    result = model.transcribe("audio", fp16=False, language='English')
    os.remove("audio")
    return result["text"]

def is_extension_file_allowed(name): 
    extension = os.path.splitext(name)[1]
    if (extension != '' and extension in UPLOAD_EXTENSIONS):
        return True
    return False

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

        text = transcribe_audio(file)
        summary = cohere_client.generate(prompt=text, max_tokens=200)

        return jsonify({
            "transcribe": text,
            "summary": summary.generations[0].text
        }), 200

    except Exception as err:
        print(err)
        return jsonify({ "message": "An error occurs when we try to summarize an audio."}), 500


if __name__ == '__main__':
    from waitress import serve
    print('Server running')
    serve(app, host="0.0.0.0", port=8080)
