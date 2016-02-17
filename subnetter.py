#Subnetting Application
import math

def calc_next_bound(cdr):
	if cdr > 8 and cdr < 16:
		return 16
	elif cdr > 16 and cdr < 24:
		return 24
	elif cdr > 24 and cdr < 32:
		return 32
	else:
		return 0

def calc_block(cdr, next_bound):
	return math.pow(2, (next_bound - cdr))

def cidr_valid(cdr):
	if cdr >= 1 and cdr <= 31:
		return True
	else:
		return False

def is_classful(cdr):
	if cdr == 8 or cdr == 16 or cdr == 24:
		return True
	else:
		return False

#Takes the IP Address as a raw_input string. Using the dot separators as positions,
# slices the string and populates a dictionary, which is then returned.
def octet_splitter(ipAdd):
	first_dot = ipAdd.index('.')
	second_dot = ipAdd.index('.', first_dot + 1, len(ipAdd))
	third_dot = ipAdd.index('.', second_dot + 1, len(ipAdd))

	first_octet = int(ipAdd[0:first_dot])
	second_octet = int(ipAdd[first_dot+1:second_dot])
	third_octet = int(ipAdd[second_dot+1:third_dot])
	fourth_octet = int(ipAdd[third_dot+1:len(ipAdd)])

	the_ipAdd = {"FirstOctet": first_octet, "SecondOctet": second_octet, "ThirdOctet": third_octet, "FourthOctet": fourth_octet}

	return the_ipAdd
	
def ipAdd_valid(ipAdd):
	ipDict = ipAdd

	if all( [ipDict["FirstOctet"] >= 0,  ipDict["FirstOctet"] <= 255,
	    ipDict["SecondOctet"] >= 0, ipDict["SecondOctet"] <= 255,
	    ipDict["ThirdOctet"] >= 0,  ipDict["ThirdOctet"] <= 255,
	    ipDict["FourthOctet"] >= 0,  ipDict["FourthOctet"] <= 255] ):
		return True
	else:
		return False

def subnetA(ipDict, cdr):
	next_boundary = calc_next_bound(cdr)
	block_size = calc_block(cdr, next_boundary)

	for sub in range(0, 255, int(block_size)):
		print str(ipDict['FirstOctet']) + '.' + str(sub) + '.0' + '.0'
		sub = sub + block_size

def subnetB(ipDict, cdr):
	next_boundary = calc_next_bound(cdr)
	block_size = calc_block(cdr, next_boundary)

	for sub in range(0, 255, int(block_size)):
		print str(ipDict['FirstOctet']) + '.' + str(ipDict['SecondOctet']) + '.' + str(sub) + '.0'
		sub = sub + block_size

def subnetC(ipDict, cdr):
	next_boundary = calc_next_bound(cdr)
	block_size = calc_block(cdr, next_boundary)

	for sub in range(0, 255, int(block_size)):
		print str(ipDict['FirstOctet']) + '.' + str(ipDict['SecondOctet']) + '.' + str(ipDict['ThirdOctet']) + '.' + str(sub)
		sub = sub + block_size

def display_results(cdr, ipDict):
	boundary = calc_next_bound(cdr)

	if boundary == 16:
		subnetA(ipDict, cdr)
	elif boundary == 24:
		subnetB(ipDict, cdr)
	elif boundary == 32:
		subnetC(ipDict, cdr)
	else:
		print "Error Subnetting"

#Main Program Loop
running = True
while running == True:

	#Allow users to quit or continue subnetting
	user_query = raw_input("Would you like to subnet (y/n)? ")
	if user_query == 'n':
		running = False
		break
	else:
		running = True

	#Get I.P. address and validate input/format
	ipValid = False
	while ipValid == False:
		try:
			ipAdd = raw_input("Enter the I.P. Address (X.X.X.X): ")
			ipAddDict = octet_splitter(ipAdd)
			ipValid = ipAdd_valid(ipAddDict)
			if ipValid == False:
				print "\n**Enter valid octets (0 - 255)**\n"
		except:
			print "\n**Enter a valid I.P. Address in the (X.X.X.X) format**\n"
			continue

	#Get CIDR notation number and validate input
	cidrValid = False
	while cidrValid == False:
		try:
			cidr = int(raw_input("Enter the CIDR notation number: /"))
			cidrValid = cidr_valid(cidr)
			if cidrValid == False:
				print "\n**Enter a valid CIDR notation number (Integer 1 - 31)**\n"
		except:
			print "\n**Enter a valid CIDR notation number (Integer 1 - 31)**\n"
			continue

	#Display Subnet Addresses
	display_results(cidr, ipAddDict)







