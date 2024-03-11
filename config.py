import os
import subprocess
from libqtile import layout, hook
from libqtile.config import Match

from const import *
from keys import def_keys
from groups import def_groups
from mouse import def_mouse
from layouts import def_layouts
from screens import def_screens

#* con esto se definen todos los binds de qtile
keys = def_keys()

#* aca se definen los grupos y sus binds
groups = def_groups(keys)

#* aca se definen los usos del mouse
mouse = def_mouse()

#* aca se definen los layouts y sus configs
layouts = def_layouts()

#* definimos un estandar para los widgets
widget_defaults = dict(
    font=FONT,
    fontsize=FONT_SIZE,
    padding=3,
)
extension_defaults = widget_defaults.copy()

#* definimos las pantallas y sus caracteristicas
screens = def_screens()

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),    # gitk
        Match(wm_class="makebranch"),      # gitk
        Match(wm_class="maketag"),         # gitk
        Match(wm_class="ssh-askpass"),     # ssh-askpass
        Match(title="branchdialog"),       # gitk
        Match(title="pinentry"),           # GPG key password entry
    ],
    border_focus            = '#D84610',   # Border colour(s) for the focused window.
    border_normal           = '#000000',   # Border colour(s) for un-focused windows.
    border_width            = 1,           # Border width.
    fullscreen_border_width = 0,           # Border width for fullscreen.
    max_border_width        = 0            # Border width for maximize.
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

#* este hook ejecuta una unica vez el script de inicio de sistema
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])
