
from flask import Flask, render_template
from flask_cors import CORS
from UnleashClient import UnleashClient
from pathlib import Path
import os

frontend_token = os.getenv("UNLEASH_FRONTEND_TOKEN", default='NOT_SET')
frontend_url = "https://eu.app.unleash-hosted.com/euii0016/api/frontend"

client_url = "https://eu.app.unleash-hosted.com/euii0016/api/"
client_token = os.getenv("UNLEASH_BACKEND_TOKEN", default='NOT_SET')

client = UnleashClient(
    url=client_url,
    app_name="poc-app",
    custom_headers={'Authorization': client_token},
    refresh_interval=10)

print(f"Connecting to  {client_url}")
client.initialize_client()

app = Flask(__name__, static_folder='static')

context = {
  "properties": {
    "email": "my@mail.com"
  }
}

@app.route("/")
def hello_world():
    if client.is_enabled("toggle-feature",context=context):
        ret= "<p>Feature is enabled!</p>"
    else:
        ret= "<p>Feature is not !enabled</p>"
    return ret

@app.route("/frontend")
def frontend():
    return render_template("index.html", email="my@mail.com", frontend_token=frontend_token, frontend_url=frontend_url)    


app.run(host='0.0.0.0', port=5000)