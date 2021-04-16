from pyngrok import ngrok
from Logger import logger
from config import NGROK_TOKEN


class Ngrok():
    def __init__(self):
        ngrok.set_auth_token(NGROK_TOKEN)
        self.error = "\n:strawberry:Raspberry:\n{}\n"

    def start_tunnel(self, command):
        try:
            command = command.split()
            port = command[1]
            protocol = command[2]

            ngrok_tunnel = ngrok.connect(port, protocol)
            return ngrok_tunnel

        except Exception as e:
            logger.exception(e)
            return self.error.format(e)

    def get_tunnels(self):
        try:
            return str(ngrok.get_tunnels())

        except Exception as e:
            logger.exception(e)
            return self.error.format(e)

    def delete_tunnels(self):
        try:
            for tunnel in ngrok.get_tunnels():
                ngrok.disconnect(tunnel.public_url)

            if not ngrok.get_tunnels():
                return 'All active Ngrok tunnels delete successfully!'

            return 'Something went wrong deleting the Ngrok tunnels!'

        except Exception as e:
            logger.exception(e)
            return self.error.format(e)
