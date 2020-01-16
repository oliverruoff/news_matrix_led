import RPi.GPIO as GPIO
from time import sleep, strftime
from datetime import datetime
import socket

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, LCD_FONT

import info_loader as il


def _get_own_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
        s.close()
    except:
        return 'No Internet'


serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, width=32, height=8, block_orientation=-90)
device.contrast(10)
start = datetime.now()
stop = datetime.now()
news_str = il.get_tagesschau_rss_feed()
try:
    while True:
        time_str = '<' + il.get_time() + '>'
        if (stop - start).total_seconds() > 300:
            news_str = il.get_tagesschau_rss_feed()
            start = datetime.now()
        led_str = time_str + ' | ' + news_str + ' | ' + _get_own_ip()
        show_message(device, led_str, fill="white",
                     font=proportional(LCD_FONT), scroll_delay=0.03)
        stop = datetime.now()
except KeyboardInterrupt:
    GPIO.cleanup()
