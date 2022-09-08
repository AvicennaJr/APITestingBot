## API Testing Bot

A Telegram bot to help developers test API endpoints.

## Features

* `/get` to get data from an endpoint
* `/post` to post data into an endpoint
* `/put` to update data in an endpoint
* `/delete` to delete data from an endpoint
* Use `headers` to access endpoints
* Post `params` and other `data` into endpoints

## How To Use

### Getting Data

To `get` data from an endpoint use: `/get [url] headers={'key':'value'} params={'key':'value'}`

Headers **MUST** come before params. Also Note that there is no space between headers/params and `=`

Example:

```bash
/get https://v2.jokeapi.dev/joke/Dark headers={'Authorization': 'Token du832s-=kda'} params={'blacklistFlags':'nsfw'}
```
Or without headers:

```bash
/get https://v2.jokeapi.dev/joke/Dark params={'blacklistFlags':'nsfw'}
```

### Posting Data

To `post` data from an endpoint use: `/post [url] headers={'key':'value'} data={'key':'value'}`

Headers **MUST** come before data. Also Note that there is **NO SPACE** between headers/data and `=`

### Updating Data

To `update` data from an endpoint use: `/put [url] headers={'key':'value'} data={'key':'value'}`

Headers **MUST** come before data. Also Note that there is **NO SPACE** between headers/data and `=`

### Deleting Data

To `delete` data from an endpoint use: `/delete [url] headers={'key':'value'}`

Note that there is **NO SPACE** between headers and `=`

## Link To The Bot

Click [Here](http://t.me/APIConsumerBot) to use the bot or follow the instructions below to host your own bot.

## Installation

Make sure you have a vaild [Telegram API Key](https://my.telegram.org/apps) (api_id and api_hash pair)

Also create a Telegram bot with [Bot Father](https://t.me/botfather) and get the bot_token.

Install the requirements:
```python
pip install -r requirements.txt
```

On your first run, fill in your api_id, api_hash and the bot_token:
```
api_id = your-api-id
api_hash = "your-api-hash"
bot_token = "your-bot-token"

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

.........

app.run()
```
That's it. Use your bot to test your APIs.

*Note:* After a successful authorization, the API key (api_id and api_hash) and the bot_token are no longer required. Read the [Pyrogram](https://docs.pyrogram.org/start/auth.html) documentation for more information.

## License

Copyright (c) Non Existing XD