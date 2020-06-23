# HLavalink

**Lavalink** on **Heroku**, in a nutshell

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/F4stZ4p/HLavalink)

## If you want to run this:

### Easy Install
- [x] Click the button "Deploy to Heroku" above to install

### The hard way
- [x] Create an application on Heroku
- [x] Add Java to buildpacks
- [x] Fork this repo and deploy it to Heroku

# Important notes:
- [x] To run this 24/7, you need to make an account on UptimeRobot service, and make HTTP request to your app every 5 minutes. For example, if your app is named `test-lavalink` then make HTTP request to `http://test-lavalink.herokuapp.com`
- [x] Do not forget to edit config file (application.yml)
- [x] Do not forget to set your password (`PASSWORD` environment variable)

# Advantages
- [x] Uses **latest** release of Lavalink on (re)start
- [x] Free to use
- [x] Easy setup in ***3 clicks***

# Connecting
- [x] Lavalink's port will be always 80, DO NOT edit port in application.yml!
- [x] Password is in `PASSWORD` environment variable, if variable does not exist, it is `youshallnotpass`

# Examples

## Python
### discord.py

- [x] **Wavelink** | **[Repo Link](https://github.com/EvieePy/Wavelink)**
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
- [x] **Lavalink.py** | **[Repo Link](https://github.com/Devoxin/Lavalink.py)**
```python
async def initiate_nodes(self):
    self.bot.lavalink = lavalink.Client(
        self.bot.user.id
    )
    
    self.bot.lavalink.add_node(
        "test-lavalink.herokuapp.com", 
        80, 
        "youshallnotpass", 
        "eu", 
        "default-node"
    )  # Host, Port, Password, Region, Name
    # ...
```

# Advanced
### If you don't like default Heroku options for Java:
- [x] You can set custom Java flags in `ADDITIONAL_JAVA_OPTIONS` variable. They **override** default config. **Do not** do this if you don't know what you're doing
- [x] You can opt out of using developer Lavalink version. To set this, you need to create `USE_DEV_LAVALINK` variable containing `n`, `no` or `0` value
