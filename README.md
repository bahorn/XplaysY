# XplaysY
It's like twitch plays x, but overkill. For adding interactity to online events.

## Architecture

### Frontend

User facing code, most logic to detect what each player does is here, connects to a backend websocket

### Backend

* This is the websocket server
* Stores user input in a redis db, with an expiry to remove stale commands.

### Collector

* Batch Queries the redis DB `HZ` times a second.
* Checks for new players every second, adding them to the query list.

### Game

You need a small script to pass the results from collector to whatever game you are playing by IPC.

## Security

Security model is #yolo. Nothing here to stop players from openning a ton of bot connections, etc.

Add that in if you need it, or just tell people to behave *bonk*.
