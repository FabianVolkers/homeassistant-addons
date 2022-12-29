import socket
import logging

logger = logging.getLogger(__name__)

class UDPServer:
    def __init__(self, source_ip, source_port):
        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.socket.bind((source_ip, source_port))

    def receive(self):
        message, addr = self.socket.recvfrom(10240)
        return self.trim_message(message)

    def trim_message(self, message):
        """
        Trim first 12 bytes of message to adhere to mpegts standard.
        See https://github.com/KonradIT/GoProStream/issues/57 for more info.
        """
        return message[12:]

class UDPClient:
    def __init__(self, dest_ip, dest_port):
        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.socket_addr = (dest_ip, dest_port)

    def send(self, message):
        self.socket.sendto(message, self.socket_addr)

if __name__ == "__main__":
    logger.info(f"Receiving UDP stream on 0.0.0.0:8554")
    print(f"Receiving UDP stream on 0.0.0.0:8554")
    udp_server = UDPServer("0.0.0.0", 8554)
    udp_client = UDPClient("127.0.0.1", 8555)
    while True:
        message = udp_server.receive()
        logger.debug(message[:10])
        udp_client.send(message)