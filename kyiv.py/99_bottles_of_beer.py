# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=2>

# for statement

# <headingcell level=3>

# for with else

# <codecell>

for i in range(3):
   if i%2:
       continue
   print i
   if i>5:
      break
else:
   print "there hasn't been any break"

# <headingcell level=3>

# exception in for loop

# <codecell>

for i in range(3):
   try:
       if i%2:
           continue
       if i>=2:
          break
   except:
       print "exception was  raised {0}".format(i)
   else:
       print "exception was not raised {0}".format(i)
   finally:
       print "anyway {0}".format(i)
else:
   print "there hasn't been any break"

# <headingcell level=2>

# Nested list comprehensions and generator expressions

# <headingcell level=3>

# General syntax

# <markdowncell>

# ####Generator expression
# ```
# (expression for i in s if cond1
#                    for j in t if cond2
#                    ...
#                    if condfinal)
# ```
# ####List comprehension
# ```
# [expression for i in s if cond1
#                    for j in t if cond2
#                    ...
#                    if condfinal]
# ```
# ####Dict comprehension
# ```
# {i:expression for i in s if cond1
#                    for j in t if cond2
#                    ...
#                    if condfinal}
# ```
# ####Set comprehension
# ```
# {i for i in s if cond1
#                    for j in t if cond2
#                    ...
#                    if condfinal}
# ```

# <headingcell level=3>

# generator expression Vs. list comprehension

# <markdowncell>

# - Does not construct a list.
# - Only useful purpose is iteration
# - Once consumed, can't be reused

# <codecell>

a = [1,2,3,4]
b = [2*x for x in a]
b

# <codecell>

c = (2*x for x in a)

# <headingcell level=3>

# simplified syntax

# <codecell>

sum(x*x for x in s)

# <headingcell level=2>

# Iterable objects

# <headingcell level=3>

# Iterator protocol

# <markdowncell>

# Iteration over containers is implemented using two distinct methods:
# 
# - ```iterator.__iter__()``` (returns an iterator object)
# - ```iterator.next()``` (returns next item for iterator)
# 
# raise ```StopIteration``` when there is no items left

# <headingcell level=3>

# Sequence

# <markdowncell>

# There are builtin sequence types such as
# 
# - list
# - tuple
# - string
# 
# And You can define Your own sequence class defining method ```__getitem__```.
# 
# iteration over instances of builtin sequences are fast because the  classes write on C
# 
# but repeated iteration over them will cause holding them in memory

# <codecell>

class A(object):
    def __getitem__(self, item):
        if item < self.value:
            return item
        else:
            raise IndexError
    def __init__(self, value):
         self.i = 0
         self.value = value
for i in A(3):
    print i

# <headingcell level=3>

# Casting to list

# <codecell>

class MyIter():
    def __len__(self):
        print "__len__"
        return 5
    def __iter__(self):
        print "__iter__"
        return iter([1,2,3,4,5])

list(MyIter())

# <markdowncell>

# casting to list call ```__iter__``` first and then trying to call ```__len__``` to allocate memory
# 
# ```
# it = PyObject_GetIter(b);
# if (it == NULL)
#    return NULL;
# iternext = *it->ob_type->tp_iternext;
# /* Guess a result list size. */
# n = _PyObject_LengthHint(b, 8);
#    if (n == -1) {
#    Py_DECREF(it);
#    return NULL;
# }
# ```
# *(Objects/listobject.c)*

# <markdowncell>

# this can cause undesired ```__len__``` code running.
# For example if ```__len__```  makes call to database or do some other things
# In this case use list comprehension instead or cast to iter first

# <codecell>

list(iter(MyIter()))

# <codecell>

[i for i in MyIter()]

# <headingcell level=3>

# length hint

# <markdowncell>

# There is PEP 424 about Cpython optimization. but I am not sure that Iam using it correctly.
# 
# ```__length_hint__``` must return an integer (else a ```TypeError``` is raised) or ```NotImplemented```, and is not required to be accurate. It may return a value that is either larger or smaller than the actual size of the container. A return value of ```NotImplemented``` indicates that there is no finite length estimate. It may not return a negative value (else a ```ValueError``` is raised).

# <codecell>

class MyIter():
    def __len__(self):
        print ("__len__")
        return 5
    def __length_hint__(self):
        """ return approximate hint"""
        print ('hint')
        return 4
    def __iter__(self):
        print ("__iter__")
        return iter([1,2,3,4,5])

list(MyIter())

# <headingcell level=3>

# collections.Iterable and collections.Iterator

# <markdowncell>

