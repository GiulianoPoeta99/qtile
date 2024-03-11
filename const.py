from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

FONT="FiraCode Nerd Font Mono"
FONT_SIZE=13

COLORS = [
    ['282C34','282C34'], # background
    ['C5C5C5','C5C5C5'], # foreground
    ['42444D','8F9AAE'], # color1 & color9
    ['FC2E51','FF637F'], # color2 & color10
    ['25A45C','3FC56A'], # color3 & color11
    ['FF9369','F9C858'], # color4 & color12
    ['3375FE','10B0FE'], # color5 & color13
    ['9F7EFE','FF78F8'], # color6 & color14
    ['4483AA','5FB9BC'], # color7 & color15
    ['CDD3E0','FFFFFF'], # color8 & color16
]

# lazy objects
LAZY = lazy
LAYOUT = lazy.layout
WINDOW = lazy.window
GROUP = lazy.group
SCREEN = lazy.screen

# Botones
MOD = "mod4" # this is everything
ALT = "mod1" # special
CONTROL = "control" # control
SHIFT = "shift" # alt

# Combinaciones
PRIMARY     = [MOD]                      # acciones principales
ALT_PRIMARY = [MOD, ALT]
ORDER       = [MOD, CONTROL]             # ordenar tiles 
ALT_ORDER   = [MOD, ALT, CONTROL]        # ordenar tiles alternativo
MODIFY      = [MOD, SHIFT]               # modificar tiles
ALT_MODIFY  = [MOD, ALT, SHIFT] 
SYSTEM      = [MOD, CONTROL, SHIFT] 
ALT_SYSTEM  = [MOD, ALT, CONTROL, SHIFT] # acciones del sistema alternativo (sensibles)

TERMINAL = guess_terminal()
BROWSER  = "com.brave.Browser"
EXPLORER = "nautilus"
STORE    = "gnome-software"
EDITOR   = "code"
DB       = "dbeaver"

LEFT  = "Left"
RIGHT = "Right"
DOWN  = "Down"
UP    = "Up"