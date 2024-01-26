#!/bin/bash

green="\033[92m"
red="\033[91m"
endc="\033[0m"
underline="\033[4m"

ssh_enabling() {
  sudo systemctl enable ssh || return 1
  sudo systemctl start ssh || return 1
  printf "
     $green -- SSH ENABLED -- $endc


  "
  sleep 3
  return 0
}

ssh_error() {
  printf "
     $red -- SSH enabling error -- $endc

  try manually enabling using 'sudo raspi-config' later
  please: disable end re-enable SSH interface
  than reboot

  Hit 'Enter' to continue

  "
  read -r _
  sleep 2
}

spi_enabling() {
  echo "
[SPI enabled - RH_Install-Manager]
dtparam=spi=on
" | sudo tee -a /boot/config.txt || return 1
  sudo sed -i 's/^blacklist spi-bcm2708/#blacklist spi-bcm2708/' /etc/modprobe.d/raspi-blacklist.conf >>/dev/null 2>&1
  printf "
     $green -- SPI ENABLED -- $endc


  "
  sleep 3
  return 0
}

spi_error() {
  printf "
     $red -- SPI enabling error -- $endc

  try manually enabling using 'sudo raspi-config' later
  please: disable end re-enable SPI interface
  than reboot

  Hit 'Enter' to continue


  "
  read -r _
  sleep 2
}

i2c_enabling() {
  if [ "$(~/RH_Install-Manager/scripts/pi_model_check.sh)" == "pi_4" ]; then
    echo "
Raspberry Pi 4 chipset found
    "
    echo "
[I2C enabled - RH_Install-Manager]
dtparam=i2c_arm=on
  " | sudo tee -a /boot/config.txt || return 1

  elif [ "$(~/RH_Install-Manager/scripts/pi_model_check.sh)" == "pi_5" ]; then
    echo "
Raspberry Pi 5 chipset found
    "
    echo "
[I2C enabled - RH_Install-Manager]
dtparam=i2c_arm=on
dtoverlay=i2c1-pi5
  " | sudo tee -a /boot/config.txt || return 1

  else
    echo "
[I2C enabled - RH_Install-Manager]
dtparam=i2c_baudrate=75000
core_freq=250
i2c-bcm2708
i2c-dev
dtparam=i2c1=on
dtparam=i2c_arm=on
  " | sudo tee -a /boot/config.txt || return 1
#    sudo sed -i 's/^blacklist i2c-bcm2708/#blacklist i2c-bcm2708/' /etc/modprobe.d/raspi-blacklist.conf || return 1

  fi
  printf "
     $green -- I2C ENABLED -- $endc


     "
  sleep 3
  return 0
}

i2c_error() {
  printf "
     $red -- I2C enabling error -- $endc

  try manually enabling using 'sudo raspi-config' later
  please: disable end re-enable I2C interface
  than reboot

  Hit 'Enter' to continue

  "
  read -r _
  sleep 2
}

uart_enabling() {
  sudo cp /boot/cmdline.txt /boot/cmdline.txt.dist
  sudo cp /boot/firmware/cmdline.txt /boot/firmware/cmdline.txt.dist || sudo cp /boot/config.txt /boot/config.txt.dist || return 1
  if [ "$(~/RH_Install-Manager/scripts/pi_model_check.sh)" == "pi_5" ]; then
    echo "
[UART enabled - RH_Install-Manager]
enable_uart=1
dtoverlay=miniuart-bt
dtoverlay=uart0-pi5
  " | sudo tee -a /boot/config.txt || return 1
  else
    echo "
[UART enabled - RH_Install-Manager]
enable_uart=1
dtoverlay=miniuart-bt
  " | sudo tee -a /boot/config.txt || return 1
  sudo raspi-config nonint do_serial_hw 0

  fi
  sudo sed -i 's/console=serial0,115200//g' /boot/firmware/cmdline.txt || echo
  sudo sed -i 's/console=serial0,115200//g' /boot/cmdline.txt || echo
  echo "console serial output disabled - requires REBOOT
  "
  sudo raspi-config nonint do_serial_cons 1

  sleep 2

  printf "
     $green -- UART ENABLED -- $endc


     "
  sleep 3
  return 0
}

uart_error() {
  printf "
     $red -- UART enabling error -- $endc

  try manually enabling using 'sudo raspi-config'
  please: disable end re-enable UART interface
  than reboot

  Hit 'Enter' to continue

  "
  read -r _
  sleep 2
}

if [ "${1}" = "ssh" ]; then
  ssh_enabling || ssh_error
fi

if [ "${1}" = "spi" ]; then
  spi_enabling || spi_error
fi

if [ "${1}" = "i2c" ]; then
  i2c_enabling || i2c_error
fi

if [ "${1}" = "uart" ]; then
  uart_enabling || uart_error
fi

reboot_message() {
  echo "

  Process completed. Please reboot Raspberry Pi now.

  "
}

if [ "${1}" = "all" ]; then
  ssh_enabling || ssh_error
  spi_enabling || spi_error
  i2c_enabling || i2c_error
  uart_enabling || uart_error
fi
