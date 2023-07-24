#!/bin/bash

cd /home/"${1}"/RH_Install-Manager || exit
mkdir log_data >/dev/null 2>&1
rm log_data/log.txt >/dev/null 2>&1
echo >./ log_data / log.txt
echo -------------------------------- | tee -a ./log_data/log.txt
echo OS info | tee -a ./log_data/log.txt
echo | tee -a ./log_data/log.txt
cat /etc/os-release | tee -a ./log_data/log.txt
echo | tee -a ./log_data/log.txt
echo -------------------------------- | tee -a ./log_data/log.txt
echo RH_Install-Manager version | tee -a ./log_data/log.txt
echo | tee -a ./log_data/log.txt
cat ~/RH_Install-Manager/version.txt | tee -a ./log_data/log.txt
echo | tee -a ./log_data/log.txt
echo -------------------------------- | tee -a ./log_data/log.txt
echo RH_Install-Manager directory | tee -a ./log_data/log.txt
echo | tee -a ./log_data/log.txt
find ~/RH_Install-Manager | tee -a ./log_data/log.txt
echo | tee -a ./log_data/log.txt
echo -------------------------------- | tee -a ./log_data/log.txt
echo FILE /boot/config.txt | tee -a ./log_data/log.txt
echo | tee -a ./log_data/log.txt
cat /boot/config.txt | tee -a ./log_data/log.txt
echo | tee -a ./log_data/log.txt
echo | tee -a ./log_data/log.txt
echo -------------------------------- | tee -a ./log_data/log.txt
echo FILE /boot/cmdline.txt | tee -a ./log_data/log.txt
echo | tee -a ./log_data/log.txt
cat /boot/cmdline.txt | tee -a ./log_data/log.txt
echo | tee -a ./log_data/log.txt
echo -------------------------------- | tee -a ./log_data/log.txt
echo DEVICES LIST | tee -a ./log_data/log.txt
echo | tee -a ./log_data/log.txt
ls /dev | grep tty | tee -a ./log_data/log.txt
echo | tee -a ./log_data/log.txt
echo -------------------------------- | tee -a ./log_data/log.txt
echo FILE updater-config.json | tee -a ./log_data/log.txt
echo | tee -a ./log_data/log.txt
cat ~/RH_Install-Manager/updater-config.json | tee -a ./log_data/log.txt
echo | tee -a ./log_data/log.txt
echo -------------------------------- | tee -a ./log_data/log.txt
echo FILE ~/.rhim_markers/rhim_config.txt | tee -a ./log_data/log.txt
echo | tee -a ./log_data/log.txt
cat ~/.rhim_markers/rhim_config.json | tee -a ./log_data/log.txt
echo | tee -a ./log_data/log.txt
echo -- please wait few seconds --
echo -------------------------------- | tee -a ./log_data/log.txt
echo pip3 packages | tee -a ./log_data/log.txt
echo | tee -a ./log_data/log.txt
pip3 freeze | tee -a ./log_data/log.txt
echo | tee -a ./log_data/log.txt
echo -------------------------------- | tee -a ./log_data/log.txt
echo
echo LOGGING TO FILE - DONE
cd /home/"${1}"/RH_Install-Manager || exit
sleep 2
