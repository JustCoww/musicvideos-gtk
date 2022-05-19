#!/usr/bin/sh
echo "Installing..."
pip3 install --upgrade musicvideos
chmod +x bin/*
sudo cp bin/* /usr/bin/
echo "Done!"
