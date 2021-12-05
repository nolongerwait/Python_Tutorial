# 学习Python的第六天

任务:
- 掌握控制流语句
- 条件语句if
    - if语句的基本构成
    - if系列语句的执行原则
- 循环语句while
    - while的基本构成
    - while的执行原则
- 循环语句for
    - for的基本构成
    - for的执行原则
- for和while的不同用途

## 控制流
截止到现在，在我们所看过的程序中，总是一系列语句从上到下编写，并交由 Python 忠实地执行，即逐行从上到下依次执行。如果你想改变这一流程，应该怎么做？比如，让程序根据不同的条件去分别执行不同的语句。或者，让程序循环执行某句话多少次。

所以，我们现在引入条件语句if和两种循环语句while和for来帮助实现Python中流程的语句执行管理和控制。

## `if`语句
`if` 语句用以检查条件：如果 条件为真（`True`），我们将运行一块语句（称作 `if`-block 或 `if` 块），否则 我们将运行另一块语句（称作 `else`-block 或 `else` 块）。其中 `else` 从句是可选的。

从上面这段话可以知道，条件语句的构成可以分为下面这几种结构:
```python
# only if
if condition:
    statements # if condition is true, then execute these statements.


# if - else
if condition:
    statements1 # if condition is true, then execute these statements1.
else:
    statements2 # if condition is false, then execute these statements2


# if - elif - else
if condition1:
    statements1 # if condition1 is true, then execute these statements.
elif condition2:
    statements2 # if condition2 is true, then execute these statements2.
elif condition3:
    statements3 # if condition3 is true, then execute these statements3.

    ...

else:
    statementsn # for other conditions(condition1 is false, condition2 is false and condition ..... ), then execute these statementsn
```

下面我们举个例子，来实际运行一下。
请将下面的代码保存为[if.py](../Code/06/if.py)

```python
number = 23
guess = int(input('Enter an integer : '))

if guess == number:
    # 新块从这里开始
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
    # 新块在这里结束
elif guess < number:
    # 另一代码块
    print('No, it is a little higher than that')
    # 你可以在此做任何你希望在该代码块内进行的事情
else:
    print('No, it is a little lower than that')
    # 你必须通过猜测一个大于（>）设置数的数字来到达这里。

print('Done')
# 这最后一句语句将在
# if 语句执行完毕后执行。
```
运行结果的输出:

```
$ python if.py
Enter an integer : 50 （50是你执行完程序，在terminal中出现Enter an integer时候输入的内容。下面同理）
No, it is a little lower than that
Done

$ python if.py
Enter an integer : 22
No, it is a little higher than that
Done

$ python if.py
Enter an integer : 23
Congratulations, you guessed it.
(but you do not win any prizes!)
Done
```
具体操作示范
![gif01](Source/QQ20200206-061328-HD.gif)

### `if`工作原理

在这个程序中，我们让用户猜测一个数字。我们将变量 number 设为任何我们所希望的整数，例如 23。然后，我们通过 `input()` 函数来获取用户的猜测数。(有关`intput`和函数的概念，明日讲解。而现在，只需要知道`input`可以让程序从Terminal中获取用户输入的内容)  

接下来，我们将用户输入的猜测数与我们所设定好的数字进行对比。如果它们相等，我们就打印一条成功信息。在这里要注意到我们使用缩进级别来告诉 Python 哪些语句分别属于哪个块。这便是为什么之前说在 Python 中缩进如此重要。

另外需要注意的是 `if` 语句在结尾处包含一个**冒号**——用语向 Python 表明接下来会有一块语句在后头。  

然后，我们检查猜测数是否小于我们设定的数字，如果是，我们将告诉用户他们必须猜一个更高一些的数字。在这里我们使用的是 `elif` 语句（elif即 else if的缩写），它们实际上将两个相连的 `if else-if else` 语句合并成一句 `if-elif-else` 语句。这能够使程序更加简便，并且可以减少所需要的缩进量。  

