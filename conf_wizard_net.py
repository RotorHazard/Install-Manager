import os

from conf_wizard_net_ap import ap_config
from modules import rhim_load_config, clear_the_screen, logo_top, Bcolors
from net_and_ap_man_conf import net_and_ap_conf


def confirm_auto_hotspot(config):
    while True:
        clear_the_screen()
        features_menu_content = """

             {bold} Automatic Hotspot / Wifi setup{endc}
         
         Automatic hotspot will configure your timer to connect to any previously
         known wifi network if detected on startup.  
         
         If no known network is found, the timer will create a self-hosting hotspot
         that can be connected to on address: 10.0.0.5 
         
         The command 'autohotspot' will be available after install to re-detect wifi.
         
                     {green} y - Start auto hotspot config {endc}

                    {yellow} e - Exit to main menu {endc}

                 """.format(bold=Bcolors.BOLD_S, underline=Bcolors.UNDERLINE, endc=Bcolors.ENDC,
                            blue=Bcolors.BLUE, yellow=Bcolors.YELLOW_S, red=Bcolors.RED_S, green=Bcolors.GREEN_S)
        print(features_menu_content)
        selection = input()
        if selection == 'y':
            clear_the_screen()
            os.system(f"sudo /home/{config.user}/RH_Install-Manager/resources/autohotspot/setup_autohotspot.sh")
            print("""
                #######################################################################
                #                                                                     #
                # {bg}   Configuring automatic hotspot is complete {endc}             #
                #                                                                     #
                #              {bold}         Thank you!        {endc}                #
                #                                                                     #
                #######################################################################\n\n
                """.format(nodes_number=config.nodes_number, bold=Bcolors.BOLD_S,
                           bg=Bcolors.BOLD + Bcolors.GREEN + (' ' * 4), endc=Bcolors.ENDC_S))
            input("Press enter to continue:")
        elif selection == 'e':
            break
    pass


def conf_wizard_net(config):
    while True:
        clear_the_screen()
        logo_top(config.debug_mode)
        features_menu_content = """

                            {rmh}NETWORKING MENU{endc}{bold}

                        
                        1 - Setup hotspot - always on (Bookworm)
                        
                        2 - Setup hotspot - always on (Bullseye/Buster)

                        3 - Setup automatic hotspot/Wi-Fi (Bullseye/Buster)

                {yellow}e - Exit to main menu {endc}

                 """.format(rmh=Bcolors.RED_MENU_HEADER, yellow=Bcolors.YELLOW_S, bold=Bcolors.BOLD, endc=Bcolors.ENDC)
        print(features_menu_content)
        selection = input()
        if selection == '1':
            ap_config()
        elif selection == '2':
            net_and_ap_conf(config)
        elif selection == '3':
            confirm_auto_hotspot(config)
        elif selection == 'e':
            break
    pass


def main():
    config = rhim_load_config()
    conf_wizard_net(config)


if __name__ == "__main__":
    main()
