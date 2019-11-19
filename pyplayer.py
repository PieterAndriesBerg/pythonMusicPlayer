
# Import Modules
import pygame
import tkinter as tkr

# Create Window
player = tkr.Tk()

# Edit Window
player.title("Audio Player")
player.geometry("205x340")

# Get Song
file = "Song-Name.mp3"

# Action Event
def play():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def exitPlayer():
    pygame.mixer.music.stop()

def pausePlayer():
    pygame.mixer.music.pause()

def unpausePlayer():
    pygame.mixer.music.unpause()


# Register Buttons
button1 = tkr.Button(player, width=5, height=3, text="PLAY", command=play)
button1.pack(fill="x")
button2 = tkr.Button(player, width=5, height=3, text="STOP", command=exitPlayer)
button2.pack(fill="x")
button3 = tkr.Button(player, width=5, height=3, text="PAUSE", command=pausePlayer)
button3.pack(fill="x")
button4 = tkr.Button(player, width=5, height=3, text="UNPAUSE", command=unpausePlayer)
button4.pack(fill="x")

# Song Name
label1 = tkr.LabelFrame(player, text="Song Name")
label1.pack(fill="both", expand="yes")
contents1 = tkr.Label(label1, text=file)
contents1.pack()

# Activate
player.mainloop()