`elif` 和 `else` 同样都必须有一个冒号在其逻辑行的末尾，后面跟着与它们相应的语句块（当然，别忘了缩进）。  

要记住 `elif` 和 `else` 部分都是可选的。一个最小规模且有效的 `if` 语句是这样的：
```python
if condition:
   statements
```
当 Python 完整执行了 `if` 语句及与其相关的 `elif` 和 `else` 子句后，它将会移动至包含 `if` 语句的代码块的下一句语句中。在本例中，也就是主代码块（程序开始执行的地方），其下一句语句就是 `print('Done')` 语句。在完成这些工作后，Python 会发现已行至程序末尾并宣告工作的完成。

#### 嵌套的if和并列的if

你可以在 `if` 块的 一个 `if` 语句中设置另一个 `if` 语句，并可以如此进行下去——这被称作**嵌套**的 `if` 语句。
```python
# 嵌套的IF语句
if condition1:
    # start the condition 1 block
    if condition2:
        # start the condition 2 block
        statements2
        # end the condition 2 block
    statements1 
    # end the condition 1 block


# 并列的if语句
if condition1:
    # start the condition 1 block
    statements1 
    # end the condition 1 block
if condition2:
    # start the condition 2 block
    statements2
    # end the condition 2 block
```
## `while` 语句
`while` 语句能够让你在条件为真的前提下重复执行某块语句。 `while` 语句是 **循环（Looping）** 语句的一种。`while` 语句同样可以拥有 `else` 子句作为可选选项。
> 说明，`while`的`else`子句，只是在循环条件结束后进行执行的。实际上有没有这个else子句影响并不大。即便没有这个`else`，我们也可以直接写其他语句来执行。

下面我们来看一个例子，将下面的代码保存为[while.py](../Code/06/while.py)
```python
number = 23
running = True

while running:
    guess = int(input('Enter an integer : '))

    if guess == number:
        print('Congratulations, you guessed it.')
        # 这将导致 while 循环中止，因为循环条件此后将不再满足
        running = False
    elif guess < number:
        print('No, it is a little higher than that.')
    else:
        print('No, it is a little lower than that.')
else:
    print('The while loop is over.')
    # 在这里你可以做你想做的任何事

print('Done')
```
输出
```
$ python while.py
Enter an integer : 50
No, it is a little lower than that.
Enter an integer : 22
No, it is a little higher than that.
Enter an integer : 23
Congratulations, you guessed it.
The while loop is over.
Done
```
![gif02](Source/QQ20200206-065516-HD.gif)

### `while`的工作原理
在这一程序中，我们依旧通过猜数游戏来演示，不过新程序的优点在于能够允许用户持续猜测直至他猜中为止——而无需像我们在上一节中所做的那样，每次猜测都要重新运行程序。这种变化恰到好处地演示了 `while` 语句的作用。

首先我们将 `input` 与 `if` 语句移到 `while` 循环之中，并在 `while` 循环开始前将变量 `running` 设置为 `True`。程序开始时，我们首先检查变量 `running` 是否为 `True`，之后再执行相应的 `while` 块。在这一代码块被执行之后，将会重新对条件进行检查，在本例中也就是 `running` 变量。如果它依旧为 True，我们将再次执行 `while` 块，否则我们将继续执行可选的 `else 块`，然后进入到下一个语句中。

`while`结束后的`else` 代码块在 `while` 循环的条件变为 `False` 时开始执行——这个开始的时机甚至可能是在第一次检查条件的时候。如果 `while` 循环中存在一个 `else` 代码块(比如`while`中`if-else`的`else`)，它将总是被执行，除非你通过 `break` 语句来中断这一循环。

## `for` 循环
`for...in` 语句是另一种循环语句，其特点是会在一系列对象上进行 **迭代（Iterates）** ，意即它会遍历序列中的每一个项目。我们将在后面的序列（Sequences）章节中了解有关它的更多内容。现在你所需要的就是所谓序列就是一系列项目的有序集合。

