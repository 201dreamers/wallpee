# Wallpee
---
Wallpee is cli (in the future may be gui) app that downloads images for desktop wallpapers that fits your laptops or PCs screen. Project is under development.

## Dependencies:
+ firefox and geckodriver
+ requests (PyPi)
+ screeninfo (PyPi)
+ fake-useragent (PyPi)
+ BeautifulSoup4 [bs4] (PyPi)

## Running:
python run_wallpee.py [options] [args]

### Options:
+ -h, --help - help message
+ -v, --version - version of wallpee
+ -p PATH, --path PATH - specify path for downloaded images
If ran without -p option then default path will be used ($HOME directory)

### Platforms:
+ Linux
+ Maybe MacOS, not tested yet