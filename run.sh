#!/bin/bash

echo Lavalink on Heroku by F4stZ4p
echo Credit to diniboy for Lavalink init script. L14

echo Downloading latest release of Lavalink...
curl -s https://api.github.com/repos/Frederikam/Lavalink/releases/latest \
  | grep browser_download_url \
  | grep Lavalink \
  | cut -d '"' -f 4 \
  | wget -qi -
 
echo Starting Lavalink...
sed -i "s|2333|$PORT|" application.yml; java -jar Lavalink.jar
