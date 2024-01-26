from rpi_update import installation
import os
import sys
import pwd
from modules import write_json, load_json
from compatibility_check import main as compatibility_check


def name_check():
    username = pwd.getpwuid(os.getuid()).pw_name
    return username


def main():
    username = name_check()
    compatibility_check()
    passed_install_step = os.getenv('INSTALL_STEP')
    if passed_install_step not in ['1', '2', 'wifi']:
        print("\n\n\tPlease specify the install step with the ./nh-install.sh command:"
              "\n\t'./nh-install.sh 1/2/wifi'\n")
        input("\n\n\tHit 'Enter' to exit and try again.\n")
        sys.exit()
    config_file = "./nh-updater-config.json"
    config = load_json(config_file)
    config.user = username
    write_json(config, config_file)
    installation(True, config, False, passed_install_step)


if __name__ == "__main__":
    main()
