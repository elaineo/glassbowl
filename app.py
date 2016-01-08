from flask import Flask, render_template, request
from query_tools import *
from query_api import *
import logging,sys
from peer_puller import *


app = Flask(__name__,  template_folder='client', static_folder='client/static')
import json
app.config['FLASK_LOG_LEVEL'] = 'DEBUG'
logging.basicConfig(stream=sys.stderr)
app.logger.addHandler(logging.StreamHandler(stream=sys.stderr))

# mysql = MySQL()

# MySQL configurations
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = ''
# app.config['MYSQL_DATABASE_DB'] = 'glass'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# mysql.init_app(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    data = request.data
    try:
        data = json.loads(data)
    except:
        return json.dumps({'status': "error"})
    url = data.get('url')
    if url:
        r = search_query(url.strip())
        return json.dumps(r)
    else:
        return json.dumps({'status': "error"})
    
LI_ACCESS_URL = "https://www.linkedin.com/uas/oauth2/accessToken"



if __name__ == '__main__':
    app.run(threaded=True)
    # app.run(host='0.0.0.0')
