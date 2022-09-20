# text-to-speech-webpage
Uses Google cloud's Text-to-Speech client libraries to convert text to downloadable audio

## Steps to run the app locally 
Create a separate virtual environment to install the required dependencies (Read [this](https://docs.python.org/3/library/venv.html#creating-virtual-environments) for details)

Install the necessary dependencies using -
pip install -r requirements.txt

You will need an google cloud service account to authenticate your TTS API requests. Follow [this](https://codelabs.developers.google.com/codelabs/cloud-text-speech-python3#3) guide to create your credentials

Run the server using the following command -
python main.py

Access your website at -
http://localhost:8080/
