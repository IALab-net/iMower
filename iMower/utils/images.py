import pyglet


def get_image(code):
    if code == 'H':
        src = "images/hight-grass.jpg"
    elif code == 'L':
        src = "images/low-grass.jpg"
    elif code == 'R':
        src = "images/rocks.jpg"
    elif code == 'M':
        src = "images/roomba.png"
    else:
        raise ValueError("Unkown code {0}".format(code))
    return pyglet.resource.image(src)
