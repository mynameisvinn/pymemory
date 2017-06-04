# pymemory
inspect memory footprint of python objects. 

for example, we'd like to determine size of str `abc`. in ascii, each char is 1 byte and a python str object consumes 37 bytes of overhead, so we should expect 40 bytes for `abc`.

## install
``` 
git clone github.com/mynameisvinn/pymemory
cd pymemory
python setup.py install
```

## example
```
>>> from pymemory import deep_getsizeof
>>> x = 'abc'
>>> deep_getsizeof(x, set())  # prints 40 bytes
```