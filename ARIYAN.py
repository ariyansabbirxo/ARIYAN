import ctypes
my_lib = ctypes.CDLL('./ariyan.cpython-313.so')
my_lib.add.argtypes = (ctypes.c_int, ctypes.c_int)
my_lib.add.restype = ctypes.c_int
result = my_lib.add(5, 7)
print("Result of add(5, 7) is:", result)
