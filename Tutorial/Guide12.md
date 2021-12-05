# 学习Python的第十二天

任务:
- 学会终端输入输出的`input()`和`print()`
- 学会进行文件的输入和输出
    - 即，学会文件的读取和写入
- 重要: 在老秦的帮助下，完成这次作业

## 输入与输出
我们可以这么简单来理解程序的交互。我们日常使用的App，每一个操作都是向手机输入了一个操作指令，程序App则根据用户的操作指令进行一系列的功能，最后返回（展示）给我们操作的结果。比如触动屏幕，打开App的过程。

如果理解了上面的栗子，我们回到最原始的程序交互，在终端命令行中的程序输入和输出。

举个例子，我希望获取用户的输入内容，并向用户打印出一些返回的结果。那么，我们可以分别通过 `input()` 函数与 `print()` 函数来实现这一需求。

另一个常见的输入输出类型是处理文件。创建、读取与写入文件对于很多程序来说是必不可少的功能。

## 终端中的输入和输出

保存以下代码为文件[io_input.py](../Code/12/io_input.py)
```python
def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


something = input("Enter text: ")
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")
```
多次运行的结果：
```
$ python3 io_input.py
Enter text: sir
No, it is not a palindrome

$ python3 io_input.py
Enter text: madam
Yes, it is a palindrome

$ python3 io_input.py
Enter text: racecar
Yes, it is a palindrome
```
### 代码逻辑
我们使用切片功能翻转文本。我们已经了解了我们可以通过使用 `seq[a:b]` 来从位置 `a` 开始到位置 `b` 结束来对序列进行切片 。我们同样可以提供第三个参数来确定切片的步长（Step）。默认的步长为 `1`，它会返回一份连续的文本。如果给定一个负数步长，如 `-1`，将返回翻转过的文本。

`input()` 函数可以接受一个字符串作为参数，并将其展示给用户。尔后它将等待用户输入内容或敲击返回键。一旦用户输入了某些内容并敲下返回键，`input()` 函数将返回用户输入的文本。

我们获得文本并将其进行翻转。如果原文本与翻转后的文本相同，则判断这一文本是回文。

### **作业练习**

要想检查文本是否属于回文需要忽略其中的标点、空格与大小写。例如，“Rise to vote, sir.”是一段回文文本，但是我们现有的程序不会这么认为。请和老秦一起完成这个作业。


## 文件
你可以通过创建一个属于 `file` 类的对象并适当使用它的 `read`、`readline`、`write` 方法来打开或使用文件，并对它们进行读取或写入。读取或写入文件的能力取决于你指定以何种方式打开文件。最后，当你完成了文件，你可以调用 `close` 方法来告诉 Python 我们已经完成了对该文件的使用。
案例（保存为[io_using_file.py](../Code/12/io_using_file.py)）：
```python
poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''

# 打开文件以编辑（'w'riting）
f = open('poem.txt', 'w')
# 向文件中编写文本
f.write(poem)
# 关闭文件
f.close()

# 如果没有特别指定，
# 将假定启用默认的阅读（'r'ead）模式
f = open('poem.txt')
while True:
    line = f.readline()
    # 零长度指示 EOF
    if len(line) == 0:
        break
    # 每行（`line`）的末尾
    # 都已经有了换行符
    #因为它是从一个文件中进行读取的
    print(line, end='')
# 关闭文件
f.close()
```
输出：
```
$ python3 io_using_file.py
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
```
### 代码逻辑
首先，我们使用内置的 `open` 函数并指定文件名以及我们所希望使用的打开模式来打开一个文件。打开模式可以是阅读模式（`'r'`），写入模式（`'w'`）和追加模式（`'a'`）。我们还可以选择是通过文本模式（`'t'`）还是二进制模式（`'b'`）来读取、写入或追加文本。在默认情况下，`open()` 会将文件视作文本（text）文件，并以阅读（read）模式打开它。
在我们的案例中，我们首先采用写入模式打开文件并使用文件对象的 write 方法来写入文件，并在最后通过 `close` 关闭文件。
接下来，我们重新在阅读模式下打开同一个文件。我们不需要特别指定某种模式，因为“阅读文本文件”是默认的。我们在循环中使用 `readline` 方法来读取文件的每一行。这一方法将会一串完整的行，其中在行末尾还包含了换行符。当一个空字符串返回时，它表示我们已经到达了文件末尾，并且通过 `break` 退出循环。
最后，我们通过 `close` 关闭了文件。
现在，你可以检查 `poem.txt` 文件的内容来确认程序确实对该文件进行了写入与读取操作。

# 作业
参见**作业练习**

<p align="center">
  <a href="Guide11.md">上一篇教程</a>  --------------------------------------  <a href="Guide13.md">下一篇教程
</p>