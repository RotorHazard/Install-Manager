from time import sleep
import os
import sys

def main():
	os.system("clear")
	print("\n\n\t\t\tAutomatic update and installation of ROTORHAZARD racing-timer software")
	print("\n\n\tThis script will automatically install or update RotorHazard software on your raspberry. ")
	print("\n\tASource will be main 'master' repository of RotorHazard software on github")
	print("\n\tAll additional software depedancies and libraries also will be installed or updated.")
	print("\n\tYour database and config file will stay on the updated software")
	print("\n\tAfter rebooting please check by typing 'sudo raspi-config' if I2C, SPI and SSH protocols are active.")
	print("\n\tMake sure that you are logged as user 'pi'.")
	print("\n\n\t\t\t\t\t\t\t\t\tEnjoy!")
	print("\n\n\n\t\t 'i' - Install software from skratch")
	print("\n\n\n\t\t 'u' - Update existing installation")
	print("\n\n\n\t\t 'a' - Abort ")
	selection=str(raw_input(""))
	if selection =='i':	
		os.system("clear")
		print("\n\n")
		os.chdir("/home/pi")
		os.system("sudo apt-get update && sudo apt-get upgrade -y")
		os.system("sudo systemctl enable ssh")
		os.system("sudo systemctl start ssh ")
		os.system("sudo apt-get install wget libjpeg-dev python-dev python-rpi.gpio libffi-dev python-smbus build-essential python-pip git scons swig -y")
		os.system("sudo pip install cffi ")
		os.system("sudo pip install pillow")
		os.system("echo 'dtparam=i2c_baudrate=75000' | sudo tee -a /boot/config.txt")
		os.system("echo 'core_freq=250' | sudo tee -a /boot/config.txt")
		os.system("echo 'dtparam=spi=on' | sudo sudo tee -a /boot/config.txt  ")  
		os.chdir("/home/pi")
		os.system("wget https://codeload.github.com/RotorHazard/RotorHazard/zip/master -O temp.zip")
		os.system("unzip temp.zip")
		os.system("rm temp.zip")
		os.system("mv RotorHazard-master /home/pi/RotorHazard")
		os.system("sudo pip install -r /home/pi/RotorHazard/src/server/requirements.txt")
		os.system("sudo chmod 777 /home/pi/RotorHazard/src/server")
		os.chdir("/home/pi")
		os.system("sudo git clone https://github.com/jgarff/rpi_ws281x.git")
		os.chdir("/home/pi/rpi_ws281x")
		os.system("sudo scons")
		os.chdir("/home/pi/rpi_ws281x/python")
		os.system("sudo python setup.py install")
		os.chdir("/home/pi")
		os.system("sudo git clone https://github.com/chrisb2/pi_ina219.git")
		os.chdir("/home/pi/pi_ina219")
		os.system("sudo python setup.py install")
		os.chdir("/home/pi")
		os.system("sudo git clone https://github.com/rm-hull/bme280.git")
		os.chdir("/home/pi/bme280")
		os.system("sudo python setup.py install")
		os.system("sudo apt-get install openjdk-8-jdk-headless -y")
		os.system("echo ' ' | sudo tee -a /lib/systemd/system/rotorhazard.service")
		os.system("echo '[Unit]' | sudo tee -a /lib/systemd/system/rotorhazard.service")
		os.system("echo 'Description=RotorHazard Server' | sudo tee -a /lib/systemd/system/rotorhazard.service")
		os.system("echo 'After=multi-user.target' | sudo tee -a /lib/systemd/system/rotorhazard.service")
		os.system("echo ' ' | sudo tee -a /lib/systemd/system/rotorhazard.service")
		os.system("echo '[Service]' | sudo tee -a /lib/systemd/system/rotorhazard.service")
		os.system("echo 'WorkingDirectory=/home/pi/RotorHazard/src/server' | sudo tee -a /lib/systemd/system/rotorhazard.service")
		os.system("echo 'ExecStart=/usr/bin/python server.py' | sudo tee -a /lib/systemd/system/rotorhazard.service")
		os.system("echo ' ' | sudo tee -a /lib/systemd/system/rotorhazard.service")
		os.system("echo '[Install]' | sudo tee -a /lib/systemd/system/rotorhazard.service")
		os.system("echo 'WantedBy=multi-user.target' | sudo tee -a /lib/systemd/system/rotorhazard.service")
		os.system("sudo chmod 644 /lib/systemd/system/rotorhazard.service")
		os.system("sudo systemctl daemon-reload")
		os.system("sudo systemctl enable rotorhazard.service")
		print("\n\n")
		print("\t##############################################")
		print("\t##                                          ##")
		print("\t##         Installation completed!          ##")
		print("\t##                                          ##")
		print("\t##############################################")
		
		
		print("\n\n\tRotorHazard service should start automatically after rebooting")
		def end():
			print("\n\n\n\n\t\tType 'r' to reboot - recommended - or 'e' to exit\n\n\n")
			def endMenu():
				selection=str(raw_input(""))
				if selection =='r':	
					os.system("sudo reboot")
				if selection =='e':	
					print("\n\n\t\t\tBye, bye\n\n\t\t")
					sleep(1.5)
					os.system("clear")
					sys.exit()
				else: 
					end()
			endMenu()	
		end()
	if selection =='u':	
		os.system("sudo systemctl stop rotorhazard")
		os.system("sudo apt-get update && sudo apt-get upgrade -y")
		os.chdir("/home/pi")
		os.system("wget https://codeload.github.com/RotorHazard/RotorHazard/zip/master -O temp.zip")
		os.system("unzip temp.zip")
		os.system("mv RotorHazard RotorHazard.old")
		os.system("mv RotorHazard-master RotorHazard")
		os.system("rm temp.zip")
		os.system("cp RotorHazard.old/src/server/config.json RotorHazard/src/server/")
		os.system("cp RotorHazard.old/src/server/database.db RotorHazard/src/server/")
		os.chdir("/home/pi/RotorHazard/src/server")
		os.system("sudo pip install --upgrade --no-cache-dir -r requirements.txt")
		print("\n\n")
		print("\t##############################################")
		print("\t##                                          ##")
		print("\t##            Updated completed!            ##")
		print("\t##                                          ##")
		print("\t##############################################")
		def end():
			print("\n\n\n\n\t\t\tType 'e' to exit\n\n\n")
			def endMenu():
				selection=str(raw_input(""))
				if selection =='e':	
					print("\n\n\t\t\tBye, bye\n\n\t\t")
					sleep(1.5)
					os.system("clear")
					sys.exit()
				else: 
					end()
			endMenu()	
		end()
	if selection =='a':	
		sys.exit()
	else :
		main()
main()
