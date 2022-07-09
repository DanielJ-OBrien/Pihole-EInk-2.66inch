![IMG_20220709_233920](https://user-images.githubusercontent.com/99108127/178126186-4ed379ef-f719-491d-8981-01141151b978.jpg)

# Pihole E-Ink 2.66inch Statistic Display
Program that displays statistics from Pi-Hole to the 2.66" Waveshare E-Ink display, and updates every 30 minutes.

## Setup

Note: This guide assumes you have already installed the libraries required to use the display. These can be found through this link:

> https://www.waveshare.com/wiki/2.66inch_e-Paper_Module#Install_libraries

1. Install PiHole-api:

> `python3 -m pip install --no-cache-dir PiHole-api`

2. Open main.py and change BOTH instances of (Write IP here) to your devices IPv4 address.

3. Run main.py
