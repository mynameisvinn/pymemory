# PyMemory

inspect memory footprint of python objects. 

for example, we'd like to determine size of str `abc`? 

in ascii, each char is 1 byte and a python str object has 37 bytes of overhead, so that means `abc` takes up 40 bytes.

## install
``` 
git clone github.com/mynameisvinn/pymemory
cd pymemory
python setup.py install
```

## example
```
>>> from pymemory import deep_getsizeof
>>> x = '1234567'
>>> deep_getsizeof(x, set())  # prints 44 bytes
```