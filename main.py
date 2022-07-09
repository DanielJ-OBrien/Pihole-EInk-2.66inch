import sys
import os
import pihole as ph
import epd2in66
import time
from PIL import Image,ImageDraw,ImageFont

x=0
while x == 0: 
    pihole = ph.PiHole("(Write IP here)")
    epd = epd2in66.EPD()
    epd.init(0)
    epd.Clear()

    font18 = ImageFont.truetype(('ibm_mono.ttc'), 18)
    
    Himage = Image.new('1', (epd.height, epd.width), 0xFF)
    draw = ImageDraw.Draw(Himage)
    bmp = Image.open('logo.bmp')
    Himage.paste(bmp, (0,0))
    draw.text((0, 65), 'IP: (Write IP here) ', font = font18, fill = 0)
    draw.text((0, 85), 'Current Clients: ', font = font18, fill = 0)   
    draw.text((0, 105), 'Total Queries: ', font = font18, fill = 0)
    draw.text((0, 125), 'Blocked Queries: ', font = font18, fill = 0)
    
    draw.text((213, 37), str(pihole.status), font = font18, fill = 0)
    draw.text((180, 85), str(pihole.total_clients), font = font18, fill = 0)   
    draw.text((160, 105), str(pihole.total_queries), font = font18, fill = 0)
    draw.text((185, 125), str(pihole.blocked), font = font18, fill = 0)
    epd.display(epd.getbuffer(Himage))
    time.sleep(1800)
