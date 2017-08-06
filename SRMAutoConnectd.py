
import urllib2, sys, time, socket

userName="USERNAME"
password="PASSWORD"

sleepTime=30
socket.setdefaulttimeout(sleepTime)

hostname = ['https://192.168.10.3/connect/PortalMain', '192.168.10.3']
url = "connect/PortalMain?action=doLoginSubmit&flowId=UserLogin&username=" + userName + "&password=" + password

file=None
if file is None:
	#try:
	fh = open("/tmp/Wifi.log", 'w')
	#except IOError: 
	#	print "Couldn't write to file /tmp/hathway.log";
else:
	try:
		fh = open(file, 'w')
	except IOError:
		print "Couldn't write to file %s\n" % (file);

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

def connectToHathway():

	if len(hostname) == 0:
		sys.exit(1)
	else:
		for host in hostname:
			real_host = "http://" + host + url
			try:
				local_write("%s\tTrying to authenticate to server %s\n" % (time.ctime(), real_host) )
				urllib2.urlopen(real_host)
			except:
				local_write("%s\tFailed to connect to %s Retrying\n" % (time.ctime(), real_host) )
				continue
	
setup()
while 1==1:
	if checkInternetConnectivity() == 0:
		local_write("%s\tInternet connectivity is dead. Trying to contact SRM WiFi auth severs.\n" % (time.ctime() ) )
		connectToHathway()
		time.sleep(sleepTime)
		continue
	else:
		local_write("%s\tInternet connectivity alive. Sleeping for %s seconds.\n" % (time.ctime(), sleepTime) )
		time.sleep(sleepTime)
		continue 
		
