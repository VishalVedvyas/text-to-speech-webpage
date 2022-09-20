# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python38_app]
# [START gae_python3_app]
from flask import Flask, send_file, render_template, request, abort
from ttsclient import TTSClient
import os


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def home():
    """Return a friendly HTTP greeting."""
    return render_template("home.html");

@app.route('/getaudio', methods=['POST'])
def getAudio():
    if not request.json or not 'text' in request.json:
        return {"message": "invalid input format"}, 400

    obj = TTSClient(request.json['text'])
    
    obj.getAudio()
    #return send_file(obj.getAudio(), mimetype="audio/mpeg", attachment_filename="audio.mp3", as_attachment=True)
    path = f"/tmp/audio.mp3"
    if os.path.isfile(path):
        return send_file(path, mimetype="audio/mpeg", as_attachment=True)
    else:
        return {"message": "cannot get audio"}, 401

@app.route('/downloadaudio')
def downloadAudio():
    path = f"/tmp/audio.mp3"
    if os.path.isfile(path):
        return send_file(path, mimetype="audio/mpeg", as_attachment=True)
    else:
        return {"message": "cannot download file"}, 401

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python3_app]
# [END gae_python38_app]
