#!/bin/bash
pip3 install -r requirements.txt --upgrade
python3 ENC.py
python3 Unlock_Flash.py
python3 Firmware_Upgrade.py
python3 Lock_Flash.py
rm STM32_Bootloader_Host.py
rm firmware.bin
rm Unlock_Flash.py
rm Firmware_Upgrade.py
rm Lock_Flash.py
rm ENC.py
rm log.txt
rm efirmware
rm upgrade.sh
