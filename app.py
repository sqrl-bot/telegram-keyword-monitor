from telethon import TelegramClient
import os
from datetime import datetime, timedelta

api_id = int(os.environ['API_ID'])
api_hash = os.environ['API_HASH']
phone = os.environ['PHONE']

keywords = os.environ['KEYWORDS'].split(',')
chats = os.environ['CHATS'].split(',')

async def main():
    async with TelegramClient('session', api_id, api_hash) as client:
        yesterday = datetime.now() - timedelta(days=1)
        report = "📊 Daily Telegram Keyword Report\n\n"

        for chat in chats:
            async for message in client.iter_messages(chat, limit=200):
                if message.date > yesterday and message.text:
                    for keyword in keywords:
                        if keyword.lower() in message.text.lower():
                            report += f"Chat: {chat}\n"
                            report += f"Message: {message.text}\n"
                            report += "-----------------\n"

        await client.send_message("me", report)

with TelegramClient('session', api_id, api_hash) as client:
    client.loop.run_until_complete(main())
