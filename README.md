**1. Arguments are passed by assignment**
  * If you pass a mutable object into a method, the method gets a reference to that same object and you can mutate it to your heart's delight, but if you rebind the reference in the method, the outer scope will know nothing about it, and after you're done, the outer reference will still point at the original object.
  * If you pass an immutable object to a method, you still can't rebind the outer reference, and you can't even mutate the object.
  * [example](https://github.com/CHENGXINHUAMARK/Python_LXF/blob/master/para_passbyreference_value.py)
**2. 匿名函数**
  * [Lambda](https://github.com/CHENGXINHUAMARK/Python_LXF/blob/master/Lambda.py)
