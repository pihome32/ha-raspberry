



wget https://download.tinkerforge.com/apt/$(lsb_release -is | tr [A-Z] [a-z])/archive.key -q -O - | sudo apt-key add -
sudo sh -c "echo 'deb https://download.tinkerforge.com/apt/$(lsb_release -is | tr [A-Z] [a-z]) $(lsb_release -cs) main' > /etc/apt/sources.list.d/tinkerforge.list"
sudo apt update
sudo apt install brickd

<<<<<<< HEAD
sudo apt install tinkerforge-mqtt
=======
sudo apt install python3-pip
pip3 install json
pip3 install paho-mqtt
sudo apt install python3-tinkerforge
>>>>>>> 5b98d8e90f6b972921b860db322873395b4eeb22
