# pymem

inspect memory footprint of python objects. 

for example, how many bytes does the string 'abc' take up? each char is 1 byte and a string object requires 37 bytes of overhead. that means 'abc' takes up 40 bytes.

## install
``` 
git clone github.com/mynameisvinn/pymem
cd pymem
python setup.py install
```

## usage
```
>>> from pymem import deep_getsizeof
>>> x = '1234567'
>>> deep_getsizeof(x, set())  # prints 44 bytes
```