# musicvideos-gtk

![image](https://user-images.githubusercontent.com/68345611/169414982-e716c322-4de6-4149-ac8d-1eb697ebb4be.png)


## Install
```shell
echo "Installing musicvideos pip package"
pip install --upgrade musicvideos > /dev/null ;
sleep 1s
echo "Downloading binary to /usr/bin/musicvideos-gtk"
sudo curl "https://raw.githubusercontent.com/JustCoww/musicvideos-gtk/main/bin/musicvideos-gtk" -o "/usr/bin/musicvideos-gtk" > /dev/null;
sudo chmod +x "/usr/bin/musicvideos-gtk" ;

echo "Done!"
```

## Update
```shell
echo "Removing old binary"
sudo rm "/usr/bin/musicvideos-gtk" ;
sleep 1s
echo "Installing musicvideos pip package"
pip install --upgrade musicvideos > /dev/null ;
sleep 1s
echo "Downloading binary to /usr/bin/musicvideos-gtk"
sudo curl "https://raw.githubusercontent.com/JustCoww/musicvideos-gtk/main/bin/musicvideos-gtk" -o "/usr/bin/musicvideos-gtk" > /dev/null;
sudo chmod +x "/usr/bin/musicvideos-gtk" ;

echo "Done!"
```

## Uninstall
```shell
echo "Removing binary"
sudo rm "/usr/bin/musicvideos-gtk" ;
sleep 1s

echo "Done!"
```
### Uninstall python library
```shell
pip uninstall musicvideos
```
