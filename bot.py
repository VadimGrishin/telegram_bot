import requests
import json
from flask import Flask

TOKEN = '1037929495:AAGwTRA-l75ot23aBKml_B3kL0bn0SxhwMg'
MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'

app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    r = requests.get(f'{MAIN_URL}/getUpdates')

    return json.dumps(r.json(), ensure_ascii=False, indent=4)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]

#proxies = {'https': 'https://51.158.165.18:8811'} , proxies=proxies


