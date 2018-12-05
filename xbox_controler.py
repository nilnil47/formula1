"""
this module is responsible for reading the values of the xbox controller and send then into the
webserver on the raspberry pi the xbox module is taken from https://github.com/FRC4564/Xbox
"""
import logging
import xbox
import json
import socket


class JoystickClient:
    """
    this class use read the controller values
    using the Joystick class and send then to server
    with the udp protocol

    the data structures of the controller values:
        direction - short
        speed - uint8

    """
    def __init__(self, server_ip, server_port):
        logging.basicConfig(level=logging.DEBUG)
        self.server_ip = server_ip
        self.server_port = server_port
        self._joy = xbox.Joystick()
        self._joy_dict = {}
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def update(self):
        """
        get the values from the xbox controller
        and send them to the server
        :return:
        """

        self._joy_dict["direction"] = self._joy.leftX()
        self._joy_dict["speed"] = self._joy.rightTrigger()
        message = json.dumps(self._joy_dict).encode()
        logging.debug(message)
        self._sock.sendto(message, (self.server_ip, self.server_port))


    def start(self):
        while True:
            self.update()

if __name__ == '__main__':
    joystickClient = JoystickClient("127.0.0.1", 1337)
    joystickClient.start()
