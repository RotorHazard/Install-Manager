from time import sleep
import os
import json
from modules import clear_the_screen, Bcolors, logo_top, check_if_string_in_file

"""
This is obsolete flashing protocol, left here only for some users.
New version is in i2c_nodes_flash.py file.
"""


def main():
    if os.path.exists("./updater-config.json"):
        with open('updater-config.json') as config_file:
            data = json.load(config_file)
    else:
        with open('distr-updater-config.json') as config_file:
            data = json.load(config_file)

    if os.path.exists("./updater-config.json"):
        if check_if_string_in_file('updater-config.json', 'assignment'):
            pins_assignment = data['pins_assignment']
        else:
            pins_assignment = 'default'
    else:
        pins_assignment = 'default'

    preferred_rh_version = data['RH_version']

    if preferred_rh_version == 'master':
        firmware_version = 'master'
    if preferred_rh_version == 'beta':
        firmware_version = 'beta'
    if preferred_rh_version == 'stable':
        firmware_version = 'stable'
    if preferred_rh_version == 'custom':
        firmware_version = 'stable'

    nodes_number = data['nodes_number']

    # default to default pins. only update if they said so.
    reset_1 = 12  # node 1   # default 12
    reset_2 = 16  # node 2   # default 16
    reset_3 = 20  # node 3   # default 20
    reset_4 = 21  # node 4   # default 21
    reset_5 = 6  # node 5   # default 6
    reset_6 = 13  # node 6   # default 13
    reset_7 = 19  # node 7   # default 19
    reset_8 = 26  # node 8   # default 26
    if pins_assignment == 'PCB' or pins_assignment == 'pcb':
        reset_1 = 12  # node 1   # default 12
        reset_2 = 16  # node 2   # default 16
        reset_3 = 4  # node 3   # default 4
        reset_4 = 21  # node 4   # default 21
        reset_5 = 6  # node 5   # default 6
        reset_6 = 13  # node 6   # default 13
        reset_7 = 19  # node 7   # default 19
        reset_8 = 26  # node 8   # default 26
    if pins_assignment == 'custom':
        reset_1 = 0  # node 1   # custom pin assignment
        reset_2 = 0  # node 2   # custom pin assignment
        reset_3 = 0  # node 3   # custom pin assignment
        reset_4 = 0  # node 4   # custom pin assignment
        reset_5 = 0  # node 5   # custom pin assignment
        reset_6 = 0  # node 6   # custom pin assignment
        reset_7 = 0  # node 7   # custom pin assignment
        reset_8 = 0  # node 8   # custom pin assignment

    if data['debug_mode']:
        linux_testing = True
    else:
        linux_testing = False

    if linux_testing:
        user = data['debug_user']
    else:
        user = data['pi_user']

    if not linux_testing:
        try:
            import RPi.GPIO as GPIO
        except ImportError:
            import RPi.GPIO as GPIO
            print("RPi.GPIO ImportError")

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
        GPIO.setup(reset_1, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(reset_2, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(reset_3, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(reset_4, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(reset_5, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(reset_6, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(reset_7, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(reset_8, GPIO.OUT, initial=GPIO.HIGH)

        # def all_pins_low():
        #     GPIO.output(reset_1, GPIO.LOW)
        #     GPIO.output(reset_2, GPIO.LOW)
        #     GPIO.output(reset_3, GPIO.LOW)
        #     GPIO.output(reset_4, GPIO.LOW)
        #     GPIO.output(reset_5, GPIO.LOW)
        #     GPIO.output(reset_6, GPIO.LOW)
        #     GPIO.output(reset_7, GPIO.LOW)
        #     GPIO.output(reset_8, GPIO.LOW)
        #     sleep(0.05)

        def all_pins_high():
            GPIO.output(reset_1, GPIO.HIGH)
            GPIO.output(reset_2, GPIO.HIGH)
            GPIO.output(reset_3, GPIO.HIGH)
            GPIO.output(reset_4, GPIO.HIGH)
            GPIO.output(reset_5, GPIO.HIGH)
            GPIO.output(reset_6, GPIO.HIGH)
            GPIO.output(reset_7, GPIO.HIGH)
            GPIO.output(reset_8, GPIO.HIGH)
            sleep(0.05)

        # def all_pins_reset():
        #     GPIO.output(reset_1, GPIO.LOW)
        #     GPIO.output(reset_2, GPIO.LOW)
        #     GPIO.output(reset_3, GPIO.LOW)
        #     GPIO.output(reset_4, GPIO.LOW)
        #     GPIO.output(reset_5, GPIO.LOW)
        #     GPIO.output(reset_6, GPIO.LOW)
        #     GPIO.output(reset_7, GPIO.LOW)
        #     GPIO.output(reset_8, GPIO.LOW)
        #     sleep(0.1)
        #     GPIO.output(reset_1, GPIO.HIGH)
        #     GPIO.output(reset_2, GPIO.HIGH)
        #     GPIO.output(reset_3, GPIO.HIGH)
        #     GPIO.output(reset_4, GPIO.HIGH)
        #     GPIO.output(reset_5, GPIO.HIGH)
        #     GPIO.output(reset_6, GPIO.HIGH)
        #     GPIO.output(reset_7, GPIO.HIGH)
        #     GPIO.output(reset_8, GPIO.HIGH)

        def node_one_reset():
            all_pins_high()
            GPIO.output(reset_1, GPIO.LOW)
            sleep(0.1)
            GPIO.output(reset_1, GPIO.HIGH)

        def node_two_reset():
            all_pins_high()
            GPIO.output(reset_2, GPIO.LOW)
            sleep(0.1)
            GPIO.output(reset_2, GPIO.HIGH)

        def node_three_reset():
            all_pins_high()
            GPIO.output(reset_3, GPIO.LOW)
            sleep(0.1)
            GPIO.output(reset_3, GPIO.HIGH)

        def node_four_reset():
            all_pins_high()
            GPIO.output(reset_4, GPIO.LOW)
            sleep(0.1)
            GPIO.output(reset_4, GPIO.HIGH)

        def node_five_reset():
            all_pins_high()
            GPIO.output(reset_5, GPIO.LOW)
            sleep(0.1)
            GPIO.output(reset_5, GPIO.HIGH)

        def node_six_reset():
            all_pins_high()
            GPIO.output(reset_6, GPIO.LOW)
            sleep(0.1)
            GPIO.output(reset_6, GPIO.HIGH)

        def node_seven_reset():
            all_pins_high()
            GPIO.output(reset_7, GPIO.LOW)
            sleep(0.1)
            GPIO.output(reset_7, GPIO.HIGH)

        def node_eight_reset():
            all_pins_high()
            GPIO.output(reset_8, GPIO.LOW)
            sleep(0.1)
            GPIO.output(reset_8, GPIO.HIGH)

    if linux_testing:
        # def all_pins_reset():
        #     print(f"\n\n\t\t\t/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/X.hex")
        #     print("\n\t\t\t\t\t Linux - PC\n\n")
        #     sleep(0.3)
        #
        # def all_pins_low():
        #     print(f"\n\n\t\t\t/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/X.hex")
        #     print("\n\t\t\t\t\t Linux - PC\n\n")
        #     sleep(0.3)

        def all_pins_high():
            print(f"\n\n\t\t\t/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/X.hex")
            print("\n\t\t\t\t\t Linux - PC\n\n")
            sleep(0.3)

        def node_one_reset():
            print(f"\n\n\t\t\t/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/X.hex")
            print("\n\t\t\t\t\t Linux - PC\n\n")
            sleep(0.3)

        def node_two_reset():
            print(f"\n\n\t\t\t/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/X.hex")
            print("\n\t\t\t\t\t Linux - PC\n\n")
            sleep(0.3)

        def node_three_reset():
            print(f"\n\n\t\t\t/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/X.hex")
            print("\n\t\t\t\t\t Linux - PC\n\n")
            sleep(0.3)

        def node_four_reset():
            print(f"\n\n\t\t\t/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/X.hex")
            print("\n\t\t\t\t\t Linux - PC\n\n")
            sleep(0.3)

        def node_five_reset():
            print(f"\n\n\t\t\t/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/X.hex")
            print("\n\t\t\t\t\t Linux - PC\n\n")
            sleep(0.3)

        def node_six_reset():
            print(f"\n\n\t\t\t/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/X.hex")
            print("\n\t\t\t\t\t Linux - PC\n\n")
            sleep(0.3)

        def node_seven_reset():
            print(f"\n\n\t\t\t/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/X.hex")
            print("\n\t\t\t\t\t Linux - PC\n\n")
            sleep(0.3)

        def node_eight_reset():
            print(f"\n\n\t\t\t/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/X.hex")
            print("\n\t\t\t\t\t Linux - PC\n\n")
            sleep(0.3)

    def logo_update():
        print("""
        #######################################################################
        #                                                                     #
        #{bold}{s}Flashing firmware onto {nodes_number} nodes - DONE{endc}{s}#
        #                                                                     #
        #                          {bold}Thank you!{endc}                     #
        #                                                                     #
        #######################################################################\n\n
        """.format(nodes_number=nodes_number, bold=Bcolors.BOLD_S, underline=Bcolors.UNDERLINE_S, endc=Bcolors.ENDC_S,
                   blue=Bcolors.BLUE, yellow=Bcolors.YELLOW_S, red=Bcolors.RED_S, orange=Bcolors.ORANGE_S, s=10 * ' '))

    def flash_all_nodes():
        node_one_reset()
        os.system(f"sudo avrdude -v -p atmega328p -c arduino -P /dev/ttyS0 -b 57600 -U \
        flash:w:/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/node_1.hex:i ")
        print(f"\n\t\t\t\t{Bcolors.BOLD}Node 1 - flashed{Bcolors.ENDC}\n\n")
        sleep(1)
        if nodes_number == 1:
            return
        node_two_reset()
        os.system("sudo avrdude -v -p atmega328p -c arduino -P /dev/ttyS0 -b 57600 -U \
        flash:w:/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/node_2.hex:i ")
        print(f"\n\t\t\t\t{Bcolors.BOLD}Node 2 - flashed{Bcolors.ENDC}\n\n")
        sleep(1)
        if nodes_number == 2:
            return
        node_three_reset()
        os.system(f"sudo avrdude -v -p atmega328p -c arduino -P /dev/ttyS0 -b 57600 -U \
        flash:w:/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/node_3.hex:i ")
        print(f"\n\t\t\t\t{Bcolors.BOLD}Node 3 - flashed{Bcolors.ENDC}\n\n")
        sleep(1)
        if nodes_number == 3:
            return
        node_four_reset()
        os.system(f"sudo avrdude -v -p atmega328p -c arduino -P /dev/ttyS0 -b 57600 -U \
        flash:w:/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/node_4.hex:i ")
        print(f"\n\t\t\t\t{Bcolors.BOLD}Node 4 - flashed{Bcolors.ENDC}\n\n")
        sleep(1)
        if nodes_number == 4:
            return
        node_five_reset()
        os.system(f"sudo avrdude -v -p atmega328p -c arduino -P /dev/ttyS0 -b 57600 -U \
        flash:w:/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/node_5.hex:i ")
        print(f"\n\t\t\t\t{Bcolors.BOLD}Node 5 - flashed{Bcolors.ENDC}\n\n")
        sleep(1)
        if nodes_number == 5:
            return
        node_six_reset()
        os.system(f"sudo avrdude -v -p atmega328p -c arduino -P /dev/ttyS0 -b 57600 -U \
        flash:w:/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/node_6.hex:i ")
        print(f"\n\t\t\t\t{Bcolors.BOLD}Node 6 - flashed{Bcolors.ENDC}\n\n")
        sleep(1)
        if nodes_number == 6:
            return
        node_seven_reset()
        os.system(f"sudo avrdude -v -p atmega328p -c arduino -P /dev/ttyS0 -b 57600 -U \
        flash:w:/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/node_7.hex:i ")
        print(f"\n\t\t\t\t{Bcolors.BOLD}Node 7 - flashed{Bcolors.ENDC}\n\n")
        sleep(1)
        if nodes_number == 7:
            return
        node_eight_reset()
        os.system(f"sudo avrdude -v -p atmega328p -c arduino -P /dev/ttyS0 -b 57600 -U \
        flash:w:/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/node_8.hex:i ")
        print(f"\n\t\t\t\t{Bcolors.BOLD}Node 8 - flashed{Bcolors.ENDC}\n\n")
        if nodes_number == 8:
            return

    def flash_all_gnd():
        node_one_reset()
        os.system(f"sudo avrdude -v -p atmega328p -c arduino -P /dev/ttyS0 -b 57600 -U \
        flash:w:/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/node_0.hex:i ")
        print(f"\n\t\t\t\t{Bcolors.BOLD}Node 1 - flashed{Bcolors.ENDC}\n\n")
        sleep(1)
        if nodes_number == 1:
            return
        node_two_reset()
        os.system(f"sudo avrdude -v -p atmega328p -c arduino -P /dev/ttyS0 -b 57600 -U \
        flash:w:/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/node_0.hex:i ")
        print(f"\n\t\t\t\t{Bcolors.BOLD}Node 2 - flashed{Bcolors.ENDC}\n\n")
        sleep(1)
        if nodes_number == 2:
            return
        node_three_reset()
        os.system(f"sudo avrdude -v -p atmega328p -c arduino -P /dev/ttyS0 -b 57600 -U \
        flash:w:/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/node_0.hex:i ")
        print(f"\n\t\t\t\t{Bcolors.BOLD}Node 3 - flashed{Bcolors.ENDC}\n\n")
        sleep(1)
        if nodes_number == 3:
            return
        node_four_reset()
        os.system(f"sudo avrdude -v -p atmega328p -c arduino -P /dev/ttyS0 -b 57600 -U \
        flash:w:/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/node_0.hex:i ")
        print(f"\n\t\t\t\t{Bcolors.BOLD}Node 4 - flashed{Bcolors.ENDC}\n\n")
        sleep(1)
        if nodes_number == 4:
            return
        node_five_reset()
        os.system(f"sudo avrdude -v -p atmega328p -c arduino -P /dev/ttyS0 -b 57600 -U \
        flash:w:/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/node_0.hex:i ")
        print(f"\n\t\t\t\t{Bcolors.BOLD}Node 5 - flashed{Bcolors.ENDC}\n\n")
        sleep(1)
        if nodes_number == 5:
            return
        node_six_reset()
        os.system(f"sudo avrdude -v -p atmega328p -c arduino -P /dev/ttyS0 -b 57600 -U \
        flash:w:/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/node_0.hex:i ")
        print(f"\n\t\t\t\t{Bcolors.BOLD}Node 6 - flashed{Bcolors.ENDC}\n\n")
        sleep(1)
        if nodes_number == 6:
            return
        node_seven_reset()
        os.system(f"sudo avrdude -v -p atmega328p -c arduino -P /dev/ttyS0 -b 57600 -U \
        flash:w:/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/node_0.hex:i ")
        print(f"\n\t\t\t\t{Bcolors.BOLD}Node 7 - flashed{Bcolors.ENDC}\n\n")
        sleep(1)
        if nodes_number == 7:
            return
        node_eight_reset()
        os.system(f"sudo avrdude -v -p atmega328p -c arduino -P /dev/ttyS0 -b 57600 -U \
        flash:w:/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/node_0.hex:i ")
        print(f"\n\t\t\t\t{Bcolors.BOLD}Node 8 - flashed{Bcolors.ENDC}\n\n")
        if nodes_number == 8:
            return

    def flash_all_blink():
        node_one_reset()
        os.system(f"sudo avrdude -v -p atmega328p -c arduino -P /dev/ttyS0 -b 57600 -U \
        flash:w:/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/blink.hex:i ")
        print(f"\n\t\t\t\t{Bcolors.BOLD}Node 1 - flashed{Bcolors.ENDC}\n\n")
        sleep(1)
        if nodes_number == 1:
            return
        node_two_reset()
        os.system(f"sudo avrdude -v -p atmega328p -c arduino -P /dev/ttyS0 -b 57600 -U \
        flash:w:/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/blink.hex:i ")
        print(f"\n\t\t\t\t{Bcolors.BOLD}Node 2 - flashed{Bcolors.ENDC}\n\n")
        sleep(1)
        if nodes_number == 2:
            return
        node_three_reset()
        os.system(f"sudo avrdude -v -p atmega328p -c arduino -P /dev/ttyS0 -b 57600 -U \
        flash:w:/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/blink.hex:i ")
        print(f"\n\t\t\t\t{Bcolors.BOLD}Node 3 - flashed{Bcolors.ENDC}\n\n")
        sleep(1)
        if nodes_number == 3:
            return
        node_four_reset()
        os.system(f"sudo avrdude -v -p atmega328p -c arduino -P /dev/ttyS0 -b 57600 -U \
        flash:w:/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/blink.hex:i ")
        print(f"\n\t\t\t\t{Bcolors.BOLD}Node 4 - flashed{Bcolors.ENDC}\n\n")
        sleep(1)
        if nodes_number == 4:
            return
        node_five_reset()
        os.system(f"sudo avrdude -v -p atmega328p -c arduino -P /dev/ttyS0 -b 57600 -U \
        flash:w:/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/blink.hex:i ")
        print(f"\n\t\t\t\t{Bcolors.BOLD}Node 5 - flashed{Bcolors.ENDC}\n\n")
        sleep(1)
        if nodes_number == 5:
            return
        node_six_reset()
        os.system(f"sudo avrdude -v -p atmega328p -c arduino -P /dev/ttyS0 -b 57600 -U \
        flash:w:/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/blink.hex:i ")
        print(f"\n\t\t\t\t{Bcolors.BOLD}Node 6 - flashed{Bcolors.ENDC}\n\n")
        sleep(1)
        if nodes_number == 6:
            return
        node_seven_reset()
        os.system(f"sudo avrdude -v -p atmega328p -c arduino -P /dev/ttyS0 -b 57600 -U \
        flash:w:/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/blink.hex:i ")
        print(f"\n\t\t\t\t{Bcolors.BOLD}Node 7 - flashed{Bcolors.ENDC}\n\n")
        sleep(1)
        if nodes_number == 7:
            return
        node_eight_reset()
        os.system(f"sudo avrdude -v -p atmega328p -c arduino -P /dev/ttyS0 -b 57600 -U \
        flash:w:/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/blink.hex:i ")
        print(f"\n\t\t\t\t{Bcolors.BOLD}Node 8 - flashed{Bcolors.ENDC}\n\n")
        if nodes_number == 8:
            return

    def flash_each_node():
        def node_x_menu(sel_node):
            while True:
                print(f"""
                {Bcolors.BOLD}\n\t\t\tNode {str(sel_node)}  selected{Bcolors.ENDC}
                        Choose flashing type:\n{Bcolors.ENDC}
                1 - {Bcolors.GREEN}Node gets own dedicated firmware - recommended{Bcolors.ENDC}{Bcolors.BOLD}
                2 - Node ground-auto selection firmware
                3 - Flashes 'Blink' on the node
                4 - Abort
                {Bcolors.ENDC}""")
                selection = input()
                if selection == '1':
                    node_one_reset()
                    if not linux_testing:
                        os.system(f"sudo avrdude -v -p atmega328p -c arduino -P /dev/ttyS0 -b 57600 -U \
                        flash:w:/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/node_"
                                  + str(sel_node) + ".hex:i ")
                    else:
                        print(f"\t\t\t/home/{user}/RH-ota/firmware/obsolete/{firmware_version}\
                        /node_{str(sel_node)}.hex:i ")
                    print(f"{Bcolors.BOLD}\n\t Node {str(sel_node)} flashed\n{Bcolors.ENDC}")
                    sleep(1.5)
                    return
                if selection == '2':
                    node_one_reset()
                    os.system(f"sudo avrdude -v -p atmega328p -c arduino -P /dev/ttyS0 -b 57600 -U \
                    flash:w:/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/node_0.hex:i")
                    print(f"{Bcolors.BOLD}\n\t Node {str(sel_node)} flashed\n{Bcolors.ENDC}")
                    sleep(1.5)
                    return
                if selection == '3':
                    node_one_reset()
                    os.system(f"sudo avrdude -v -p atmega328p -c arduino -P /dev/ttyS0 -b 57600 -U \
                    flash:w:/home/{user}/RH-ota/firmware/obsolete/{firmware_version}/blink.hex:i ")
                    print(f"{Bcolors.BOLD}\n\t Node {str(sel_node)} flashed\n{Bcolors.ENDC}")
                    sleep(1.5)
                    return
                if selection == '4':
                    break

        def node_menu():
            while True:
                clear_the_screen()
                logo_top(linux_testing)
                sleep(0.05)
                flash_node_menu = """
                                    {red}{bold}NODES MENU{endc}
                                {bold}
                        1 - Flash node 1        5 - Flash node 5
                    
                        2 - Flash node 2        6 - Flash node 6
                    
                        3 - Flash node 3        7 - Flash node 7
                    
                        4 - Flash node 4        8 - Flash node 8
                                {yellow}
                            'e'- Exit to main menu{endc}
                """.format(bold=Bcolors.BOLD, red=Bcolors.RED, yellow=Bcolors.YELLOW, endc=Bcolors.ENDC)
                print(flash_node_menu)
                selection = input("""
                        {bold}Which node do you want to program:{endc} """.format(bold=Bcolors.BOLD, endc=Bcolors.ENDC))
                if selection == '1':
                    node_x_menu(int(selection))
                if selection == '2':
                    node_x_menu(int(selection))
                if selection == '3':
                    node_x_menu(int(selection))
                if selection == '4':
                    node_x_menu(int(selection))
                if selection == '5':
                    node_x_menu(int(selection))
                if selection == '6':
                    node_x_menu(int(selection))
                if selection == '7':
                    node_x_menu(int(selection))
                if selection == '8':
                    node_x_menu(int(selection))
                if selection == 'e':
                    break
                else:
                    continue

        node_menu()

    def gpio_state():
        clear_the_screen()
        logo_top(linux_testing)
        print("\n\n\n")
        os.system(f"echo {reset_1} > /sys/class/GPIO/unexport")
        os.system(f"echo {reset_2} > /sys/class/GPIO/unexport")
        os.system(f"echo {reset_3} > /sys/class/GPIO/unexport")
        os.system(f"echo {reset_4} > /sys/class/GPIO/unexport")
        os.system(f"echo {reset_5} > /sys/class/GPIO/unexport")
        os.system(f"echo {reset_6} > /sys/class/GPIO/unexport")
        os.system(f"echo {reset_7} > /sys/class/GPIO/unexport")
        os.system(f"echo {reset_8} > /sys/class/GPIO/unexport")
        os.system("echo 19 > /sys/class/GPIO/unexport")
        os.system("echo 20 > /sys/class/GPIO/unexport")
        os.system("echo 21 > /sys/class/GPIO/unexport")
        print("\n\n        DONE\n\n")
        sleep(0.3)

    # def connectionTest():
    # nodeOneReset()
    # os.system("sudo avrdude -c arduino -p m328p -v")
    # sleep(2)
    # if nodes_number == 1:
    # return
    # nodeTwoReset()
    # os.system("sudo avrdude -c arduino -p m328p -v")
    # sleep(2)
    # if nodes_number == 2:
    # return
    # nodeThreeReset()
    # os.system("sudo avrdude -c arduino -p m328p -v")
    # sleep(2)
    # if nodes_number == 3:
    # return
    # nodeFourReset()
    # os.system("sudo avrdude -c arduino -p m328p -v")
    # sleep(2)
    # if nodes_number == 4:
    # return
    # nodeFiveReset()
    # os.system("sudo avrdude -c arduino -p m328p -v")
    # sleep(2)
    # if nodes_number == 5:
    # return
    # nodeSixReset()
    # os.system("sudo avrdude -c arduino -p m328p -v")
    # sleep(2)
    # if nodes_number == 6:
    # return
    # nodeSevenReset()
    # os.system("sudo avrdude -c arduino -p m328p -v")
    # sleep(2)
    # if nodes_number == 7:
    # return
    # nodeEightReset()
    # os.system("sudo avrdude -c arduino -p m328p -v")
    # sleep(2)
    # if nodes_number == 8:
    # return

    def nodes_update():
        while True:
            clear_the_screen()
            logo_top(linux_testing)
            sleep(0.05)
            node_menu = """\n
                            {bold}{underline}CHOOSE FLASHING TYPE:{endc}
            
                    {green}{bold}1 - Every Node gets own dedicated firmware - rec.{endc}
                    
                    {bold}2 - Nodes using ground-auto numbering firmware
                    
                    3 - Flash 'Blink' on every node
                    
                    4 - Flash each node individually
                    
                    5 - Fix GPIO pins state - obsolete
                    
                    {yellow}e - Exit to main menu{endc}
            """.format(bold=Bcolors.BOLD, green=Bcolors.GREEN, yellow=Bcolors.YELLOW,
                       endc=Bcolors.ENDC, underline=Bcolors.UNDERLINE)
            print(node_menu)
            sleep(0.1)
            selection = input()
            if selection == '1':
                flash_all_nodes()
                logo_update()
                sleep(3)
            if selection == '2':
                flash_all_gnd()
                logo_update()
                sleep(3)
            if selection == '3':
                flash_all_blink()
                logo_update()
                sleep(3)
            if selection == '4':
                flash_each_node()
            if selection == '5':
                gpio_state()
            if selection == 'e':
                break
            else:
                continue

    nodes_update()


if __name__ == '__main__':
    main()
