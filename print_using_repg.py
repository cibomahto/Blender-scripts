#!BPY

"""
 Name: 'Print using ReplicatorG'
 Blender: 249
 Group: 'Export'
 Tooltip: 'Print this model on a 3d printer'
"""

__version__ = ".1"
__author__  = "Matt Mets"
__license__ = "GPL"
__url__  = "http://replicat.org"
__bpydoc__ =""" Print your model to a 3d printer!
""" 

# --------------------------------------------------------------------------
# Script copyright (C) 2011 Matt Mets
# --------------------------------------------------------------------------

# Super simple: Just export the model as an stl, then tell ReplicatorG to
# print it.

import Blender
from Blender import Scene

import socket
import sys

HOST = 'localhost'
PORT = 2000

fileName = '/home/matt/Desktop/blender_out.stl'

scn = Scene.GetCurrent()
scn.objects.selected = scn.objects # select all

# Export the model
Blender.Save(fileName, 1)


# Print the model!
try:
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
  sys.stderr.write("[ERROR] %s\n" % msg[1])
  sys.exit(1)
 
try:
  sock.connect((HOST, PORT))
except socket.error, msg:
  sys.stderr.write("[ERROR] %s\n" % msg[1])
  sys.exit(2)
 
#sock.send('{"command":"open", "filename":"' + fileName + '"}')
sock.send('{"command":"printToFile", "inputFile":"' + fileName + '", "destinationFile":"/home/matt/Desktop/hex.s3g"}')
