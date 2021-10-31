#!/usr/bin/python3

import pathlib
import glob
import sys
import time

from_time=163541605200
to_time=0
conns={}
total_size=0

def analyze_line(line):
	global to_time
	global from_time
	global conns
	global total_size
	
	if not "ACCEPT OK" in line:
		return
	
	# Format: version account-id interface-id srcaddr dstaddr srcport dstport protocol packets bytes start end action log-status
	parts = line.rstrip().split()
	from_ip=parts[3]
	from_port=parts[5]
	to_ip=parts[4]
	to_port=parts[6]
	size=int(parts[9])
	begin_epoch=int(parts[10])
	end_epoch=int(parts[11])
	formatted_time=time.strftime('%Y-%m-%d-%H', time.localtime(begin_epoch))
	
	if begin_epoch < from_time:
		from_time=begin_epoch
	
	if end_epoch > to_time:
		to_time=end_epoch
	
	key = "{}\t{}\t{}".format(formatted_time, from_ip, to_ip)
	
	if not key in conns:
		conns[key] = 0
	
	conns[key] = conns[key] + size
	total_size = total_size + size

def analyze_file(log_file):
	with open(log_file) as file:
		for line in file:
			analyze_line(line)

for log_file in glob.glob(sys.argv[1] + '/**/*.log', recursive=True):
	analyze_file(log_file)

print ("From {} TO {}".format(
	time.strftime('%Y-%m-%d-%H-%M', time.localtime(from_time)), 
	time.strftime('%Y-%m-%d-%H-%M', time.localtime(to_time))))

for key in conns:
	print ("{}\t{}".format( key, conns[key]))

print (" \t \t \t {}".format(total_size))
