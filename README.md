# Zfsdisktray

# Zfsdisktray

This program requests data from `ZFS Storage appliance` this program prints out disk tray information. 

## USAGE
`zfsdisktray_show` will show you the Chassis informations available on the storage. 
    (e.g. Name, chassis status, Manufacturer, Model)

## Requirements

```
# Python 3.6 or higher

# ZFS 0.8.1 or higher (untested on earlier versions)

# Install docopt using pip

`pip install docopt`

# Install PrettyTable using pip

`pip install prettytable`  
```
Check [install docopt](https://pypi.org/project/docopt/) for more information. 

Check [install prettytable](https://pypi.org/project/prettytable/) for more information

### Usage Example
## Run the program

```
- zfsdisktray_show.py.py
# Show Chassis information
    - zfsdisktray_show.py.py -s <STORAGE> -d 

# Show Chassis information and Create csv file with the data from the storage
    - zfsdisktray_show.py.py -s <STORAGE> -d --csv <FILENAME>

# Show Chassis information and Create csv and json  file with the data from the storage
	- zfsdisktray_show.py.py -s <STORAGE> -d --csv <FILENAME> --json <JSON_FN>
  
  *<STORAGE> - your zfs storage appliance

# Show options
    python -h || --help
```

