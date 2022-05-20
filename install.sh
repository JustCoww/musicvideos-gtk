#!/usr/bin/sh
echo "Installing musicvideos pip package"
pip install --upgrade musicvideos > /dev/null ;
sleep 1s
echo "Downloading..."
sudo curl "https://raw.githubusercontent.com/JustCoww/musicvideos-gtk/main/bin/musicvideos-gtk" -o "/usr/bin/musicvideos-gtk" > /dev/null;
sudo curl "https://raw.githubusercontent.com/JustCoww/musicvideos-gtk/main/icons/icon.svg" -o "/usr/share/musicvideos-gtk/icon.svg" > /dev/null;
sudo curl "https://raw.githubusercontent.com/JustCoww/musicvideos-gtk/main/musicvideos-gtk.desktop" -o "/usr/share/applications/org.justcow.musicvideos-gtk.desktop"
sudo chmod +x "/usr/bin/musicvideos-gtk" ;

echo "Done!"
