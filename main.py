from pyrogram import Client, filters
from utils import get_response, post_response, update_response, delete_response
import json


app = Client("api_consumer_bot")


@app.on_message(
    filters.command(commands="get", prefixes=["!", "/", "#"], case_sensitive=False)
)
async def get_command(client, message):

    headers = ""

    params = ""

    if "headers=" in message.text and "params=" in message.text:
        dummy = message.text.split("headers=")[1].replace("'", '"')

        dummy = dummy.split("params=")

        headers = dummy[0]
        params = dummy[1]

        try:
            headers = json.loads(headers)
            params = json.loads(params)
        except:
            await message.reply_text(text="Incorrect Formatting")
            return

    elif "headers=" in message.text:
        headers = message.text.split("headers=")[1].replace("'", '"')
        try:
            headers = json.loads(headers)
        except:
            await message.reply_text(text="Incorrect `header` format")
            return

    elif "params=" in message.text:
        params = message.text.split("params=")[1].replace("'", '"')
        try:
            params = json.loads(params)
        except:
            await message.reply_text(text="Incorrect `params` format")
            return

    received_message = message.text.split()
    url_to_request = received_message[1]
    try:
        await message.reply_text(
            text=f"API GET RESPONSE:\n{get_response(url_to_request, headers, params)}",
            quote=True,
        )
    except:
        await message.reply_text(
            text=f"Failed to get response of requested URL", quote=True
        )


@app.on_message(
    filters.command(commands="post", prefixes=["!", "/", "#"], case_sensitive=False)
)
async def post_command(client, message):

    headers = ""

    data = ""

    if "headers=" in message.text and "data=" in message.text:
        dummy = message.text.split("headers=")[1].replace("'", '"')

        dummy = dummy.split("data=")

        headers = dummy[0]
        data = dummy[1]

        try:
            headers = json.loads(headers)
            data = json.loads(data)
        except:
            await message.reply_text(text="Incorrect Formatting")
            return

    elif "headers=" in message.text:
        headers = message.text.split("headers=")[1].replace("'", '"')
        try:
            headers = json.loads(headers)
        except:
            await message.reply_text(text="Incorrect `header` format")
            return

    elif "data=" in message.text:
        data = message.text.split("data=")[1].replace("'", '"')
        try:
            data = json.loads(data)
        except:
            await message.reply_text(text="Incorrect `data` format")
            return

    received_message = message.text.split()
    url_to_request = received_message[1]
    try:
        await message.reply_text(
            text=f"API GET RESPONSE:\n{post_response(url_to_request, headers, data)}",
            quote=True,
        )
    except:
        await message.reply_text(
            text=f"Failed to get response of requested URL", quote=True
        )


@app.on_message(
    filters.command(commands="put", prefixes=["!", "/", "#"], case_sensitive=False)
)
async def put_command(client, message):

    headers = ""

    data = ""

    if "headers=" in message.text and "data=" in message.text:
        dummy = message.text.split("headers=")[1].replace("'", '"')

        dummy = dummy.split("data=")

        headers = dummy[0]
        data = dummy[1]

        try:
            headers = json.loads(headers)
            data = json.loads(data)
        except:
            await message.reply_text(text="Incorrect Formatting")
            return

    elif "headers=" in message.text:
        headers = message.text.split("headers=")[1].replace("'", '"')
        try:
            headers = json.loads(headers)
        except:
            await message.reply_text(text="Incorrect `header` format")
            return

    elif "data=" in message.text:
        data = message.text.split("data=")[1].replace("'", '"')
        try:
            data = json.loads(data)
        except:
            await message.reply_text(text="Incorrect `data` format")
            return

    received_message = message.text.split()
    url_to_request = received_message[1]
    try:
        await message.reply_text(
            text=f"API GET RESPONSE:\n{update_response(url_to_request, headers, data)}",
            quote=True,
        )
    except:
        await message.reply_text(
            text=f"Failed to get response of requested URL", quote=True
        )


@app.on_message(
    filters.command(commands="delete", prefixes=["!", "/", "#"], case_sensitive=False)
)
async def delete_command(client, message):

    headers = ""

    if "headers=" in message.text:
        headers = message.text.split("headers=")[1].replace("'", '"')
        try:
            headers = json.loads(headers)
        except:
            await message.reply_text(text="Incorrect `header` format")
            return

    received_message = message.text.split()
    url_to_request = received_message[1]
    try:
        await message.reply_text(
            text=f"API GET RESPONSE:\n{delete_response(url_to_request, headers)}",
            quote=True,
        )
    except:
        await message.reply_text(
            text=f"Failed to get response of requested URL", quote=True
        )


app.run()
