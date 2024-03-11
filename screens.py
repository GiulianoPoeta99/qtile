from libqtile import bar, widget
from libqtile.config import Screen

from widgets import *

def def_screens():

    widgets = def_widgets()

    return[
        Screen(
            wallpaper='~/.config/qtile/wallpaper.jpg',
            wallpaper_mode='fill',
            top=bar.Bar(
                widgets,
                26,
            ),
            # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
            # By default we handle these events delayed to already improve performance, however your system might still be struggling
            # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
            # x11_drag_polling_rate = 60,
        ),
        Screen(
            wallpaper='~/.config/qtile/wallpaper.jpg',
            wallpaper_mode='fill',
            top=bar.Bar(
                widgets,
                26,
            ),
            # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
            # By default we handle these events delayed to already improve performance, however your system might still be struggling
            # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
            # x11_drag_polling_rate = 60,
        ),
    ]