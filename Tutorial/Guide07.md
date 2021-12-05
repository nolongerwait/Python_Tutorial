# 学习Python的第七天

任务:
- 掌握函数这一重要的编程概念
    - 学会如何自己定义一个函数
    - 了解如何调用一个函数
    - 函数的参数和它的返回值
- 理解局部变量和变量的作用域 

## 函数
首先，思考一下这样一个场景。我要计算任意两个变量的和，并且这里有很多个变量。给任意两个变量都单独写一个 `x + y` 肯定不现实。所以我们必须把 *两个数相加的和* 作为一个功能块，在需要使用的时候调用这个功能块，它就可以计算任意两变量的和了。

**函数（Functions）** 是指可重复使用的程序片段。它们允许你为某个代码块赋予名字，允许你通过这一特殊的名字在你的程序任何地方来运行该代码块，并可重复任何次数。这个过程就是所谓的 **调用（Calling）** 函数。我们已经使用过了许多内置的函数，例如 `print()`和`format()`。

函数概念可能是在任何复杂的软件（无论使用的是何种编程语言）中最重要的构建块，所以我们接下来将在本章中探讨有关函数的各个方面。

函数可以通过关键字 `def` 来定义。这一关键字后跟一个函数的标识符名称(即 **函数名** )，再跟一对圆括号，括号中会有一些变量(即 **参数** )，再以冒号结尾，结束这一行。冒号之后的新的语句块是函数的 **函数体** 。

我们来看一个栗子🌰吧：(将下面的程序保存为[function1.py](../Code/07/function1.py))
```python
# start the function say_hello()
def say_hello():
    # start the function body block
    print('hello world')
    # end the function body block
# end the function say_hello()

say_hello()  # call the function
say_hello()  # call the function again
```
运行后得到输出
```
hello world
hello world
```
![gif01](Source/QQ20200206-234031-HD.gif)

*问题来了，这是怎么一回事？*

在这个程序文件中，我们一开始定义了一个函数`say_hello()`，它的功能就是打印`hello world`。在函数定义完成后，我们调用了两次`say_hello()`，所以就实现了打印两次`hello world`。

### 函数参数 和 函数的返回值
上面的栗子中，我们定义的函数是没有参数的。因为它的功能只是打印一串特定的内容，不需要接收其他变量，或者对其他变量进行处理。但是接下来，我们来认识一下函数的参数。

我们通过实际例子来感受一下，什么是函数的参数(保存代码到[function2.py](../Code/07/function2.py))
```python
def add_two_num(a, b):
    # a and b are the parameters of add_two_num()
    '''This function compute the sum of two numbers(a and b).
    '''
    return a + b # the result which function will return

print(add_two_num(3, 5)) # 3 and 5 are the arguments of add_two_num()

x = 10
y = 20
print(add_two_num(x, y)) # x and y are the arguments of add_two_num()
```
代码的运行结果为：
```
8
30
```
![gif02](Source/QQ20200207-000033-HD.gif)

*让我们继续来分析上面的代码的是如何工作的*

首先在程序中，定义了一个`add_two_num()`的函数，这个函数有两个参数，表明函数可以接收两个外来的变量a和b来在函数内部进行处理。此时，我们把在定义函数时候的参数，称之为 **形参(parameter)** 。函数体内部，则是计算了`a + b`的结果。然后将它返回给外界。
> 为什么要有返回值，如果我们不用`return`语句进行返回，那么计算出来的`a + b`的结果永远只能留在那个函数内部，而在其他地方我们无法获取到计算的结果。为了能让计算的结果被使用到，我们需要 **返回** 计算的结果。
> > 这就好比，一个函数相当于一个加工站，我们加入原料（参数），得到加工后的产品（返回值） 

在定义函数后，我们调用了两次`add_two_num()`。第一次调用的时候，我们直接将字面常量`3`和`5`作为参数，此时的参数，我们称之为 **实参(argument)** 。
> 此时程序将实参分别替换到形参，也就是`3`被拷贝了一份，复制给`a`。同理`5`被拷贝了一份，复制给`b`，然后计算`a + b`得到`3 + 5`即`8`。

