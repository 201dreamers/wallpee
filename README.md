# Wallpee
---
Wallpee is cli (in the future may be gui) app that downloads images for desktop wallpapers that suits your laptop or PC screen. Project is under development.
(I know that there are better tools for writing this app but I want to learn selenium better)

## Dependencies:
+ firefox and geckodriver
+ selenium (PyPi)
+ screeninfo (PyPi)

## Running:
python run_wallpee.py [options] [args]

### Options:
+ -h, --help - help message
+ -v, --version - version of wallpee
+ -p PATH, --path PATH - specify path for downloaded images
If ran without -p option then default path will be used ($HOME directory)

### Platforms:
+ Linux
+ Maybe MacOS