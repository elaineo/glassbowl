import MySQLdb as db
from flask import Flask, render_template
app = Flask(__name__,  template_folder='client', static_folder='client/static')


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

if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0')
