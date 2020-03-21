![OTA Logo](./resources/ota_logo.png)

# Easy mange and update your [RotorHazard](https://github.com/RotorHazard/RotorHazard) installation. 

</br>
Additional features like nodes flashing are included.
</br>
</br>

If you want all hardware functionalities - visit: [Instructables page](https://www.instructables.com/id/RotorHazard-Updater/)
or check the [RotorHazard-Updater.pdf](/how_to/RotorHazard-Updater.pdf).</br>
</br>
Facebook discussion on the [GROUP](https://www.facebook.com/groups/207159263704015).</br>
</br>
You may also read [update notes](/docs/update-notes.txt) - new features are present.
</br>

#### Commands to download the repo onto Raspberry Pi (or Linux):
    cd ~
    sudo apt install zip unzip
    wget https://codeload.github.com/szafranski/RH-ota/zip/master -O tempota.zip
    unzip tempota.zip
    rm tempota.zip
    mv RH-ota-* RH-ota

#### Commands to open the software (only on 'master' release):
    cd ~/RH-ota
    sh ./ota.sh

</br>

>If you want detailed description of this software and actions that are being performed during operations</br>
>or you have some programming experience you may read [developer notes](/docs/dev-notes.txt). Legal stuff - here: [license file](/docs/LICENSE.txt).