# #### class collections.abc.Iterable
# 
#    ABC for classes that provide the ```__iter__()``` method. See also the definition of iterable.
# 
# 
# #### class collections.abc.Iterator
# 
#    ABC for classes that provide the ```__iter__()``` and ```next()``` methods. See also the definition of iterator.

# <codecell>

import collections

# <codecell>

isinstance((i for i in [1, 2]), collections.Iterable)

# <codecell>

isinstance((i for i in [1, 2]), collections.Iterator)

# <codecell>

isinstance([1, 2], collections.Iterable)

# <codecell>

[1, 2].__iter__

# <codecell>

isinstance([1, 2], collections.Iterator)

# <codecell>

isinstance(iter([1, 2]), collections.Iterator)

# <codecell>

class SomeIteratorContainer(object):
    def __iter__(self):
        return iter(SomeIterator())

class SomeIterator(object):
    def __init__(self):
        self.i = 0
    def __iter__(self):
        return self
    def next(self):
        self.i += 1
        if self.i > 10: raise StopIteration
        return self.i

# <codecell>

isinstance(SomeIteratorContainer(), collections.Iterable)

# <codecell>

isinstance(SomeIteratorContainer(), collections.Iterator)

# <codecell>

isinstance(iter(SomeIteratorContainer()), collections.Iterator)

# <codecell>

isinstance(SomeIterator(), collections.Iterable)

# <codecell>

isinstance(SomeIterator(), collections.Iterator)

# <codecell>

isinstance('', collections.Iterator)

# <codecell>

isinstance('', collections.Iterable)

# <codecell>

''.__iter__

# <headingcell level=3>

# N.B. Abstract Base Class

# <codecell>

from abc import ABCMeta, abstractmethod
class Donkey(object):
    pass
class Horse:
   __metaclass__ = ABCMeta

   @abstractmethod
   def neigh(self):
       return "i-go-go"

   @classmethod
   def __subclasshook__(cls, C):
       if cls is Horse:
           if issubclass(C, Donkey):
               return False
           if isinstance(C, type):
               if any("neigh" in B.__dict__ for B in C.__mro__):
                   return True
           else:
               if hasattr(C, "neigh"):
                   return True
       return NotImplemented

# <codecell>

class Mare(Horse):
   def neigh(self):
       return '-'.join([super(Mare, self).neigh(), 'go-go'])

# <codecell>

issubclass(Mare, Horse)

# <codecell>

Mare().neigh()

# <codecell>

class Mule(Horse, Donkey):
   def neigh(self):
       return super(Mule, self).neigh()

# <codecell>

issubclass(Mule, Horse)

# <codecell>

Mule().neigh()

# <codecell>

class Elk(object):
   def neigh(self):
       return "i-gu-gu"

# <codecell>

issubclass(Elk, Horse)

# <codecell>

Elk().neigh()

# <codecell>

class Locomotive(object):
   pass

Horse.register(Locomotive)

# <codecell>

issubclass(Locomotive, Horse)

# <codecell>

Locomotive().neigh()

# <codecell>

class SphericalHorseInVacuum(Horse):
    pass

# <codecell>

issubclass(SphericalHorseInVacuum, Horse)

# <codecell>

SphericalHorseInVacuum().neigh()

# <headingcell level=2>

# Generators

# <markdowncell>

# Generators are functions which are generate series of data instead of returning value.

# <codecell>

couplet =  """
    {0} bottles of beer on the wall, {0} bottles of beer.
    Take one down, pass it around, {1} bottles of beer on the wall."""
def beer_on_the_wall():
    n = 99
    while n:
        yield couplet.format(n, n - 1)
        n -= 1

# <codecell>

song = beer_on_the_wall()

# <codecell>

song.next()

# <codecell>

for i in range(97):
    song.next()
    
song.next()

# <codecell>

song.next()

# <headingcell level=3>

# Generators as a Pipeline

# <codecell>

bottles = ('{0} bottles of beer on the wall'.format(i)
                             for i in xrange(99, 0, -1))
repeated_beer = ('{0} {1}.'.format(i, ' '.join(i.split()[:4])) 
                                               for i in bottles)
taken_beer = ('{0}\nTake 1 down'.format(i) for i in repeated_beer)
open_beer = ('{0},  pass it around'.format(i) for i in  taken_beer)
left_beer = ('{0}. {1} bottles of beer '
             'on the wall'.format(i, int(i.split(' ', 1)[0]) - 1) 
                                                for i in open_beer)
print '\n'.join(left_beer)

# <markdowncell>

