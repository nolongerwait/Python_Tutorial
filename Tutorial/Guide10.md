# 学习Python的第十天

任务:
- 复习函数相关概念
- 学习函数参数的不同参数的应用和定义
    - 位置参数
    - 默认参数
    - 可变参数
    - 关键字参数
- 参数的组合

## 函数的参数

在此前，我们定义函数的时候，将参数的名字和位置确定下来，函数的定义就完成了。对于函数的调用者来说，只需要知道如何传递正确的参数，以及函数将返回什么样的值就够了，函数内部的复杂逻辑被封装起来，调用者无需了解。

Python的函数定义非常简单，但灵活度却非常大。除了正常定义的 **必选参数** 外，还可以使用 **默认参数** 、**可变参数** 和 **关键字参数**，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。

### 位置参数
我们先写一个计算x<sup>2</sup>的函数：
```python
def power(x):
    return x * x
```
对于`power(x)`函数，参数`x`就是一个位置参数。

当我们调用`power`函数时，必须传入有且仅有的一个参数x：
```
>>> power(5)
25
>>> power(15)
225
```

现在，如果我们要计算x<sup>3</sup>怎么办？可以再定义一个`power3`函数，但是如果要计算x<sup>4</sup>、x<sup>5</sup>……怎么办？我们不可能定义无限多个函数。

你也许想到了，可以把`power(x)`修改为`power(x, n)`，用来计算x<sup>n</sup>，说干就干：
```python
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
```

对于这个修改后的`power(x, n)`函数，可以计算任意n次方：
```
>>> power(5, 2)
25
>>> power(5, 3)
125
```
修改后的`power(x, n)`函数有两个参数：`x`和`n`，这两个参数都是位置参数，调用函数时，传入的两个值按照位置顺序依次赋给参数`x`和`n`。

### 默认参数
新的`power(x, n)`函数定义没有问题，但是，旧的调用代码失败了，原因是我们增加了一个参数，导致旧的代码因为缺少一个参数而无法正常调用：
```
>>> power(5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: power() missing 1 required positional argument: 'n'
```
> Python的错误信息很明确：调用函数power()缺少了一个位置参数n。

这个时候，默认参数就排上用场了。由于我们经常计算x<sup>2</sup>，所以，完全可以把第二个参数`n`的默认值设定为`2`：
```python
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
```
这样，当我们调用`power(5)`时，相当于调用`power(5, 2)`：
```
>>> power(5)
25
>>> power(5, 2)
25
```
而对于`n > 2`的其他情况，就必须明确地传入`n`，比如`power(5, 3)`。

从上面的例子可以看出，默认参数可以简化函数的调用。设置默认参数时，有几点要注意：
+ 一是必选参数在前，默认参数在后，否则Python的解释器会报错
    - （思考一下为什么默认参数不能放在必选参数前面）；
+ 二是如何设置默认参数。

### 可变参数
在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。

我们以数学题为例子，给定一组数字`a，b，c……`，请计算`a^2 + b^2 + c^2 + ……`。

要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，我们首先想到可以把`a，b，c……`作为一个`list`或`tuple`传进来，这样，函数可以定义如下：
```python
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
```
但是调用的时候，需要先组装出一个list或tuple：
```
>>> calc([1, 2, 3])
14
>>> calc((1, 3, 5, 7))
84
```
如果利用可变参数，调用函数的方式可以简化成这样：
```
>>> calc(1, 2, 3)
14
>>> calc(1, 3, 5, 7)
84
```
所以，我们把函数的参数改为可变参数：
```python
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
```
定义可变参数和定义一个`list`或`tuple`参数相比，仅仅在参数前面加了一个*号。在函数内部，参数`numbers`接收到的是一个`tuple`，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数， **包括0个参数** ：
```
>>> calc(1, 2)
5
>>> calc()
0
```
如果已经有一个`list`或者`tuple`，要调用一个可变参数怎么办？可以这样做：
```
>>> nums = [1, 2, 3]
>>> calc(nums[0], nums[1], nums[2])
14
```
这种写法当然是可行的，问题是太繁琐，所以Python允许你在`list`或`tuple`前面加一个`*`号，把list或tuple的元素变成可变参数传进去：
```
>>> nums = [1, 2, 3]
>>> calc(*nums)
14
```
`*nums`表示把`nums`这个`list`的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。

### 关键字参数
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个`tuple`。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个`dict`。请看示例：
```python
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
```
函数`person()`除了必选参数`name`和`age`外，还接受 **关键字参数** `kw`。在调用该函数时，可以只传入必选参数：
```
>>> person('Michael', 30)
name: Michael age: 30 other: {}
```
也可以传入任意个数的关键字参数：
```
>>> person('Bob', 35, city='Beijing')
name: Bob age: 35 other: {'city': 'Beijing'}
>>> person('Adam', 45, gender='M', job='Engineer')
name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
```
关键字参数有什么用？它可以扩展函数的功能。比如，在`person()`函数里，我们保证能接收到`name`和`age`这两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。

### 命名关键字参数
对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在 **函数内部** 通过`kw`检查。

仍以`person()`函数为例，我们希望检查是否有`city`和`job`参数：
```python
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)
```
但是调用者仍可以传入不受限制的关键字参数：
```
>>> person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
```
如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
```python
def person(name, age, *, city, job):
    print(name, age, city, job)
```
和关键字参数`**kw`不同，命名关键字参数需要一个特殊分隔符`*`，`*`后面的参数被视为命名关键字参数。

调用方式如下：
```
>>> person('Jack', 24, city='Beijing', job='Engineer')
Jack 24 Beijing Engineer
```
如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符`*`了：
```python
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
```
命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
```
>>> person('Jack', 24, 'Beijing', 'Engineer')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: person() takes 2 positional arguments but 4 were given
```
由于调用时缺少参数名`city`和`job`，Python解释器把这4个参数均视为位置参数，但`person()`函数仅接受2个位置参数。

命名关键字参数可以有缺省值，从而简化调用：
```python
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)
```
由于命名关键字参数`city`具有默认值，调用时，可不传入`city`参数：
```
>>> person('Jack', 24, job='Engineer')
Jack 24 Beijing Engineer
```

## 参数组合
在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

比如定义一个函数，包含上述若干种参数：
```python
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
```
在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去。
```
>>> f1(1, 2)
a = 1 b = 2 c = 0 args = () kw = {}
>>> f1(1, 2, c=3)
a = 1 b = 2 c = 3 args = () kw = {}
>>> f1(1, 2, 3, 'a', 'b')
a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
>>> f1(1, 2, 3, 'a', 'b', x=99)
a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
>>> f2(1, 2, d=99, ext=None)
a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}
```
最神奇的是通过一个tuple和dict，你也可以调用上述函数：
```
>>> args = (1, 2, 3, 4)
>>> kw = {'d': 99, 'x': '#'}
>>> f1(*args, **kw)
a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
>>> args = (1, 2, 3)
>>> kw = {'d': 88, 'x': '#'}
>>> f2(*args, **kw)
a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
```
所以，对于任意函数，都可以通过类似`func_name(*args, **kw)`的形式调用它，无论它的参数是如何定义的。

<p align="center">
  <a href="Guide09.md">上一篇教程</a>  --------------------------------------  <a href="Guide11.md">下一篇教程
</p>