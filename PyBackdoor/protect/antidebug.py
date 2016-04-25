
Anti disassembly with python ..
Works on:
	-> http://www.pydev.org/
	-> https://docs.python.org/2/library/pdb.html
	-> http://www.ollydbg.de/
	-> http://debugger.immunityinc.com/

How to use:
	#import this script to top of ur codes and have fun.
	import antidebug


Is that really working ?:
	root@b3mb4m:~/Desktop#python -m pdb test.py
	
	> /root/Desktop/test.py(1)<module>()
	-> import antidebug
	(Pdb) continue
	Terminated  <--- There you go ..

	root@b3mb4m:~/Desktop#
"""



def start():
	from os import kill,getpid
	from sys import gettrace
	if gettrace() != None:
		kill(getpid(), SIGTERM)
  	else:
  		from inspect import stack
		for frame in stack():
			if frame[1].endswith("pydevd.py") or frame[1].endswith("pdb.py"):
				from signal import SIGTERM
				kill(getpid(), SIGTERM) 

	from sys import platform
	if platform == "win32":		
		from os.path import basename
		_ = "Immunity Debugger - %s - [CPU - main thread, module %s]" % (basename(__file__).split(".py")[0]+".exe",basename(__file__).split(".py")[0])
		__ = "OllyDbg - %s - [CPU - main thread, module %s]" % (basename(__file__).split(".py")[0]+".exe",basename(__file__).split(".py")[0])
		for x in [_,__]:
			from win32gui import FindWindow
			handle = FindWindow(None, x)
			from win32gui import PostMessage
			from win32con import WM_CLOSE
			PostMessage(handle,WM_CLOSE,0,0)
start()
