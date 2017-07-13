import urllib2, sys, time, socket
from wireless import Wireless

userName="RA1611xxxxxxxxx"
password="xxxxxxxx"	

ssid = Wireless()

print ssid.current()

sleepTime=10
socket.setdefaulttimeout(sleepTime)

hostname = ['https://192.168.10.3/connect/PortalMain', '192.168.10.3']
url = "connect/PortalMain?action=doLoginSubmit&flowId=UserLogin&username=" + userName + "&password=" + password

file=None
if file is None:
	fh = open("/tmp/Wifi.log", 'w')

else:
	try:
		fh = open(file, 'w')
	except IOError:
		print "Error writing to file %s\n" % (file);

def setup():
	if len(sys.argv) > 1:
		userName=sys.argv[1]
		password=sys.argv[2]
		sleepTime=sys.argv[3]
	
def local_write(str):
	sys.stdout.write(str)
	fh.write(str)
	fh.flush()

def checkInternetConnectivity():
	x = 1
	try:
		socket.create_connection( ("www.google.com", 80) )
	except:
		x = 0
	finally:
		return x

def connectToSRM():

	if len(hostname) == 0:
		sys.exit(1)
	else:
		for host in hostname:
			real_host = "http://" + host + url
			try:
				local_write("%s\tAuthenticating ...\n" % time.ctime() )
				urllib2.urlopen(real_host)
			except:
				local_write("%s\tFailed, Retrying ...\n" % time.ctime() )
				continue
	
setup()
while 1==1:
	if checkInternetConnectivity() == 0:
		local_write("%s\tConnectivity error.\n" % (time.ctime() ) )
		connectToSRM()
		time.sleep(sleepTime)
		continue
	else:
		local_write("%s\tConnected.\n" % (time.ctime()) )
		time.sleep(sleepTime)
		continue 
