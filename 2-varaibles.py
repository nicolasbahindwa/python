Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> num=5
>>> id(num)
1689778160
>>> 
>>> a= 10
>>> b=11
>>> b=a
>>> 
>>> id(a)
1689778240
>>> id(b)
1689778240
>>> 
>>> 
>>> num = 2.5
>>> 
>>> type(num)
<class 'float'>
>>> 
>>> num=3
>>> 
>>> tpw
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    tpw
NameError: name 'tpw' is not defined
>>> type(num)
<class 'int'>
>>> 
>>>  num =5+5j
 
SyntaxError: unexpected indent
>>> 
>>> num = 6 + 5j
>>> 
>>> type(num)
<class 'complex'>
>>> 
>>> 
>>> a = 5.6
>>> b=int(a)
>>> type(b)
<class 'int'>
>>> 
>>> k =float(b)
>>> k
5.0
>>> 
>>> k=6
>>> 
>>> c=complex(b,k)
>>> c
(5+6j)
>>> 
>>> 
>>> b<k
True
>>> bool = b<k
>>> bool
True
>>> type(bool)
<class 'bool'>
>>> 
>>> 
>>> b>k
False
>>> 
>>> int(true)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined
>>> 
>>> int(false)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    int(false)
NameError: name 'false' is not defined
>>> 
>>> lst[2,5,6,4,3,2]
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    lst[2,5,6,4,3,2]
NameError: name 'lst' is not defined
>>> 
>>> 
>>> 
>>> lst=[3,4,3,2,4,5]
>>> type(lst)
<class 'list'>
>>> 
>>> s = {3,4,5,3,3,45,5}
>>> type(s)
<class 'set'>
>>> 
>>> t = (3,5,4,5,3,24,5)
>>> type(t)
<class 'tuple'>
>>> 
>>> 
>>> range(10)
range(0, 10)
>>> 
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> 
>>> list(range(2,10,2))
[2, 4, 6, 8]
>>> 
>>> type(range(10))
<class 'range'>
>>> 
>>> 
>>> d={'nicolas:iphone', 'crispin:sumsung','john:nokia','joe:techno'}
>>> d.values()
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    d.values()
AttributeError: 'set' object has no attribute 'values'
>>> d.keys()
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    d.keys()
AttributeError: 'set' object has no attribute 'keys'
>>> d={'nicolas':'iphone', 'crispin':'sumsung','john':'nokia','joe':'techno'}
>>> 
>>> d.values()
dict_values(['iphone', 'sumsung', 'nokia', 'techno'])
>>> d.keys()
dict_keys(['nicolas', 'crispin', 'john', 'joe'])
>>> 
>>> 
>>> d['nicolas']
'iphone'
>>> 
>>> d.get('nicolas')
'iphone'
>>> 