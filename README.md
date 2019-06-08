# multiprocessing-helper
A wrapper for safe Python Multiprocessing using Pebble

 The wrapper allows time based termination of processes in case of a buggy underlying process, and the ability to easily retry the calculations in case of an exception or a timeout. The motive behind the script is a random deadlock caused when multiprocessing.Pool is called in python 3.6. 
 
