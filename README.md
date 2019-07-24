# HLavalink
Lavalink on heroku, in a nutshell

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/F4stZ4p/HLavalink)

## If you want to run this:

### Easy Install
- [x] Click the button "Deploy to Heroku" above to install

### The hard way
- [x] Create an application on Heroku
- [x] Add Java to buildpacks
- [x] Fork this repo and deploy it to Heroku

## Important notes:
- [x] To run this 24/7, you need to make an account on UptimeRobot service, and make HTTP request to your app every 5 minutes. For example, if your app is named `test-lavalink` then make HTTP request to `http://test-lavalink.herokuapp.com`
- [x] Do not forget to edit config file (application.yml)

# Connecting
- [x] Lavalink's port will be always 80, DO NOT edit port in application.yml!

## Examples (Python - wavelink)

```python
async def initiate_nodes(self):
    nodes = {"MAIN": 
        {
            "host": "test-lavalink.herokuapp.com",
            "port": 80,
            "rest_url": "http://test-lavalink.herokuapp.com",
            "password": "youshallnotpass",
            "identifier": "MAIN",
            "region": "europe"
        }
    }

    for n in nodes.values():
        # ...
```
