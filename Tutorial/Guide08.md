# 学习Python的第八天

任务:
- 开始简单了解Python中的进阶数据结构
    - 掌握什么是列表List
    - 掌握什么是元组Tuple
    - 掌握什么是字典Dictionary
      - 掌握什么是序列Sequence
    - 掌握什么是集合Set
- 了解Python中的引用

## 数据结构
我们之前了解了Python里面最基本的数据类型，那些数据类型都是很基础的。只能存储单个数据。但实际上，我们有时候会需要处理一系列数据，这一系列数据在程序中药存储在某一个对象中，然后我们去操作这个对象，就能够进行数据的处理了。  

那么，

**数据结构（Data Structures）** 应运而生——它们只是一种结构，能够将一些数据聚合在一起。换句话说，它们是用来存储一系列相关数据的集合。
Python 中有四种内置的数据结构——列表（List）、元组（Tuple）、字典（Dictionary）和集合（Set）。下面咱来了解下这些东西都是个啥。

### 列表List
列表是一种用于保存一系列 **有序项目** 的集合，也就是说，你可以利用列表保存一串项目的序列。想象起来也不难，你可以想象你有一张购物清单，上面列出了需要购买的商品。只不过购物清单上的每项都是独占一行，Python里面定义列表的时候，每项和每项之间要通过逗号`,`分开。
> 请注意，咋编写程序时候，请将输入法调整为英文。所有的编程语言不支持中文标点（作为字符串内容的除外）

项目的列表应该用方括号括起来，这样 Python 才能理解到你正在指定一张列表。一旦你创建了一张列表，你可以添加、移除或搜索列表中的项目。既然我们可以添加或删除项目，我们会说列表是一种 **可变的（Mutable）** 数据类型，意即，这种类型是可以被程序所改变的。

我们来看一个列表的栗子🌰（将下面示范代码保存为[ds_using_list.py](../Code/08/ds_using_list.py)）
```python
# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shoplist), 'items to purchase.')

print('These items are:', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist)

print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)
```
运行上述程序后的结果输出为：
```
I have 4 items to purchase.
These items are: apple mango carrot banana
I also have to buy rice.
My shopping list is now ['apple', 'mango', 'carrot', 'banana', 'rice']
I will sort my list now
Sorted shopping list is ['apple', 'banana', 'carrot', 'mango', 'rice']
The first item I will buy is apple
I bought the apple
My shopping list is now ['banana', 'carrot', 'mango', 'rice']
```
*现在，我们捋一捋List是怎么使用和起作用的*

首先程序一开始，定义了一个 *名为`shoplist`的list对象*，当然它同时也是一个变量。所以如何定义一个list对象呢？就是通过 `变量名 = [item1, item2, ..., itemn]`这样的形式来定义一个list对象（变量）。  

在这个`shoplist`对象中，包含了四个字符串元素`'apple'`, `'mango'`, `'carrot'`, `'banana'`。那么我们就说这个列表的长度为`4`，因为它包含四个元素。当然，在第一次打印输出中，我们也可以通过`len()`函数来计算一个列表的长度。

那么，我们如何给一个已经存在的list对象添加新的元素呢？这里就要用到`append()`方法了。请注意，给一个list添加新的元素的方法是：`要添加进的list的名字.append(新元素)`
> 请务必注意到是list.append()，这个过程是通过`.`这种成员操作符进行的。

同理，如何删除一个列表中的元素呢？我们可以使用`del`方法。比如我们要删掉第一个元素。那就是`del shoplist[0]`这样就将0号元素（第一个元素）删除掉了。删除掉一个元素之后，后面的元素会自动往前补齐，不会说删掉某个位置的元素之后，这个位置就空出来了。

当然了，作为一个列表，肯定还有其他功能，比如排序。我们可以对列表中的元素按照顺序进行排序。比如`shoplist.sort()`这个方法，就会让shoplist中的元素按照从小到大的顺序排序，如果是字符串，就按照首字母升序进行排序。

### 元组

**元组（Tuple）** 用于将多个 **对象** 保存到一起。你可以将它们近似地看作列表，但是元组不能提供列表类能够提供给你的广泛的功能。元组的一大特征是，他们是不可变的，也就是说，你不能编辑或更改元组。

元组是通过特别指定项目来定义的，在指定项目时，你可以给它们加上括号，并在括号内部用逗号进行分隔。

元组通常用于保证某一语句或某一用户定义的函数可以安全地采用一组数值，意即元组内的数值不会改变。
案例（保存为[ds_using_tuple.py](../Code/08/ds_using_tuple.py)）：
```python
# 我会推荐你总是使用括号
# 来指明元组的开始与结束
# 尽管括号是一个可选选项。
# 明了胜过晦涩，显式优于隐式。
zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))

# 这里，就是元组将多个对象放在一起的表现了。元组中科院包含元组自身。
# new_zoo包含三个元素：猴子，骆驼和zoo元组
new_zoo = 'monkey', 'camel', zoo 
# 推荐写成 new_zoo = ('monkey', 'camel', zoo)
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is',
      len(new_zoo)-1+len(new_zoo[2]))
```
运行后结果：
```
Number of animals in the zoo is 3
Number of cages in the new zoo is 3
All animals in new zoo are ('monkey', 'camel', ('python', 'elephant', 'penguin'))
Animals brought from old zoo are ('python', 'elephant', 'penguin')
Last animal brought from old zoo is penguin
Number of animals in the new zoo is 5
```
*给你讲讲上面代码中有关元组的细节*

