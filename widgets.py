from libqtile import widget

def def_widgets():
    return [
            widget.CurrentLayout(),
            widget.Sep(),
            widget.GroupBox(),
            widget.Sep(),
            widget.WindowName(),
            widget.Sep(),
            widget.Prompt(),
            widget.Chord(
                chords_colors={
                    "launch": ("#ff0000", "#ffffff"),
                },
                name_transform=lambda name: name.upper(),
            ),
            # widget.StatusNotifier(),
            widget.Systray(), #! no funciona en ambos
            widget.Clock(format="%d/%m/%Y %H:%M:%S"), # DD/MM/YYYY hh:mm:ss
            widget.Sep(),
            # widget.Backlight(), #TODO: hay que hacerlo andar
            widget.Sep(),
            widget.QuickExit(
                default_text='[]', 
                countdown_format='[{}]',
                countdown_start=7,
                foreground='#FF004A'
            ),
        ]