# ![Generators as pipeline](https://s3-eu-west-1.amazonaws.com/uploads-eu.hipchat.com/15409/63331/q3mpikbh9u6emtp/pipeline.jpg)
# 
# - At each step of the pipeline, we declare an operation that will be applied to the entire data set
# - Instead of focusing on the problem at a line-by-line level, you just break it down into big operations that operate on the whole dataset
# - This stile is more unix-like because we have separate utilities which perform separate complete tasks.

# <headingcell level=3>

# Important generators concepts

# <markdowncell>

# - Generators decouple iteration from the code that uses the results of the iteration
# 
# - In the last example, we're performing a calculation on a sequence of lines
# 
# - It doesn't matter where or how those lines are generated
# 
# - Thus, we can plug any number of components together up front as long as they eventually produce a line sequence

# <headingcell level=3>

# Generator shutdown

# <codecell>

def my_generator():
    while 1:
        yield 1
my_gen = my_generator()
for i, j in enumerate(my_gen):
    if i > 2: my_gen.close()
    print i, j

# <codecell>

my_gen.next()

# <codecell>

my_gen = my_generator()
for i, j in enumerate(my_gen):
    if i > 2: 
        break
    print i, j

# <codecell>

my_gen.next()

# <markdowncell>

# In the generator, ```GeneratorExit``` is raised

# <codecell>

def my_generator():
    while 1:
        try:
            yield 1
        except GeneratorExit, e:
            print 'I am dying... +_+'
            raise GeneratorExit
my_gen = my_generator()
my_gen.next()

# <codecell>

my_gen.close()

# <markdowncell>

# ```close()``` is called when a generator is garbage-collected.
# This means the generator’s code gets one last chance to run before the generator is destroyed.

# <codecell>

my_gen = my_generator()
my_gen.next()
del my_gen

# <markdowncell>

# - GeneratorExit Exception can't be ignored. RuntimeError will be raised otherwise.
# - Separate threads can not call .close() ValueError: will be raised otherwise
# - Generator can't be shutdowned with a signal. ValueError: will be raised otherwise

# <headingcell level=2>

# Co-routines

# <codecell>

#TODO

# <codecell>

def grep(pattern):
    print "Looking for %s" % pattern
    while True:
        line = (yield)
        if pattern in line:
            print line

grepper = grep('value_1')
for i in range(25):
    grepper.send('value_{0}'.format(i))
    

# <markdowncell>

# Remembering to call .next() is easy to forget

# <codecell>

def coroutine(func):
    def start(*args,**kwargs):
        cr = func(*args,**kwargs)
        cr.next()
        return cr
    return start

@coroutine
def grep(pattern):
    print "Looking for %s" % pattern
    while True:
        line = (yield)
        if pattern in line:
            print line

grepper = grep('value_1')
for i in range(25):
    grepper.send('value_{0}'.format(i))

# <headingcell level=3>

# Closing a Coroutine

# <codecell>

grepper.close()

# <headingcell level=3>

# Throwing an Exception

# <codecell>


grepper = grep('value_1')
for i in range(25):
    grepper.send('value_{0}'.format(i))
grepper.throw(RuntimeError,"You're hosed")

# <codecell>

@coroutine
def grep(pattern):
    print "Looking for %s" % pattern
    while True:
        try:
            line = (yield)
        except RuntimeError, e:
            print 'exception was raised', e
        if pattern in line:
            print line

grepper = grep('value_1')
for i in range(25):
    grepper.send('value_{0}'.format(i))
grepper.throw(RuntimeError,"You're hosed")

# <headingcell level=3>

# Processing Pipelines

# <markdowncell>

# Coroutines can be used to set up pipes
# 
# ![coroutines](http://img715.imageshack.us/img715/788/coroutines1.png)

# <codecell>

@coroutine
def some_coroutine(*args, **kwargs):
    print "Looking for %s" % pattern
    while True:
        line = (yield)
        # do some action here
        # ...
        # ...
        another_coroutine.send(line)
        # ...

# <headingcell level=3>

# Filtering with coroutine

# <markdowncell>

# One can use coroutine as filter on pipeline
# 
# ![coroutine filter](http://img689.imageshack.us/img689/296/84990340.png)

# <codecell>

@coroutine
def filter_coroutine(*args, **kwargs):
    print "Looking for %s" % pattern
    while True:
        line = (yield)
        # do some action here
        # ...
        # ...
        if some condition:
            another_coroutine.send(line)
        # ...

# <headingcell level=3>

# Broadcasting

# <markdowncell>

# With coroutines, you can send data to multiple destinations
# 
# ![branching](http://img833.imageshack.us/img833/9135/23447597.png)

