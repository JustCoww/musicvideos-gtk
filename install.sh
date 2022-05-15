#!/usr/bin/sh
echo "Installing..."
pip3 install --upgrade musicvideos
chmod +x bin/videomacheen
sudo cp bin/videomacheen /usr/bin/
echo "Done!"
