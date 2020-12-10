# [自动化测试-selenium（python版)](https://www.bilibili.com/video/av54112959?p=11)



## 10 如何控制多个窗口

`d.window_handles`是所有窗口的句柄

`d.current_window_handle`是当前窗口的句柄

在不同窗口间切换的方法:

`d.switch_to_window(d.window_handles[1])`

`switch_to_window`方法中要传入想要切换到的句柄, `window_handles`返回的是所有句柄的一个列表,所以可以用索引的方式来指定想要访问的句柄

`d.current_url`来查看当前的url

`d.title`当前窗口的标题栏文本





## 11 测试脚本中的等待方法

1. 等待是为了使脚本执行更加稳定
2. 常用的休眠方式:time模块的sleep方法

除了time模块中的sleep方法外,selenium中等待方法:

|      方法名       |                             含义                             |
| :---------------: | :----------------------------------------------------------: |
| Implicitly_wait() |                    设置webdriver等待时间                     |
|   WebDriverWait   | 等待条件满足或者超时后退出(from selenium.webdriver.support.ui import WebDriverWait) |

```python
def get_ele_times(driver, times, func):
    return WebDriverWait(drive, times).until(func)
```

## 12 处理alert对象

|   方法或属性名    |            含义             |
| :---------------: | :-------------------------: |
| switch_to_alert() | 切到alert,返回一个alert对象 |
|      accept       |            确认             |
|      dismiss      |            取消             |
|    send_keys()    |  有输入框才能使用,否则报错  |
|       text        |   弹出框中显示的文字信息    |

## 13 测试用例设计

优点:独立,可单独执行

不足: 灵活性差,不具备大规模测试条件,维护成本大

脚本功能分析与模块化:

```flow
st=>start: OpenBrowser
op1=>operation: OpenUrl
op2=>operation: FindElement
op3=>operation: SendKeys
op4=>end: CheckResult

st->op1->op2->op3->op4
```

测试脚本模块化和数据隔离



## 14



## 15 数据和代码分离

代码和用户数据分离:

1. 将代码中的数据剥离,设计合理的数据结构
2. 设计数据读取模块,从文件中读取测试数据

数据设计:

字典形式:

|         key          |     val      |
| :------------------: | :----------: |
|         url          |   打开地址   |
|       Text_id        |   登录元素   |
| Userid/pwdid/loginin | 输入账号元素 |
|      uname/pwd       | 输入账号信息 |
|       Errorid        | 检查错误条件 |

## 16 设计数据读取模块

## 17 测试用例优化--错误处理

错误类型:

1. 账号不能为空
2. 密码不能为空
3. 该账号格式不正确
4. 账号或者密码错误,请重新输入



















