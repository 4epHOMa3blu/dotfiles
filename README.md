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
[More useful information about i3](https://i3wm.org/docs/userguide.html)

# polybar
Install polybar
```bash
sudo pacman -S polybar
```
Default polybar config
```bash
sudo cp /usr/share/doc/polybar/config ~/.config/polybar/config
sudo chown username:username .config/polybar/config
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
My current polybar appearance
![github-small](https://github.com/4epHOMa3blu/dotfiles/issues/1#issue-725888464)
[More useful information about polybar](https://github.com/polybar/polybar/wiki)

# ranger
Install ranger
```bash
sudo pacman -S ranger
```
Default ranger config
```bash
ranger --copy-config=all
```
```ranger``` uses 4 main configuration files:
* ```commands.py``` contains various functions' implementation, written in Python, used to modify ranger's behavior
* ```rc.conf``` is used for setting various options and binding the keys to functions
* ```rifle.conf``` decides which program to use for opening which file
* ```scope.sh``` is a shell script used to generate the previews for various file types\
[More useful information about ranger](https://wiki.archlinux.org/index.php/ranger)\
[Official User Guide](https://github.com/ranger/ranger/wiki/Official-user-guide)

# dunst
Install dunst
```bash
sudo pacman -S dunst
```
Default dunst config
```bash
sudo cp /usr/share/dunst/dunstrc ~/.config/dunst/dunstrc
sudo chown username:username .config/dunst/dunstrc
```
Add this to your .xprofile
```bash 
dunst &
```
[More useful information about dunst](https://wiki.archlinux.org/index.php/Dunst)

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
Add this to your .xinitrc file to get battery popups
```bash
exec --no-startup-id i3-battery-popup -n -L 20 -l 15 -t 60s
```
[More useful information about i3-battery-popup](https://github.com/rjekker/i3-battery-popup)

# Dotfiles

## .Xresources
Add a file named ```.Xresources``` to your **$HOME** directory\
Make sure that you have this line in your .xinitrc file
```bash
userresources=$HOME/.Xresources
```
[More useful information about .Xresources](https://wiki.debian.org/Xresources)

## .xprofile
Add a file named ```.xprofile``` to your **$HOME** directory\
Don't forget to put a **&** sign at the end of each command line
Line example:
```bash
dunst &
```
[More useful information about .xprofile](https://wiki.archlinux.org/index.php/Xprofile)
