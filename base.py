from enum import Enum 

class int_type(Enum):
	Serial = se
	GigaEthernet = gi
	FastEthernet = fa
	Ethernet = eth 


class interface(object):
	def __init__(self,int_type,shelf,slot,port):
		self.int_type = int_type
		#self.shelf = shelf # TODO: moddify this 
		self.slot = slot
		self.port = port
		self.name = int_type + slot + "/"+ port



class switch(object):
	def __init__(self,hostname,interfaces):
		self.hostname = hostname
		self.interfaces = interfaces # interface list of the device


class link(object):
	def __init__(self,from_int,to_int):
		self.from_int = from_int
		self.to_int = to_int
		self.name = "from " + from_int + " to " + to_int


class topology(object): # the base topology 
	def __init__(self,name,switches,links):
		self.name = name 
		self.switches = switches # switches list
		self.links = links # links list
		