和前面一样，我们还是看个案例（保存为[for.py](../Code/06/for.py)）：
```python
for i in range(1, 5):
    print(i) # i will be changed in each looping
else:
    print('The for loop is over')
```
运行输出
```
$ python for.py
1
2
3
4
The for loop is over
```
### `for`的工作原理
在这一程序中，我们打印了一个数字序列，通过内置的 `range()` 函数生成这个数字序列。(这里并不详细讲解`range()`的工作原理，你只需知道。此处它提供了一个从1到5的数字序列`[1, 2, 3, 4]`)

然后 `for` 循环就会在这一范围内展开递归——`for i in range(1,5)` 等价于 `for i in [1, 2, 3, 4]`，这个操作将依次将队列里的每个数字（或是对象）分配给 `i`，一次一个，然后以每个 `i` 的值执行语句块。在本例中，我们这一语句块所做的就是打印出这些值。

同样要记住，`for`结束后的`else` 部分是可选的。当循环中包含他时，它总会在 `for` 循环结束后开始执行，除非程序遇到了 `break` 语句。

## 循环中的特殊控制 —— **中断** 和 **继续**
### 中断(break)语句
`break` 语句用以中断（Break）循环语句，也就是**中止循环**语句的执行，即使循环条件没有变更为 `False`，或者序列中的项目尚未完成全部迭代。  

有一点需要尤其注意，如果你 **中断** 了一个 `for` 或 `while` 循环，从`break`之后的任何循环体内的代码都不会执行。

看个案例吧（保存为[break.py](../Code/06/break.py)）
```python
while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    print('Length of the string is', len(s))
print('Done')
```
运行输出
```
$ python break.py
Enter something : Programming is fun
Length of the string is 18
Enter something : When the work is done
Length of the string is 21
Enter something : if you wanna make your work also fun:
Length of the string is 37
Enter something : use Python!
Length of the string is 11
Enter something : quit
Done
```
#### `break`的工作原理
在这个程序中，我们重复地接受用户的输入内容并打印出每一次输入内容的长度。我们通过检查用户输入的是否是 `quit` 这一特殊条件来判断是否应该终止程序。

当然或许你也注意到了，这个程序中`while`的条件始终是`True`这就意味着，如果我们不通过其他手段终止循环，那么这个循环将成为死循环而一直执行下去。

### 继续(continue)语句
`continue` 语句用以告诉 Python 跳过当前循环块中的剩余语句，直接进入下一次循环中。
案例（保存为[continue.py](../Code/06/continue.py)）：
```python
for i in range(0, 9):
    if i == 5:
        continue
    print(i)
print("Loop is end.")
```
执行输出
```
0
1
2
3
4
6 
7
8
Loop is end.
```
#### `continue`的工作原理
这个程序，我们用`for`循环语句来依次输出0-8这9个数。但是在中途，我进行了一次判断，当轮到`5`的时候，执行`continue`语句，直接跳到下一次循环。这样，在`continue`后面的`print`语句在`i = 5`的时候没有得到执行，最后的输出结果也没有`5`。

> `break`和`continue`语句都是控制循环语句的，他们无法控制其他语句，只对循环起作用。

> 如果 `break` 和 `continue` 在嵌套的循环语句内。那么请注意`break`和`continue`所处的层级，他们控制的是与他们当前层级一致的循环语。

```python
for i in range(0, 10):
    for j in range(10, 20):
        if j = 15:
            continue # this control the j looping
    if i = 5:
        continue # this control the i looping
```

# 作业
- 创建一个worksheet06.py文件
- 在这个文件中完成如下内容
    - 使用循环语句和条件语句，输出0-20内所有的奇数

<p align="center">
  <a href="Guide05.md">上一篇教程</a>  --------------------------------------  <a href="Guide07.md">下一篇教程
</p>