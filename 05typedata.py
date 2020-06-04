#type data angka satuan (integer) tidak ada kome

data_integer = 1
print ("data : ", data_integer)
print ("bertype : ", type(data_integer))

#type data satuan (float) menggunakan koma

data_float = 1.5
print ("data : ", data_float)
print ("bertype : ", type(data_float))

#type data satuan (string)

data_string = "otong"
print ("data : ", data_string)
print ("bertype : ", type(data_string))

# type data satuan (boolean)

data_bool = True
print ("data : ", data_bool)
print ("bertype : ", type(data_bool))


#bilangan kompleks
data_bool = complex(5,6)
print ("data : ", data_bool)
print ("bertype : ", type(data_bool))

#tipe data dari bahasa C

from ctypes import c_double

data_c_double =c_double(10.5)
print ("data : ", data_c_double)
print ("bertype : ", type(data_c_double))