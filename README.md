# .config

## i3

## polybar
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
