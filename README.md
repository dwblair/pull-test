Try it out:

user@comp:~$ chmod 755 ./pull

usage: pull [-h] -p PATH [-v]

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  path to the sensor
  -v, --verbose         increase output verbosity

user@comp:~$ ./pull -p /dev/USB0

/dev/USB0

user@comp:~$ ./pull -p /dev/USB0 -v

pulling sensor value from path /dev/USB0
