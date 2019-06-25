import numpy as np
import ctypes
from ctypes import *
import platform
import os

currdir = str(os.path.dirname(os.path.abspath(__file__))) #get current directory of the python script
currdir = currdir.replace("exec","") #replace 'exec' to get the root dir
print("Working directory:",currdir) # diagnostic...
#Set up Output for the no-return function
c = np.zeros((1)) #single element array to be passed as a pointer

#inputs
a = 10.0
b = np.pi


if platform.system() == 'Darwin' : #file names
	libname = 'adder.dylib'
else :
	libname = 'adder.so'
#Import Library
lib = ctypes.CDLL(currdir+"/build/"+libname) #import library using the absolute path

#Set Return Types for the C functions

lib.add_ret.restype = c_double #Returns Double

lib.add_noret.restype = None #Returns nothing


#execution

lib.add_noret(c_void_p(c.ctypes.data),c_double(a),c_double(b))
# Sending the destination address as a pointer to the data section
# of the numpy array of length 1 c, and converting the numbers a and
# b to double for C.
print ("In Python:")
print ("Value saved in the destination: ", c[0])
#Will print the NumPy array
print ("What the destination really is: " , c)



c = lib.add_ret(c_double(a),c_double(b))
print ("In Python:")
print ("Value saved in the destination: ", c)
#Will print the NumPy array
print ("What the destination really is: " , c)