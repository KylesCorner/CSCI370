"""
Kyle Krstulich
3/2/24
CSCI370
main.py
"""
import backend
from frontend import gui

data = backend.get_data()
g = gui(data)
g.plot_data()
