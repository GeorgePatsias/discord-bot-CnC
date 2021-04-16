# REFERENCE: https://www.gngrninja.com/code/2017/3/24/python-create-discord-bot-on-raspberry-pi

import discord
import subprocess
from Logger import logger
from pyngrok import ngrok
from config import BOT_TOKEN, NGROK_TOKEN


class MyClient(discord.Client):

    async def on_ready(self):
        logger.info(f'[SUCCESS]: Connected as {self.user}')

    async def on_message(self, message):
        logger.info(f'[MESSAGE]: {message.content}')

        if message.author == self.user:
            return

        messageContent = message.content
        if not messageContent:
            return

        if messageContent.startswith('bot help'):
            try:
                output = """
                Commands:
                - Any linux command (Restricted to 2000 lines)
                - ngrok <port> <protocol> (Starts tunnel)
                - get ngrok (Shows all tunnels)
                - delete ngrok (Deletes all tunnels)
                """

                await message.channel.send(output)
                return

            except Exception as e:
                logger.exception(e)
                await message.channel.send(f"\n:strawberry:Raspberry:\n{e}\n")
                return

        if messageContent.startswith('ngrok'):
            try:
                ngrok.set_auth_token(NGROK_TOKEN)
                ngrok_tunnel = ngrok.connect(messageContent.split()[1], messageContent.split()[2])

                await message.channel.send(ngrok_tunnel)
                return

            except Exception as e:
                logger.exception(e)
                await message.channel.send(f"\n:strawberry:Raspberry:\n{e}\n")
                return

        if messageContent.startswith('get ngrok'):
            try:
                ngrok.set_auth_token(NGROK_TOKEN)
                tunnels = ngrok.get_tunnels()
                await message.channel.send(str(tunnels))
                return

            except Exception as e:
                logger.exception(e)
                await message.channel.send(f"\n:strawberry:Raspberry:\n{e}\n")
                return

        if messageContent.startswith('delete ngrok'):
            try:
                ngrok.set_auth_token(NGROK_TOKEN)
                tunnels = ngrok.get_tunnels()

                for tunnel in tunnels:
                    ngrok.disconnect(tunnel.public_url)

                await message.channel.send("Ngrok deleted all tunnels!")
                return

            except Exception as e:
                logger.exception(e)
                await message.channel.send(f"\n:strawberry:Raspberry:\n{e}\n")
                return

        try:
            output = subprocess.check_output(messageContent, shell=True, encoding='utf-8')
            await message.channel.send(f"\n:strawberry:Raspberry:\n{output}\n")

        except Exception as e:
            logger.exception(e)
            await message.channel.send(f"\n:strawberry:Raspberry:\n{e}\n")

            return


if __name__ == "__main__":
    client = MyClient()
    client.run(BOT_TOKEN)