列表是通过方括号创建的，元组则是通过圆括号创建的。比如`zoo`元组，它包含三个元素，长度为3。`new_zoo`也是包含3个元素，长度为3。

在`zoo`元组中`zoo[0]`, `zoo[1]`, `zoo[2]`分别表示`'python'`, `'elephant'`, `'penguin'`。

在`new_zoo`元组中`new_zoo[0]`, `new_zoo[1]`, `new_zoo[2]`分别表示`'monkey'`, `'camel'`, `zoo`。也就是说`new_zoo[2]`表示的是`zoo`元组，那么就可以再次通过角标访问`zoo`的内容了。比如`new_zoo[2][0]`就是`python`了。

### 字典
字典就像一本通讯录，如果你知道了他或她的姓名，你就可以在这里找到其地址或是能够联系上对方的更多详细信息。
换言之，我们将键值（Keys）（即姓名）与值（Values）（即地址等详细信息）联立到一起。在这里要注意到键值必须是 **唯一** 的。  

另外要注意的是你只能使用不可变的对象（如字符串）作为字典的键值，但是你可以使用可变或不可变的对象作为字典中的值。

如何创建一个字典呢，你可以用 `d = {key : value1 , key2 : value2}` 这样的形式，来成对地指定键值与值。在这里要注意到成对的键值与值之间使用冒号分隔，而每一对键值与值则使用逗号进行区分，它们全都由一对花括号括起。

另外需要记住，字典中的成对的键值—值配对不会以任何方式进行排序。如果你希望为它们安排一个特别的次序，只能在使用它们之前自行进行排序。

案例（保存[ds_using_dict.py](../Code/08/ds_using_dict.py)）：
```python
ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

print("Swaroop's address is", ab['Swaroop'])

# 删除一对键值—值配对
del ab['Spammer']

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))

# 添加一对键值—值配对
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])
```
运行后结果：
```
Swaroop's address is swaroop@swaroopch.com

There are 3 contacts in the address-book

Contact Swaroop at swaroop@swaroopch.com
Contact Matsumoto at matz@ruby-lang.org
Contact Larry at larry@wall.org

Guido's address is guido@python.org
```
*字典中的一些细节*

我们可以通过我们的老朋友—— `del` 语句——来删除某一键值—值配对。我们只需指定字典、包含需要删除的键值名称的索引算符，并将其传递给 del 语句。这一操作不需要你知道与该键值相对应的值。

接着，我们通过使用字典的 `items()` 方法来访问字典中的每一对键值—值配对信息，这一操作将返回一份包含元组的列表，每一元组中则包含了每一对相应的信息——键值以及其相应的值。我们检索这一配对，并通过 `for...in` 循环将每一对配对的信息相应地分配给 `name` 与 `address` 变量，并将结果打印在 `for` 代码块中。

如果想增加一堆新的键值—值配对，我们可以简单地通过使用索引运算符访问一个键值并为其分配与之相应的值，就像我们在上面的例子中对 `Guido` 键值所做的那样。

我们可以使用 `in` 运算符来检查某对键值—值配对是否存在。

#### 序列

列表、元组和字符串可以看作 **序列（Sequence）** 的某种表现形式，可是究竟什么是序列，它又有什么特别之处？

序列的主要功能是 **资格测试（Membership Test）** （也就是 in 与 not in 表达式）和 **索引操作（Indexing Operations）** ，它们能够允许我们直接获取序列中的特定项目。
上面所提到的序列的三种形态——列表、元组与字符串，同样拥有一种 **切片（Slicing）** 操作，它能够允许我们序列中的某段切片——也就是获取序列之中的一部分。
> 这个翻译很神奇，但它的确就是这样的意思。

废话不多说。看例子[ds_seq.py](../Code/08/ds_seq.py)
```python
shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

# Indexing or 'Subscription' operation #
# 索引或“下标（Subscription）”操作符 #
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])

# Slicing on a list #
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

# 从某一字符串中切片 #
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])
```
运行结果：
```
Item 0 is apple
Item 1 is mango
Item 2 is carrot
Item 3 is banana
Item -1 is banana
Item -2 is carrot
Character 0 is s
Item 1 to 3 is ['mango', 'carrot']
Item 2 to end is ['carrot', 'banana']
Item 1 to -1 is ['mango', 'carrot']
Item start to end is ['apple', 'mango', 'carrot', 'banana']
characters 1 to 3 is wa
characters 2 to end is aroop
characters 1 to -1 is waroo
characters start to end is swaroop
```
*絮絮叨叨的时间，关于序列的*

