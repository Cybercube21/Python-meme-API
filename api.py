#Imports
import os
import random
import threading
import inotify.adapters
from flask import Flask
from flask_restful import Resource, Api
from flask import render_template
from flask_bootstrap import Bootstrap

#Setting Flask's Static Folder 
app = Flask(__name__,
            static_url_path='', 
            static_folder='./',
            template_folder='templates/')
api = Api(app)

# Get a list of Filenames
file_list=os.listdir(r"memes/")

# Creating the adapter for updating the list of filenames
notify_adapter = inotify.adapters.Inotify()
notify_adapter.add_watch('memes/')

# Thread function
def watch_dir():
    global file_list
    for event in notify_adapter.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event

        # If new memes getting imported
        if (('IN_CLOSE_WRITE' in type_names or 'IN_MOVED_TO' in type_names) and filename != ''):
            file_list=os.listdir(r"memes/")
            print("New File added")

# Creating the thread
watch_thread = threading.Thread(target=watch_dir)
watch_thread.daemon = True
watch_thread.start()

# Using index.html as frontpage
@app.route("/")
def index():
    return render_template("index.html")

# Updates the count.txt
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

# /ping endpoint
class Ping(Resource):
    def get(self):
        update_counter()
        return {'respone': 'your mom','error': 'none','code': 200}

# /memes endpoint
class Memes(Resource):
    def get(self):
        update_counter()
        meme = random.choice(file_list)
        return {'url': 'https://api.cybercube21.de/memes/' + meme}, 200 

# Adding the Resources for flask
api.add_resource(Ping, '/ping')
api.add_resource(Memes, '/memes')

# Using Flask Bootstrap
Bootstrap(app)

# Endpoint for sharing memes in an embed
@app.route('/share/<string:meme>')
def meme(meme):
    fileExt = os.path.splitext(meme)[1]

    if(fileExt == ".webp"):
        meme_tag = '<img src="https://api.cybercube21.de/memes/' + meme + '" />'
        meta_tags = ['<meta property="twitter:card" content="summary_large_image">',
        '<meta property="twitter:title" content="memes.cybercube21.de">',
        '<meta property="twitter:image" content="https://api.cybercube21.de/memes/'+ meme + '">']

        return render_template("share.html", meme=meme, meme_tag=meme_tag, meta_tags=meta_tags)

    
    elif (fileExt == ".webm"):
        meme_tag = '<video src="https://api.cybercube21.de/memes/' + meme + '" controls playsInline />'
        meta_tags = ['<meta property="og:type" content="video">', 
        '<meta property="og:video" content="https://api.cybercube21.de/memes/' + meme + '">']

        return render_template("share.html", meme=meme, meme_tag=meme_tag, meta_tags=meta_tags)

    else:
        return render_template("share.html", meme=meme, meme_tag=meme_tag, meta_tags=meta_tags)

# Run flask
if __name__ == '__main__':
    app.run(port=6969)