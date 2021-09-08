

echo none > /sys/class/leds/beaglebone\:green\:usr0/trigger
echo none > /sys/class/leds/beaglebone\:green\:usr1/trigger
echo none > /sys/class/leds/beaglebone\:green\:usr2/trigger
echo none > /sys/class/leds/beaglebone\:green\:usr3/trigger

wget https://download.tinkerforge.com/apt/$(lsb_release -is | tr [A-Z] [a-z])/archive.key -q -O - | sudo apt-key add -
sudo sh -c "echo 'deb https://download.tinkerforge.com/apt/$(lsb_release -is | tr [A-Z] [a-z]) $(lsb_release -cs) main' > /etc/apt/sources.list.d/tinkerforge.list"
sudo apt update
sudo apt install brickd

sudo apt install python3-pip
pip3 install json
pip3 install paho-mqtt
sudo apt install python3-tinkerforge
