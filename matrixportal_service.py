import board
import displayio
import terminalio

from adafruit_matrixportal.matrixportal import MatrixPortal
from adafruit_display_text import label

def create_matrixportal():
    matrixportal = MatrixPortal(status_neopixel=board.NEOPIXEL, debug=False)
    return matrixportal

def set_colors():
    colors = displayio.Palette(3)  # Create a color palette
    colors[0] = 0x000000  # black background
    colors[1] = 0xFF0000  # red
    colors[2] = 0xCC4000  # amber
    return colors

def create_grid(colors):
    bitmap = displayio.Bitmap(64, 32, 2)  # Create a bitmap object,width, height, bit depth
    tile_grid = displayio.TileGrid(bitmap, pixel_shader=colors)
    parent_group = displayio.Group()  # Create a Group
    parent_group.append(tile_grid)  # Add the TileGrid to the Group
    return parent_group

def create_text_label(color, parent_group, display):
    message_label = label.Label(terminalio.FONT, text='', color=color)
    center_label(message_label, display)
    parent_group.append(message_label)
    message_label.hidden = True
    return message_label

def set_label_text(label, text, color, display, hide):
    label.text = text
    label.color = color
    center_label(label, display)
    label.hidden = hide
    return label

def center_label(label: label.Label, display):
    bbx, bby, bbwidth, bbh = label.bounding_box
    # Center the label
    label.x = round(display.width / 2 - bbwidth / 2)
    label.y = display.height // 2
