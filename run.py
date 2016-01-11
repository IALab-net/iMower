import pyglet
from iMower.main import app

if __name__ == "__main__":
    # Print all events
    app.select_world("world-1")
    # window.push_handlers(pyglet.window.event.WindowEventLogger())
    pyglet.app.run()
