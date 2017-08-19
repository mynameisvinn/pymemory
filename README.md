# pymemory
inspect memory footprint of python objects. 

## install
``` 
git clone github.com/mynameisvinn/pymemory
cd pymemory
python setup.py install
```

## example
for example, we'd like to determine size of int `1`. since a python object consumes 16 bytes of overhead and each int is 1 byte, so we should expect 24 bytes for `1`.
```python
>>> from pymemory import deep_getsizeof
>>> x = 1
>>> deep_getsizeof(x, set())  # prints 24 bytes
```

## a deeper dive into python internals
in the above example, a cython struct `PyLongObject` was created to hold the integer 1. 

a PyLongObject struct holds three attributes: a `PyObject_HEAD` object (16 bytes); length of array (4 bytes); and an array for value (another 4 bytes).

the `PyObject_HEAD` is a struct:
```c
// https://code.woboq.org/llvm/include/python2.7/object.h.html

/* PyObject_HEAD defines the initial segment of every PyObject. */
PyObject_HEAD
{
	size_t refcnt;  // 8 bytes
	typeobject *type;  // 8 bytes
}
```