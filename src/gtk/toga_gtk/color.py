from gi.repository import Gdk

CACHE = {}


def native_color(c):
    try:
        color = CACHE[c]
    except KeyError:
    	color = Gdk.RGBA()
    	color.red = c.rgba.r/255
    	color.green = c.rgba.g/255
    	color.blue = c.rgba.b/255
    	color.alpha = c.rgba.a
		# color = Gdk.from_color(c.rgba.r / 255, c.rgba.g / 255, c.rgba.b / 255, c.rgba.a)

    return color
