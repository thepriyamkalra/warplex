# Warplex -- A command-line tool that extends your Cloudflare WARP+ Quota

## About Cloudflare WARP+
WARP+ uses Cloudflare’s virtual private backbone, known as Argo, to achieve higher speeds and ensure your connection is encrypted across the long haul of the Internet  
[ [Read more] ](https://blog.cloudflare.com/announcing-warp-plus/)  

## What is this?
Warplex is a cleanish and extended version of [this project](https://github.com/ALIILAPRO/warp-plus-cloudflare/blob/master/wp-plus.py)

## How do I use this?

### On Windows:
1. Download [warplex v1.0](https://github.com/justaprudev/warplex/releases/download/v1.0/warplex.exe)
3. Open the commad line or terminal in the same directory
4. Run warplex using `warplex <Your Cloudflare WARP+ ID> <Amount of bandwidth to be added your WARP+ Account>`

### On Linux:
1. Ensure that Python 3.9 or above is installed on your computer. You can get it from [here](https://www.python.org/downloads/)
2. Download [warplex](https://raw.githubusercontent.com/justaprudev/warplex/master/warplex.py)
3. Open the commad line or terminal in the same directory
4. Run warplex using `python -m warplex <Your Cloudflare WARP+ ID> <Amount of bandwidth to be added your WARP+ Account>`

## How do I get my Cloudflare WARP+ ID?

### On Android:
1. Open 1.1.1.1 App
2. Click on the Hamburger Menu Icon ☰
3. Advanced > Diagonistics
4. Under Client Configuration > Copy the ID

### On PC:
1. Open Cloudflare WARP App
2. Click on the Settings Icon ⚙
3. Preferences > General
4. Copy the Device ID

## Changes not reflecting on WARP+ Quota?

### On Android:
1. Open 1.1.1.1 App
2. Click on the Hamburger Menu Icon ☰
3. Advanced > Connection Options
4. Click on 'Reset Security Keys'

### On PC:
1. Open Cloudflare WARP App
2. Click on the Settings Icon ⚙
3. Preferences > Account
4. Copy the license key and click on 'Use Different Key'
5. Paste the same key and click on 'OK'


