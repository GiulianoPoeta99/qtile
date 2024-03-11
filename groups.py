from libqtile.config import Group, Key

from const import *

#? con ScratchPad y DropDowns podemos hacer que los grupos ejecuten lo que queramos
def def_groups(keys):

    group_data = {
        '1': {'layout': 'treetab', 'label': ''},
        '2': {'layout': 'monadtall', 'label': '󰙯'},
        '3': {'layout': 'monadtall', 'label': ''},
        '4': {'layout': 'monadtall', 'label': '󰆼'},
        '5': {'layout': 'monadtall', 'label': ''},
        '6': {'layout': 'monadtall', 'label': '1'},
        '7': {'layout': 'monadtall', 'label': '2'},
        '8': {'layout': 'monadtall', 'label': '3'},
        '9': {'layout': 'monadtall', 'label': '4'},
        '0': {'layout': 'max', 'label': ''}
    }

    groups = []
    for name, data in group_data.items():
        groups.append(Group(name=name, layout=data['layout'], label=data['label']))


    for i in groups:
        keys.extend([
            Key(PRIMARY, i.name, GROUP[i.name].toscreen(),                   desc=f"Switch to group {i.name}"),
            Key(ORDER,   i.name, WINDOW.togroup(i.name, switch_group=False), desc=f"Switch to & move focused window to group {i.name}"),
        ])

    return groups