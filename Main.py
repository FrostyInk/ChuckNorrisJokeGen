import tkinter as tk
from chuck import ChuckNorris
from tkinter import font
from Config import Config


# Methods

def random_joke():
	data = cn.random()
	text_var.set(data.joke)


# Create the config
config = Config()

# Create the API object for Chuck Norris
cn = ChuckNorris()

# Create our window and apply settings
root = tk.Tk()
root.title(config.TITLE)
root.geometry(f'{config.WIDTH}x{config.HEIGHT}')
root.resizable(False, False)

# Fonts
font_n = font.Font(family=config.FONT_FAMILY, size=config.FONT_SIZE)

# Window layout
frame = tk.Frame(root, bg=config.FRAME_COLOR)
frame.pack(fill='both', expand=True)

joke_frame = tk.Frame(frame, bg=config.JOKE_BACKGROUND_COLOR)
joke_frame.pack(fill='both', expand=True, side='top', padx=10, pady=10)
joke_frame.config(highlightbackground=config.JOKE_BORDER_COLOR)
joke_frame.config(highlightthickness=config.JOKE_BORDER_THICKNESS)

button = tk.Button(frame, text='Get A Random Joke', command=random_joke, bg=config.BUTTON_COLOR,
				   fg=config.JOKE_TEXT_COLOR,
				   activebackground=config.BUTTON_PRESSED_COLOR)
button.pack(side='bottom', fill='x')

text_var = tk.StringVar(joke_frame)
text = tk.Label(joke_frame, textvariable=text_var, font=font_n, bg=config.JOKE_BACKGROUND_COLOR,
				fg=config.JOKE_TEXT_COLOR,
				wraplength=300)
text_var.set('Welcome, press the button for fun :)')
text.place(relx=0.5, rely=0.5, anchor='center')

# Main loop for our window
root.mainloop()
