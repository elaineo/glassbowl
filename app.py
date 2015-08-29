# import MySQLdb as db
from flask import Flask, render_template, request
from query_tools import *
from query_api import *
import logging,logging.config, yaml
logging.config.dictConfig(yaml.load(open('logging.conf')))

app = Flask(__name__,  template_folder='client', static_folder='client/static')
import json

temp = {
  "links": [
    {"link": {
    "name": "Jay",
    "Title": "Software Engineer",
    "Company":"Google",
    "url": "https://www.linkedin.com/profile/view?id=ADEAAAauYmQBGwCTxbICPCV-k53MsxyYuaGiOyw"
  }},{"link": {
    "name": "Tang",
    "Title": "Software Developer",
    "Company":"Cisco",
    "url": "https://www.linkedin.com/profile/view?id=ADEAAAS-uHMBmmfUr8-urMQ0GGDu9odW3VYjK1w"
  }},
    {"link": {
    "name": "Ahmadreza",
    "Title": "Software Developer",
    "Company":"Wells Fargo",
    "url": "https://www.linkedin.com/profile/view?id=ADEAAA93W-MBpZgbhfh6gD2mcvbXZmVNZ9DurXs"
  }}
  ],
  "salary": "$13,500"
}

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
    # data = request.data
    # data = json.loads(data)
    # url = data.get('url')
    # logconsole.debug(url)
    # if url:
    #     return search_query(url)
    # else:
    #     return "error"
    return json.dumps(temp)

if __name__ == '__main__':
    logfile    = logging.getLogger('file')
    logconsole = logging.getLogger('console')
    logfile.debug("Debug FILE")
    logconsole.debug("Debug CONSOLE")
    app.run()
    # app.run(host='0.0.0.0')
