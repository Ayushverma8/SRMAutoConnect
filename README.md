# SRMAutoConnect
This script will try to connect to SRM WiFi portal ( https://192.168.10.3/connect/PortalMain) and checks if internet is connected and if it's not, it will run the automated login script.
This  will log you in automatically if SRM Wifi logs you out. They kicks you out every few hours and this is very annoying while downloading huge files. This script requires Python 2.7

#Usage

```sh
$ python SRMAutoConnect.py  <username> <password> <sleep> time in seconds

```


Where username is your RegisterNUM, password is your password and sleep time is the time between 2 consecutive internet connectivity tests and default is 30seconds. You can alternatively save username and password in the variables in the file and simply run by typing
```sh
$ python AutoConnect.py
```



