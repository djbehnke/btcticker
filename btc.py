#!/usr/bin/python3

import requests
import json
import pyglet
import time


window = pyglet.window.Window(fullscreen=True)
label = pyglet.text.Label()
i = 0
last = 0
size = 256

def update(dt):
    global last 
    global size

    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    content = json.loads(r.text)

    current = float(content["bpi"]["USD"]["rate"].replace(',', ''))
    delta = round(current - last, 2)

    vlist = pyglet.graphics.vertex_list(3, ('v2f', [0, 0, 400, 50, 200, 300]))

    if current > last:
        change = '\u25b2'
        label = pyglet.text.Label(change+'$'+content["bpi"]["USD"]["rate"][:-2],
                              font_size=size,
                              x=window.width//2,
                              y=window.height//2,
                              anchor_x='center',
                              anchor_y='center',
                              color=(132,255,104,100))
        deltext = pyglet.text.Label('('+str(delta)+')',
                                    font_size=size//2,
                                    x=window.width//2,
                                    y=window.height//5,
                                    anchor_x='center',
                                    anchor_y='center',
                                    color=(132,255,104,100))


    elif last > current:
        change = '\u25bc'
        label = pyglet.text.Label(change+'$'+content["bpi"]["USD"]["rate"][:-2],
                              font_size=size,
                              x=window.width//2,
                              y=window.height//2,
                              anchor_x='center',
                              anchor_y='center',
                              color=(255,73,73,100))
        deltext = pyglet.text.Label('('+str(delta)+')',
                                    font_size=size//2,
                                    x=window.width//2,
                                    y=window.height//5,
                                    anchor_x='center',
                                    anchor_y='center',
                                    color=(255,73,73,100))



    else:
        change = '~'
        label = pyglet.text.Label(change+'$'+content["bpi"]["USD"]["rate"][:-2],
                              font_size=size,
                              x=window.width//2,
                              y=window.height//2,
                              anchor_x='center',
                              anchor_y='center',
                              color=(255,255,255,100))
        deltext = pyglet.text.Label('('+str(delta)+')',
                                    font_size=size//2,
                                    x=window.width//2,
                                    y=window.height//5,
                                    anchor_x='center',
                                    anchor_y='center',
                                    color=(255,255,255,100))



    flavor = pyglet.text.Label("Current Bitcoin Price:",
                                font_size = size//2,
                                x=window.width//2,
                                y=window.height-window.height//5,
                                anchor_x='center',
                                anchor_y='center',
                                color=(255,255,255,100))



    last = float(content["bpi"]["USD"]["rate"].replace(',', ''))

    @window.event
    def on_draw():
        window.clear()
        label.draw()
        flavor.draw()
        deltext.draw()

if __name__ == "__main__":
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    content = json.loads(r.text)

    label = pyglet.text.Label(content["bpi"]["USD"]["rate"],
                              font_size=36,
                              x=window.width//2,
                              y=window.height//2,
                              anchor_x='center',
                              anchor_y='center')

    pyglet.clock.schedule_interval(update, 45.0)

    pyglet.app.run()
