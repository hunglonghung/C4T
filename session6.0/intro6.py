import pyglet
import time
import datetime 
while True:
    n=datetime.datetime.now()
    print(n.minute)
    if n.minute == 40 :
        music = pyglet.resource.media('sample.wav')
        music.play()

        pyglet.app.run()
    
