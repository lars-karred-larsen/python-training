'''
Created on Mar 5, 2024

@author: student
'''
import platform

#platform() function returns a string identifying the underlying platform
print("Platform:", platform.platform())

#machine() function returns the machine type (e.g.'x86_64')
print("Machine type:", platform.machine())

#processor() function returns the processor type (e.g.'x86_64')
print("Processor type:", platform.processor())

#system() function returns the operating system (e.g. 'Linux' or 'Windows'
print("Operating system:", platform.system())

#version() function returns the operating system vesion
print("Operating system version:", platform.version())



#python_implementation() function returns the name of the Python implementation (e.g., 'CPython', 'Jython', 'IronPython', etc.) 
print("Python implementation:", platform.python_implementation())

#python_version_tuple() function returns a tuple containing the Python version
print("python_version_tuple:", platform.python_version_tuple())

#python attribute function returns the Python version as a string
print("Python version:", platform.python_version())

