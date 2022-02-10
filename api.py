from flask import Flask
from flask_restful import Resource, Api
from flask import render_template
import os, random

app = Flask(__name__,
            static_url_path='', 
            static_folder='./',
            template_folder='templates/')
api = Api(app)
file_list=os.listdir(r"memes/")

@app.route("/")
def index():
    return render_template("index.html")

class Ping(Resource):
    def get(self):
        return {'respone': 'your mom','error': 'none','code': 200}


class Memes(Resource):
    def get(self):
        meme = random.choice(file_list)
        return {'url': 'https://api.cybercube21.de/memes/' + meme}, 200  # return data and 200 OK

api.add_resource(Ping, '/ping')
api.add_resource(Memes, '/memes')

if __name__ == '__main__':
    app.run(port=6969)