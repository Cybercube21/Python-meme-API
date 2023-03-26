
# Python meme API

In this repo i provide the code ~~hosted on [api.cybercube21.de](https://api.cybercube21.de).~~ This will be replaced by a backend written in Nuxt soon.

An API in Python i wrote as backend for [my meme website](https://github.com/Cybercube21/ReactJS-Frontend). It uses Flask to provide the Endpoints which are easily expandable. 
## Installation

Clone the repo and install the dependencies via the requerements.txt.

```shell
git clone https://github.com/Cybercube21/Python-meme-API
cd Python-meme-API/
pip3 install -r requirements.txt
```

To start, make sure you create a folder called "memes". Right now pictures has to be .webp's and videos .webm's.

Then you can just execute the api.py to start the API.

```shell
python3 ./api.py
```

You can change the Port its running on at the bottom of the api.py. The default port is 6969
## API Reference

#### Get a ping response

```
  GET /ping
```

| Type     | Description                |
| :------- | :------------------------- |
| `json` | Returns a response :o |

#### Get a URL to a random meme 

```
  GET /memes
```

| Type     | Description                |
| :------- | :------------------------- |
| `json` | Get a random URL for a meme stored on my Server |


Example Response:
```json
{"url": "https://api.cybercube21.de/memes/61-unknown.webp"}
```

## Contact 
Join my [Discord Server](https://discord.gg/4XYcD2Jk54) or DM me: Cybercube#0499


## License
[GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html)
