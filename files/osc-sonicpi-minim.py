#####################################################
#Use MaKey MaKey to trigger sounds in Sonic Pi
#written by Claire Quigley, January 2018
#####################################################
from random import randint
from pythonosc import osc_message_builder
from pythonosc import udp_client

# set size of Pygame Zero window
WIDTH = 800
HEIGHT = 600

# where to send the OSC messages
sender = udp_client.SimpleUDPClient("127.0.0.1", 4559)

# send play via osc:
sender.send_message("/play", 1)