# <codecell>

@coroutine
def fbroadcasting_coroutine(*args, **kwargs):
    print "Looking for %s" % pattern
    while True:
        line = (yield)
        # do some action here
        # ...
        # ...
        for branch_coroutine in coroutine_list:
            branch_coroutine.send(line)
        # ...

# <markdowncell>

# #### Key difference between Generators and Coroutines.  
# Generators pull data through the pipe with iteration.  Coroutines push data into the pipeline with send().

# <headingcell level=3>

# Delegating to a Subgenerator

# <markdowncell>

# PEP 380 adds the yield from expression, allowing a generator to delegate part of its operations to another generator. This allows a section of code containing ‘yield’ to be factored out and placed in another generator. Additionally, the subgenerator is allowed to return with a value, and the value is made available to the delegating generator.
# While designed primarily for use in delegating to a subgenerator, the ```yield from``` expression actually allows delegation to arbitrary subiterators.
# For simple iterators, yield from iterable is essentially just a shortened form of 
# 
#     for item in iterable: 
#         yield item
# 
# For example
# 
#     def g(x):
#         yield from range(x, 0, -1)
#         yield from range(x)
# 
#     list(g(5))
# 
# [5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
# 

# <markdowncell>

# However, unlike an ordinary loop, yield from allows subgenerators to receive sent and thrown values directly from the calling scope, and return a final value to the outer generator:
#     
#     def accumulate(start=0):
#         tally = start
#         while 1:
#             next = yield
#             if next is None:
#                 return tally
#             tally += next
# 
#     def gather_tallies(tallies, start=0):
#         while 1:
#             tally = yield from accumulate()
#             tallies.append(tally)

# <markdowncell>

#     tallies = []
#     acc = gather_tallies(tallies)
#     next(acc) # Ensure the accumulator is ready to accept values
#     for i in range(10):
#          acc.send(i)
# 
#     acc.send(None) # Finish the first tally
#     for i in range(5):
#         acc.send(i)
# 
#     acc.send(None) # Finish the second tally
#     tallies
# 
# [45, 10]

# <markdowncell>

# 
# The main principle driving this change is to allow even generators that are designed to be used with the send and throw methods to be split into multiple subgenerators as easily as a single large function can be split into multiple subfunctions.

# <headingcell level=2>

# Iterators

# <codecell>

class CustomIterator(object):
    def __init__(self, limit):
        self.limit = limit
        self.i = 0
    def __iter__(self):
        return self
    def next(self):
        self.i += 1
        if self.i > self.limit:
            raise StopIteration
        return self.i
        
my_iterator = CustomIterator(5)
for i in my_iterator:
    print i

# <codecell>

# but what if we will try to iterate over it again
for i in my_iterator:
    print i

# <codecell>

class CustomIterator(object):
    def __init__(self, limit):
        self.limit = limit
        self.i = 0
    def __iter__(self):
        self.i = 0
        return self
    def next(self):
        self.i += 1
        if self.i > self.limit:
            raise StopIteration
        return self.i

my_iterator = CustomIterator(5)
for i in my_iterator:
    print i

for i in my_iterator:
    print i

# <codecell>

my_iterator = CustomIterator(3)
for i in my_iterator:
    for j in my_iterator:
        print i, j

# <codecell>

class CustomIterator(object):
    def __init__(self, limit):
        self.limit = limit
        self.i = 0
    def next(self):
        self.i += 1
        if self.i > self.limit:
            raise StopIteration
        return self.i
        
class CustomIteratorContainer(object):    
    def __init__(self, limit):
        self.limit = limit
        self.i = 0
    def __iter__(self):
        return CustomIterator(self.limit)

# <codecell>

my_iterator = CustomIteratorContainer(3)
for i in my_iterator:
    for j in my_iterator:
        print i, j

# <codecell>

my_iterator = iter(CustomIteratorContainer(3))
for i in my_iterator:
    print i

# <codecell>

class CustomIterator(object):
    def __init__(self, limit):
        self.limit = limit
        self.i = 0
    def __iter__(self):
        return self.__class__(self.limit)
    def next(self):
        self.i += 1
        if self.i > self.limit:
            raise StopIteration
        return self.i

# <codecell>

c = CustomIterator(3)
for i in c:
    print i

# <codecell>

# get iterator of iterator of iterator .... of iterator
for i in reduce(lambda x, y: iter(x), xrange(5), c):
    print i

# <headingcell level=3>

# iter() can take a callable argument

# <codecell>

def foo():
    i = [0] 
    def wrapped():
        i[0]+=1
        return i[0]
    return wrapped

