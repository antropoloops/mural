* Miércoles 14 de Febrero 2018
------------

objetivo: instalación en RPI de lo necesario para conectar MKMK y poder hacer sonidos via OSC y SonicPi


##  pasos seguidos

Raspberry Pi:

1. conectado rasberrypi a monitor, con teclado y raton y wifi
2. clonado este repo
3. install vim

```
sudo apt-get update
sudo apt-get install vim
```

4. instalar python-osc package:

```
pip3 install python-osc
``` 

ojo: para python 2.7 el módulo python-osc no funciona. Tiene un bug conocido. Hay que usarlo en python 3.

Una vez instalado el `python-osc` se pueden enviar mensajes a sonic-pi mediante:

```
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

```

(ver /files/osc-sonicpi-minim.py)

Con python también se puede hacer un servidor osc que escuche mensajes osc (y con ello por ejemplo disparar sonidos o bien visuales, etc.)

```
from pythonosc import dispatcher
from pythonosc import osc_server

dispatcher = dispatcher.Dispatcher()
dispatcher.map("/play", lambda _: print('Received'))

print('Waiting')
server = osc_server.ThreadingOSCUDPServer(
    ('localhost', 5005), dispatcher)
print("Serving on {}".format(server.server_address))
server.serve_forever()

```


