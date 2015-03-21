Try it out:

**user@computer:~$** chmod 755 ./pull

**user@computer:~$** ./pull -h

usage: pull [-h] -p PATH [-v]

optional arguments:

  -h, --help            show this help message and exit

  -p PATH, --path PATH  path to the sensor

  -v, --verbose         increase output verbosity

**user@computer:~$** ./pull -p /dev/USB0

18.6

**user@computer:~$** ./pull -p /dev/USB0 -v

sensor value via path /dev/USB0: 18.6
