# list usage

squares = [1,4,5,19,290,39]

# print(squares)
#
# # 输出list中的第4位数字
#
# print(squares[3])
#
# # 打印列表中的最后一位数据
# print(squares[-1])
#
# # 切片并返回新的列表
#
# print(squares[-3:])
#
#
# # list的复制
# print(squares[:])

'''
append 可以用来在list的末尾添加一个元素

这个元素可以是一个字符串或数学算法

'''
# squares.append(3**9)
#
# print(squares)
#
#
# squares.append(190)
#
# print(squares)

'''
insert 可以把一个元素添加到list中指定的位置  

语法：list.insert(index,obj)

insert ：对象obj需要插入列表中的索引位置

obj：要插入列表中的对象

'''

# squares.insert(3, 90)

'''
index 可以用于从列表中找出某个值第一个匹配项的索引位置

语法： list.index(obj)

'''

# print(squares.index(5))

'''
删除list中的元素有三种方法

del  pop 切片 和 remove

del 删除list指定索引位置的一个元素

语法：del list[index]

----------------------------------

pop 删除list中的元素

语法：list.pop(index)


-----------------------------------

remove 删除指定值的元素

语法：list.remove(value)

'''

# use del 删除list 中的元素

# del squares[3]
#
# print(squares)

# use pop 删除list中的元素

squares.pop(2)

print(squares)

# 如果不指定参数的话 默认删除最后一个元素
squares.pop()

print(squares)

squares.remove(4)

print(squares)




print(help(list("index")))

'''

Help on list object:

class list(object)
 |  list() -> new empty list
 |  list(iterable) -> new list initialized from iterable's items
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.n
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(...)
 |      L.__reversed__() -- return a reverse iterator over the list
 |  
 |  __rmul__(self, value, /)
 |      Return self*value.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      L.__sizeof__() -- size of L in memory, in bytes
 |  
 |  append(...)
 |      L.append(object) -> None -- append object to end
 |  
 |  clear(...)
 |      L.clear() -> None -- remove all items from L
 |  
 |  copy(...)
 |      L.copy() -> list -- a shallow copy of L
 |  
 |  count(...)
 |      L.count(value) -> integer -- return number of occurrences of value
 |  
 |  extend(...)
 |      L.extend(iterable) -> None -- extend list by appending elements from the iterable
 |  
 |  index(...)
 |      L.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.
 |  
 |  insert(...)
 |      L.insert(index, object) -- insert object before index
 |  
 |  pop(...)
 |      L.pop([index]) -> item -- remove and return item at index (default last).
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(...)
 |      L.remove(value) -> None -- remove first occurrence of value.
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(...)
 |      L.reverse() -- reverse *IN PLACE*
 |  
 |  sort(...)
 |      L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None


'''