# REFERENCE: https://www.gngrninja.com/code/2017/3/24/python-create-discord-bot-on-raspberry-pi

import os
import signal
import discord
import subprocess
from Ngrok import Ngrok
from Logger import logger
from config import BOT_TOKEN

ngrok = Ngrok()
error = "\n:strawberry:Raspberry:\n{}\n"


class DiscordClient(discord.Client):
    async def on_ready(self):
        logger.info(f'[SUCCESS]: Connected as {self.user}')

    async def on_message(self, message):
        logger.info(f'[MESSAGE]: {message.content}')

        if message.author == self.user:
            return

        command = message.content
        if not command:
            return

        if command.startswith('bot help'):
            try:
                await message.channel.send("""
                Commands:
                - Any linux command (Restricted to 2000 lines)
                - ngrok <port> <protocol> (Starts tunnel)
                - get ngrok (Shows all tunnels)
                - delete ngrok (Deletes all tunnels)
                """)
                return

            except Exception as e:
                await message.channel.send(error.format(e))
                return

        if command.startswith('ngrok'):
            response = ngrok.start_tunnel(command)
            await message.channel.send(response)
            return

        if command.startswith('get ngrok'):
            response = ngrok.get_tunnels()
            await message.channel.send(response)
            return

        if command.startswith('delete ngrok'):
            response = ngrok.delete_tunnels()
            await message.channel.send(response)
            return

        try:
            output = subprocess.Popen(
                command.split(),
                stdout=subprocess.PIPE,
                cwd=os.getcwd(),
                bufsize=-1,
                encoding='utf-8'
            )

            for line in iter(output.stdout.readline, b''):
                try:
                    await message.channel.send(line)
                except:
                    pass

            return

        except Exception as e:
            logger.exception(e)
            await message.channel.send(error.format(e))

            return


if __name__ == "__main__":
    client = DiscordClient()
    client.run(BOT_TOKEN)
