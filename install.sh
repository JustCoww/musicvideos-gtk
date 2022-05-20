#!/usr/bin/sh
echo "Installing musicvideos pip packages"
pip install --upgrade musicvideos-extras;
pip install --upgrade pygobject;
sleep 1s
clear
echo "Downloading..."
sudo curl -H "Cache-Control: no-cache" "https://raw.githubusercontent.com/JustCoww/musicvideos-gtk/main/bin/musicvideos-gtk" -o "/usr/bin/musicvideos-gtk" > /dev/null;
sudo mkdir "/usr/share/musicvideos-gtk/"
sudo curl -H "Cache-Control: no-cache" "https://raw.githubusercontent.com/JustCoww/musicvideos-gtk/main/icons/icon.svg" -o "/usr/share/musicvideos-gtk/icon.svg" > /dev/null;
sudo curl -H "Cache-Control: no-cache" "https://raw.githubusercontent.com/JustCoww/musicvideos-gtk/main/musicvideos-gtk.desktop" -o "/usr/share/applications/org.justcow.musicvideos-gtk.desktop"
sudo chmod +x "/usr/bin/musicvideos-gtk" ;

echo "Done!"
