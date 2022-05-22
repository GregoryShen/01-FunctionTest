# [Python + Selenium Web自动化 全套教程](https://www.bilibili.com/video/av64421994)

### Css 选择器-上篇

如果元素

根据id是根据,都是

https://www.imooc.com/video/13963

https://www.bilibili.com/video/av64421994?p=13

https://www.bilibili.com/video/av35122164?p=9

https://www.bilibili.com/video/av54112959?p=22

https://www.bilibili.com/video/av30566232?p=162

http://www.selenium.org.cn/category/use

根据它的属性值, 

```python
elements = wd.find_elements_by_css_selector()
```

验证

次序通过冒号来确定.

`span:nth-child(2)`

父元素

`nth-last-child(2)`

`span:nth-fo-type(1)`

有正数也有倒数,`span:nth-last-of-type(1)`

奇数节点和偶数节点:

`#t1:nth-child(odd)`

### radio选择框

 ### checkbox选择框

### select框

redio框及checkbox框都是input元素,只是里面的type不同而已.

select框则是一个新的select标签,大家可以对照浏览器网页内容查看一下.

对于select选择框,selenium专门提供了一个Select类进行操作.

select类提供了如下的方法:

`select_by_value`

根据选项的value属性值,选择元素.

```python
# 导入select类
from selenium.webdriver.support.ui import Select

# 创建Select对象

```

#### select多选框

对于select多选框,要选中某几个选项,要注意去掉原来已经选中的选项

例如,我们选择示例多选框中的 小雷老师 和 小凯老师

可以用select类的deselect_all方法,清除所有已经选中的选项

然后再通过select_by_visible_text方法选择 小雷老师 和 小凯老师

### 浏览器窗口切换

```python
for handle in wd.window_handles:
    wd.switch_to_window(handle)
    if 'Bing' in wd.title:
      	break
```

切换回之前的窗口,没有switch_to_default_window这种方法,

### 实战技巧

选择元素/点击元素/输入字符串



[元素定位有八法，web功能自动化元素定位之xpath](https://www.bilibili.com/video/BV1vE41167P8)

1. xpath使用绝对位置定位
2. xpath使用相对位置定位
3. xpath使用索引定位
4. xpath使用属性值定位
5. xpath使用部分属性值定位
6. xpath使用文本定位

# [Selenium中三大等待的用法](https://www.bilibili.com/video/BV1bE411v7Gy)

等待的作用

​	在系统的功能运行过程中,所有的内容是需要一定时间来实现展示的.而时间耗费的长短,与网络速度,与系统的框架设定,与接口的执行复杂程度

​	在自动化中,

三类等待方式

自动化该注意避免的坑有哪些

显式等待(从40分钟开始):

​	  专门用于对指定的条件进行等待.在设置的最大时常中,依照查找的时间频率来进行搜索,查找指定的对象,until表示如果找到,则继续下一步,否则,爆出异常NoSuchElementException/TimeOut异常; 

until not与until相反,

优点:精确对某个特定条件进行等待,不会浪费多余的任何时间在等待上.如果条件成立,立即进入下一步.如果不成立则抛出异常.

缺点:应用上而言,相较于其他两种等待更为复杂

跟断言比较像所以,通过显式等待还可以设置有自动化测试的断言内容

### 自动化应该避免的坑有哪些?

1. 页面元素定位不到,基本都是因为没有添加等待时间或者元素定位的方式有误造成的
		 id/name/class/xpath/cssselector 单纯的copy很可能会出错,需要通过手写xpath来定位,再经过验证,确认元素定位的准确性
2. 		iframe和handles的操作:切换iframe用以操作iframe中的元素

   

























