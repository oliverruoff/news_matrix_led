# news_matrix_led  
![News Matrix LED](nml.gif)  
Displays news on a led matrix.

## Prerequisites

* Setup hardware (connect pins)
* Setup software (install drivers)
* Setup linux service (for daily use)

### Hardware wiring / pin setup 

| 4 In 1 MAX7219 Dot Matrix Display Module	| Raspberry |
|--|--|
| VCC	| 5V |
| GND	| GND |
| DIN	| MOSI |
| CS	| CE0 |
| CLK	| SCK |

### Software Setup

* Install led matrix using [this](https://tutorial.cytron.io/2018/11/22/displaying-max7219-dot-matrix-using-raspberry-pi/) guide
  * `sudo apt-get install build-essential`
  * `sudo apt-get install python-dev python-pip`
  * `sudo apt-get install libfreetype6-dev libjpeg-dev`
  * `git clone http://github.com/rm-hull/luma.led_matrix.git`
  * `sudo -H pip install –upgrade luma.led_matrix`

## Setting things up for linux systems (developed for Raspberry Pi)

* Install python3
* Install modules listed in `requirements.txt`
* Copy `led_matrix.py` and `info_loader.py`to raspberry pi
* Make `led_matrix.py` executable
    * $ `chmod +x led_matrix.py`
* Copy `nml.service` to `/lib/systemd/system`
* Change `ExecStart=` command inside `nml.service` accordingly to path where `led_matrix.py` was copied
* Enable daemon process
    * $ `sudo systemctl daemon-reload`
    * $ `sudo systemctl enable nml.service`
    * $ `sudo systemctl start nml.service`
* Enable daily reboot at midnight (to automatically fix (e.g.) networking errors
  * `sudo crontab -e`
  * Enter as new line and save --> `0 0 * * * /sbin/reboot`

## 3D printed shell

* As shell for the led matrix and raspberry zero, you can use the shell.stl file

## Useful commands for process monitoring

* Check status
    * $ `sudo systemctl status nml.service`
* Start service
    * $ `sudo systemctl start nml.service`
* Stop service
    * $ `sudo systemctl stop nml.service`
* Check service's log
    * $ `sudo journalctl -f -u nml.service`
