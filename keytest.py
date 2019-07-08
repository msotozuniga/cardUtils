#!/usr/bin/python

#
# send_apdu.py - Python code for Sending raw APDU commands
# version 0.1
# Nick von Dadelszen (nick@lateralsecurity.com)
# Lateral Security (www.lateralsecurity.com)

#
# This code is copyright (c) Lateral Security, 2011, All rights reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import rfidiot
import sys
import os

def autenticarbloque(bloque):
	hexacompleto=hex(bloque)
	if bloque <16:
		zona='0'+hexacompleto[2:]
	else:
		zona=hexacompleto[2:]
	return zona


try:
        card= rfidiot.card
except:
	print "Couldn't open reader!"
        os._exit(True)


card.info('send_apdu v0.1a')
card.select()
print '\nID: ' + card.uid
print '  Data:'

bloque=0
int(bloque)
cont = True
#while cont:
#	apdu = raw_input("enter the apdu to send now, send \'close\' to finish :")
#	print apdu
#	if apdu == 'close':
#		cont = False
#	else:
#		zona=autenticarbloque(bloque)
#		r = card.pcsc_send_apdu('ff8800'+zona+'6000')
#		print 'bloque: '+zona
#		print card.data + card.errorcode
#		bloque+1

for i in range(255):
	zona=autenticarbloque(i)
	r = card.pcsc_send_apdu('ff8800'+zona+'6000')
	#print card.errorcode
	if card.errorcode=='6300':
		print 'bloque: '+zona
				
print 'Ending now ...'

