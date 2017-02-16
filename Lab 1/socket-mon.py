import psutil
import operator
from collections import defaultdict


def getTCPConnections():
	tcpConn = psutil.net_connections(kind='tcp')
	#print "Connections are %s %s:" % (len(tcpConn),tcpConn)
	return tcpConn

def formatOutput(tcpConnections):
	#Groupt TCP connections on the basis of Process Id

	#Dictionary of Process Id to count of TCP Connections	
	pidToCount = defaultdict(int)

	#Dictionary of Process Id to the list of TCP connections for that process id
	d = defaultdict(list)
	for process in tcpConnections:
		if process.laddr != '' or process.raddr != '':
			key = process.pid 
			d[key].append(process)
			pidToCount[key]+=1
		else :
			print "laddr and raddr does not exist for process" , process.pid
	#print "*******Grouped dictionary %s %s" % (len(d),d)		
	
	#sort dictionary 'pidToCount' in descending order of pid count
	sortedPidToCountList=sorted(pidToCount.items(),key=operator.itemgetter(1),reverse=True)	
	#print "sortedPidToCountList...", sortedPidToCountList
	
	header = "\"pid\",\"laddr\",\"raddr\",\"status\""
	print header
	for var in sortedPidToCountList:
		pid = var[0]
		#Get the list of connections for this pid
		connectionsList = d[pid]
		for connectionDetails in connectionsList:
			localIP = ''
			localPort = ''
			lAddr = ''
			remoteIP = ''
			remotePort = ''
			rAddr = ''
			if len(connectionDetails.laddr) > 0:
				localIP = str(connectionDetails.laddr[0])			
				localPort= str(connectionDetails.laddr[1])
				lAddr = localIP+'@'+localPort
			if len(connectionDetails.raddr) > 0:
				remoteIP = str(connectionDetails.raddr[0])			
				remotePort= str(connectionDetails.raddr[1])
				rAddr = remoteIP+'@'+remotePort			
			print "\"%s\", \"%s\", \"%s\", \"%s\"" %(connectionDetails.pid,lAddr,rAddr,connectionDetails.status)


tcpConnections=getTCPConnections()
formatOutput(tcpConnections)
