#!/bin/python3
import os
import json
import sys

#location of the repo
loc = "/home/arjun/arjun/apps/hyperwalset"


def hyperset(c1, wall):
    file = open(f"{loc}/config/hyper/hyprland.conf", "r")
    data = file.read()
    file.close()
    data = data.replace("{insertCol}", c1.strip("#"))
    data = data.replace("{wallpaperset}", wall)
    file = open("/home/arjun/.config/hypr/hyprland.conf", "w")
    file.write(data)
    file.close()


def waybar(c1, c2):
    for i in ["config", "style.css"]:
        file = open(f"{loc}/config/waybar/{i}", "r")
        data = file.read()
        file.close()

        data = data.replace("{insertCol1}", c1)
        data = data.replace("{insertCol2}", c2)

        file = open(f"/home/arjun/.config/waybar/{i}", "w")
        file.write(data)

        # os.system('killall waybar')
        # os.system('waybar -c ~/.config/waybar/config -s ~/.config/waybar/style.css')
        #


if __name__ == "__main__":
    os.system("rm /home/arjun/.cache/wal/schemes/*")
    os.system(f"swaybg -m fill -i {sys.argv[1]} & wal -i {sys.argv[1]}")

    dirs = os.listdir("/home/arjun/.cache/wal/schemes/")
    jsfile = dirs[0]

    file = open(f"/home/arjun/.cache/wal/schemes/{jsfile}")

    data = json.load(file)
    colors = data["colors"]
    c1, c2 = colors["color1"], colors["color15"]
    walldata = "~/arjun/"+data["wallpaper"].strip('/home/arjun/')
    hyperset(c1, walldata)
    waybar(c1, c2)
    print(walldata)
