1- If this is the first time upgrading your FW, then ssh to your Dorna controller:

ssh dorna@dorna

or 

ssh dorna@ip_address_of_robot

Then modify the "config.txt" file in the Raspberry Pi (RPi) by running the following command:

sudo nano /boot/config.txt

In the text editor that opens, add the following two lines to the end of the file:

dtoverlay=pi3-miniuart-bt
enable_uart=1

Then save the edited file and exit (press ^X (Ctrl + X) and then press Y).

Then type the following command in the command line in Raspberry Pi:
sudo raspi-config

Then select the following options:

select "Interfacing options"
select "Serial"
select "No"
Select "Yes"

Then select "Finish" and select "Yes" when asked about "Reboot now".



If you have done steps above, then you don't need to repeat them and you can follow the next steps:

2- Copy the content of the current directory to the /home/dorna/app directory of your RPi using a software such as Winscp:

3- ssh to RPi and go to the app directory of the RPi by typing the following command in the command line of RPi:

cd /home/dorna/app

and run the following command:

sh upgrade

4- Turn off the controller box and turn on it again and it is ready to work with the new firmware. 