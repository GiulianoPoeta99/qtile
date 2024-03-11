from libqtile import layout

from const import *

def def_layouts():
    global_config = {
        'border_focus': '#D84610', # Border colour(s) for the focused window.
        'border_normal': '#000000', # Border colour(s) for un-focused windows.
        'border_width': 2, # Border width.
        'margin': 8, # Margin of the layout
    }

    return [
        layout.MonadTall( # sirve buena mov 
            single_border_width = 2, # Border width for single window
            single_margin = 8, # Margin size for single window
            **global_config #* si paso esto como kwargs me ahorro espacio
        ),
        layout.TreeTab( # SUPER GOD
            active_bg        = '#000080',               # Background color of active tab
            active_fg        = '#ffffff',               # Foreground color of active tab
            inactive_bg      = '#606060',               # Background color of inactive tab
            inactive_fg      = '#ffffff',               # Foreground color of inactive tab
            urgent_bg        = '#ff0000',               # Background color of urgent tab
            urgent_fg        = '#ffffff',               # Foreground color of urgent tab
            bg_color         = '#000000',               # Background color of tabs
            section_fg       = 'ffffff',                # Color of section label
            border_width     = 2, # Width of the border
            font             = FONT, # Font
            fontsize         = FONT_SIZE, # Font pixel size.
            padding_left     = 8, # Left padding for tabs
            padding_x        = 8, # Left padding for tab label
            padding_y        = 6, # Top padding for tab label
            vspace           = 1, # Space between tabs
            level_shift      = 8, # Shift for children tabs
            sections         = ["ONE", "TWO", "THREE"], # Titles of section instances
            section_fontsize = 10, # Font pixel size of section label
            section_top      = 8, # Top margin of section label
            section_bottom   = 8, # Bottom margin of section
            previous_on_rm   = True, # Focus previous window on close instead of first.
            panel_width      = 190, # Width of the left panel
        ),
        layout.Bsp(),
        layout.Columns(),
        layout.Matrix(),
        layout.Max(),
        layout.MonadThreeCol(),
        layout.MonadWide(),
        layout.RatioTile()
    ]
