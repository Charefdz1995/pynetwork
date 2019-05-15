from enum import Enum 

class int_type(Enum):
	Serial = se
	GigaEthernet = gi
	FastEthernet = fa
	Ethernet = eth 
class zone_type(Enum):
        Ingress = ing
        Egress = eg


class aceess(object):
	def __init__(self,address,username,password,secret):
		self.address = address
		self.username = username
		self.password = password
		self.secret = secret 

class interface(object):
	def __init__(self,int_type,shelf,slot,port,zone_type):
		self.int_type = int_type
		#self.shelf = shelf # TODO: moddify this 
		self.slot = slot
		self.port = port
		self.name = int_type + slot + "/"+ port
		self.zone_type = zone_type


class switch(object):
	def __init__(self,hostname,access,interfaces,zone_type):
		self.hostname = hostname
		self.interfaces = interfaces # interface list of the device
		self.access = access
		self.zone_type = zone_type

class link(object):
	def __init__(self,from_int,to_int):
		self.from_int = from_int # This is a tuple that contain the switch and port
		self.to_int = to_int
		self.name = "from " + from_int + " to " + to_int


class topology(object): # the base topology 
	def __init__(self,name,switches,links):
		self.name = name 
		self.switches = switches # switches list
		self.links = links # links list
class qos_classification_class(object):
        def __init__(self,name_int,dscp_value):
                self.name = name
                self.dscp_value = dscp_value
                # TODO: add attributes
class qos_class(object)
        def __init__(self,name,markes):
                self.name = name
                self.markes = markes #list of dcsp values for matching
                # TODO: add attributes
		

