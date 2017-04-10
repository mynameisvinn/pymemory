# pymem

inspect memory footprint of python objects.

## install
``` 
git clone github.com/mynameisvinn/pymem
cd pymem
python setup.py install
```

## usage
```
>>> from pymem import deepget_sizeOF
>>> x = '1234567'
>>> deep_getsizeof(x, set())  # prints 44 bytes
```