"""
this module is the server which is used by the raspberry pi
it got the controller information by from the pc by udb socket
"""

import socket
import json
import logging
import turtle


BUFSIZE = 1024


class JoyStickServer:
    """
    this class ןד responsible on receiving the
    controller information from the pc client
    """

    def __init__(self, bufsize, port):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._bufsize = bufsize
        self._sock.bind(("0.0.0.0", port))

    def _update(self):
        data, addr = self._sock.recvfrom(self._bufsize)


        joy_dict = json.loads(data.decode())

    def start(self):
        while True:
            self._update()


class VirtualCar:
    """
    this class simulate the car using the turtle module
    """
    def __init__(self):
        self.tr = turtle.Turtle()

    def update(self, **kwargs):
        """
        this part is with liam
        :param kwargs:
        :return:
        """
        pass



if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    joystickServer = JoyStickServer(BUFSIZE, 1337)
    joystickServer.start()