for c in iter(foo(), 3):
    print c

# <headingcell level=3>

# next can take second argument

# <rawcell>

# ```next(iterator[, default])```
# 
# Retrieve the next item from the iterator by calling its ```next()``` method. If ```default``` is given, it is returned if the iterator is exhausted, otherwise ```StopIteration``` is raised.

# <codecell>

next(iter([]))

# <codecell>

next(iter([]), None)

# <headingcell level=3>

# Generators vs. Iterators

# <markdowncell>

# - A generator function is slightly different than an object that supports iteration
# 
# - A generator is a one-time operation. You can iterate over the generated data once, but if you want to do it again, you have to call the generator function again.
# 
# - This is different than a list (which you can iterate over as many times as you want)

# <headingcell level=3>

# reusable generator

# <codecell>

def reusable_generator(func):
    class Iter(object):
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
        def __iter__(self):
            return func(*self.args, **self.kwargs)
    return Iter

# <codecell>

@reusable_generator
def foo():
    [(yield i) for i in (1, 2, 3)]
    
foo_ins = foo()
[[i for i in foo_ins] for j in range(2)]

# <codecell>

class Test(object):
    @reusable_generator
    def foo(self):
        [(yield i) for i in (1, 2, 3)]
        
[i for i in Test().foo()]

# <codecell>

def reusable_generator(func):
    class WrappedIterator(object):
        def __init__(self, *args, **kwargs):
            self.args, self.kwargs = args, kwargs
        def __iter__(self):
            return func(*self.args, **self.kwargs)
    class inner(object):
        def __get__(self, instance, owner):
            def wrapped(*args, **kwargs):
                return WrappedIterator(instance, *args, **kwargs)
            return wrapped
    return inner()


class Test(object):
    @reusable_generator
    def foo(self):
        [(yield i) for i in (1, 2, 3)]
        
d = Test().foo()
[[i for i in d] for j in range(2)]

# <codecell>

d = Test.foo(Test())
[[i for i in d] for j in range(2)]

# <codecell>

def reusable_generator(func):
    class WrappedIterator(object):
        def __init__(self, *args, **kwargs):
            self.args, self.kwargs = args, kwargs
        def __iter__(self):
            return func(*self.args, **self.kwargs)
    class inner(object):
        def __call__(self, *args, **kwargs):
            return WrappedIterator(*args, **kwargs) 
        def __get__(self, instance, owner):
            if instance is None:
                return self
            def wrapped(*args, **kwargs):
                return self(instance, *args, **kwargs)
            return wrapped
    inner.__name__ = func.__name__
    return inner()


class Test(object):
    @reusable_generator
    def foo(self):
        [(yield i) for i in (1, 2, 3)]
        

@reusable_generator
def foo():
    [(yield i) for i in (1, 2, 3)]

# <codecell>

d =  Test().foo()
[[i for i in d] for j in range(2)]

# <codecell>

d = Test.foo(Test())
[[i for i in d] for j in range(2)]

# <codecell>

foo_ins = foo()
[[i for i in foo_ins] for j in range(2)]

# <codecell>

def reusable_generator(func):
    def wrapped(*args, **kwargs):
        class Iter(object):
            def __iter__(self):
                return func(*args, **kwargs)
        return Iter()
    return wrapped


class Test(object):
    @reusable_generator
    def foo(self):
        [(yield i) for i in (1, 2, 3)]
        

@reusable_generator
def foo():
    [(yield i) for i in (1, 2, 3)]

# <codecell>

d =  Test().foo()
[[i for i in d] for j in range(2)]

# <codecell>

d = Test.foo(Test())
[[i for i in d] for j in range(2)]

# <codecell>

foo_ins = foo()
[[i for i in foo_ins] for j in range(2)]

# <codecell>

from IPython.display import Image
def wat_generator():
    while True:
        for i in ['http://img213.imageshack.us/img213/3077/77663735.jpg',
                  'http://img580.imageshack.us/img580/4312/32411151.jpg',
                  'http://img803.imageshack.us/img803/4895/41730701.jpg',
                  'http://img22.imageshack.us/img22/1668/49588801.jpg',
                  'http://img803.imageshack.us/img803/6015/48104534.jpg',
                  'http://img560.imageshack.us/img560/3059/86402809.jpg',
                  'http://img15.imageshack.us/img15/2200/88668083.jpg',
                  'http://img543.imageshack.us/img543/3853/44000662.jpg']:
            yield Image(i)
            
wg = wat_generator()
wg.next()
def wat():
    return wg.next()

