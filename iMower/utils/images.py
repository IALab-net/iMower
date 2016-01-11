import pyglet


def get_image(code):
    if code == 'H':
        src = "iMower/images/hight-grass.jpg"
    elif code == 'L':
        src = "iMower/images/low-grass.jpg"
    elif code == 'R':
        src = "iMower/images/rocks.jpg"
    elif code == 'M':
        src = "iMower/images/roomba.png"
    else:
        raise ValueError("Unkown code {0}".format(code))
    return pyglet.resource.image(src)