首先，我们已经了解了如何通过使用索引来获取序列中的各个项目。这也被称作 **下标操作（Subscription Operation）** 。如上所示，每当你在方括号中为序列指定一个数字，Python 将获取序列中与该位置编号相对应的项目。要记得 Python 从 0 开始计数。因此 `shoplist[0]` 将获得 `shoplist` 序列中的第一个项目，而 `shoplist[3]` 将获得第四个项目。

索引操作也可以使用负数，在这种情况下，位置计数将从队列的末尾开始。因此，`shoplist[-1]` 指的是序列的最后一个项目，`shoplist[-2]` 将获取序列中倒数第二个项目。

你需要通过指定序列名称来进行序列操作，在指定时序列名称后面可以跟一对数字——这是可选的操作，这一对数字使用方括号括起，并使用冒号分隔。在这里需要注意，它与你至今为止使用的索引操作显得十分相像。但是你要记住数字是可选的，冒号却不是。

在切片操作中，第一个数字（冒号前面的那位）指的是切片开始的位置，第二个数字（冒号后面的那位）指的是切片结束的位置。如果第一位数字没有指定，Python 将会从序列的起始处开始操作。如果第二个数字留空，Python 将会在序列的末尾结束操作。要注意的是切片操作会在开始处返回 `start`，并在 `end` 前面的位置结束工作。也就是说，序列切片将包括起始位置，但不包括结束位置。(左闭右开区间)

因此，`shoplist[1:3]` 返回的序列的一组切片将从位置 `1` 开始，包含位置 `2` 并在位置 `3` 时结束，因此，这块切片返回的是两个元素。类似地，`shoplist[:]` 返回的是整个序列。

你同样可以在切片操作中使用负数位置。使用负数时位置将从序列末端开始计算。例如，`shoplist[:-1]` 强返回一组序列切片，其中不包括序列的最后一项项目，但其它所有项目都包含其中。

你同样可以在切片操作中提供第三个参数，这一参数将被视为切片的 **步长（Step）**（在默认情况下，步长大小为 `1`）：
```python
>>> shoplist = ['apple', 'mango', 'carrot', 'banana']
>>> shoplist[::1]
['apple', 'mango', 'carrot', 'banana']
>>> shoplist[::2]
['apple', 'carrot']
>>> shoplist[::3]
['apple', 'banana']
>>> shoplist[::-1]
['banana', 'carrot', 'mango', 'apple']
```
你会注意到当步长为 2 时，我们得到的是第 0、2、4…… 位项目。当步长为 3 时，我们得到的是第 0、3……位项目。


### 集合
集合（Set）是简单对象的无序集合（Collection）。

通过使用集合，你可以测试某些对象的资格或情况，检查它们是否是其它集合的子集，找到两个集合的交集，等等。
```python
>>> bri = set(['brazil', 'russia', 'india'])
>>> 'india' in bri
True
>>> 'usa' in bri
False
>>> bric = bri.copy()
>>> bric.add('china')
>>> bric.issuperset(bri)
True
>>> bri.remove('russia')
>>> bri & bric # OR bri.intersection(bric)
{'brazil', 'india'}
```

## 引用（非常非常重要）
当你创建了一个对象并将其分配给某个变量时，变量只会 **查阅（Refer）** 某个对象，并且它也不会代表对象本身。也就是说，变量名只是指向你计算机内存中存储了相应对象的那一部分。这叫作将名称 **绑定（Binding）** 给那一个对象。

一般来说，你不需要去关心这个，不过由于这一引用操作困难会产生某些微妙的效果，这是需要你注意的：
案例（保存为 [ds_reference.py](../Code/08/ds_reference.py)）：
```python
print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
# mylist 只是指向同一对象的另一种名称
mylist = shoplist

# 我购买了第一项项目，所以我将其从列表中删除
del shoplist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
# 注意到 shoplist 和 mylist 二者都
# 打印出了其中都没有 apple 的同样的列表，以此我们确认
# 它们指向的是同一个对象

print('Copy by making a full slice')
# 通过生成一份完整的切片制作一份列表的副本
mylist = shoplist[:]
# 删除第一个项目
del mylist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
# 注意到现在两份列表已出现不同
```
输出：
```
Simple Assignment
shoplist is ['mango', 'carrot', 'banana']
mylist is ['mango', 'carrot', 'banana']
Copy by making a full slice
shoplist is ['mango', 'carrot', 'banana']
mylist is ['carrot', 'banana']
```

直接将两个引用对象的变量进行相互赋值，实际上只是进行了引用的传递。而不是创建了新的内容。所以在上面的时候删了mylist的值，shoplist也变化了。而通过切片方法则是返回了一个新的对象内容，所以从切片中生成的新的mylist就不再影响原来的对象了。


<p align="center">
  <a href="Guide07.md">上一篇教程</a>  --------------------------------------  <a href="Guide09.md">下一篇教程
</p>