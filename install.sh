
sudo apt install git
bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)

wget https://download.tinkerforge.com/apt/$(. /etc/os-release; echo $ID)/tinkerforge.gpg -q -O - | sudo tee /etc/apt/trusted.gpg.d/tinkerforge.gpg > /dev/null
echo "deb https://download.tinkerforge.com/apt/$(. /etc/os-release; echo $ID $VERSION_CODENAME) main" | sudo tee /etc/apt/sources.list.d/tinkerforge.list
sudo apt update

sudo apt install brickd

sudo apt install tinkerforge-mqtt

sudo apt install python3-pip
pip3 install json
pip3 install paho-mqtt
sudo apt install python3-tinkerforge



sudo systemctl enable nodered.service
