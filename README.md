# i3
Refresh servers before getting started
```bash
sudo pacman -Syy
```
Install i3
```bash
sudo pacman -S i3-gaps i3blocks i3lock i3status
```

Install required packages
```bash
sudo pacman -S xorg xorg-xinit dmenu
```

Reboot your machine or run ```startx``` command in your terminal to change window manager

When **i3: first configuration** window will be shown
1. Hit _Enter_ to generate your own config
2. Choose _Win_ key as a default modifier

[More useful information about i3](https://i3wm.org/docs/userguide.html)

# polybar
Install polybar
```bash
sudo pacman -S polybar
```

Default polybar config
```bash
sudo cp /usr/share/doc/polybar/config ~/.config/polybar/
sudo chown usernmae:username .config/polybar/config
```

Change the access permission for launch.sh
```bash
chmod +x ~/.config/polybar/launch.sh
```

Check if you've addded this to your i3 config file
```bash
exec_always --no-startup-id $HOME/.config/polybar/launch.sh
```

Disable i3's default bar by commenting these
```
bar {
    i3bar_command i3bar
}
```
[More useful information about polybar](https://github.com/polybar/polybar/wiki)

# dunst
Install dunst
```bash
sudo pacman -S dunst
```

Add this to your .xinitrc file
```bash
dunst > /dev/null 2>&1 &
```

## i3-battery-popup
Clone i3-battery-popup package
```bash
git clone https://aur.archlinux.org/i3-battery-popup-git.git
```
Then change your current working directory to ```i3-battery-popup-git```

And finally run this
```bash
makepkg -si
```

Add this to your i3 config to get battery popups
```bash
exec_always --no-startup-id i3-battery-popup -n -L 20 -l 15 -t 60s
```

[More useful information about dunst](https://wiki.archlinux.org/index.php/Dunst)
[More useful information about i3-battery-popup](https://github.com/rjekker/i3-battery-popup)