第二次，我们定义了两个变量`x`和`y`，调用函数来计算他们的和`add_two_num(x, y)`此时，`x`和`y`就是函数的实参。
> 此时程序将实参分别替换到形参，也就是`x`的值被拷贝了一份，复制给`a`。同理`y`的值被拷贝了一份，复制给`b`，然后计算`a + b`得到`10 + 20`即`30`。

### 参数的默认值
对于一些函数来说，你可能为希望使一些参数成为可选的，而且他们可以拥有默认的值。默认参数值可以有效帮助解决这一情况。你可以通过在函数定义时附加一个赋值运算符（=）来为参数指定默认参数值。

要注意到，默认参数值应该是常量。更确切地说，默认参数值应该是不可变的——这将在后面的章节中予以更详细的解释。就目前来说，只要记住就行了。
案例（保存为[function_default.py](../Code/07/function_default.py)）：
```python
def say(message, times=1):
    print(message * times)

say('Hello') # using the default parameter time = 1
say('World', 5) # using the argument time = 5
```
输出：
```
Hello
WorldWorldWorldWorldWorld
```

## 局部(local)变量，全局(global)变量和变量的作用域(scope)
为了更好的了解函数内的变量的工作方式，我们现在讨论一下一个变量的生命周期。

还是老样子，先来看一个代码[local_variable.py](../Code/07/local_variable.py)
```python
# The 1st level block start
x = 50

def func(x):
    # The 2nd level block start
    print('x is', x)
    x = 2 # this x is local variable in func().
    print('Changed local x to', x)
    # The 2nd level block end

func(x)
print('x is still', x)
# The 1st level block end
```
运行，得到的结果
```
x is 50
Changed local x to 2
x is still 50
```
![gif03](Source/QQ20200207-003412-HD.gif)  

*分析工作过程*
一开始，我们定义了一个变量`x`，此时这个`x`是处于第一层级的语句块中的。然后我们定义了一个`func()`函数，在这个函数体中内，因为强制性的缩进要求，函数体的语句块，成为了第二层级的语句块。  
在第二层级的语句块中，我们先打印了一下`x`。此时由于第二层级的语句块中并么有`x`，所以此时打印的是第一层级的`x`即`50`。而后，定义了局部变量`x`为`2`，再打印`x`，此时第二层级的语句块拥有了它自己范围内的`x`。所以打印的`2`。  
而在函数结束后，我们又回到了第一层级的语句块中，我们再次打印`x`。由于第一层级无法访问第二层级的内容，所以打印的结果只能是第一层级的`50`。

知道了这个过程，我们可以知道。第一层级的变量的作用域只在第一层级和隶属于第一层级的第二层级。而第二层级的变量的作用域只能存在于第二层级中。

那么我们如何让第二层级的局部变量也能在第一层级使用呢？这就要讲到 **全局变量** 我们在`x = 2`前面加上一个关键字`global`（`global x = 2`）就可以实现将了。

加上`global`之后的输出就成了
```
x is 50
Changed global x to 2
Value of x is 2
```

## 调用其他文件中定义的函数
有时候我们会将不同功能的函数定义在不同的文件中。举个例子，我如何在function1.py中调用function2.py定义的`add_two_num()`呢？

着我们就需要在function1.py的开头，加上这么一段代码`import function2`。然后在程序用使用`function2.add_two_num()`就可以调用到`add_two_num()`了。
```python
import function2

function2.add_two_num(3, 5)
```

# 作业
- 创建一个worksheet07.py文件
- 在这个文件中完成如下内容
    - 编写一个能够计算两个数加法的函数`addition(a, b)`
    - 编写一个能够计算两个数减法的函数`subtraction(a, b)`
    - 编写一个能够计算两个数乘法的函数`multiplication(a, b)`
    - 编写一个能够计算两个数除法的函数`division(a, b)`
- 在本地创建[sample.py](../Code/sample.py)放在和worksheet07.py同目录的文件夹下
    - 在worksheet07.py中，调用sample.py的`show()`函数


<p align="center">
  <a href="Guide06.md">上一篇教程</a>  --------------------------------------  <a href="Guide08.md">下一篇教程
</p>