# mural
Todo acerca de la programación necesaria para el mural de los talleres antropoloops, II trimestre, primer año.

## Opción Sonic Pi + Makey makey
Una posible solución es usar Sonic Pi para lanzar los loops y un script de python para escuchar el input del makey makey y lanzar los mensajes OSC.

Ejemplo que podemos usar de base: [Sonic Pi goes Bananas](https://alcluith.wordpress.com/2018/01/25/sonic-pi-goes-bananas/)

Espe lo ha montado en su mac y funciona. Habra que probarlo en la Raspberry Pi. Única dificultad que encontró fue instalar PyGame porque requiere ciertas dependencias y no estaba muy claro.

Algunos enlaces que han ayudado a Espe a instalar Pygame en Mac:
* http://brysonpayne.com/2015/01/10/setting-up-pygame-on-a-mac/
* https://pygame.org/wiki/macintosh
* https://pygame-zero.readthedocs.io/en/stable/installation.html#on-osx

Para que Sonic Pi pueda recibir y enviar OSC tiene que ser la [versión 3.0](https://github.com/samaaron/sonic-pi/blob/master/CHANGELOG.md#v3.0) 

Sonic Pi 3.0 viene preinstalado para [Raspbian Strech](https://www.raspberrypi.org/blog/raspbian-stretch/)

Posibles dificultades:
* Cómo hacer que esto funcione en la Raspberry Pi sin monitor, es decir que tendría que arrancar todo automáticamente al arrancar la Pi.
