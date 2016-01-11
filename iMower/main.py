# Pyglet
import pyglet

# Pyglet Events
from pyglet.window import key
from pyglet.window import mouse

# Here
from utils.images import get_image

class App():

    # World def
    world_src = None
    world_tiles = []
    world_width = 0
    world_height = 0

    # Tiles def
    tile_size = 50


    def select_world(self, code):
        self.world_src = "worlds/{0}.txt".format(code)

    def load_world(self):
        if self.world_width > 0:
            return
        self.world_width = 0
        with open(self.world_src) as f:
            for line in f:
                line = line.strip()
                self.world_width = len(line)
                self.world_tiles.extend(list(line))
        self.world_height = len(self.world_tiles) / self.world_width
        print("World loaded: tiles={length}, widht={width}, height={height}".format(
            length=len(self.world_tiles), width=self.world_width, height=self.world_height))

    def draw_world(self):
        self.load_world()
        x = 0
        y = (self.world_height - 1) * self.tile_size
        for i, tile_code in enumerate(self.world_tiles):
            tile = get_image(tile_code)
            print("{code}({x},{y},{i})".format(code=tile_code, x=x, y=y, i=i+1), end='')
            tile.blit(x, y, width=self.tile_size, height=self.tile_size)
            x += self.tile_size
            if (i+1) % self.world_width == 0:
                print()
                y -= self.tile_size
                x = 0


app = App()

window = pyglet.window.Window()
label = pyglet.text.Label("Hello, world",
                          font_name="Times New Roman",
                          font_size=36,
                          x=window.width / 2,
                          y=window.height / 2,
                          anchor_x="center",
                          anchor_y="center")

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print("Key A was pressed")
    elif symbol == key.LEFT:
        print("Key LEFT was pressed")

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print("Left mouse button pressed")

@window.event
def on_draw():
    window.clear()
    app.draw_world()

if __name__ == "__main__":
    # Print all events
    app.select_world("world-1")
    # window.push_handlers(pyglet.window.event.WindowEventLogger())
    pyglet.app.run()
