import base64 as b64
import binascii as ba

def hex2b64(hexstr):
	try:
		binstr = ba.a2b_hex(hexstr)
		b64str = b64.b64encode(binstr)
	except Exception as e:
		raise e
	return b64str