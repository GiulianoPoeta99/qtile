from libqtile.config import Click, Drag

from const import *

def def_mouse():
    return [
        Drag( PRIMARY, "Button1", WINDOW.set_position_floating(), start=WINDOW.get_position()),
        Drag( PRIMARY, "Button3", WINDOW.set_size_floating(),     start=WINDOW.get_size()),
        Click(PRIMARY, "Button2", WINDOW.bring_to_front()),
    ]