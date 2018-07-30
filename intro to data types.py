Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a=5
>>> b=10
>>> a=b
>>> a=5
>>> temp=a
>>> a=b
>>> b=temp
>>> a
10
>>> b
5
>>> 
>>> four='4'
>>> print(four*3)
444
>>> five=4
>>> print
<built-in function print>
>>> (five)
4
>>> print(five*3)
12
>>> >>> my_name = ‘student’
>>> print(“Hi,” + myName’)
SyntaxError: invalid syntax
>>> my_name = ‘student’
>>> print(“Hi,” + myName’)
SyntaxError: invalid character in identifier
>>>  my_name = ‘student’
>>> print(“My name is ’ + ‘my_name”)
SyntaxError: unexpected indent
>>> my_name='student'
>>> print("hi"+myname)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print("hi"+myname)
NameError: name 'myname' is not defined
>>> print("hi"+'myname')
himyname
>>> 
