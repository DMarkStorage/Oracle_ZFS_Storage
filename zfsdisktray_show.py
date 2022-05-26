import requests
import json
import os
import traceback
from docopt import docopt
requests.packages.urllib3.disable_warnings()

__version__ = '1.0'
__revision__ = '20190626'
__deprecated__ = False

data = {}
def get_headers():
	# Function that will return the headers and the Auth for the API
	headers = {
		"Content-Type":"application/json",
		"X-Auth-User": 'root',
		"X-Auth-Key": 'password'

	}
	return headers

def get_args():

	usage = """
	Usage:
		try.py -s <STORAGE> --diag
		try.py --version
		try.py -h | --help

	Options:
		-h --help            Show this message and exit
		-s <STORAGE>         ZFS appliance/storage name

	"""
	# version = '{} VER: {} REV: {}'.format(__program__, __version__, __revision__)
	# args = docopt(usage, version=version)
	args = docopt(usage)
	return args	


def api_list():

	url = [	
			'/hardware/v1/chassis',]

	return url


def get_data(storage):

	header = get_headers()
	base_url = 'https://{}:215'.format(storage)
	
	url = api_list()

	for i in url:
		ch1_uri = '{}/api'.format(base_url)+i
		print(ch1_uri)
		r = requests.get(ch1_uri, verify=False, headers = header)
		j = r.json()
		data.update(j)

	# print( data['fault']['code'])
	# if data['fault']['code'] ==401:
	# 	print('Unauthorized! Try to check your USERNAME and PASSWORD')
	# 	exit()
	# else:
	# 	get_val()

	# with open('chassis_output.json', 'w') as outfile:
	# 	json.dump(data, outfile, indent = 2)

def get_val():

	def get_chassis():

		print('\n')
		print('+'+'-'*30+'+')
		print('  *** CHASSIS INFORMATION ***\n')
		for i in data['chassis']:
			print('* Chassis Name: ',i['name'])
			print('* Chassis Faulted: ',i['faulted'])
			print('* Chassis Manufacturer: ',i['manufacturer'])
			print('* Chassis Model: ',i['model'])
			if 'part' in data:
				print('* Chassis Part: ',i['part'])
			else:
				pass
			print('* Chassis Type: ',i['type'])
			if 'rpm' in data:
				print('* Chassis RPM: ',i['rpm'])
			else:
				pass
			if 'path' in data:
				print('* Chassis Path: ',i['path'])
			else:
				pass
			print('* Chassis Serial: ',i['serial'])
			href = i['href']

			print('* Chassis HREF: ',href[-11:],"\n")



	get_chassis()

def main(args):
	storage = args['<STORAGE>']
	get_data(storage)
	get_val()


if __name__ == '__main__':
	try:
		ARGS = get_args()

		main(ARGS)
	except KeyboardInterrupt:
		print('\nReceived Ctrl^C. Exiting....')
	except Exception:
	    ETRACE = traceback.format_exc()
	    print(ETRACE)
	except KeyError:
		print("data")