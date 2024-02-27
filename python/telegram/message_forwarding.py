from telethon import TelegramClient, events
import asyncio

api_id = '' # str | get from telegram api
api_hash = '' # str | get from telegram api
to_chat_id = 0 # int | get from telegram

client = TelegramClient("forwarder", api_id, api_hash)
client.start()

message_pattern = '' # pattern with regex

@client.on(events.NewMessage(pattern=message_pattern))
async def my_event_handler(event):
    await client.forward_messages(to_chat_id, event.message)

asyncio.get_event_loop().run_forever()
