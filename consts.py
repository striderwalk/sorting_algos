# constants
import json


WIDTH, HEIGHT = 800, 600
BUTTON_WIDTH, BUTTON_HEIGHT = 300, 35
FPS = 60
# colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 128, 0)
MAGENTA = (255, 0, 255)
LIME = (0, 255, 0)
CYAN = (0, 255, 255)
SILVER = (192, 192, 192)
GRAY = (128, 128, 128)
MAROON = (128, 0, 0)
OLIVE = (128, 128, 0)
PURPLE = (128, 0, 128)
TEAL = (0, 128, 128)
NAVY = (0, 0, 128)

# ALGO DATA
with open("algo_data.json") as file:
    ALGO_DATA = json.load(file)
