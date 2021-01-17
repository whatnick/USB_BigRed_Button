#!/usr/bin/env python

import sys
import pyglet
pyglet.options['search_local_libs'] = True

# Goose Honk from : https://commons.wikimedia.org/wiki/File:Geese_Honking_(loud).ogg
# my_music = pyglet.media.load("software\Geese_Honking_(loud).ogg")

# Train Horn from : https://bigsoundbank.com/detail-0277-train-horn.html
my_music = pyglet.media.load("software\TRNHorn_Train horn (ID 0277)_BSB.ogg")	# Loads the audio file you want to play (it does not have to be a .ogg

my_player = pyglet.media.Player()	# Creates a player

my_player.queue(my_music)	# Adds your song to the players queue
my_player.loop = True 		# If you want the player to loop your song. By default this value is False
my_player.pause()			# Starts playing your audio file when you run the app

event_loop = pyglet.app.EventLoop()
win = pyglet.window.Window()

@win.event
def on_key_press(symbol, modifiers):
    if symbol==97:
        my_player.play()

@win.event
def on_key_release(symbol, modifiers):
    my_player.pause()

@event_loop.event
def on_window_close(window):
    event_loop.exit()

pyglet.app.run()			# Runs the app