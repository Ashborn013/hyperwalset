#!/bin/python3
import os
import json
import sys
username='arjun'
#location of the repo
loc = f"/home/{username}/apps/hyperwalset"


def hyperset(c1, wall):
    file = open(f"{loc}/config/hyper/hyprland.conf", "r")
    data = file.read()
    file.close()
    data = data.replace("{insertCol}", c1.strip("#"))
    data = data.replace("{wallpaperset}", wall)
    file = open(f"/home/{username}/.config/hypr/hyprland.conf", "w")
    file.write(data)
    file.close()


def waybar(c1, c2):
    for i in ["style.css"]:
        file = open(f"{loc}/config/waybar/{i}", "r")
        data = file.read()
        file.close()

        data = data.replace("{insertCol1}", c1)
        data = data.replace("{insertCol2}", c2)

        file = open(f"/home/{username}/.config/waybar/{i}", "w")
        file.write(data)

def wofi(c1, c2):
    for i in ["style.css"]:
        file = open(f"{loc}/config/wofi/{i}", "r")
        data = file.read()
        file.close()

        data = data.replace("{insertCol1}", c1)
        data = data.replace("{insertCol2}", c2)

        file = open(f"/home/{username}/.config/wofi/{i}", "w")
        file.write(data)



if __name__ == "__main__":
    os.system(f"rm /home/{username}/.cache/wal/schemes/*")
    os.system(f"swaybg -m fill -i {sys.argv[1]} & wal -i {sys.argv[1]}")

    dirs = os.listdir(f"/home/{username}/.cache/wal/schemes/")
    jsfile = dirs[0]

    file = open(f"/home/{username}/.cache/wal/schemes/{jsfile}")

    data = json.load(file)
    colors = data["colors"]
    c1, c2 = colors["color1"], colors["color15"]
    walldata = f"~/"+data["wallpaper"].strip(f'/home/{username}/')
    hyperset(c1, walldata)
    waybar(c1, c2)
    wofi(c1,c2)

