# Discord Bot Command and Control

The project's purpose is for the complete remote control of a machine via Discord messages.
Currently running only on Linux machines.

## Requirements
Python +v3.x

## Installation
```bash
pip install -r requirements.txt
```

## Usage
#### Standalone
```bash
python3 run_bot.py
```

#### Run as a Service (change configs in discord_bot.service to your needs)
```bash
sudo cp discord_bot.service /etc/systemd/system/
sudo systemctl start discord_bot.service
sudo systemctl enable discord_bot.service
```

## Bot Commands
- ```help``` (Displays this menu)
- Any Linux command (Constrained to 2000 lines)
- ```ngrok <port> <protocol>``` (Starts tunnel)
- ```get ngrok``` (Shows all tunnels)
- ```delete ngrok``` (Deletes all tunnels)

## Reference
[https://www.gngrninja.com/code/2017/3/24/python-create-discord-bot-on-raspberry-pi](https://www.gngrninja.com/code/2017/3/24/python-create-discord-bot-on-raspberry-pi)
