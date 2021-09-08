



wget https://download.tinkerforge.com/apt/$(lsb_release -is | tr [A-Z] [a-z])/archive.key -q -O - | sudo apt-key add -
sudo sh -c "echo 'deb https://download.tinkerforge.com/apt/$(lsb_release -is | tr [A-Z] [a-z]) $(lsb_release -cs) main' > /etc/apt/sources.list.d/tinkerforge.list"
sudo apt update
sudo apt install brickd

sudo apt install tinkerforge-mqtt