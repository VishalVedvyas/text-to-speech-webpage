from flask import Flask, send_file, render_template, request, abort
from ttsclient import TTSClient
import os

app = Flask(__name__)

#Render main web page
@app.route('/')
def home():
    return render_template("home.html");

#Query GCP text-to-speech service and serve the audio file
@app.route('/getaudio', methods=['POST'])
def getAudio():
    if not request.json or not 'text' in request.json:
        return {"message": "invalid input format"}, 400

    obj = TTSClient(request.json['text'])
    
    obj.getAudio()
    path = f"/tmp/audio.mp3"
    if os.path.isfile(path):
        return send_file(path, mimetype="audio/mpeg", as_attachment=True)
    else:
        return {"message": "cannot get audio"}, 401

#Return the saved audio files for downloads (Don't call the TTS service again)
@app.route('/downloadaudio')
def downloadAudio():
    path = f"/tmp/audio.mp3"
    if os.path.isfile(path):
        return send_file(path, mimetype="audio/mpeg", as_attachment=True)
    else:
        return {"message": "cannot download file"}, 401

if __name__ == '__main__':
    # This is used when running locally only. GCP uses Gunicorn
    app.run(host='127.0.0.1', port=8080, debug=True)
