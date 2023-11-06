#!/bin/bash

red="\033[91m"
yellow="\033[93m"
green="\033[92m"
endc="\033[0m"

time_warning_show() {
  echo "


      Installing additional software may take few minutes

"
}

sudo apt-get update && sudo apt-get --with-new-pkgs upgrade -y
sudo apt-get install libjpeg-dev ntp htop iptables -y python*-venv
sudo apt autoremove -y
sudo chmod -R 777 "/home/${1}/RotorHazard" # to ensure smooth operation if files in RH directory were edited etc. and permissions changed
upgradeDate="$(date +%Y%m%d%H%M)"
cd /home/"${1}" || exit
if [ -d "/home/${1}/RotorHazard" ]; then
  # Control will enter here if $DIRECTORY exists.
  mv "/home/${1}/RotorHazard" "/home/${1}/RotorHazard_${upgradeDate}" || exit 1
fi
if [ -d "/home/${1}/RotorHazard-*" ]; then
  # Control will enter here if $DIRECTORY exists.
  mv "/home/${1}/RotorHazard-*" "/home/${1}/RotorHazard_${2}_${upgradeDate}" || exit 1
fi
sudo rm -r /home/"${1}"/temp.zip >/dev/null 2>&1 # in case of weird sys config or previous unsuccessful installations
cd /home/"${1}" || exit
wget https://codeload.github.com/RotorHazard/RotorHazard/zip/"${2}" -O temp.zip
unzip temp.zip
rm ~/wget* >/dev/null 2>&1
mv /home/"${1}"/RotorHazard-* /home/"${1}"/RotorHazard
sudo rm temp.zip
sudo mkdir /home/"${1}"/backup_RH_data >/dev/null 2>&1
sudo chmod 777 -R /home/"${1}"/RotorHazard/src/server
sudo chmod 777 -R /home/"${1}"/RotorHazard_"${upgradeDate}"
sudo chmod 777 -R /home/"${1}"/backup_RH_data
sudo chmod 777 -R /home/"${1}"/.rhim_markers
sudo chmod 777 -R ~/RotorHazard
cp /home/"${1}"/RotorHazard_"${upgradeDate}"/src/server/config.json /home/"${1}"/RotorHazard/src/server/ >/dev/null 2>&1 &
cp -r /home/"${1}"/RotorHazard_"${upgradeDate}"/src/server/static /home/"${1}"/backup_RH_data
cp -r /home/"${1}"/RotorHazard_"${upgradeDate}"/src/server/static/user/* /home/"${1}"/RotorHazard/src/server/static/user/ || printf "\n no user folder found in this RotorHazard version - skipping \n" #rh_pr
mkdir /home/"${1}"/RotorHazard/src/server/db_bkp
cp -r /home/"${1}"/RotorHazard_"${upgradeDate}"/src/server/db_bkp/* /home/"${1}"/RotorHazard/src/server/db_bkp/ || printf "\n no backup folder found in this RotorHazard version - skipping \n" #rh_pr
cp -r /home/"${1}"/RotorHazard_"${upgradeDate}"/src/server/static/image /home/"${1}"/RotorHazard/src/server/static/image
cp /home/"${1}"/RotorHazard_"${upgradeDate}"/src/server/config.json /home/"${1}"/backup_RH_data >/dev/null 2>&1 &
cp /home/"${1}"/RotorHazard_"${upgradeDate}"/src/server/database.db /home/"${1}"/RotorHazard/src/server/ >/dev/null 2>&1 &
cp /home/"${1}"/RotorHazard_"${upgradeDate}"/src/server/database.db /home/"${1}"/backup_RH_data >/dev/null 2>&1 &
time_warning_show
cd /home/"${1}"/RotorHazard/src/server || echo "$red missing RotorHazard directory"
python -m venv venv
source venv/bin/activate
pip3 install --upgrade pip
pip3 install --upgrade --no-cache-dir -r requirements.txt
pip3 install cffi pillow

### python 3 transition handling ###

PYTHON3_CONVERSION_FLAG_FILE=/home/"${1}"/.rhim_markers/python3_support_was_added

if ! test -f "$PYTHON3_CONVERSION_FLAG_FILE"; then

  SERVICE_FILE=/lib/systemd/system/rotorhazard.service
  old_python_service_statement="ExecStart=/usr/bin/python server.py"

  if test -f "$SERVICE_FILE"; then

    if grep -Fxq "$old_python_service_statement" "$SERVICE_FILE"; then
      printf "\n"
      echo "old python based RotorHazard autostart service found"
      sudo sed -i 's/python/python3/g' "$SERVICE_FILE"
      echo "changed to python3 based service"
    else
      echo "RotorHazard autostart service is up to date"
    fi
  else
    echo "no RotorHazard autostart service found - no changes"
  fi

  printf "\n"

  if grep -Fq "python server.py" "/home/"${1}"/.bashrc"; then
    echo "old python based server-start alias found"
    sed -i 's/python server.py/python3 server.py/g' ~/.bashrc
    echo "'ss' alias changed to python3 version"
  fi

  ### sensors transition to python3 handling ###

  printf "\n\n    Converting existing sensors libraries to python3 versions \n\n\n"

  INA_SENSOR_FILES=/home/"${1}"/pi_ina219

  if test -d "$INA_SENSOR_FILES"; then
    cd /home/"${1}" || exit
    sudo rm -r "$INA_SENSOR_FILES" || exit
    sudo git clone https://github.com/chrisb2/pi_ina219.git
    cd /home/"${1}"/pi_ina219 || exit
    printf "\n\n  INA sensor library will be updated to python3 \n\n"
    sudo python3 setup.py install
  fi

  BME_SENSOR_FILES=/home/"${1}"/bme280

  if test -d "$INA_SENSOR_FILES"; then
    cd /home/"${1}" || exit
    sudo rm -r "$BME_SENSOR_FILES" || exit
    sudo git clone https://github.com/rm-hull/bme280.git
    cd /home/"${1}"/bme280 || exit
    printf "\n\n  BME sensor library will be updated to python3 \n\n"
    sudo python3 setup.py install
  fi

#  LEDS_LIBRARY_FILES=/home/"${1}"/rpi_ws281x
#
#  if test -d "$LEDS_LIBRARY_FILES"; then
#    cd /home/"${1}" || exit
#    sudo rm -r "$LEDS_LIBRARY_FILES" || exit
#    sudo git clone https://github.com/jgarff/rpi_ws281x.git
#    cd /home/"${1}"/rpi_ws281x || exit
#    printf "\n\n  LEDs controller library will be updated to python3  \n\n"
#    sudo scons
#    cd /home/"${1}"/rpi_ws281x/python || exit
#    sudo python3 setup.py install
#  fi
# above - obsolete - keeping here for now

  touch "$PYTHON3_CONVERSION_FLAG_FILE"

  echo "


      supporting libraries updated to python3

"

fi

# added because of the broken Adafruit_GPIO compatibility on Raspbian 11 Bullseye
(sudo sed -i 's/UNKNOWN          = 0/UNKNOWN          = 1/' /usr/local/lib/python3*/dist-packages/Adafruit_GPIO/Platform.py && \
printf "\n $green Adafruit_GPIO compatibility is now OK $endc \n\n") || \
(printf "$endc \nAdafruit_GPIO compatibility file probably missing \n\n $endc" && sleep 2)

# port forwarding
if ! grep -q "sudo iptables -A PREROUTING -t nat -p tcp --dport 8080 -j REDIRECT --to-ports 80" /etc/rc.local; then
cd /home/"${1}"/RH_Install-Manager/scripts/ || exit
sudo ./iptables_conf.sh
fi

cd /home/"${1}" || exit
