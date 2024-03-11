from libqtile.config import Key

from const import *

def def_keys():
    #TODO: esto falta
    # [
    #     LAYOUT.flip_down(),
    #     LAYOUT.flip_up(),
    #     LAYOUT.flip_left(),
    #     LAYOUT.flip_right(),
    #     LAYOUT.swap_column_left(),
    #     LAYOUT.swap_column_right(),
    #     LAYOUT.swap_left(),
    #     LAYOUT.swap_right(),
    #     LAYOUT.grow(),
    #     LAYOUT.shrink(),
    #     LAYOUT.maximize(),
    #     LAYOUT.flip(),
    # ]

    # Add key bindings to switch VTs in Wayland.
    # We can't check qtile.core.name in default config as it is loaded before qtile is started
    # We therefore defer the check until the key binding is run by using .when(func=...)
    # for vt in range(1, 8):
    #     keys.append(
    #         Key(
    #             ["control", "mod1"],
    #             f"f{vt}",
    #             lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
    #             desc=f"Switch to VT{vt}",
    #         )
    #     )

    #* con esto se definen todos los binds de qtile
    return [ 
        # esto se puede mejorar con keychords, modes y chains
        # https://docs.qtile.org/en/stable/manual/config/keys.html
        #* Aplicaciones 
        Key(PRIMARY,     "Return", LAZY.spawn(TERMINAL),       desc="Launch terminal"), # TODO: cambiar a t
        Key(PRIMARY,     "b",      LAZY.spawn(BROWSER),        desc="Launch browser"),
        Key(PRIMARY,     "f",      LAZY.spawn(EXPLORER),       desc="Launch File explorer"),
        Key(PRIMARY,     "s",      LAZY.spawn(STORE),          desc="Launch App store"),
        Key(PRIMARY,     "t",      LAZY.spawn(EDITOR),         desc="Launch Text editor"), # TODO: cambiar a c
        Key(PRIMARY,     "d",      LAZY.spawn(DB),             desc="Launch Database manager"),
        Key(PRIMARY,     "r",      LAZY.spawncmd(),            desc="Spawn a command using a prompt widget"),
        Key(PRIMARY,     "q",      WINDOW.kill(),              desc="Kill focused window"), 
        #* Movilidad 
        Key(PRIMARY,     LEFT,     LAYOUT.left(),              desc="Move focus to left"), 
        Key(PRIMARY,     RIGHT,    LAYOUT.right(),             desc="Move focus to right"),
        Key(PRIMARY,     DOWN,     LAYOUT.down(),              desc="Move focus down"),
        Key(PRIMARY,     UP,       LAYOUT.up(),                desc="Move focus up"),    
        # Key(PRIMARY,     "space",  LAYOUT.next(),              desc="Move window focus to other window"),
        #* pantallas
        Key(PRIMARY,     "space",  LAZY.next_screen(),         desc="Move window focus to the next screen"),
        Key(ALT_PRIMARY, "space",  LAZY.prev_screen(),         desc="Move window focus to the previus screen"),
        #* grupos 
        Key(ALT_PRIMARY, LEFT,     SCREEN.prev_group(),        desc="Move focus to left group"), 
        Key(ALT_PRIMARY, RIGHT,    SCREEN.next_group(),        desc="Move focus to right group"),
        Key(ALT_PRIMARY, DOWN,     GROUP.prev_window(),        desc="Switch focus to previous window in group"),
        Key(ALT_PRIMARY, UP,       GROUP.next_window(),        desc="Switch focus to next window in group"),
        #* Redimensionar 
        Key(MODIFY,      LEFT,     LAYOUT.grow_left(),         desc="Grow window to the left"), 
        Key(MODIFY,      RIGHT,    LAYOUT.grow_right(),        desc="Grow window to the right"),
        Key(MODIFY,      DOWN,     LAYOUT.grow_down(),         desc="Grow window down"),
        Key(MODIFY,      UP,       LAYOUT.grow_up(),           desc="Grow window up"),
        Key(MODIFY,      "space",  LAYOUT.increase_ratio(),    desc="Increase the space for master window"),
        Key(ALT_MODIFY,  "space",  LAYOUT.decrease_ratio(),    desc="Decrease the space for master window"),
        Key(MODIFY,      "r",      LAYOUT.normalize(),         desc="Reset all window sizes"),
        #* Acomodar 
        Key(ORDER,       LEFT,     LAYOUT.shuffle_left(),      desc="Move window to the left"), 
        Key(ORDER,       RIGHT,    LAYOUT.shuffle_right(),     desc="Move window to the right"),
        Key(ORDER,       DOWN,     LAYOUT.shuffle_down(),      desc="Move window down"),
        Key(ORDER,       UP,       LAYOUT.shuffle_up(),        desc="Move window up"),
        Key(ORDER,       "f",      WINDOW.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
        Key(ORDER,       "t",      WINDOW.toggle_floating(),   desc="Toggle floating on the focused window"),
        Key(ALT_ORDER,   UP,       WINDOW.move_up(),           desc="Move the window above the next window"),
        Key(ALT_ORDER,   DOWN,     WINDOW.move_down(),         desc="Move the window below the previous window"),
        Key(ALT_ORDER,   "space",  WINDOW.move_to_top(),       desc="Move the window above all"),
        Key(ALT_ORDER,   "space",  WINDOW.move_to_bottom(),    desc="Move the window below all"),
        Key(ORDER,       "x",      WINDOW.keep_above(),        desc="Keep window above other windows"),
        Key(ALT_ORDER,   "x",      WINDOW.keep_below(),        desc="Keep window below other windows"),
        Key(ALT_ORDER,   "f",      WINDOW.bring_to_front(),    desc="Toggle fullscreen on the focused window"), #* faltan los dropdown
        #* Layout 
        Key(ORDER,       "Tab",    LAZY.next_layout(),         desc="Move next layouts"), 
        Key(ALT_ORDER,   "Tab",    LAZY.prev_layout(),         desc="Move previus layouts"),
        Key(ORDER,       "Return", LAYOUT.toggle_split(),      desc="Toggle between split and unsplit sides of stack"),
        #* Control de sistema 
        Key(SYSTEM,      "r",      LAZY.reload_config(),       desc="Reload the config"), 
        Key(SYSTEM,      "q",      LAZY.shutdown(),            desc="Shutdown Qtile"),
    ]