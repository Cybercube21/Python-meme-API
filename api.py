from email.errors import UndecodableBytesDefect
from flask import Flask
from flask_restful import Resource, Api
from flask import render_template
import os, random
import threading
import inotify.adapters

app = Flask(__name__,
            static_url_path='', 
            static_folder='./',
            template_folder='templates/')
api = Api(app)

file_list=os.listdir(r"memes/")

notify_adapter = inotify.adapters.Inotify()
notify_adapter.add_watch('memes/')

def watch_dir():
    global file_list
    for event in notify_adapter.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event
        print(type_names)

        if (('IN_CLOSE_WRITE' in type_names or 'IN_MOVED_TO' in type_names) and filename != ''):
            file_list=os.listdir(r"memes/")
            print("New File")


watch_thread = threading.Thread(target=watch_dir)
watch_thread.start()

@app.route("/")
def index():
    return render_template("index.html")

def update_counter():
    # Get Count & add 1
    f = open("count.txt", "r")
    api_calls_counter = (f.read())
    api_calls_counter = int(api_calls_counter) + 1
    lines = f.readlines()
    f.close()

    #Remove old count & write new count to file
    f = open("count.txt", "w")
    for line in lines:
        f.write(line)
    f.write(str(api_calls_counter)) 
    f.close()

class Ping(Resource):
    def get(self):
        update_counter()
        return {'respone': 'your mom','error': 'none','code': 200}

class Memes(Resource):
    def get(self):
        update_counter()
        meme = random.choice(file_list)
        return {'url': 'https://api.cybercube21.de/memes/' + meme}, 200  # return data and 200 OK

api.add_resource(Ping, '/ping')
api.add_resource(Memes, '/memes')

if __name__ == '__main__':
    app.run(port=6969)
    watch_thread.join()