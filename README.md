# IpGiverBot
created on arch linux

requirements: pythonTelegramBotAPI, python-dotenv, curl + uv


this script creates telegram bot that send ip of owner's machine to anyone who write to it with password and code phrase

Clone this repository, use uv sync
then rename .env.example file to .env and change values in it

after that start main.py script

and now bot in telegram can answer you, write him
"{phrase} {password}" if you placed zero on USEOWN in dotenv file
else write him "{phrase}",
then bot will use curl ifconfig.me on host machine and send you the output of command
