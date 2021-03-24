# UI自动化测试经典项目实战 强化编程能力

## 第1章 Selenium 补充

参考资料：

[白月黑羽](http://www.python3.vip/tut/auto/selenium/01/)

[Selenium WebDriver 架构](http://aosabook.org/en/selenium.html)

[Selenium 官方文档](https://www.selenium.dev/documentation/en/) ([什么是UmbrellaProjects](https://projects.coin-or.org/CoinTLC/wiki/UmbrellaProjects))

[基于 Docker 构建 Selenium Grid 分布式测试环境](https://developer.ibm.com/zh/articles/os-cn-docker-selenium-grid-test/#)

[张挺公众号： Selenium的学习](https://mp.weixin.qq.com/s/XuxGL9ZgTJanFPco-eLP_g)

[张挺公众号：GUI自动化测试进阶：页面对象模式](https://mp.weixin.qq.com/s/BtG-JAcGPeuK5I1WaHkpWg)

[张挺公众号：读者问题：selenium里的等待](https://mp.weixin.qq.com/s/y1IOJxe79O_ZjVI5RbY5GQ)

[Martin Fowler: pageObject](https://martinfowler.com/bliki/PageObject.html)

[Martin Fowler: FluentInterface](https://www.martinfowler.com/bliki/FluentInterface.html)

[Page Object Model (POM) & Page Factory in Selenium Tutorial](https://www.guru99.com/page-object-model-pom-page-factory-in-selenium-ultimate-guide.html)

EventFiringWebDriver

[github上的例子: screenshot-listener.py](https://gist.github.com/billagee/080e21842bafb8b22586)

[selenium文档:Event Firing WebDriver Support](https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.event_firing_webdriver)

[selenium官网:evnet_firing_webdriver API](https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.event_firing_webdriver.html)

[Selenium WebDriver Event Listener(JAVA版)](https://www.toolsqa.com/selenium-webdriver/event-listener/)

[Java的selenium:Class EventFiringWebDriver](https://www.selenium.dev/selenium/docs/api/java/org/openqa/selenium/support/events/EventFiringWebDriver.html)

[Java的selenium事件支持](https://www.selenium.dev/selenium/docs/api/java/org/openqa/selenium/support/events/package-summary.html)

[张挺的小例子:simpleWebtest](https://github.com/zhangting85/simpleWebtest)





## 第2章 全面元素定位

### 2-1 课前准备说明

* 安装Python 3.6
  * 目前Python的版本3.6比较稳定
* 安装selenium命令: `pip install selenium`
* 下载Chrome driver
  * 地址1:https://sites.google.com/a/chromium.org/chromedriver/downloads
  * 地址2: http://npm.taobao.org/mirrors/chromedriver

### 2-2 基本元素定位方法id(回顾基础定位方法)

新建python包`part_one`, 新建python文件`basic_location.py`

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# chromedriver的存储路径
path = "/Users/zjy/Documents/imooc/code/python_ui/chromedriver"
driver = webdriver.Chrome(path)

# 将浏览器最大化
driver.maximize_window()
# 打开京东首页
driver.get("https://www.jd.com")
# id定位: 定位搜索框, 输入内容后回车,进行搜索
search_element = driver.find_element_by_id("key")
search_element.send_keys("电脑")
# 点击回车进行搜索
search_element.send_keys(Keys.RETURN)
```

每次启动时都会启动一个浏览器, 手动关闭非常麻烦, 可以使用`try…finally`的方式, 这样即使发生异常也能正常关闭

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

try:
    # chromedriver的存储路径
    path = "/Users/zjy/Documents/imooc/code/python_ui/chromedriver"
    driver = webdriver.Chrome(path)

    # 将浏览器最大化
    driver.maximize_window()
    # 打开京东首页
    driver.get("https://www.jd.com")
    # id定位: 定位搜索框, 输入内容后回车,进行搜索
    search_element = driver.find_element_by_id("key")
    search_element.send_keys("电脑")
    # 点击回车进行搜索
    search_element.send_keys(Keys.RETURN)
finally:
  	time.sleep(3)
    driver.quit()
```

#### 1022自测结果

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.jd.com")

# 2-2 使用id定位方式定位京东首页输入框并输入电脑进行搜索
time.sleep(3)
input_element = driver.find_element_by_id("key")
input_element.click()
input_element.send_keys("电脑")
input_element.send_keys(Keys.RETURN)
```

存在问题:

1. 一开始找搜索框的`id`找的不对,导致定位错误.
2. 找到输入框以后可以直接`send_keys`, 不需要先`click`
3. 没有使用`try…finally`结构

### 2-3 类名、文字链接与局部文字链接定位的方法

#### 类名

例子: 使用 京东首页左侧“家用电器”举例

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

try:
    # chromedriver的存储路径
    path = "/Users/zjy/Documents/imooc/code/python_ui/chromedriver"
    driver = webdriver.Chrome(path)

    # 将浏览器最大化
    driver.maximize_window()
    # 打开京东首页
    driver.get("https://www.jd.com")
    # class_name 定位, 点击左侧菜单栏中的家用电器
    menu_item = driver.find_element_by_class_name("cate_menu_lk")
    menu_item.click()
finally:
  	time.sleep(3)
    driver.quit()
```

##### 1019自测结果

```python
# 使用类名定位的方式定位京东首页左侧"家用电器"
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.jd.com")

element = driver.find_element_by_class_name("cate_menu_lk")
ActionChains(driver).move_to_element(element).perform()
```

点评：

基本上没什么大问题，原作里用的是`try…finally`结构，我没用，而且是直接定位到家用电器并且点击，我是使用悬浮，不过也不影响什么。

关于使用`class_name`的几个小疑问也解决了：

* 使用`class_name`定位元素，`class_name`一般要求唯一，但是课件里`class=“cate_menu_lk”`这个并不唯一，可他还是定位到了，是因为他是第一个元素。

* 如果在多元素的情况下，可以使用下标的方式来进行筛选。

* `find_element_by_class_name()`中只能填入一个class名称，如果填入多个就会报错。所以当元素有多个class name时，用css或xpath定位的方式更合适，`class_name`的方式只适合`class`只有一个名字且唯一的情况，而这种情况在实际使用中并不多见。

* 参考资料：[根据 class属性 选择元素](http://www.python3.vip/tut/auto/selenium/02/)     [Selenium在定位的class含有空格的复合类的解决办法](https://blog.csdn.net/cyjs1988/article/details/75006167)

* 补充：`find_element_by_tag_name`因为tag在HTML中更不可能唯一，所以这种方法用的更少 

	[八种定位方法](https://blog.csdn.net/CloserSide/article/details/109078300)

* 补充：`find_element_by_name`：通过name属性来查找元素，一般和id方法比对，id整个页面唯一，而name可不唯一，所以这种方法用的也少。


#### 文字链接

例子: 定位京东首页左侧菜单栏中的“手机”

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

try:
    # chromedriver的存储路径
    path = "/Users/zjy/Documents/imooc/code/python_ui/chromedriver"
    driver = webdriver.Chrome(path)

    # 将浏览器最大化
    driver.maximize_window()
    # 打开京东首页
    driver.get("https://www.jd.com")
    # link_tesxt进行左侧菜单栏中的手机链接进行定位
    link_text = driver.find_element_by_link_text("手机")
    link_text.click()
finally:
  	time.sleep(3)
    driver.quit()
```

#### 局部文字链接

例子: 定位京东首页左侧菜单栏中的“汽车用品”中的“汽车用”三个字

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

try:
    # chromedriver的存储路径
    path = "/Users/zjy/Documents/imooc/code/python_ui/chromedriver"
    driver = webdriver.Chrome(path)

    # 将浏览器最大化
    driver.maximize_window()
    # 打开京东首页
    driver.get("https://www.jd.com")
    # 使用partial_link_text方法定位, 定位汽车用品
    link_text = driver.find_element_by_partial_link_text("汽车用")
    link_text.click()
finally:
  	time.sleep(3)
    driver.quit()
```

### 2-4 xpath与css选择器定位

xpath定位:

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

try:
    # chromedriver的存储路径
    path = "/Users/zjy/Documents/imooc/code/python_ui/chromedriver"
    driver = webdriver.Chrome(path)

    # 将浏览器最大化
    driver.maximize_window()
    # 打开京东首页
    driver.get("https://www.jd.com")
    # 点击运营商
    x_path = driver.find_element_by_xpath("//*[@id=\"J_cate\"]/ul/li[2]/a[2]")
    x_path.click()
finally:
  	time.sleep(3)
    driver.quit()
```

css选择器定位

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

try:
    # chromedriver的存储路径
    path = "/Users/zjy/Documents/imooc/code/python_ui/chromedriver"
    driver = webdriver.Chrome(path)

    # 将浏览器最大化
    driver.maximize_window()
    # 打开京东首页
    driver.get("https://www.jd.com")
    # 点击厨具
    css = driver.find_element_by_css_selector("#J_cate > ul > li:nth-child(4) > a:nth-child(7)")
    css.click()
finally:
  	time.sleep(3)
    driver.quit()
```

除了单个元素定位外, 还有多个元素定位(`find_elements_by_xxx`), 返回的是list of WebElement

#### 1025自测结果

```python
from selenium import webdriver
import time

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.jd.com")
    # 2-3 1. 使用类名定位方式定位京东首页左侧"家用电器"
    # driver.find_element_by_class_name("cate_menu_lk").click()
    # 2-3 2. 使用文字链接的方式定位首页"手机"
    # driver.find_element_by_link_text("手机").click()
    # 2-3 3. 使用局部文字链接定位汽车用品的"汽车用"三个字
    # driver.find_element_by_partial_link_text("汽车用").click()
    # 2-4 1. 使用xpath方式定位京东首页"运营商"
    # driver.find_element_by_xpath('//*[@id="J_cate"]/ul/li[2]/a[2]').click()
    # 2-4 2. 使用css选择器方式定位"厨具"
    driver.find_element_by_css_selector('#J_cate > ul > li:nth-child(4) > a:nth-child(7)').click()
finally:
    time.sleep(3)
    driver.quit()

# 2-0 1. 一共有几种定位方法
# id, name, class_name, tag_name, link_text, partial_link_text, css_selector,
# xpath
# 2. id和name和class_name和tag_name有什么特点？
# id若存在则整个页面唯一，name是一个属性，不一定存在， class_name和tag_name可能有多个，但调用
# 的时候只能写一个，所以重复的元素比较多，需要使用下标的方式来选择。
```

总体上这几种定位方式的使用没有太大问题, 还剩一些细化的细节, 比如在定位到元素之后的一些操作, 获取元素HTML, 冻结窗口之类, 还有一些没讲到的, 选择框, 这些都需要参考白月黑羽的教程, 至于CSS和XPATH的细节操作在第四章展开.

### 2-5 鼠标和键盘事件演示及源代码阅读

新建一个`mouse_and_keyboard.py`

#### 鼠标事件

悬停: 打开京东首页, 悬停到手机上,打开二级菜单后点击老人机

除了悬停还有右击事件,双击事件(用到的不多),左击事件, 其他的方法可以到`action_chains.py`中查看.

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

try: 
  	path = "/Users/zjy/Documents/imooc/code/python_ui/chromedriver"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.jd.com")
    elem = driver.find_element_by_link_text("手机")
    # 鼠标悬停
    ActionChains(driver).move_to_element(elem).perform()
    time.sleep(3)
    old_phone = dirver.find_element_by_link_text("老人机")
    old_phone.click()
    
    # 键盘事件
    search_element = driver.find_element_by_id("key")   # 这个就是那个搜索框
    search_element.send_keys("电脑")
    search_element.send_keys(Keys.RETURN)
finally:
    time.sleep(3)
    driver.quit()
```

在第13行, 进入到`move_to_element`查看源代码, 查看传入的参数以及注释.

#### 键盘事件

从搜索框输入“电脑”并点击回车进行搜索

查看源代码: 查看`keys.py`中的具体内容

#### 1023自测结果

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
try:
    driver.get("https://www.jd.com")
    phone = driver.find_element_by_link_text("手机")
    ActionChains(driver).move_to_element(phone).perform()
    time.sleep(1)
    driver.find_element_by_link_text("老人机").click()
finally:
    time.sleep(3)
    driver.quit()
```

也没有什么问题, 讲了鼠标悬停之后, 对于京东首页来说, 才是正常的操作, 之前2-2 ~ 2-4 介绍的几种定位方式都是直接点击, 没有悬停.

### 2-6 截图方法的应用及简单方法封装

主要实现的动作: 打开京东首页左侧菜单的“手机”类目下的“老人机”页面, 然后保存老人机页面到项目下 images 目录中.

创建`my_screenshot.py`

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

# 接受两个参数, 这个要注意
def screenshot(driver, file_path=None):
    # 用户并没有传filepath参数
    if file_path is None:
      	project_path = os.path.dirname(os.getcwd())
        print(project_path)
        file_path = project_path + '/images/'   # 用images目录存取所有的图片
        # 如果images路径不存在则创建
        if not os.path.exists(file_path):
          	os.mkdir(file_path)
        image_name = time.strftime("%Y%m%d-%H%M%S", time.localtime()) # 这里不能用/分隔,因为和路径冲突
        file_path = file_path + image_name + ".png"
        print(file_path)
    driver.save_screenshot(file_path)

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.jd.com/")
    elem = driver.find_element_by_link_text("手机")
    # 先用鼠标悬停
    ActionChains(driver).move_to_element(elem).perform()
    time.sleep(3)
    old_phone = driver.find_element_by_link_text("老人机")
    old_phone.click()
    # driver.save_screenshot("laorenji.png") # 这是错误的方法, 因为driver的句柄没切换
    
    # 浏览器句柄切换
    handles = driver.window_handles  # 获取浏览器所有当前句柄
    current_handle = driver.current_window_handle
    for handle in handles:
        if handle != current_handle:
            driver.switch_to.window(handle)
            screenshot(driver)
finally:
    time.sleep(2)
    driver.quit()
```

#### 20200815自测结果

1. 导包:

`ActionChains`包有点迷茫, 不太记得在哪个下面了, 经过试错吧, 找出来了

```python
from selenium.webdriver.common.action_chains import ActionChains
```

2. 整体大框架的搭建:

```python
driver = webdriver.Chrome()
driver.maximize_window()
```

这两句应该放在`try`下面, 但是也差别不大吧.

3. 这一小节涉及到的知识点:

   1. 悬浮

   2. 句柄切换

   3. 截图方法的使用(就是直接使用`driver.save_screenshot()`)

   4. 截图方法的封装

      1. 自定义方法的命名(`selenium`已经有方法叫`save_screenshot`了, 就不要再叫这个名字了)

      2. 函数参数的传递, 以及整个函数的设计(要可以接受一个`file_path`, 当调用者没传的时候,给个默认值`None`, 然后按默认值的方式进行处理)

      3. 获取项目的路径

      4. 新建一个文件夹

      5. ==获取当前时间并转换成字符串格式==

         ```python
         time.strftime("%Y%m%d-%H%M%S", time.localtime())
         ```

      6. 直接调用driver的`save_screenshot`方法, 并传递更新过的`file_path`, 就不要自己造轮子去`with open了`

#### 20201025自测结果

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.jd.com")


def screenshot(driver, filename=None):
    if filename is None:
        filepath = os.path.join(os.path.dirname(os.getcwd()), "screenshot")
        if not os.path.exists(filepath):
            os.mkdir(filepath)
        filename = time.strftime("%Y%m%d-%H%M%S", time.time())
        filepath = filepath + filename
    driver.save_screenshot(filepath)


try:
    elem = driver.find_element_by_link_text("手机")
    ActionChains(driver).move_to_element(elem).perform()
    time.sleep(2)
    old_phone = driver.find_element_by_link_text("老人机")
    old_phone.click()
    cur_handler = driver.current_window_handle
    handlers = driver.window_handles
    for handler in handlers:
        if handler != cur_handler:
            driver.switch_to.window(handler)
    driver.save_screenshot("laorenji_1025.png")
finally:
    time.sleep(2)
    driver.quit()
```

##### 存在的问题

1. `time.time()`获取当前时间用的不对，`time.time()`返回的是一个浮点数，而`time.strftime()`需要的是一个`time.struct_time`， 所以需要调用`time.localtime()`来获取合适的当前时间
2. 在传递 filepath 的时候没有加文件名后缀 `".png"`
3. 没有在整个程序中应用`screenshot`方法
4. 还有一个拼写需要注意的是：句柄是 handle，不是handler

写的比原作好的地方：

1. 原作中在获取存储截图的目录时候用的是字符串拼接的方法，而更合适的方式是`os.path.join()`
2. `save_screenshot`方法用的参数名字是`filename`，所以我觉得用filename更合适

#### 20210213自测结果

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import os


def screenshot(_driver):
    project_path = os.path.dirname(os.getcwd())
    images_path = os.path.join(project_path, 'images_0214')
    if not os.path.exists(images_path):
        os.mkdir(images_path)
    images_name = os.path.join(images_path, 'laorenji_0214.png')
    _driver.save_screenshot(images_name)


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://jd.com")
sleep(3)  # 为了等待大banner自动缩小
ele = driver.find_element_by_link_text("手机")
ActionChains(driver).move_to_element(ele).perform()
sleep(1)
laorenji = driver.find_element_by_link_text("老人机")
laorenji.click()
for handler in driver.window_handles:
    if handler != driver.current_window_handle:
        # driver.switch_to.frame(handler)
        driver.switch_to.window(handler)
# driver.save_screenshot("laorenji_0214.png")
        screenshot(driver)
```

##### 存在的问题

1. 没有使用 `try…finally` 结构
2. 切换句柄的方法是 `driver.switch_to.window(handle)`
3. 没有调用封装的截图方法
4. 截图方法的设计上,需要传递两个参数, 以 `file_path` 是否传递分类讨论
5. 在给截图起名上, 直接用路径+自定义的名字, 可以使用当前时间来作为名字这样可以反复调用查看结果

#### 20210323自测结果

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os
import time

path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.maximize_window()


def screenshot(file_name=None):
    if file_name is None:
        project_path = os.path.dirname(os.path.dirname(os.getcwd()))
        images_path = os.path.join(project_path, "images")
        if not os.path.exists(images_path):
            os.mkdir(images_path)
        image_name = time.strftime("%Y%m%d-%H%M%S", time.localtime())
        file_name = os.path.join(images_path, image_name, ".png")
    driver.save_screenshot(file_name)


try:
    driver.get("https://www.jd.com")
    phone = driver.find_element_by_link_text("手机")
    ActionChains(driver).move_to_element(phone).perform()
    time.sleep(1)
    old_phone = driver.find_element_by_link_text("老人机")
    old_phone.click()
    handlers = driver.window_handles
    index_handler = driver.current_window_handle
    for handler in handlers:
        if handler != index_handler:
            driver.switch_to.window(handler)
    screenshot()
finally:
    time.sleep(3)
    driver.quit()
```

##### 存在的问题

1. 在拼接最后的文件名时, 不应该使用 `os.path.join(images_path, image_name, ".png”)`, 因为这样会使得路径变为: `xxx/xxx/images/时间/.png`, 所以要先把 `.png` 用字符串合并的方式加到文件名上

### 2-7 获取登录后的cookies

整个的思路:首先获取到 cookies , 把 cookie 存储到一个文件里, 再从文件里读出来, 以后的访问都带着这个 cookie 去看看能不能把登录绕过去.

创建`my_cookies.py`

```python
from selenium import webdriver
import time
import os
import json

driver = webdriver.Chrome()
driver.maximize_window()


# 保存cookies到文件中
def save_cookies(driver):
  	project_path = os.path.dirname(os.getcwd())
    file_path = project_path + "/cookies/"
    if not os.path.exists(file_path):
    	  os.mkdir(file_path)
    # 从driver中获取到cookies
    cookies = driver.get_cookeis()
    with open(file_path + "jd.cookeis", "w") as c:
      	# 这里必须用json.dump方法写入文件
        # 将来我们在取cookies时候会使用json.loads方法,这里的格式就不匹配了
        json.dump(cookies, c)
    print(cookies)
 
def login():
  	try:
      	driver.get("https://www.jd.com")
        driver.find_element_by_class_name("link-login").click()
        driver.find_element_by_link_text("账户登录").click()
        driver.find_element_by_id("loginname").send_keys("")
        driver.find_element_by_id("nloginpwd").send_keys("")
        driver.find_element_by_id("loginsubmit").click()
        # 保存cookies信息到文件中
        save_cookies(driver)
    finally:
      	time.sleep(3)


if __name__ == '__main__':
  	login()
```

然后把断点打在`login`函数的`save_cookies`哪一行, 以 debug 的方式运行, 因为中间需要手动拖动验证码

#### 1030自测结果

```python
from selenium import webdriver
import os
import time

driver = webdriver.Chrome()
driver.maximize_window()


def save_cookies():
    file_path = get_cookies_dir()
    filename = os.path.join(file_path, "jd.cookies")
    with open(filename, "w") as f:
        cookies = str(driver.get_cookies())
        f.write(cookies)


# def get_cookies_dict(cookies):
#     cookies_dict = json.loads(cookies)
#     return cookies_dict


def get_cookies_dir():
    project_path = os.path.dirname(os.getcwd())
    file_path = os.path.join(project_path, "cookies_1030")
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    return file_path


try:
    driver.get("https://www.jd.com")
    driver.find_element_by_xpath('//*[@id="ttbar-login"]/a[1]').click()
    time.sleep(3)
    driver.find_element_by_link_text("账户登录").click()
    driver.find_element_by_id("loginname").send_keys("13120597275")
    driver.find_element_by_id("nloginpwd").send_keys("shenxin22019891")
    driver.find_element_by_id("loginsubmit").click()
    time.sleep(3)
    save_cookies()
finally:
    time.sleep(3)
    driver.quit()
```

存在问题：

1. 在获取cookies的时候，应该先获取，然后打开文件，也就是`cookies = driver.get_cookies()`应该放在with的外面
2. ==在写入文件的时候应该用`json.dump(cookies, f)`存成json的格式==
3. 没有把登录写成一个函数，写成函数的话，可以通过 `if __name__ == __main__`来调用

#### 0219自测结果

```python
from selenium import webdriver
from time import sleep
import os

path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.maximize_window()



def login():
    driver.get("https://jd.com")
    driver.find_element_by_class_name("link-login").click()
    driver.find_element_by_link_text("账户登录").click()
    driver.find_element_by_id("loginname").send_keys("GregoryShen")
    driver.find_element_by_id("nloginpwd").send_keys("shenxin22019891")
    driver.find_element_by_id("loginsubmit").click()


def save_cookies_to_file(driver):
    cookies_path = get_cookies_path()
    cookies_name = os.path.join(cookies_path, "jd.cookies")
    with open(cookies_name, "w", encoding="utf-8") as f:
        f.write(driver.get_cookies())


def get_cookies_path():
    project_path = os.path.dirname(os.getcwd())
    cookies_path = os.path.join(project_path, "cookies")
    if not os.path.exists(cookies_path):
        os.mkdir(cookies_path)
    return cookies_path

```

##### 存在的问题

1. 使用 cookies 绕过登录的思路不清晰：在登录完成后, 就应该把 cookie 保存下来了, 可是并没有调用 `save_cookies_to_file` 函数
2. 在往文件中写入 cookies 时, 不是调用 `f.write`, 而是调用 `json.dump(cookies, f)`

### 2-8 使用cookies绕过登录

上一小节中拿到了登录后的cookies, 本小节的重点是用cookies看看是否能够绕过登录

```python
def get_url_with_cookies():
  	# 使用个人订单页面是否能够访问成功来验证我们的cookies是否有效
    # 1 获取cookies文件
    project_path = os.path.dirname(os.getcwd())
    file_path = project_path + "/cookies/"
    cookies_file = file_path + "jd.cookies"
    jd_cookies_file = open(cookies_file, "r")
    jd_cookies_str = jd_cookies_file.readline()
    # 加载cookies信息
    jd_cookies_dict = json.loads(jd_cookies_str)
    
    # 2 这个地方必须先访问一下网站,然后把旧的cookies删掉之后再把我们保存的cookies添加进去
    driver.get("https://www.jd.com")
    driver.delete_all_cookies()
    # 3 将cookies信息添加到driver中
    for cookie in jd_cookies_dict:
      	driver.add_cookie(cookie)
    
    # 4 检查登录是否成功
    driver.get("https://order.jd.com/center/list.action")
    
    
if __name__ == '__main__':
  	get_url_with_cookies()
```

#### 1030自测结果

```python
def get_driver_with_cookies():
    cookie_path = get_cookies_dir()
    cookie_file = os.path.join(cookie_path, "jd.cookies")
    with open(cookie_file) as f:
        cookies_list = json.load(f)
    driver.get("https://www.jd.com")
    driver.delete_all_cookies()
    for cookie in cookies_list:
        driver.add_cookie(cookie)
    driver.get("https://order.jd.com/center/list.action")
    if driver.current_url == "https://order.jd.com/center/list.action":
        print("success")
        return driver
```

存在问题：

1. 在读取cookies的时候，应该先调用`readline()`方法读取到一个字符串，然后再loads进来。（但我直接调用好像也没啥问题）

### 2-9 js操作定位页面上的元素

通过js来操作界面上的元素, 因为有些元素的定位,定位不到.

新创建一个`js_location.py`

我们用`12306.cn`来演示: 就是输入出发地, 到达地, 出发日期, 其中主要是出发日期是时间控件需要使用js

```python
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.12306.cn/index/")
from_element = driver.find_element_by_id("fromStationText")
from_element.click()
time.sleep(2)
from_element.send_keys("北京")
driver.find_element_by_xpath("//*[text()='北京北']").click()

to_element = driver.find_element_by_id("toStationText")
to_element.click()
time.sleep(2)
to_element.send_keys("长春")
driver.find_element_by_xpath("//*[text()='长春南']").click()


```

### 2-10 js定位操作

js定位第一步要去掉`readonly`属性

```python
js = "$('input[id= train_date]').removeAttr('readonly')"
driver.execute_script(js)
date_element = driver.find_element_by_id("train_date")
date_element.click()
# 先去掉原有的东西
date_element.clear()
date_element.send_keys("2019-03-10")
time.sleep(2)
# 直接点击查询按钮
driver.find_element_by_id("search_one").click()
```

元素遮挡

先在别的地方点一下

```python
driver.find_element_by_class_name("form-lable").click()
```

补充一个面试题: 在driver操作中, `quit`和close方法有什么区别

quit是退出浏览器进程,close是关闭浏览器标签(close可以在句柄切换的时候用)

#### 1102自测结果

```python
from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.12306.cn/index/")
from_station = driver.find_element_by_id("fromStationText")
from_station.click()
from_station.send_keys("上海")
time.sleep(1)
driver.find_element_by_xpath('//*[text()="上海南"]').click()
to_station = driver.find_element_by_id("toStationText")
to_station.click()
to_station.send_keys("天津")
time.sleep(1)
driver.find_element_by_xpath('//*[text()="天津西"]').click()
train_date = driver.find_element_by_id("train_date")
js = '$(train_date).removeAttr("readonly")'
driver.execute_script(js)
train_date.clear()
train_date.send_keys("2020-11-05")
driver.find_element_by_class_name("form-label").click()
driver.find_element_by_id("search_one").click()
```

存在的问题：

1. 一开始出发站元素的id找的不对，后面经过调试才找对。

2. 操作的顺序可能有一点点问题，应该是先去掉readonly的属性，然后再定位元素（不过我写的先定位元素然后再去掉readonly属性也没什么问题）

3. js的写法：`$().removeAttr` 这个是 JQuery 的写法，根据说明\$里写的是 selector，原作里写的是用的css的方式：`$('input[id=train_date]').removeAttr('readonly')`

	我直接在\$里写的id，也可以定位到，但是不通用。

## 第3章 实战电商平台商品信息浏览流程

### 3-1 实战业务流程说明

第一个实战: 就是电商平台里商品信息查看整个流程.

本小节主要讲一下怎么来查看这个商品信息, 具体流程是什么,在用selenium操作前端页面元素的时候里面有一些坑,这些坑到底在哪, 这些在本小节讲一下.

首先打开京东首页, 比如说我们现在想要查看某种商品信息,按照什么样的流程来呢?

首先把鼠标悬停到“电脑”上,右侧会弹出一个二级菜单. (前面要应用cookies绕过登录), 然后点击“笔记本”, 这个时候会跳出一个新的页面,这是第一个即将面临到有可能的问题.这个涉及到的问题是句柄切换, 因为两个标签的时候他会有两个句柄,切换到第二个句柄需要做的事: 首先检查一共有多少个句柄, 现在一共有两个句柄, 那么要获取第一个页面的句柄, 如果判断不等于第一个页面的句柄的时候, 要切换到第二个页面上, 这个是我们面临的第一个问题.

接下来要进行商品品类以及条件的一些筛选,这里直接定位就行了.点击Thinkpad, 再点击一下7000以上,再点击一下评论数, 排名第一的就是评论数最多的商品.

点击这一款Thinkpad电脑, 又跳出了一个新的页面, 这里仍然涉及到句柄的切换. 这里面临的另外一个条件是此时拥有三个标签页面, 所以说要记住前两个,切换方法仍然是之前那种思路, 不等于前两个的时候, 把driver句柄跳转到第三个页面当中, 第三个页面中如果我想要查看这里边商品的一些信息, 比如我要查看他详细的规格与包装, 然后把这些信息拿下来,存储到文件中, 如果在真实的测试场景之下, 还需要跟一些商品信息进行核对, 断言和判断暂时就不做了. 问题是如何抓取这样的信息?

### 3-2 无经验时的代码开发思路建议和登录保存cookies流程开发

新创建包`part_two`, 创建`jingdong.py`

无经验的时候先用中文描述.

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import json

# 启动浏览器
path = "/Users/zjy/Documents/imooc/code/python_ui/chromedriver"
driver = webdriver.Chrome(path)
driver.maximize_window()

if __name__ == '__main__':
  	# 要有一个循环来控制登录状态,判断登录是否成功
    try:
      	loop_status = True
        while loop_status:
          	# 检验cookies是否生效
            login_status = check_cookies()
            if login_status:
            	loop_status = False
            else:
              	login()
        # 跳转到商品信息页面
        to_goods_page()
    finally:
      	time.sleep(3)
      	driver.quit()
```

然后开始实现具体的函数: `check_cookies`, `login`, `to_goods_page`:

```python
# 登录功能
def login():
  	driver.get("https://www.jd. com")
    driver.find_element_by_class_name("link-login").click()
    driver.find_element_by_link_text("账户登录").click()
    driver.find_element_by_id("loginname").send_keys("用户名")
    driver.find_element_by_id("nloginpwd").send_keys("密码")
    driver.find_element_by_id("loginsubmit").click()
    
    # 要保存cookies到文件中
    save_cookies_to_file(driver)
    
# 把cookies保存到文件中    
def save_cookies_to_file(driver):
  	# 获取存储cookies的文件夹
    file_path = get_cookies_dir()
    # 获取cookies
    cookies = driver.get_cookies()
    # 存储cookies到文件中
    with open(file_path + "jd.cookies", "w") as f:
      	json.dump(cookies, f)
 

def get_cookies_dir():
  	project_path = os.path.dirname(os.getcwd())
    file_path = project_path + "/cookies/"
    if not os.path.exists(file_path):
      	os.mkdir(file_path)
    return file_path
```

11/22复测的时候还发现了问题: 

当cookies失效的时候, 执行`check_cookies`函数访问`https://order.jd.com/center/list.action`的时候, ==页面会强制跳转到登录页面而不是首页==,`cookies_status`会返回`False`, 按照逻辑会跳转到`else`执行`login` 再次获取cookies, 当执行到第一个`find`语句会找不到元素, 目前的解决办法是把打开首页的语句写进`login`函数里, 这样每次都会重新打开首页.(再update: **<u>老师没写错, 获取到首页的操作就是在`login`函数里, 是我写错了</u>**)

目前想到的测试这段代码的三种方式是:

1. cookies文件存在且生效
2. cookies不存在
3. cookies文件存在但不生效

#### 0815自测结果

1. 首先, `if __name__ == ‘__main__’`下面的循环写的不对:

一开始写的是这样的:

```python
if __name__ == '__main__':
  	login_status = False
    while True:
      ....
```

也就是大概能记得要设置一个布尔变量, 然后通过循环来控制, 先去检查cookies的状态, 如果不对的话再去获取, 但是实现的时候并不完善.

首先, 设置的布尔值是来控制while循环的,并不是来显示登录的状态的, 然后,在这里要用try…finally, 但是也没有用

正确的写法是:

```python
if __name__ == '__main__':
  	try:
        # 首先设置一个变量来控制循环的进行和跳出
        loop_status = True
        while loop_status:
          	login_status = check_cookies()
            if login_status:
              	loop_status = False
            else:
              	login()
        to_goods_page()
    finally:
      	time.sleep(3)
        driver.quit()
```

也就是先把最外层最大的框架搭建好, 然后分别实现`login`, `check_cookies`, `to_goods_page`

首先来实现`login`, 那这部分的思路就很清晰了, 通过`login`来获取cookies并存储到文件中.

#### 1119自测结果

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import json
import os

driver = webdriver.Chrome()
driver.get("https://www.jd.com")


def login():
    driver.find_element_by_class_name("link-login").click()
    driver.find_element_by_link_text("账户登录")
    driver.find_element_by_id("loginname").send_keys("13120597275")
    driver.find_element_by_id("nloginpwd").send_keys("shenxin22019891")
    driver.find_element_by_id("loginsubmit").click()


def save_cookies_to_file():
    cookies_path = get_cookies_dir()
    jd_cookies = driver.get_cookies()
    with open(cookies_path + "jd_1119.cookies", "w", encoding="utf-8") as f:
        json.dump(f, jd_cookies)


def get_cookies_dir():
    project_path = os.path.dirname(os.getcwd())
    cookies_path = os.path.join(project_path, "cookies")
    return cookies_path

if __name__ == '__main__':
    loop_status = True
    try:
        while loop_status:
            cookies_status = check_cookies()
            if cookies_status:
                loop_status = False
            else:
                login()
        # to_goods_page()
    finally:
        time.sleep(3)
        driver.quit()
```

##### 存在的问题

1. 启动浏览器的部分:应该是最大化浏览器就好, 跳转到具体URL的语句应该放在`login`函数里.==这个非常重要! 不然会发生7. 的问题==
2. 在判断是否获取到cookies的部分, `loop_status`应该放在`try`里面, 不过应该区别不大. `cookies_status` 形容不太准确, 应该是`login_status`, 总的来说这块的逻辑没有什么大问题, 但是当时跑不通, 应该是内层函数出了问题.(update: 问题找到了, 是因为cookies文件一开始没有创建,所以在打开文件的时候会报错,无法继续执行, 详细解决方式可见下一节)
3. `login`函数的问题:
   1. 在定位“账户登录”的时候, 没有`click`
   2. :exclamation: 登录成功后要把cookies保存到文件中. 已经记得写保存的逻辑了,但是不记得在哪里使用了, 其实就是在这里使用, 而且保存cookies, 是要把driver传进去的, 因为要从driver中获取cookies(==这一点很重要, 忘记了这个部分说明对整个流程还是不清晰==)
4. `save_cookies_to_file`函数的问题:
   1. 需要传入driver作为参数
   2. 打开文件中不需要写`encoding`了, 因为cookies中不包含中文
   3. `json.dump()`还是写错了, 应该先写`cookies`, 然后写`f`(==这一点也很重要)==
5. `get_cookies_dir`函数中少了一个cookies文件夹是否存在的判断, 如果不存在则新建
6. 还发现一个很重要的问题是, 在获取路径的时候, `os.path.join`和字符串拼接不要混用. 比如在`get_cookies_dir`中获取cookies文件夹的方式如果写成了`os.path.join(project_path, “cookies”)`, 那么获取到的cookies文件夹就是`${project_path}/cookies`, 也就是最后是没有`/`的, 这时候再以这个路径在`save_cookies_to_file()`的`open(cookies_path + “jd_1119.cookies”, “r”)`中去拼接的话, 就拼出来:`${project_path}/cookiesjd_1119.cookies`这样的一个文件了, 路径就错的很离谱了, 所以这里也要用`os.path.join`的方式来写一下要写入的文件名字, 或者都用字符串拼接的方式也行.
7. 复测的时候还发现了问题: 当cookies失效的时候, 执行`check_cookies`函数的时候, 访问`https://order.jd.com/center/list.action`的时候, ==页面会强制跳转到登录页面而不是首页, 所以在再次获取cookies执行`login`函数的时候第一个`find`语句会找不到元素==, 目前的解决办法是把打开首页的语句写进`login`函数里, 这样每次都会重新打开首页.

### 3-3 cookies验证功能开发

```python
def check_cookies():
    # 设置一个登录状态,初始值是未登录
    login_status = False
    # 将cookies信息保存到driver中
    driver = save_cookies_to_driver()

    #进行跳转链接的检测
    driver.get("https://order.jd.com/center/list.action")
    current_url = driver.current_url
    if current_url == "https://order.jd.com/center/list.action":
        login_status = True
        return login_status
    else:
        return login_status
  
# 保存cookies信息到driver中
def save_cookies_to_driver():
    cookies_file = get_cookies_file()
    jd_cookies_file = open(cookies_file, "r")
    jd_cookies_str = jd_cookies_file.readline()
    jd_cookies_dict = json.loads(jd_cookies_str)
    # 这里必须清除掉旧的cookies
    driver.get("https://www.jd.com")
    driver.delete_all_cookies()
    for cookie in jd_cookies_dict:
      	driver.add_cookie(cookie)
    return driver
  
def get_cookies_file():
  	return get_cookies_dir() + "jd.cookies"
```

在1119自测的时候发现问题: 如果是从未获取过cookies的状态, 那么在进行cookies判断的时候,在获取cookies的时候,因为从未获取过cookies,所以cookies并未生成,所以是无法打开cooies文件的, 从而报错. imooc上已经有人提了这个问题并给了解决方法, 记录如下:

[京东是未登录状态执行时，如果jd.cookies文件不存在的话，执行是会报文件不存在的。加了判断处理，如图](https://coding.imooc.com/learn/questiondetail/199197.html)

```python
# 保存cookies信息到driver中
def save_cookies_to_file():
    cookies_file = get_cookies_file()
    if os.path.isfile(cookies_file):
        login()
    with open(cookies_file, "r") as f:
        jd_cookies = json.load(f)
    # 必须清除旧的cookies
    driver.get("https://www.jd.com")
    driver.delete_all_cookies()
    for cookie in jd_cookies:
        if "expiry" in cookie:
            del cookie["expiry"]
        driver.add_cookie(cookie)
    return driver
```

其中第4、5行是新加的, 写的还是挺简洁的.

**<u>扩展: 除了这种方法, 还有哪些方法还可以判断文件是否存在?</u>**

1. 使用os模块的os.path.exists
2. 使用try语句
3. 使用pathlib模块

详见[Python判断文件是否存在的三种方法](http://www.spiderpy.cn/blog/detail/28/)

#### 0819自测结果

在实现`check_cookies`的时候思路是对的, 不过对于函数的功能的具体分配不如原讲师处理的好, ==该函数主要应该实现的功能只是将获取到cookies的driver去访问带有限制的url, 如果可以访问,则证明cookies有效.== 其他的逻辑不应放在该函数中. 而我在实现该函数时, 仅仅是获取到了cookies, 并未将cookies加载到driver上.

```python
def check_cookies(driver):
    login_status = False
    jd_cookies_dict = get_cookies_from_file()
    driver.get("https://www.jd.com")
    driver.delete_all_cookies()
    for cookie in jd_cookies_dict:
        driver.add_cookie(cookie)
    driver.get("https://order.jd.com/center/list.action")
    if driver.current_url == "https://order.jd.com/center/list.action":
        login_status = True
    return login_status


def get_cookies_from_file():
    file_path = get_cookies_dir()
    with open(file_path + "jd.cookies") as f:
        jd_cookies_str = f.readline()
        jd_cookies_dict = json.loads(jd_cookies_str)
    return jd_cookies_dict
```

应该为:

```python
def check_cookies():
  	login_stats = False
    driver = save_cookies_to_driver()
    driver.get("https://order.jd.com/center/list.action")
    if driver.current_url = "https://order.jd.com/center/list.action":
      	login_status = True
    return login_status
  
def save_cookies_to_driver():
  	cookies_file = get_cookies_file()
    with open(cookies_file) as f:
      	jd_cookies_str = f.readline()
        jd_cookies_dict = json.loads(jd_cookies_str)
    driver.get("https://www.jd.com")
    driver.delete_all_cookies()
    for cookie in jd_cookies_dict:
      	driver.add_cookie(cookie)
    return driver
  
def get_cookies_file():
  	return get_cookies_dir() + "jd.cookies"
```

#### 1119自测结果

```python
def check_cookies():
    driver = get_driver_with_cookies()
    url = "https://order.jd.com/center/list.action"
    driver.get(url)
    if driver.current_url == url:
        return True
    else:
        return False


def get_driver_with_cookies():
    cookies_path = get_cookies_dir()
    with open(cookies_path + "jd_1119.cookies", "r", encoding="utf-8") as f:
        jd_cookies_str = f.readline()
        jd_cookies_list = json.loads(jd_cookies_str)
    driver.get("https://www.jd.com")
    driver.delete_all_cookies()
    for cookie in jd_cookies_list:
        driver.add_cookie(cookie)
    return driver


def to_goods_page():
    pass
```

##### 存在的问题

1. `check_cookies`函数中存在的问题

   原作中是通过设置一个flag来表示登录的状态, 虽然自己是直接通过最终返回True或False来表示cookies是否生效, 虽然好像看起来也没啥问题, 但是感觉逻辑不够完整, 就是首先应该假定是未登录的状态, 然后通过判断,来改变登录状态. 

2. `get_driver_with_cookies`函数中存在的问题

   1. 读cookies文件不需要传`encoding`参数了

### 3-4 获取商品详情信息开发(1)

到现在为止就剩下`to_goods_page()`这个函数没有实现了, 这个函数就是从首页跳转到商品最终的信息页面,

```python
def to_goods_page(driver):
    # 首先把页面放在首页上, 原因是假如在操作别的页面,代码跑起来就会直接报错
    driver.get("https://www.jd.com")
    # 定位到电脑上
    computer_element = driver.find_element_by_link_text("电脑")
    # 鼠标悬停在电脑上
    ActionChains(driver).move_to_element(computer_element).perform()
    # 点击笔记本
    time.sleep(2)
    driver.find_element_by_link_text("笔记本").click()
    # 切换句柄
    handles = driver.window_handles
    index_handle = driver.current_window_handle
    for handle in handles:
      	if handle != index_handle:
          	driver.switch_to.window(handle)
    # 点击thinkpad
    drive.find_element_by_xpath("//*[@id=\"brand-11518\"]/a").click()
    # 点击7000以上
    drive.find_element_by_xpath("").click()
    # 点击评论数
    drive.find_element_by_xpath("//*				[@id=\"J_filter\"]/div[1]/div[1]/a[3]/span").click()
    # 点击第一款电脑
    drive.find_element_by_xpath("//*[@id=\"J_goodsList\"]/ul/li[1]/div/div[1]/a/img").click()
    # 切换句柄
    notebook_handle = driver.current_window_handle
    #### 这里必须重新获取一下所有的句柄,因为这里已经有3个窗口了
    handles = driver.window_handles
    for handle in handles:
        if handle != index_handle and handle != notbook_handle:
            driver.switch_to.window(handle)
    # 0是横轴,代表最左侧, 10000代表最右侧;第二个参数代表上下,0是最上, 10000是最下
    js = "window.scrollTo(0,1500)"
    driver.execute_script(js)
    # 点击规格与包装
    driver.find_element_by_xpath("//*[@id=\"detail\"]/div[1]/ul/li[2]").click()
    # 解析所有的标签 思路是先拿整体,把所有的信息都拿下来,然后它变成一个格式化的字符串,或者叫它字典或者	# json
    info_elements = driver.find_elements_by_class_name("Ptable-item")
    
    # 有一个list存储最终的结果, 存储一块一块的信息,里面是一个一个的json
    result_list = []
    
    # 标签一个一个解析, 就是解析一个个的"Ptable-item"
    for info_element in info_elements:
      	info_element_dict = get_info_element_dict(info_element)
        result_list.append(info_element_dict)
    # 保存这些信息到文件中
    save_goods_info(result_list)
```

#### 1122自测结果

```python
def to_goods_page():
    driver.get("https://www.jd.com")
    ActionChains(driver).move_to_element(
        driver.find_element_by_link_text("电脑")).perform()
    time.sleep(1)
    driver.find_element_by_link_text("笔记本").click()
    index_handle = driver.current_window_handle
    handles = driver.window_handles
    for handle in handles:
        if handle != index_handle:
            driver.switch_to.window(handle)
    driver.find_element_by_xpath(
        '//*[@id="J_selectorPrice"]/div[1]/div[1]/input').send_keys("7000")
    # 要先冻结页面， 获取确定按钮
    driver.find_element_by_xpath(
        '//*[@id="J_selectorPrice"]/div[2]/a[2]').click()
    # 按评论数由高到低排列
    driver.find_element_by_xpath(
        '//*[@id="J_filter"]/div[1]/div[1]/a[3]/span').click()
    # 点击筛选结果的第一个商品
    driver.find_element_by_xpath(
        '//*[@id="J_goodsList"]/ul/li[1]/div/div[1]/a/img').click()
    goods_list_handle = driver.current_window_handle
    handles = driver.window_handles
    for handle in handles:
        if handle != index_handle and handle != goods_list_handle:
            driver.switch_to.window(handle)
    # 向下滚动到规格与包装
    js = "$(window.scrollTo(0, 1000))"
    driver.execute_script(js)
    # 点击规格与包装
    driver.find_element_by_xpath('//*[@id="detail"]/div[1]/ul/li[2]').click()
    # 获取所有的
    driver.find_elements_by_class_name("Ptable-item")
    # 在每个Ptable-item中获取h3标签的作为

```



### 3-5 获取商品详情信息开发(2)

现在只剩下两个函数没有实现了`get_info_element_dict`, `save_goods_info`

先要对页面结构进行分析, 选中`Ptable-itme`就选中了一块, `<h3>`就是左边的“主体”, 再往下, 两层`dl`,它用`<dl>`标签把一行一行的所有的信息都保存了, 再打开`<dl>`, 里面有一个`<dt>`还有一个`<dd>`, 对应的就是类似key和value, 其中还有带问号的,它占用了一个`<dd>`标签(`class`属性为`Ptable-tips`), 这不是我们要的, 要去掉.(思路是可以对比两个`<dd>`标签, 其中valve是没有class属性的, 所以就可以根据这个来做筛选, 将含有class属性的dd标签去掉)

所以拿的顺序是: 首先拿`h3`标签的内容,然后拿`dt`和`dd`标签,拿`dd`的时候记得去掉问号的`dd`

```python
def get_info_element_dict(info_element):
    # 拿到第一列的信息
    computer_part = info_element.find_element_by_tag_name("h3")
    # 计算机信息中的key值
    computer_info_keys = info_element.find_elements_by_tag_name("dt")
    # 计算机信息中的value值
    computer_info_values = info_element.find_elements_by_xpath(
      										 "dl//dd[not(contains(@class, 'Ptable-tips'))]") # 注意这里路径的写法, 并不是从// 开始的,而是直接从dl开始的, 以及在[]内的not也是一个函数,并不是对contains取反的意思
    # 存储计算机信息的key和value
    key_and_value_dict = {}
    # 存储所有的计算机组成信息
    parts_dict = {}
    for i in range(len(computer_info_keys)):   # 这个地方其实是在用下标进行迭代
      	key_and_value_dict[computer_info_keys[i].text] = computer_info_values[i].text
    parts_dict[computer_part.text] = key_and_value_dict
    return parts_dict
        
def save_goods_info(info_list):
  	project_path = os.path.dirname(os.getcwd())
    file_path = project_path + "/goods_infos/"
    if not os.path.exists(file_path):
      	os.mkdir(file_path)
    with open(file_path + "computer.infos", "a", encoding="utf-8") as f:
      	f.write(str(info_list)) # write不可以直接写list类型,要先转成字符串
        print(str(info_list))
```

#### 0819自测结果

```python
def to_goods_page(driver):
    # 点击电脑， 然后点击笔记本
    driver.get("https://www.jd.com")
    computer_element = driver.find_element_by_link_text("电脑")
    ActionChains(driver).move_to_element(computer_element).perform()
    time.sleep(2)
    driver.find_element_by_link_text("笔记本").click()
    # 切换句柄
    index_handle = driver.current_window_handle
    handles = driver.window_handles
    for handle in handles:
        if handle != index_handle:
            driver.switch_to.window(handle)
    # 点击thinkpad
    driver.find_element_by_xpath('//*[@id="brand-11518"]/a').click()
    # 输入价格区间7000以上
    driver.find_element_by_xpath('//*[@id="J_selectorPrice"]/div[1]/div[1]/input').send_keys("7000")
    driver.find_element_by_xpath('//*[@id="J_selectorPrice"]/div[2]/a[2]').click()
    # 点击按评论数排序
    driver.find_element_by_xpath('//*[@id="J_filter"]/div[1]/div[1]/a[3]/span').click()
    # 点击第一个商品
    driver.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[1]/a/img').click()
    # 切换句柄
    handles = driver.window_handles
    goods_handle = driver.current_window_handle
    for handle in handles:
        if handle != index_handle and handle != goods_handle:
            driver.switch_to.window(handle)

    # 向下滚动显示出规格与包装

    # 点击规格与包装
    driver.find_element_by_xpath('//*[@id="detail"]/div[1]/ul/li[2]').click()
    # 提取数据

    # 把数据存储到文件
    
```

##### 存在的问题

大体上思路正确, 具体到实现上的时候有两个地方不会

1. 操纵js向下滚动不会了,忘记了
2. 知道要提取数据, 但是怎么提取没思路
3. 把数据保存到文件也没太明确的思路

#### 1123自测结果

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import json
import os

driver = webdriver.Chrome()
driver.maximize_window()


def login():
    driver.get("https://www.jd.com")
    driver.find_element_by_class_name("link-login").click()
    driver.find_element_by_link_text("账户登录").click()
    driver.find_element_by_id("loginname").send_keys("13120597275")
    driver.find_element_by_id("nloginpwd").send_keys("shenxin22019891")
    driver.find_element_by_id("loginsubmit").click()
    save_cookies_to_file()


def save_cookies_to_file():
    cookies_file = get_cookies_file()
    jd_cookies = driver.get_cookies()
    with open(cookies_file, "w") as f:
        json.dump(jd_cookies, f)


def get_cookies_dir():
    project_path = os.path.dirname(os.getcwd())
    cookies_path = os.path.join(project_path, "cookies")
    if not os.path.exists(cookies_path):
        os.mkdir(cookies_path)
    return cookies_path


def get_cookies_file():
    return os.path.join(get_cookies_dir(), "jd_1119.cookies")


def check_cookies():
    login_status = False
    driver = get_driver_with_cookies()
    url = "https://order.jd.com/center/list.action"
    driver.get(url)
    if driver.current_url == url:
        login_status = True
    return login_status


def get_driver_with_cookies():
    cookies_file = get_cookies_file()
    if not os.path.isfile(cookies_file):
        login()
    with open(cookies_file, "r") as f:
        jd_cookies_str = f.readline()
        jd_cookies_list = json.loads(jd_cookies_str)
    driver.get("https://www.jd.com")
    driver.delete_all_cookies()
    for cookie in jd_cookies_list:
        driver.add_cookie(cookie)
    return driver


def to_goods_page():
    driver.get("https://www.jd.com")
    computer_elem = driver.find_element_by_link_text("电脑")
    ActionChains(driver).move_to_element(computer_elem).perform()
    time.sleep(1)
    driver.find_element_by_link_text("笔记本").click()
    index_handle = driver.current_window_handle
    handles = driver.window_handles
    for handle in handles:
        if handle != index_handle:
            driver.switch_to.window(handle)
    # 点击thinkpad
    driver.find_element_by_xpath('//*[@id="brand-11518"]/a').click()
    # 点击价格区间框
    price = driver.find_element_by_xpath(
        '//*[@id="J_selectorPrice"]/div[1]/div[1]/input')
    price.send_keys("7000")
    # 点击价格区间框的确定
    # 设定冻结窗口的方式是 setTimeout(function(){debugger}, 5000) 老是记不住
    # ActionChains(driver).move_to_element(price).perform()
    # driver.find_element_by_xpath(
    #     '//*[@id="J_selectorPrice"]/div[2]/a[2]').click()
    # 点击按评论数排序
    driver.find_element_by_xpath('//*[@id="J_filter"]/div[1]/div[1]/a['
                                 '3]/span').click()
    # 点击第一款电脑
    driver.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div['
                                 '1]/a/img').click()
    goods_list_handle = driver.current_window_handle
    handles = driver.window_handles
    for handle in handles:
        if handle != index_handle and handle != goods_list_handle:
            driver.switch_to.window(handle)
    js = 'window.scrollTo(0, 1000)'
    driver.execute_script(js)
    driver.find_element_by_xpath('//*[@id="detail"]/div[1]/ul/li[2]').click()
    # 先拿到所有的大块
    info_elements = driver.find_elements_by_class_name("Ptable-item")
    # 有一个结果列表存储所有的大块
    result_list = []
    for info_element in info_elements:
        info_element_dict = get_info_element_dict(info_element)
        result_list.append(info_element_dict)
    save_goods_to_file(result_list)


def get_info_element_dict(info_element):
    computer_part = info_element.find_element_by_tag_name("h3")
    computer_info_keys = info_element.find_elements_by_xpath('//dl/dt')
    # computer_info_values = info_element.find_element_by_xpath(
    #     '//dl/dd[not contains(class="Ptable-tips")]')
    computer_info_values = info_element.find_elements_by_xpath(
        "dl//dd[not(contains(@class, 'Ptable-tips'))]")
    computer_info_dict = dict(zip(computer_info_keys.text,
                                  computer_info_values.text))
    computer_part_dict = {}
    computer_part_dict[computer_part.text] = computer_info_dict
    return computer_part_dict


def save_goods_to_file(goods_list):
    project_path = os.path.dirname(os.getcwd())
    file_path = os.path.join(project_path, "goods_info")
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    file_name = os.path.join(file_path, "goods_1123.infos")
    # with open(file_name, "w", encoding="utf-8") as f:
    #     f.write(str(goods_list))
    #     print(str(goods_list))
    with open(file_name, "a", encoding="utf-8") as f:
        f.write(str(goods_list))
        print(str(goods_list))


if __name__ == '__main__':
    loop_status = True
    try:
        while loop_status:
            cookies_status = check_cookies()
            if cookies_status:
                loop_status = False
            else:
                login()
        to_goods_page()
    finally:
        time.sleep(3)
        driver.quit()
```

#### 1123优化结果

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import json
import os

options = webdriver.ChromeOptions()
# options.add_argument("disable-infobars")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
driver = webdriver.Chrome(options=options)
driver.maximize_window()


def login():
    driver.get("https://www.jd.com")
    driver.find_element_by_class_name("link-login").click()
    driver.find_element_by_link_text("账户登录").click()
    driver.find_element_by_id("loginname").send_keys("13120597275")
    driver.find_element_by_id("nloginpwd").send_keys("shenxin22019891")
    driver.find_element_by_id("loginsubmit").click()
    save_cookies_to_file()


def save_cookies_to_file():
    cookies_file = get_cookies_file()
    jd_cookies = driver.get_cookies()
    with open(cookies_file, "w") as f:
        json.dump(jd_cookies, f)


def get_cookies_dir():
    project_path = os.path.dirname(os.getcwd())
    cookies_path = os.path.join(project_path, "cookies")
    if not os.path.exists(cookies_path):
        os.mkdir(cookies_path)
    return cookies_path


def get_cookies_file():
    return os.path.join(get_cookies_dir(), "jd_1119.cookies")


def check_cookies():
    login_status = False
    driver = get_driver_with_cookies()
    url = "https://order.jd.com/center/list.action"
    driver.get(url)
    if driver.current_url == url:
        login_status = True
    return login_status


def get_driver_with_cookies():
    cookies_file = get_cookies_file()
    if not os.path.isfile(cookies_file):
        login()
    with open(cookies_file, "r") as f:
        jd_cookies_str = f.readline()
        jd_cookies_list = json.loads(jd_cookies_str)
    driver.get("https://www.jd.com")
    driver.delete_all_cookies()
    for cookie in jd_cookies_list:
        driver.add_cookie(cookie)
    return driver


def to_goods_page():
    driver.get("https://www.jd.com")
    computer_elem = driver.find_element_by_link_text("电脑")
    ActionChains(driver).move_to_element(computer_elem).perform()
    time.sleep(1)
    driver.find_element_by_link_text("笔记本").click()
    index_handle = driver.current_window_handle
    handles = driver.window_handles
    for handle in handles:
        if handle != index_handle:
            driver.switch_to.window(handle)
    # 点击thinkpad
    driver.find_element_by_xpath('//*[@id="brand-11518"]/a').click()
    # 点击价格区间框
    price = driver.find_element_by_xpath(
        '//*[@id="J_selectorPrice"]/div[1]/div[1]/input')
    price.send_keys("7000")
    # 点击价格区间框的确定
    # 设定冻结窗口的方式是 setTimeout(function(){debugger}, 5000) 老是记不住
    ActionChains(driver).move_to_element(price).perform()
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="J_selectorPrice"]/div[2]/a[2]').click()
    # 点击按评论数排序
    driver.find_element_by_xpath(
        '//*[@id="J_filter"]/div[1]/div[1]/a[3]/span').click()
    time.sleep(1)
    # 点击第一款电脑
    driver.find_element_by_xpath(
        '//*[@id="J_goodsList"]/ul/li[1]/div/div[1]/a/img').click()
    goods_list_handle = driver.current_window_handle
    handles = driver.window_handles
    for handle in handles:
        if handle != index_handle and handle != goods_list_handle:
            driver.switch_to.window(handle)
    js = 'window.scrollTo(0, 1000)'
    driver.execute_script(js)
    driver.find_element_by_xpath('//*[@id="detail"]/div[1]/ul/li[2]').click()
    # 先拿到所有的大块
    info_elements = driver.find_elements_by_class_name("Ptable-item")
    # 有一个结果列表存储所有的大块
    result_list = []
    for info_element in info_elements:
        info_element_dict = get_info_element_dict(info_element)
        result_list.append(info_element_dict)
    save_goods_to_file(result_list)


def get_info_element_dict(info_element):
    computer_part = info_element.find_element_by_tag_name("h3")
    # computer_info_keys_elem = info_element.find_elements_by_xpath('//dl/dt')
    computer_info_keys_elem = info_element.find_elements_by_tag_name('dt')
    # computer_info_values = info_element.find_element_by_xpath(
    #     '//dl/dd[not contains(class="Ptable-tips")]')
    computer_info_values_elem = info_element.find_elements_by_xpath(
        "dl//dd[not(contains(@class, 'Ptable-tips'))]")
    computer_info_keys = [x.text for x in computer_info_keys_elem]
    computer_info_values = [y.text for y in computer_info_values_elem]
    computer_info_dict = dict(zip(computer_info_keys, computer_info_values))
    computer_part_dict = {computer_part.text: computer_info_dict}
    return computer_part_dict


def save_goods_to_file(goods_list):
    project_path = os.path.dirname(os.getcwd())
    file_path = os.path.join(project_path, "goods_info")
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    file_name = os.path.join(file_path, "goods_1123.infos")
    # with open(file_name, "w", encoding="utf-8") as f:
    #     f.write(str(goods_list))
    #     print(str(goods_list))
    with open(file_name, "a", encoding="utf-8") as f:
        f.write(str(goods_list))
        print(json.dumps(goods_list, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    loop_status = True
    try:
        while loop_status:
            cookies_status = check_cookies()
            if cookies_status:
                loop_status = False
            else:
                login()
        to_goods_page()
    finally:
        time.sleep(3)
        # driver.quit()

```



### 3-6 有Error和无Error的错误排查思路

 在跑代码之前,要在`login`函数的`save_cookies_to_file`处打一个断点,来手动处理一下验证码.

以debug方式运行.

遇到问题应该怎样排查:

首先看异常:

## 第4章 强化元素定位的方法

### 4-1 绝对定位与相对定位

强化定位:XPath与CSS Selector

有很多元素没有常规的定位,这就给定位造成了一定的困难. 这时候Xpath和CSS Selector运用的熟练.

打开console, 输入`$x(" “)`, 中间的部分就是xpath表达式,举例:

`$x("/html")`

就可以定位到整个html文档, 这也是绝对定位的一种方式. 也可以有多个层级:

`$x("/html/body")`

回车就定位到了`body`这个元素

打开京东登录页面, 比如我想定位京东的logo, 假设用绝对定位的方式应该怎么定位?

`$x("/html/body/div[1]/div")`

如果觉得在elements标签页切换到console标签页麻烦, 可以在elements标签页按esc,这时会弹出console标签页.

相对定位: 就是在整个页面上进行查找

举例:比如想要定位“账户登录”:

如果不使用属性进行定位, 那就要向上一级一级找到具有唯一标识的元素, 比如找到id为content的元素,

`$x('//div[@id="content"]/div[2]/div[1]/div/div[3]')`

除了这种定位方式我们也可以直接指定class的属性值

`$x('//div[@class="login-tab login-tab-r"]')`

### 4-2 通配符与不包含筛选

比如一个商品的页面, 比如把页面上的商品全都获取到,先定位第一个商品,所有的电脑都是`<li>`标签,我们可以从上面往下定位, 但是这个标签上有太多父级元素, 记不住,这时候就可以用通配符`*`, 可以数它有几级父级元素.数到最上面有9级父级元素.

```javascript
> $x("/*/*/*/*/*/*/*/*/*/li")
```

这样就定位了有9级父标签的`<li>`元素

标签匹配是从1开始, 1代表第一个.

通配符不仅可以放到前面,也可以放到后面代表所有的子标签

```javascript
> $x('/*/*/*/*/*/*/*/*/*/li[1]/*')
```

关于属性的演示:

不包含筛选的写法:

```javascript
> $x('//div[@class="Ptable-item"]//dd[not(@class="Ptable-tips")]')
```

或者:

```javascript
> $x('//div[@class="Ptable-item"]//dd[not(contains(@class,"Ptable-tips"))]')
```

`not`接受的是`@class="Ptable-tips"`这样的一个表达式

`contains`接受的是`@class`, `"Ptable-tips”`这两个参数, 这是二者的区别.

### 4-3 XPath 函数运算的简单使用

#### 去除属性两端的空格

如果class属性两边有空格, 一种方法可以在定位的时候把空格写上:

```javascript
> $x('//div[@class=" my-Ptable-item "]')
```

另外一种方法是使用函数:

```javascript
> $x('//div[normalize-space(@class)="my-Ptable-item"]')
```

#### 统计元素个数的应用:

比如想要统计只有两行数据的

是在商品详情页上, 有几个`<dl>`就有几行数据

```javascript
> $x('//*[count(dl)=2]')
```

含义是:选择含有两个`<dl>`子标签的元素

```javascript
> $x('//dl[count(dl)=3]')
```

含义: 要定位`<dl>`标签,这个标签下一共有3个`<dl>`子标签

#### 其他

以什么开头的:

```javascript
> $x('//*[starts-with(name(), "d")]')
```

`name()`是标签名, 这个会筛选出所有以d开头的标签

限定标签长度:

```javascript
> $x('//*[string-length(name())=2]')
```

含义: 筛选标签名字长度为2的所有元素

### 4-4 各种亲戚标签的定位

以京东登录页的用户名输入框为例:

假如想定位用户名父标签, 这个标签是`<div class="item item-fore1">` 没有明显标识, 比较难定位

父标签的使用:

```javascript
> $x('//input[@id="loginname"]/parent::div')  <-- 代表父标签为div的 -->
> $x('//input[@id="loginname"]/parent::*')  <-- 代表所有的父标签 -->
```

弟弟标签的定位:

```javascript
> $x('//input[@id="loginname"]/following-sibling::*')
```

哥哥标签的定位:

```javascript
> $x('//input[@id="loginname"]/preceding-sibling::*')
```

所有后代节点:

```javascript
> $x('//div[@class="item item-fore1"]/descendant::*')

<-- 也可以指定后代节点的类型 -->
> $x('//div[@class="item item-fore1"]/descendant::input')
```

所有祖先标签:

```javascript
> $x('//div[@class="item item-fore1"]/ancestor::*')
```

通配符也可以使用指定的标签名

### 4-5 CSS选择器中的那些符号

CSS指的是层叠样式表,它就是来修饰前端的样式的,CSS选择器就是根据样式来进行元素的选择,这里仍然有两种方式来进行CSS选择器代码的调试,就是在console里`> $("")` 或者`> $$("")`都可以.

本小节主要讲的是关于CSS中特殊符号的应用

`.`代表了每个标签中class的属性

依旧以京东登录页面的用户名输入框为例, 它的`class=“itxt”`, 那么就可以写成:

```javascript
> $$(".itxt")    <-- 表示定位到文档树中class属性为itxt的元素 -->
```

`#`代表的是`id`属性

```javascript
> $$("#loginname")  <-- 表示定位文档树中标签里有id的元素并且id的值是loginname的 -->
```

`,`代表和的意思

```javascript
> $$("#loginname,#nloginpwd")  <同时定位了用户名和密码输入框>
```

`空格`代表所有的后代元素 举例: id为entry的div元素

```javascript
> $$("#entry input")  <id等于entry这样的元素的所有后代input元素>
```

`>`代表儿子标签: 以某一商品规格与包装页面为例

```javascript
> $$(".Ptable-item dl")    <这时候搜出来的是所有的后代dl元素>
> $$(".Ptable-item>dl")    <这时候只是搜出来儿子dl元素>
```

### 4-6 CSS选择器的属性筛选

定位页面上所有的class属性为p-price的div元素(以某一商品规格与包装页面为例)

```javascript
> $$("div[class=p-price]")
```

这里要注意和xpath的区别:

1. xpath的属性前面有@符号,css没有; xpath的属性值要用引号括起来,css不用
2. 当class有多个值,css选择器应该怎么写:比如页面上元素的`class=“lh clearfix”`, 写成css选择器就是:

```javascript
> $$(".lh.clearfix")
```

如果是包含:

```javascript
> $$("div[id*=fit]")  <id属性值中含有fit这几个字符就可以>
```

如果是某一个属性值开头的:

```javascript
> $$("div[id^=f]")  <id属性值以f开头的>
```

### 4-7 回顾js定位写法及webdriver模块源代码初探



```javascript
js = "$('input[id=train_date]').removeAttr('readonly')"
```

w3c

格式化 `By.CSS_SELECTOR`

最终会去执行 `Commend.FIND_ELEMENT`

驼峰命名法.

回到上一个定位: `Option`+`command`+:arrow_left:

首先它是什么样的一种封装思路. find_element, 如果是符合w3c标准的一个浏览器

## 第5章 Selenium 分布式测试

### 5-1 Python 虚拟环境的创建

#### 分布式测试的作用与意义

分布式测试的应用场景:

1. 兼容性测试

   现在的Web应用程序会运行在不同的浏览器上, 各个浏览器它的兼容性怎么样可以用分布式的方式来进行测试, 就是同时启多个浏览器, 然后在这些浏览器上跑相同的业务流程, 来测试所有的步骤.

2. 提高UI测试效率

   整个UI的自动化测试效率是比较低的, 比接口自动化等跑的都要慢, 提高速度可以采用这种分布式测试, 在不同浏览器上跑不同的测试流程, 这样就可以提高效率.

#### Python的虚拟环境

​		作用就是隔离的效果, 类似虚拟机. 

如何安装:

打开命令行工具:

```shell
pip install virtualenvwrapper (for Mac/Linux)
pip install virtualenvwrapper-win (for Windows)
```

配置环境变量:

Windows的配置方法: 我的电脑-> 属性 -> 高级

Linux/Mac:  `cat ~/.bash_profile`(个人的环境变量的目录设置)

需要在某个目录下创建一个文件夹, 这个文件夹的作用就是python虚拟环境的存储目录:

`export WORKON_HOME=/workspace/python_env`

虚拟环境中的Python用的是什么版本:

`export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3`

必须要让`virtualenvwarpper.sh`这个文件生效, 虚拟环境才能生效

`source /Library/Framework/Python.framework/Versions/3.6/bin/virtualenvwarpper.sh`

> 如何找virtualenvwarpper.sh

​	`sudo find / -name virtualenvwrapper.sh`(前面必须加sudo)

如何创建虚拟环境:

先切到存储虚拟环境的目录:`cd /workspace/python_env`

列出所有的虚拟环境: `workon`

创建虚拟环境: `mkvirtualenv imooc_test`

创建完成后自动进入新创建的虚拟环境(在命令行前面有括号提示)

退出虚拟环境: `deactivate imooc_test`

进入虚拟环境: `workon imooc_test`

删除虚拟环境: `rmvirtualenv imooc_test`

在pycharm中如何选择虚拟环境, 选择已经存在的interpreter

一种是修改已有的项目的虚拟环境

一种是创建新项目的时候就生成



### 5-2 环境迁移必备的requirements

打开GitHub, 随便搜索一个项目, 都会有一个`requirements.txt`

进入到工程目录下:

生成`requirements.txt`: `pip freeze > requirements.txt`

安装`requirements.txt`: `pip install -r requirements.txt`

### 5-3 分布式环境搭建

使用虚拟机解决这个问题:

虚拟机有一个windows, 还有一个Ubuntu 64位.

打开https://docs.seleniumhq.org/download

下载selenium standalone server, 需要把它放在需要远程机器上.

它是一个jar包, 所以要先安装好jdk8, 并且配置好 环境变量,(Ubuntu是在 `~/.profile`或者是 `/etc/profile`), 

具体配置方式:

```shell
export JAVA_HOME=/workspace/software/jdk1.8.0_201
export PATH=$JAVA_HOME/bin
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
```

然后`source /etc/profile` 使配置生效

在Windows机器上也配好JDK8

然后在selenium standalone server的jar包所在的目录分别运行`java -jar selenium-server-standalone-3.141.59.jar`(`selenium-server-standalone-3.141.59.jar` 不需要放入环境变量)

看到Selenium Server is up and running on port 4444 字样且无报错证明分 布式环境启动成功.

### 5-4 环境搭建补充和分布式环境测试代码开发

然后在每个环境里的chromedriver也装好, chromedriver的路径也要添加到环境变量里. 当然chrome浏览器也要下好

新建包`part_five`, 创建`connect_remoteserver.py`

```python
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapbilities 
from threading import Thread

# 书写我的业务逻辑
def to_baidu(name, server_address):
  	print(name)
    driver = webdriver.Remote(
    		command_executor=server_address,
    		desired_capabilities=DesiredCapabilities.CHROME  	
    )
    driver.get("https://www.baidu.com")
    
my_address = {
  	"linux": "http://192.168.1.35:4444/wd/hub",
  	"windows": "http://192.168.1.38:4444/wd/hub"
}

threads = []
for name, url in my_address.items():
  	t = Thread(target=to_baidu, args=(name, url))
    threads.append(t)
    
for t in threads:
  	t.start()
```

#### 0823自测结果

```python
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from threading import Thread

driver = webdriver.Remote(
    command_executor="pass",
    DesiredCapabilities=webdriver.Chrome
)


def to_baidu():
    driver.get("https://www.baidu.com")
    current_url = driver.current_url
    if current_url == "https://www.baidu.com":
        return True
    else:
        return False


server_address = {
    "windows": "192.168.0.1",
    "linux": "192.168.0.2"
}

threads = []
for k, v in server_address.items():
    t = Thread(target=to_baidu, args=(k, v))
    threads.append(t)
for t in threads:
    t.start()
```

##### 存在的问题

1. 首先思路有点不正确，不应该在这个连接远程机器的py文件里实例化driver, 应该在每个远程机器里实例化
这样的话就需要将driver初始化的代码写在测试函数里，在调用测试函数的时候实例化driver
2. 在实例化远程driver的时候，忘记command_executor应该写什么了，command_executor写的是远程
机器的IP， DesiredCapabilities记得引入，但是不知道怎么使用了。
3. 在构造测试函数的时候，需要传入name和address两个参数，隐约记得该传，但是里面怎么用就不记得了，
所以没传
4. 测试函数只需要去访问URL，不需要对driver的返回结果进行判断，因为如果不对的话，就应该报错了
5. 在写address的时候，只记得有IP，而不记得后缀 `:4444/wd/hub`

### 5-5 PyMySQL的基本使用

安装: `pip install pymysql`

首先新建数据库python_ui, 字符集utf8, 新建goods表

|     列名      |     定义     |             其他              |
| :-----------: | :----------: | :---------------------------: |
|      id       |    bigint    | not null, auto_increment,主键 |
| computer_part | varchar(200) |           not null            |
| computer_info |     text     |           not null            |



在`part_five`下创建`my_mysql_connection.py` 

```python
import pymysql

# 获取mysql的连接
db_connection = pymysql.connect(
		host="192.168.1.35",
		user="admin",
		password="123456",
		database="python_ui",
		charset="utf8"
)
# 获取游标
cursor = db_connection.cursor()
# 书写sql
sql = "insert into goods(computer_part, computer_info) values ('主体', '主体信息')"
# 执行sql
cursor.execute(sql)
# 提交sql
db_connection.commit()
# 关闭游标
cursor.close()
# 关闭连接
db_connection.close()
```



### 5-6 实战多个业务流程同时运行代码拆分(1)

将`part_two`下的`jingdong.py`, 复制一份; 然后在`part_five`下新建一个`jingdong`的包, 把前面的文件粘贴进去, 在那个文件的基础上进行修改.

想要实现最终的效果: 在“电脑”这一页当中, 我们可以选择很多品牌, 比如说, Linux选择Thinkpad, Windows选择戴尔, 这就实现了用多个浏览器来进行启动,不同的浏览器走不同的业务流程.

先对`jingdong.py`进行拆分, 新建一个`my_cookies.py`, 存储所有的cookies操作.

```python
import json
import os


# 把cookies保存到文件中
def save_cookies_to_file(driver):
  	# 获取存储cookies的文件夹
    file_path = get_cookies_dir()
    # 获取cookies
    cookies = driver.get_cookies()
    # 存储cookies到文件中
    with open(file_path + "jd.cookies", "w") as f:
      	json.dump(cookies, f)
        

def get_cookies_dir():
  	project_path = os.path.dirname(os.getcwd())
    file_path = project_path + "/cookies/"
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    return file_path
  
  
def check_cookies(driver):
  	# 设置一个登录状态, 初始值是未登录
    login_status = False
    # 将cookies信息保存到driver中
    driver = save_cookies_to_driver(driver)
    # 进行跳转链接的检测
    driver.get("https://order.jd.com/center/list.action")
    current_url = driver.current_url
    if current_url == "https://order.jd.com/center/list.action":
      	login_status = True
        return login_status
    else:
      	return login_status
  
# 保存cookies信息到driver中
def save_cookies_to_driver(driver):
  	cookie_file = get_cookies_file()
    jd_cookies_file = open(cookies_file, "r")
    jd_cookies_str = jd_cookies_file.readline()
    jd_cookies_dict = json.loads(jd_cookies_str)
    
    #这里必须清除掉旧的cookies
    driver.get("https://www.jd.com")
    driver.delete_all_cookies()
    for cookie in jd_cookies_dict:
      	driver.add_cookie(cookie)
    return driver
  
def get_cookies_file():
  	return get_cookies_dir() + "jd.cookies"
```

还要将`jingdong.py`中原来`if __name__ == ‘__main__’ `下面的部分改写成一个函数:

```python
def to_start(driver, name):
  	# 要有一个循环来控制登录状态, 判断登录是否成功
    try:
      	loop_status = True
        while loop_status:
          	# 检验cookies是否生效
            login_status = check_cookies(driver)
            if login_status:
              	loop_status = False
            else:
              	login(driver)
        # 跳转到商品信息页面
        to_goods_page(driver, name)
    finally:
      	time.sleep(3)
        driver.quit()

# 然后把刚才分出去的my_cookies 倒进来
from part_five.jingdong.my_cookies import *
```

然后把启动浏览器那几句删掉,

```python
# 然后把启动浏览器那几句删掉
# path = "/Users/zjy/Documents/imooc/code/python_ui/chromedriver"
# driver = webdriver.Chrome(path)
# driver.maximize_window()
```

然后在`part_five`下直接创建`remote_start_jingdong.py`, 当作统一的入口:

```python
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapbilities
from threading import Thread
from part_five.jingdong import jingdong


def to_jingdong(name, server_address):
  	print(name + "启动")
    driver = webdriver.Remote(
    		command_executor=server_address,
      	desired_capabilities=DesiredCapabilities.CHROME
    )
    driver.maximize_window()
    if name == "linux":
      	jingdong.thinkpad_start(driver)
    if name == "windows":
      	jingdong.dell_start(driver)
        
my_address = {
  	"linux" : "http://192.168.1.35:4444/wd/hub",
  	"windows": "http://192.168.1.38:4444/wd/hub"
}

threads = []
for name, url in my_address.items():
  	t = Thread(target=to_jingdong, args=(name, url))
    threads.append(t)

for t in threads:
  	t.start()
```

现在回到`jingdong.py`, 完善刚才上面两个函数,`thinkpad_start`和`dell_start`, 修改部分代码

```python
# 登录功能
def login(driver):
  	driver.get("https://www.jd.com")
    driver.find_element_by_class_name("link-login").click()
    driver.find_element_by_link_text("账户登录").click()
    driver.find_element_by_id("loginname").send_keys("1111111")
    driver.find_element_by_id("nloginpwd").send_keys("22222222")
    driver.find_element_by_id("loginsubmit").click()
    
    # 要保存cookies到文件中
    save_cookies_to_file(driver)
    
    
def to_goods_page(driver):
    # 首先把页面放在首页上
    driver.get("https://www.jd.com")
    # 定位到电脑上
    computer_element = driver.find_element_by_link_text("电脑")
    # 鼠标悬停在电脑上
    ActionChains(driver).move_to_element(computer_element).perform()
    # 点击笔记本
    time.sleep(2)
    driver.find_element_by_link_text("笔记本").click()
    # 切换句柄
    handles = driver.window_handles
    index_handle = driver.current_window_handle
    for handle in handles:
      	if handle != index_handle:
          	driver.switch_to.window(handle)
    # 点击thinkpad
    drive.find_element_by_xpath("//*[@id=\"brand-11518\"]/a").click()
    # 点击7000以上
    drive.find_element_by_xpath("").click()
    # 点击评论数
    drive.find_element_by_xpath("//*				[@id=\"J_filter\"]/div[1]/div[1]/a[3]/span").click()
    # 点击第一款电脑
    drive.find_element_by_xpath("//*[@id=\"J_goodsList\"]/ul/li[1]/div/div[1]/a/img").click()
    # 切换句柄
    notebook_handle = driver.current_window_handle
    #### 这里必须重新获取一下所有的句柄,因为这里已经有3个窗口了
    handles = driver.window_handles
    for handle in handles:
        if handle != index_handle and handle != notbook_handle:
            driver.switch_to.window(handle)
    # 0是横轴,代表最左侧;第二个参数代笔上下,0是最上
    js = "window.scrollTo(0,1500)"
    driver.execute_script(js)
    # 点击规格与包装
    driver.find_element_by_xpath("//*[@id=\"detail\"]/div[1]/ul/li[2]").click()
    # 解析所有的标签 思路是先拿整体
    info_elements = driver.find_elements_by_class_name("Ptable-item")
    
    # 有一个list存储最终的结果, 存储一块一块的信息,里面是一个一个的json
    result_list = []
    
    # 标签一个一个解析
    for info_element in info_elements:
      	info_element_dict = get_info_element_dict(info_element)
        result_list.append(info_element_dict)
    # 保存这些信息到文件中
    save_goods_info(result_list)


def get_info_element_dict(info_element):
    # 拿到第一列的信息
    computer_part = info_element.find_element_by_tag_name("h3")
    # 计算机信息中的key值
    computer_info_keys = info_element.find_elements_by_tag_name("dt")
    # 计算机信息中的value值
    computer_info_values = info_element.find_elements_by_xpath(
      										 "dl//dd[not(contains(@class, 'Ptable-tips'))]")
    # 存储计算机信息的key和value
    key_and_value_dict = {}
    # 存储所有的计算机组成信息
    parts_dict = {}
    for i in range(len(computer_info_keys)):
      	key_and_value_dict[computer_info_keys[i].text] = computer_info_values[i].text
    parts_dict[computer_part.text] = key_and_value_dict
    return parts_dict
        
def save_goods_info(info_list):
  	project_path = os.path.dirname(os.getcwd())
    file_path = project_path + "goods_infos"
    if not os.path.exists(file_path):
      	os.mkdir(file_path)
    with open(file_path + "computer.infos", "a", encoding="utf-8") as f:
      	f.write(str(info_list))
        print(str(info_list))
        

def thinkpad_start(driver):
  	to_start(driver, "thinkpad")
    

def dell_start(driver):
  	to_start(driver, "dell")
```

然后修改`to_goods_page`函数:

```python
def to_goods_page(driver, name):
    # 首先把页面放在首页上
    driver.get("https://www.jd.com")
    # 定位到电脑上
    computer_element = driver.find_element_by_link_text("电脑")
    # 鼠标悬停在电脑上
    ActionChains(driver).move_to_element(computer_element).perform()
    # 点击笔记本
    time.sleep(2)
    driver.find_element_by_link_text("笔记本").click()
    # 切换句柄
    handles = driver.window_handles
    index_handle = driver.current_window_handle
    for handle in handles:
      	if handle != index_handle:
          	driver.switch_to.window(handle)
    if name == "thinkpad":
        # 点击thinkpad
        drive.find_element_by_xpath("//*[@id=\"brand-11518\"]/a").click()
    if name == "dell":
      	# 点击戴尔
        drive.find_element_by_xpath("//*[@id=\"brand-5821\"]/a").click()
    # 点击7000以上
    drive.find_element_by_xpath("").click()
    # 点击评论数
    drive.find_element_by_xpath("//*				[@id=\"J_filter\"]/div[1]/div[1]/a[3]/span").click()
    # 点击第一款电脑
    drive.find_element_by_xpath("//*[@id=\"J_goodsList\"]/ul/li[1]/div/div[1]/a/img").click()
    # 切换句柄
    notebook_handle = driver.current_window_handle
    #### 这里必须重新获取一下所有的句柄,因为这里已经有3个窗口了
    handles = driver.window_handles
    for handle in handles:
        if handle != index_handle and handle != notbook_handle:
            driver.switch_to.window(handle)
    # 0是横轴,代表最左侧;第二个参数代笔上下,0是最上
    js = "window.scrollTo(0,1500)"
    driver.execute_script(js)
    # 点击规格与包装
    driver.find_element_by_xpath("//*[@id=\"detail\"]/div[1]/ul/li[2]").click()
    # 解析所有的标签 思路是先拿整体
    info_elements = driver.find_elements_by_class_name("Ptable-item")
    
    # 有一个list存储最终的结果, 存储一块一块的信息,里面是一个一个的json
    result_list = []
    
    # 标签一个一个解析
    for info_element in info_elements:
      	info_element_dict = get_info_element_dict(info_element)
        result_list.append(info_element_dict)
    # 保存这些信息到文件中
    save_goods_info(result_list)
```



### 5-7 实战多个业务流程同时运行代码拆分(2)

代码拆分完之后, 还有这样的一个需求: 把他们获取到的信息写到数据库中

在`jingdong`包下新建`my_mysql.py`

```python
import pymysql

def save_goods_info_to_mysql(info_list):
  	try:
      	db_connection = get_connection()
        cursor = db_connection.cursor()
        # 遍历info_list然后把数据存进去
        for info in info_list:
          	for key, value in info.items():
              	sql = "insert into goods(computer_part, computer_info) \
              				values(\"%s\", \"%s\")" % (key, value)
                print(sql)
                cursor.execute(sql)
                db_connection.commit()
    finally:
      	close_db(db_connection, cursor)
        
def get_connection():
  	db_connection = pymysql.connect(
    		host = "192.168.1.35",
      	user = "admin",
        password="123456",
        database="python_ui",
        charset="utf8"
    )
    return db_connection

  
def close_db(db_connection, cursor):
  	cursor.close()
  	db_connection.close()
```

然后回到`jingdong.py`中修改, 把之前的保存这些信息到文件中修改为保存到数据库

```python
# 要先把函数导进来
from part_five.jingdong.my_mysql import *

# 保存这些信息到文件中
# save_goods_info(result_list)
save_goods_info_to_mysql(result_list)
```



### 5-8 实战多个业务流程同时运行代码拆分(3)

在调试的时候要现在`jingdong.py` 的`login`方法的`save_cookies_to_file`这一行打一个断点.

从`remote_start_jingdong.py` 以debug方式运行

打开两个虚拟机查看运行情况



## 第6章 等待的几种方式及源代码分析

### 6-1 等待的几种方式

新建一个包`part_six`,新创建一个`my_wait.py`:

等待主要有以下几种方法:

1. 强制等待
2. 隐性等待
3. 显性等待

```python
from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/zjy/Documents/imooc/code/python_ui/chromedriver")
driver.get("https://passport.jd.com/new/login.aspx")

# 强制等待
time.sleep(3)

# 隐性等待
driver.implicitly_wait(10)
# 隐性等待就是设置了一个最长的等待时间,假设在规定的时间内网页加载完成则执行下一步.否则就一直等到时间截
# 止,然后执行下一步. 这里面有个弊端就是程序会一直等待程序加载完成,有的时候网页加载速度是很慢的,或者个别
# js加载不出来,这个时候它就一直等待了.
# 隐性等待只要设置一次,就围绕着driver的生命周期全都起作用,也就是说是一个全局设置

# 显性等待
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 定位元素  定位的是登录页面的「账户登录」四个字  源代码是 class="login-tab login-tab-r"
locator = (By.CSS_SELECTOR, ".login-tab.login-tab-r")

# 判断账号登录这个元素是否存在
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
element.click()
```

### 6-2 Python 中的几个魔法方法

几个等待方法中最主要的是显性等待.为了看懂显式等待为什么传那些参数,以及`until`后面怎么写的,首先需要讲解关于Python中的几个魔法方法.

创建`/part_six/person.py`

```python
class Person:
  	def __init__(self):
      	print("构造函数运行")
        
    def __call__(self, *args, **kwargs):
      	print("call方法运行")
    
    def __new__(cls, *args, **kwargs):
      	print("new方法运行")
        
    def __del__(self):
      	print("析构函数 del方法运行")
        
        
p = Person()
```

以以上代码去运行:

第一次运行的时候只会打印: `new方法运行`.

第二次的时候把`new`方法注释掉, 会打印: `构造函数运行, 析构函数 del方法运行`

第三次把`new`打开,然后修改new的返回值:

```python
def __new__(cls, *args, **kwargs):
  	print("new方法运行")
    return object.__new__(Person)  # 这里是返回了Person父类的new方法
```

再次运行, 会打印: 

`new方法运行`

`构造函数运行` 

`析构函数 del方法运行`

也就是说`__new__`方法在构造函数`__init__`之前执行

此时打印一下p的类型: `print(type(p))`

此时控制台的输出为 `<class '__main__.Person'>`

再增加一个新的类

```python
class Dog:
    def run(self):
      	print("dog run")
        
# 并修改Person类中的__new__方法
def __new__(cls, *args, **kwargs):
  	print("new方法运行")
    return Dog()
```

这时候控制台打印的p的类型为`<class '__main__.Dog'>`

调用`p.run()`控制台输出为`dog run`

结论: ==这个`__new__`方法是真正决定我们要实例化哪个类, 决定了对象的数据类型, 它的生命周期要有印象==

> `object.__new__(cls[,...])`
>
> ​		Called to create a new instance of class cls. `__new__()`is a static method (special-cased so you need not declare it as such) that takes the class of which an instance was requested as its first argument. The remaining arguments are those passed to the object constructor expression (the call to the class). The return value of `__new__()` should be the new object instance (usually an instance of cls).
>
> ​		Typical implementations create a new instance of the class by invoking the superclass’s `__new__()` method using `super().__new__(cls[, ...])` with appropriate arguments and then modifying the newly-created instance as necessary before returning it.
>
> ​		If `__new__()` is invoked during object construction and it returns an instance or subclass of cls, then the new instance’s `__init__()` method will be invoked like `__init__(self[, ...])`, where self is the new instance and the remaining arguments are the same as were passed to the object constructor.
>
> ​		If `__new__()` does not return an instance of cls, then the new instance’s `__init__()`method will not be invoked.
>
> ​		`__new__()` is intended mainly to allow subclasses of immutable types(like int, str, or tuple) to customize instance creation. It is also commonly overridden in custom metaclasses in order to customize class creation.
>
> `object.__init__(self[, ...])`
>
> ​		Called after the instance has been created (by `__new__()`), but before it is returned to the caller. The arguments are those passed to the class constructor expression. If a base class has an `__init__()`method, the derived class’s `__init__()` method, if any, must explicitly call it to ensure proper initialization of the base class part of the instance; for example: `super().__init__([args...])`
>
> ​		Because `__new__()` and `__init__()` work together in constructing objects(`__new__()` to create it, and `__init__()` to customize it), no non-None vlaue may be returned by `__init__()`;  doing so will cause a TypeError to be raised at runtime.
>
> `object.__del__(self)`
>
> Called when the instance is about to be destroyed. This is also called a finalizer or (improperly) a destructor. If a base class has a `__del__()`, the derived class’s `__del__()` method, if any, must explicitly call it to ensure proper deletion of the base class part of the instance.
>
> It is possilbe (though not recommended!) for the `__del__()` method to postpone destruction of the instance by creating a new reference to it. This is called object resurrection. It is implementation-dependent whether `__del__()`is called a second time when a resurrected object is about to be destroyed; the current CPython implementation only calls it once.
>
> It is not guaranteed that `__del__()`methods are called for objects that still exist when the interpreter exits.
>
> Note: `del x` doesn’t directly call `x.__del__()` —  the former decrements the reference count for `x` by one, and the latter is only called when `x`’s reference count reaches zero.
>
> CPython implementation detail: 
>
> It is possible for a reference cycle to prevent the reference count of an object from going to zero. In this case, the cycle will be later detected and deleted by the cyclic garbage collector. A common cause of reference cycles is when an exception has been caught in a loval variable. The frame’s local s then reference the exception, which references its own traceback, which references the locals of all frames caught in the traceback.
>
> Warning: 
>
> Due to the precarious circumstances under which `__del__()` methods are invoked, exceptions that occur during their execution are ignored, and a warning is printed to `sys.stderr` instead. In particular:
>
> * `__del__()` can be invoked when arbitrary code is being executed, including from any arbitrary thread. If `__del__()` needs to take a lock or invoke any other blocking resource, it may deadlock as the resource may already be taken by the code that gets interrupted to execute `__del__()`
> * 



然后来看`__call__`:

```python
# 将之前__new__方法返回的dog改回返回父类的new方法
def __new__(cls, *args, **kwargs):
  	print("new方法运行")
    return object.__new__(Person)

p = Person()
# 在最后调用p(1)
p(1)
```

控制台输出为: `new方法运行, 构造函数运行, call方法运行, 析构函数 del方法运行`

那么`p(1)`具体是怎么调用的?(就是像方法一样被调用)

把`p=Person()`, `p(1)`注释掉,还可以有另外一种方法进行调用,就是把类当成一个具体函数调用.

```python
Person(1)  # 在这传参数是调用构造函数, (在这构造函数的入参里补充一个name)
# 上面的这句话 控制台会输出 new方法运行 构造函数运行 析构函数 del方法运行

# 如果写成下面的形式,相当于之前的p(1)
Person(1)(2)
# 上面的这句话 控制台会输出 new方法运行 构造函数运行 call方法运行 析构函数 del方法运行
```

总结: ==`__call__`方法可以让类像一个变量来进行使用, 就是直接在类后边添加参数,这个时候`__call__`方法将被自动调用.==

我们使用一个函数的时候就是往里面传参数, 把类像一个函数来使用就是`__call__`方法的一个被调用的生命周期.

> 一个对象实例可以有自己的属性和方法, 当我们调用实例方法时, 我们用`instance.method()`来调用. 能不能在实例本身上调用呢? 
>
> 任何类, 只需要定义一个`__call__()`方法, 就可以直接对实例进行调用
>
> ```python
> class Student:
>   	def __init__(self, name):
>       	self.name = name
>     
>     def __call__(self):
>       	print('My name is {}'.format(self.name))
> ```
>
> 调用方式如下:
>
> ```python
> >>> s = Student('Michale')
> >>> s()
> My name is Michael
> ```
>
> `__call__`还可以定义参数. 对实例进行直接调用就好比对一个函数进行调用一样, 所以你完全可以把对象看成函数, 把函数看成对象, 因为这两者本来就没啥根本的区别.
>
> 如果把对象看成函数, 那么函数本身其实也可以在运行期动态创建出来, 因为类的实例都是运行期创建出来的, 这么一来, 我们就模糊了对象和函数的界限.
>
> 那么, 怎么判断一个变量是对象还是函数呢? 其实, 更多的时候, 我们需要判断一个对象是否能被调用, 能被调用的对象就是一个Callable对象, 比如函数和我们上面定义的带有`__call__()`的类的实例. 通过callable()函数, 我们就可以判断一个对象是否是“可调用”对象.

### 6-3 WebDriverWait的源代码解读

本小节主要来分析一下

```python
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
```

这句话.

首先来看一下`WebDriverWait`, `WebDriverWait`接受很多参数, 最常用的就是driver和timeout. 进入到`WebDriverWait`的构造方法中查看各个参数的说明.

然后看`until`方法,`until`方法中传入一个method和message, 它会去运行这个方法, 具体体现在这句:

```python
value = method(self._driver)
```

然后查看`self._driver`, 定位到

```python
self._driver = driver    # driver就是在WebDriverWait的构造函数中传进来的driver
```

那么`method`我们是怎么传的呢? 就是通过`EC.presence_of_element_located(locator)`

进入到`presence_of_element_located`这个方法查看:

```python
class presence_of_element_located(object):
    def __init__(self, locator):
        self.locator = locator
        
    def __call__(self, driver):
        return _find_element(driver, self.locator)
```

所以真正运行的是`__call__`方法.

这个方法结合看就是: `EC.presence_of_element_located(locator)`实例化一个类, 得到一个实例, 这个实例作为until方法的`method`传入, 然后调用这个实例(由`value = method(self._driver)`), 所以就调用了`presence_of_element_located`类下的`__call__`方法, 传入driver, 然后继续调用`_find_element`. 所以说`EC.presence_of_element_located`是一个定位条件, 而实例化这个条件的参数是某个元素的locator, 并不是传入某个元素.

### 补充: [Selenium 官网关于Waits的说明](https://www.selenium.dev/documentation/en/webdriver/waits/)

WebDriver can generally be said to have a blocking API. Because it is an out-of-process library that instructs the browser what to do, and because the web platform has an intrinsically asynchronous nature, WebDriver does not track the active, real-time state of the DOM. This comes with some challenges that we will discuss here.

An example could be that the user instructs the browser to navigate to a page, then gets a no such element error when trying to find an element.

The WebDriver instructions might look innocent enouth:

```python
driver.navigate("file://race_condition.html")
el = driver.find_element(By.TAG_NAME, "p")
assert el.text == "Hello from JavaScript!"
```

The issue here is that the default <u>**page load strategy**</u> used in WebDriver listens for the `document.readyState` to change to `"complete"` before returning from the call to navigate. Because the `p` element is added after the document has completed loading, this WebDriver script might be intermittent. It “might” be intermittent because no guarantees can be made about elements or events that trigger asynchronously without explicitly waiting — or blocking — on those events.

Fortunately, the normal instruction set available on the WebElement interface—such as WebElement.click and WebElement.sendKeys—are guaranteed to by synchronous, in that the function calls will not return (or the callback will not trigger in callback-style languages) until the command has been completed in the browser. The advanced user interaction APIs, Keyboard and Mouse, are exceptions as they are explicitly intended as “do what I say” asynchronous commands.

Waiting is having the automated task execution elapse a certain amount of time before continuing with the next step.

To overcome the problem of race conditions between the browser and your WebDriver script, most Selenium clients ship with a wait package. When employing a wait, you are using what is commonly referred to as an explicit wait.

#### Explicit wait

Explicit waits are available to Selenium clients for imperative, prodedural languages. They allow your code to halt program execution, or freeze the thread, until the condition you pass it resolves. The condition is called with a certain frequency until the timeout of the wait is elapsed. This means that for as long as the condition returns a falsy value, it will keep trying and waiting.

Since explicit waits allow you to wait for a condition to occur, they make a good fit for synchronising the state between the browser and its DOM, and your WebDriver script.

To remedy our buggy instruction set from eariler, we could employ a wait to have the *findElement* call wait until the dynamically added element from the script has been added to the DOM:

```python
from selenium.webdriver.support.ui import WebDriverWait
def document_initialised(driver):
    return driver.execute_script("return initialised")

driver.navigate("file://race_condition.html")
WebDriverWait(driver).until(document_initialised)
el = driver.find_element(By.TAG_NAME, "p")
assert el.text == "Hello from JavaScript!"
```

<u>We pass in the condition</u> as a function reference that the wait will run repeatedly <u>until its return value is truthy</u>.(划线的部分是主体, 是说, 我们传入的条件是一个函数, wait将会反复执行这个函数直到这个函数的返回值是truthy, its指的是这个函数) A “truthful” return value is anything that evalutes to boolean true in the language at hand, such as a string, number, a boolean, an object(including a WebElement), or a populated(non-empty) sequence or list. That means an empty list evaluates to false. ==When the condition is truthful and the blocking wait is aborted, the return value from the condition becomes the return value of the wait.==(当传入的等待条件为真, 就不再继续等待了, 等待条件的返回值就变成了wait的返回值)

With this knowledge, and because the wait utility ignores *no such element* errors by default, we can refactor our instructions to be more concise:

```python
from selenium.webdriver.support.ui import WebDriverWait

driver.navigate("file://race_condition.html")
el = WebDriverWait(driver).until(lambda d: d.find_element_by_tag_name("p"))
assert el.text == "Hello from JavaScript!"
```

In that example, we pass in an anonymour function(but we could also define it explicitly as we did earlier so it may be reused). The first and only argument that is passed to our condition is always a refernece to our driver object, WebDriver(called `d` in the example). ==In a multi-threaded environment, you should be careful to opreate on the driver reference passed in to the condition rather than the reference to the driver in the outer scope.==

Because the wait will swallow no such element errors that are raised when the element is not found, the condition will retry until the element is found. Then it will take the return value, a WebElement, and pass it back through to our script.

If the condition fails, e.g. a truthful return value from the condition is never reached, the wait will throw/raise an error/exception called *timeout error*.

#### Options

The wait condition can be customised to match your needs. Sometimes it is unnecessary to wait the full extent of the default timeout, as the penalty for not hitting a successful condition can be expensive.(这里的意思就是不需要等待默认的超时事件长度, 可以自己定义一个超时的时间)

The wait lets you pass in an argument to override the timeout:

```python
WebDriverWait(driver, timeout=3).until(some_condition)
```

#### Expected conditions

Because it is quite a common occurrence to have to synchronise the DOM and your instructions, most clients also come with a set of predefined expected conditions. As might be obvious by the name, they are conditions that are predefined for frequent wait opreations.

The conditions available in the different language bindings vary, but this is a non-exhaustive list of a few:

* alert is present
* element exists
* element is visible
* title contains
* title is
* element staleness
* visible text

You can refer to the API documentation for each client binding to find an exhaustive list of expected conditions:

#### Implicit wait

There is a second type fo wait that is distinct from explicit wait called implicit wait. By implicitly waiting, WebDriver polls the DOM for a certain duration when trying to find any element. This can be userful when certain elements on the webpage are not available immediately and need some time to load.

Implicit waiting for elements to appear is disabled by default and will need to be manually enabled on a per-session basis. ==Mixing expllicit waits and implicit waits will cause unintended consequences, namely waits sleeping for the maximum time even if the element is available or condition is true.==

Warning: Do not mix implicit and explicit waits. Doing so can cause unpredictable wait times. For example, setting an implicit wait of 10 seconds and an explicit wait of 15 seconds could cause a timeout to occur after 20 seconds.

<u>An implicit wait is to tell WebDriver to poll the DOM for a certain amount of time when trying to find an element or elements if they are not immediately available.</u> The default setting is 0, meaning disabled. Once set, the implicit wait is set for the life of the session.

```python
driver = Firefox()
driver.implicitly_wait(10)
driver.get("httpo://somedomain/url_that_delays_loading")
my_dynamic_element = driver.find_element(By.ID, "myDynamicElement")
```

#### FluentWait

FluentWait instance defines the maximum amount of time to wait for a condition, as well as the frequency with which to check the condition.

Users may configure the wait to ignore specific types of exceptions whilst waiting, such as NoSuchElementException when searching for an element on the page.

(也就是说FluentWait除了定义了超时时间, 还定义了轮询条件的时间间隔, 还可以配置特定的想要忽略的异常, 其实也就是比显示等待多了这两个参数)

```python
driver = Firefox()
driver.get("http://somedomain/url_that_delays_loading")
wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div")))
```

### 补充: [Selenium 官网关于Page loading strategy的说明](https://www.selenium.dev/documentation/en/webdriver/page_loading_strategy/)

Defines the current session’s page loading strategy. By default, when selenium WebDriver loads a page, it follows the normal pageLoadStrategy. It is always recommended to stop downloading addtional resources(like images, css, js)when the page loading takes lot of time.

The document.readyState property of a document describes the loading state of the current document. By default, WebDriver will hold off on responding to a driver.get() or driver.navigate().to() call until the document ready state is complete.

In SPA applications(like Angular, Recat, Ember) once the dynamic content is already loaded(i.e. the pageLoadStrategy status is COMPLETE), clicking on a link or performing some action within the page will not make a new request to the server as the content is dynamically loaded at the client side without a pul page refresh.

SPA applications can load many views dynamically without any server requests, so page load strategy will always show COMPLETE status until we do a new `driver.get()` and `driver.navigate().to()`

WebDriver page load strategy supports the following values:

#### normal

This will make Selenium WebDriver to wait for the entire page is loaded. When set to normal, Selenium WebDriver waits until the `load` event fire is returned.

By default normal is set to browser if none is provided.

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.page_load_strategy = 'normal'
driver. = webdriver.Chrome(options=options)
# Navigate to url
driver.get("http://www.google.com")
driver.quit()
```

#### eager

This will make Selenium WebDriver to wait until the initial HTML document has been completely loaded and parsed, and discards loading of stylesheets, images and subframes. When set to **eager**, Selenium WebDriver waits until `DOMContentLoaded` event fire is returned.

```python
from selenium import Webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=options)
driver.get("http://www.google.com")
driver.quit()
```

#### none

When set to **none** Selenium WebDriver only waits until the initial page is downloaded.

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.page_load_strategy = 'none'
driver = webdriver.Chrome(options=options)
driver.get("http://www.google.com")
driver.quit()
```

### 补充: robotframework Wait Until Keyword Succeeds

#### 官网: [Wait Until Keyword Succeeds](https://robotframework.org/robotframework/latest/libraries/BuiltIn.html)

argument: retry, retry_interval, name, *args

文档:

Runs the specified keyword and retries if it fails.

`name` and `args` define the keyword that is executed similarly as with <u>*Run Keyword*</u>. How long to retry running the keyword is defined using `retry` argument either as timeout or count. `retry_interval` is the time to wait before trying to run the keyword again after the previous run has failed.

If `retry` is given as timeout, it must be in Robot Framework’s time format(e.g. `1 minute`, `2 min 3 s`, `4.5`) that is explained in an appendix of Robot Framework User Guide. If it is given as count, it must have times or x post ifx (e.g. 5 times, 10 x). retry_interval must always be given in Robot Framework’s time format.

If the keyword does not succeed regardless of retries, this keyword fails. If the executed keyword passes, its return value is returned.

Examples:

| Wait Until Keyword Succeeds | 2 min                       | 5 sec | My keyword | arugment   |
| --------------------------- | --------------------------- | ----- | ---------- | ---------- |
| ${result} =                 | Wait Until Keyword Succeeds | 3x    | 200ms      | My Keyword |

All normal failures are caught by this keyword. Errors caused by invalid syntax, test or keyword timeouts, or fatal exceptions (caused e.g. by *<u>Fatal Error</u>*) are not caught.

Running the same keyword multiple times inside this keyword can create lots of output and considerably increase the size of the generated output files. It is possible to remove unnecessary keywords from the outputs using `--RemoveKeywords WUKS` command line option.

#### [Robot Framework自动化测试用具 Wait Until Keyword Succeeds关键字使用案例](https://blog.csdn.net/qq_33163046/article/details/102682801)

在对批量测试用例进行测试的时候，往往会不知道这个用例到底执行多久结束。绝大多数情况下，含有某个关键词的日志打印出来可以对应着某个用例的流程结束。

如果用sleep ns方法等待执行结束，我们不得不采用放大执行时间的方法来保障在机器比较卡的时候也能执行完流程。如果可以实时监测结果日志是否出现，便可以大大降低批量测试用例实行的总时间。RF可以使用Wait Until Keyword Succeeds关键字实现我们的需要。

语法： Wait Until Keyword Succeeds| timeout, retry_interval, name, *args

解释：



## 第7章 对象关系映射与model的封装

### 7-1 类的创建与动态创建

简单来介绍一下model的封装最后的效果: 现在连接数据库的时候都是直接写一些sql语句,学习完本章以后,大家以后在连接数据库的时候把底层架构封装完毕之后,咱们就正常来写一个类,直接调用里面的比如`insert`方法, `select`方法就可以完成对数据库的操作,以后不用写sql语句, 达到了这样的一个效果.

对象关系映射,要从Python基础知识的元类开始说起. 讲元类要先讲类的一个由来.

新建包`part_seven`, 新建`my_metaclass.py`

```python
"""
按照 类 元类的由来 类的创建 类的动态创建 这个脉络梳理下来
首先有一个类
"""
class Person:
  	pass
"""这样就完成了一个类的基本书写"""

# 1.类的特性
print(Person)        # 我们可以把这个类打印一下
p = Person			 # 也可以把类赋值给一个变量
print(p)			 # 和上面 print(Person) 的打印结果一样
p.name = "张三"	    # 还可以给类赋上一个属性
print(p.name)        

# 还可以当作一个参数来传递
def func(p):
  	print(p.name)

func(p)			# 调用这个函数, 打印结果是 张三

# 2.动态的创建一个类 第一种方式
def get_class(name):
  	if name == "dog":
      	class Dog:
          	def run(self):
              	print("dog run")
        return Dog	# 这里返回的是类而不是类的实例
    else:
      	class Cat:
          	def run(self):
              	print("cat run")
		return Cat

c = get_class("dog")
print(c)		# 打印结果为 <class '__main__'.get_class.<locals>.Dog'>
c.run(c)		# 这里要把c传进去才能调用c.run()  这里相当于是把类传给self参数
				# 打印结果为dog run.
    			# 这也就证明我们用get_class
c = get_class("c")
print(c)		# 打印结果为 <class '__main__'.get_class.<locals>.Cat'>
c.run(c)		# 打印结果为cat run

# 动态创建类的第二种方式

# type 之前用来观察数据的数据类型
print(type(1))		# <class 'int'>
print(type("aaa"))	# <class 'str'>

# 使用type来动态构造一个类
print(c)		# 打印结果为 <class '__main__.get_class.<locals>.Cat'>
print(type(c))		# 打印结果为 <class 'type'>

Person2 = type('Person2', (), {})  # type里接受这样几个参数:Person2是类的名字, 第二个是这个类要继承哪些父类, 第三个是它的属性(包括它里面有哪些方法和变量值) 为了验证这个结果,进入到type的源代码中查看, 查案具体的__init__构造方法的注释
print(Person2)   # <class '__main__.Person2'> 说明type给我们创建了一个类Person2
p2 = Person2()
print(p2)		# <__main__.Person2 object at 0x.....> 说明Person2可以被实例化

# 如何用type构建的方式给类加上一些属性

# 之前给类增加属性的方法
class Person3:
  	name = "张三"

# 使用type给类增加属性的方式 
Person3 = type('Person3', (), {'name': "李四"})
print(Person3.name)			# 打印结果为 李四, 说明属性添加成功

# 继承的相关
Person4 = type('Person4', (Person3,), {})
print(Person4.name)    # 打印结果: 李四

# 增加方法
def person4_run():
  	print("person4 run")

Person4 = type('Person4', (Person3,), {'person4_run': person4_run})
p = Person4()
p.person4_run()  # 这里会报错: person4_run() takes 0 positional arguments but 1 was given

# 重新定义person4_run
def person4_run(self):
  	print("person4 run")

Person4 = type('Person4', (Person3,), {'person4_run': person4_run})
p = Person4()
p.person4_run()		# 打印出person4 run
```

#### 1014自测结果

```python
# 1，类有哪些特性
# 1. 可以被赋值
# 2. 可以实例化
# 3. 可以作为参数传递

# 2. 动态创建类的两种方式
def dynamic_create(name):
    if name == "Dog":
        class Dog:
            def run(self):
                print("Dog run")

        return Dog
    else:
        class Cat:
            def run(self):
                print("Cat run")

        return Cat


# D = dynamic_create("Dog")
# print(D)
# d = D()
# print(D.run(D))
# print(d.run())

Person = type("Person", (), {})
print(Person)
p = Person()
print(p)
```



### 7-2 使用元类来构建一个类

元类: 类创造实例, 元类是用来创造类的

(通过修改`type`函数中的`bases`(去掉括号)引起的报错信息来引入`type`类的`__new__`方法)

```python
class MyMetaclass(type):
  	
    def __new__(cls, name, bases, attrs):
      	print("元类new方法运行")
        print(name)
        print(bases)
       	attrs['add'] = lambda self, value: value + value
        print(attrs)
        # 下边这一行调用type方法来动态的构建类
        return type.__new__(cls, name, bases, attrs)
    
class MyClass(Person4, metaclass=MyMetaclass):
  	# 上边的metaclass=MyMetaclass 就指定了使用MyMetaclass来定制类(说是定制类是因为attrs中可以随	  #	意加东西)
    # 就是通过type.__new__来创建的
    
my_class = MyClass()
r = my_class.add(2)
print(r)		# 结果是4
```

创建元类的时候必须要继承自`type`类.

#### 1023自测结果

```python
class MyMetaclass(type):

    def __new__(cls, name, bases, attrs):
        print("cls 是 {}".format(cls))
        print("name 是 {}".format(name))
        print("bases 是 {}".format(bases))
        attrs['add'] = lambda self, value: value + value
        print("attrs 是 {}".format(attrs))
        return type.__new__(cls, name, bases, attrs)


class MyClass(metaclass=MyMetaclass):
    pass


my_class = MyClass()
result = my_class.add(2)
print(result)

# 打印结果为
# cls 是 <class '__main__.MyMetaclass'>
# name 是 MyClass
# bases 是 ()
# attrs 是 {'__module__': '__main__', '__qualname__': 'MyClass', 'add': <function  MyMetaclass.__new__.<locals>.<lambda> at 0x7f8aa78d6950>}
# 4
```

基本没有什么问题, 原课程中没有打印`cls`

### 7-3 数据库连接池的创建与环境隔离配置的写法

先创建一个`model.py`, 我们想要达到的效果:

```python
class Goods:		# 数据库里的表名
  	computer_part = ""    # 数据库里的字段
    computer_info = ""
    
goods = Goods()
goods.insert("")
```

`Goods`就是数据库里面的那个表名,然后表里边有两个字段, 一个叫`computer_part`(具体内容先空起来用“”代替), 一个叫`computer_info`,再实例化这样一个类,然后这里边就提供一个`goods.insert`, 就可以在里面加上我要插入的参数. 运行代码,数据就自动写入到数据库里了.

首先写数据库连接. 

一般来说我们写应用程序要有一个环境上的区分,就是不同的环境调不同的配置, 我们可以来一个非常简单的写法:

新建包`config`, 这里面放的全都是配置文件. 再在`config`下新建`mysql_config.py`

```python
def set_mysql_config(env):
  	if env == 'dev':
      	db_config = {
          	'host': '192.168.1.35',
          	'user': 'admin',
          	'passwd': '123456',
          	'db': 'python_ui',
          	'port': 3306,
          	'charset': 'utf8'
        }
    if env == 'pro':
      	db_config = {
          	'host': '192.168.1.35',
          	'user': 'admin',
          	'passwd': '123456',
          	'db': 'python_ui',
          	'port': 3306,
          	'charset': 'utf8'
        }
    return db_config
```

这样就实现了环境的配置隔离.

在`part_seven`下创建`my_database.py`,真正去连接数据库

```python
import pymysql
from DBUtils.PooledDB import PooledDB
from part_seven.config.mysql_config import set_mysql_config

def create_pool():
  	db_config = set_mysql_config("dev")
    return PooledDB(pymysql,  # 代表用谁来创建这个连接池
                    5,	# 初始化缓存的最小线程数
                    host=db_config['host'],
                   	port=db_config['port'],
                    user=db_config['user'],
                    passwd=db_config['password'],
                   	db=db_config['db'],
                   	charset=db_config['charset']).connection()
```

注意最后必须加上`.connection()`才能连接上数据库, 并且把连接池返回回去

关于`PooledDB`的参数如何书写, 需要查看`PooledDB.py`的源代码, 包括`creator`, `mincached`等.

#### 1025自测结果

```python
def set_mysql_config(env):
    if env == "test":
        db_config = {
            "host": "localhost",
            "port": 3306,
            "user": "root",
            "passwd": "sx22019891",
            "db": "python_ui",
            "charset": "utf8"
        }
    if env == "prod":
        db_config = {
            "host": "localhost",
            "port": 3306,
            "user": "root",
            "passwd": "sx22019891",
            "db": "python_ui",
            "charset": "utf8"
        }
    return db_config


from dbutils.pooled_db import PooledDB
import pymysql
from part_7.config.mysql_config_1025 import set_mysql_config


def create_pool():
    db_config = set_mysql_config("test")
    return PooledDB(pymysql,
                    5,
                    host=db_config['host'],
                    port=db_config['port'],
                    user=db_config['user'],
                    passwd=db_config['passwd'],
                    db=db_config['db'],
                    charset=db_config['charset']).connection()

```



### 7-4 Field类开发

`computer_part`和`computer_info`这两个“字段”要映射到`Field`类上(要达成下面的效果):

```python
class Goods:
  	computer_part = Field("computer_part")
    computer_info = Field("computer_info")
    
goods = Goods()
```

要达成的效果就是类中的属性对应的就是数据库中的`Field(“具体字段名”)`的字段, 把它给连接起来.

新建一个`field.py`

```python
# 定义Field类,用来保存数据库表的字段名称和字段类型
class Field:
  	
    def __init__(self, column_name, column_type):
      	self.column_name = column_name
        self.column_type = column_type
```

在model里补一下

```python
from part_seven.field import Field

class Goods:
  	computer_part = Field("computer_part", "varchar(200)")
    computer_info = Field("computer_info", "text")
    
goods = Goods()
```

另外的写法:

```python
class StringField(Field):
  	def __init__(self, column_name):
      	super().__init__(column_name, "varchar(200)")
        
class IntegerField(Field):
  	def __init__(self, column_name):
      	super().__init__(column_name, "bigint")
        
class TextField(Field):
  	def __init__(self, column_name):
      	super().__init__(column_name, "text")
        
class Goods:
  	computer_part = StringField("computer_part")
    computer_info = TextField("computer_info")
```

#### 1101自测结果

```python
class Field:
    def __init__(self, column_name, column_type):
        self.column_name = column_name
        self.column_type = column_type


class StringField(Field):
    def __init__(self, column_name):
        super(StringField, self).__init__(column_name, "varchar(200)")


class TextField(Field):
    def __init__(self, column_name):
        super(TextField, self).__init__(column_name, "text")

```

没有写IntegerField, 因为id字段也没有用到.

### 7-5 Model 元类的开发

本节进入到对象关系映射的开发

新建`orm.py`

```python
from part_seven.field import Field
from part_seven.my_database import create_pool

# 定义元类, 控制model对象的创建
class ModelMetaclass(type):
  	"""
  	关于参数
  	table_name: 类名, 也就是对应数据库中的表名
  	bases: 父类的元组
  	attrs: 类的属性方法和值组成的键值对
  	"""
    def __new__(cls, table_name, bases, attrs):
      	if table_name == "Model":
          	return super(ModelMetaclass, cls).__new__(cls, table_name, bases, attrs)
        # mappings用来保存属性和列的映射关系
        mappings = dict()
        for k, v in attrs.items():
          	# 保存类属性和列的映射关系到mappings字典中
            if isinstance(v, Field):
              	mappings[k] = v	# 这个mappings就存放了 属性名称: 字段类型, 列名
        for k in mappings.keys():
          	# 将类的属性移除,使得定义的类字段不污染User的类属性
            # 也就是说只有在实例中才可以访问这些key
            # 就是类名.属性名称不可以调用
          	attrs.pop(k)
        # 把表名转换为小写, 也就是那个类名要变成小写
        # 并且要添加一个__table__属性, 来表示属性中存储的表名
        attrs['__table__'] = table_name.lower()
        
        # 保存属性和列的映射关系
        attrs['__mappings__'] = mappings
        
        return super(ModelMetaclass, cls).__new__(cls, table_name, bases, attrs)
        
```

#### 1102自测结果

```python
from part_7.field_1015 import Field


class ModelMetaclass(type):
    def __new__(cls, table_name, bases, attrs):
        if table_name == "Model":
            return type.__new__(cls, table_name, bases, attrs)
        mappings = {}
        for k, v in attrs.items():
            if isinstance(v, Field):
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        return type.__new__(cls, table_name, bases, attrs)
```

##### 存在的问题

1. 忘记在`attrs`中添加属性：`__table__`, `__mappings__`

### 7-6 Model子类开发, 实现insert方法

继续在`orm.py`中编写`Model`类

```python
# 编写一个model子类(基类), 这个类用于被具体的model对象继承
# 由它来实现具体的增删改查方法
# 基于面向对象中三大特性的继承规则, 那么以后每一个model类的实现都有了这些方法

class Model(dict, metaclass=ModelMetaclass):
  	def __init__(self, **kwargs):
      	super(Model, self).__init__(**kwargs)
    
    # insert语法: insert into table_name (字段名称) values(值)    
    def insert(self, column_list, param_list):
      	print("执行了insert方法")
        fields = []
        for k, v in self.__mappings__.items():
          	fields.append(k)
        for key in column_list:
          	if key not in fields:
              	raise RuntimeError("这个字段没有发现")
    
        # 检查参数的合法性	"va"lue"
        args = self.__check_params(param_list)
        sql = 'insert into %s (%s) values (%s)' % 
              (self.__table__, ','.join(column_list), ','.join(args))
        res = self.__do_execute(sql)
        print(res)
    
    
    def __check_params(self, param_list):
      	args = []
        for param in param_list:
          	#	如果参数中包含双引号,全部换成字符串双引号, 防止sql注入
            if "\"" in param:
              	param = param.replace("\"", "\\\"")
            # 自己在参数的两边加上双引号
            param = "\"" + param + "\""
            args.append(param)
        return args
      
	def __do_execute(self, sql):
      	conn = create_pool()
        cur = conn.cursor()
        print(sql)
        rs = cur.execute(sql)
        conn.commit()
        cur.close()
        return rs
```

在拼接sql的时候为什么不是传的`fields`而是`column_list`:

```python
sql = 'insert into %s (%s) values (%s)' % 
              (self.__table__, ','.join(column_list), ','.join(args))
```

假设有两种情况, 有一种情况字段不能为空, 但是用户写的时候想增加他的自由度, 那么可以写fields,然后自己拼接的时候把那些值带上默认的,或者有的时候数据库里会给带上默认的那种情况, 但是需要你自己做些判断了.

如果是像当前这种写法:

```python
fields = []
for k, v in self.__mappings__.items():
    fields.append(k)
```

`fields`在后面用处就不是很大,它只是代表了它里边一共有多少个key. 



#### 1007 自测结果

```python
from part_7.orm_1007 import ModelMetaclass
from part_7.my_mysql_connection import create_pool


class Model(dict, metaclass=ModelMetaclass):
    # insert into table_name (column_list) values (args_list)
    def insert(self, column_list, args_list):
        sql = 'insert into {} ({}) values ({})'.format(
            self.__table__,
            ','.join(column_list), ','.join(args_list))
        print(sql)
        conn = create_pool()
        cur = conn.cursor()
        rs = cur.execute(sql)
        return rs


# 在定义Model类的时候，完全没有方向。
# 1. 没有写构造方法
# 2. 没有对字段做健壮性检查
# 3. 没有检查参数的合法性
# 4. 应该把执行sql的操作抽象出来成为一个函数
```



### 7-7 Debug调试插入数据流程

前面已经把相关内容写好了:

```python
class Goods(Model):
  	computer_part = Field("computer_part", "varchar(200)")
    computer_info = Field("computer_info", "text")
    
goods = Goods()
goods.insert(["computer_part", "computer_info"], ["组件", "组件信息"])
```

运行这个脚本, 然后在数据库中查看, 发现新增了一条“组件”“组件信息”的数据

以debug方式运行,在orm的每个 方法都入口处都打上断点

### 7-8 实现查询、修改和删除方法

继续在`orm.py`中添加方法:

```python
def select(self, column_list, where_list):
  	print("调用select方法")
    # 把where_list再次传到args列表里的意义: 如果参数传递错误, 可以准确定位到是哪里的错误
    args = []  
    fields = []
    for k, v in self.__mappings__.items():
      	fields.append(k)
    for key in where_list:
      	args.append(key)
    for key in column_list:
      	if key not in fields:
          	raise RuntimeError("field not found")
    sql = 'select %s from %s where %s' % 
    			(','.join(column_list), self.__table__, ' and '.join(args))
    res = self.__do_execute(sql)
    return res


# 修改__do_execute方法, 增加select的判断
def __do_execute(self, sql):
  	conn = create_pool()
    cur = conn.cursor()
    print(sql)
    if "select" in sql:
      	cur.execute(sql)
        rs = cur.fetchall()
    else:
      	rs = cur.execute(sql)
    conn.commit()
    cur.close()
    return rs

  
def update(self, set_column_list, where_list):
    print("调用update方法")
    args = []
    fields = []
    for key in set_column_list:
        fields.append(key)
    for key in where_list:
        args.append(key)
    for key in set_column_list:
          if key not in fields:
              raise RuntimeError("field not found")

    sql = 'update %s set %s where %s' % 
          (self.__table__, ','.join(set_column_list), ' and '.join(args))
    res = self.__do_execute(sql)
    return res


def delete(self, where_list):
  	print("调用删除方法")
    args = []
    for key in where_list:
      	args.append(key)
    sql = 'delete from %s where %s' % (self.__table__, ' and '.join(args))
    res = self.__do_execute(sql)
    return res
```

#### 1009自测结果

```python
def select(self, column_list, where_list):
    print("执行select方法")
    fields = []
    for k in self.__mapppings__.keys():
        fields.append(k)
    for key in column_list:
        if key not in fields:
            raise RuntimeError("field not found")
    sql = "select {} from {} where {}".format(','.join(column_list),
                                              self.__table__,
                                              ' and '.join(where_list))
    rs = self.__do_execute(sql)
    return rs

@staticmethod
def __do_execute(sql):
    conn = create_pool()
    cur = conn.cursor()
    print(sql)
    if "select" in sql:
        cur.execute(sql)
        rs = cur.fetchall()
    else:
        rs = cur.execute(sql)
    conn.commit()
    cur.close()
    return rs

def update(self, where_list):
    print("执行update方法")
    sql = "update {} set {}".format(self.__table__, ' and '.join(where_list))
    rs = self.__do_execute(sql)
    return rs

def delete(self, where_list):
    print("执行delete方法")
    sql = "delete from {} where {}".format(self.__table__, ' and '.join(where_list))
    rs = self.__do_execute(sql)
    return rs
```

##### 存在的问题

1. 没有把`where_list`存到内置的`args`列表里, `select`, `update`和`delete`方法都需要写
2. `update`方法缺少`set_column_list`参数

### 7-9 方法的测试和重写数据存储

在`model.py`中新增:

```python
result = goods.select(["computer_part", "computer_info"], ["computer_part='组件'"])
print(result)
# 得到结果 (('组件', '组件信息'),)
```

然后执行

```python
goods.update(["computer_part='组件1'"], ["computer_part='组件'"])
```

运行, 然后查看数据库

然后把抓取京东的代码放过来,以这种方式运行

将`part_five/jingdong`复制到`part_seven`下, `part_five/remote_start_jingdong.py`也复制到`part_seven`下

修改`remote_start_jingdong.py`: 去掉启动Windows, 然后把导包的 `from part_five.jingdong` 改为 `from part_seven.jingdong`

然后在 `part_seven/jingdong/jingdong.py`的 `if __name__ == ‘__main__’`下的内容都注释掉,因为打开商品信息页面不需要登录也可以进去,  直接改为:

```python
to_goods_page(driver, name)
```

`part_seven/jingdong/my_mysql.py`下修改`save_goods_info_to_mysql`:

```python
from part_seven.model import Goods

# 新增一个new_save_goods_info_to_mysql
def new_save_goods_info_to_mysql(info_list):
  	goods = Goods()
    for info in info_list:
      	for key, value in info.items():
          	goods.insert(["computer_part", "computer_info"], [str(key), str(value)])
```

然后把`jingdong.py`中引用到`save_goods_info_to_mysql`的地方改为

`new_save_goods_info_to_mysql(result_list)`

并修改导包信息:

```python
from part_seven.jingdong.my_cookies import *
from part_seven.jingdong.my_mysql import *
```

打开`remote_start_jingdong.py`, 运行, 查看结果

## 第8章 从日志的使用到日志加载引擎的开发

### 8-1 从源代码开始入门日志的使用

首先来看一下日志基本使用,然后看一下它里面都有哪些配置,然后再写一个日志加载引擎,如何把日志从配置文件里加载出来,到应用程序里面怎么使用,最后再看看一般在python的应用程序里面大家都是怎样使用日志来配置的.

首先创建`part_eight`包,再创建`log_operation.py`: 日志的操作,就是日志的基本使用

首先导入`logging`模块

```python
import logging

# 但是一般写日志的时候我们都是这么写

# debug指调试信息,也是日志打印最详细的一个级别,用于帮助我们调试程序
logging.debug("This is debug logging")    # debug 是日志中常用的一个等级

# 常用的等级有:
# 日志详细信息, 打印的频率会比debug稍微低一些, 一般生产环境开启此日志级别
logging.info("info logging")

# 警告信息, 当程序已经发生错误,但并不影响程序的运行
logging.warning("warning logging")

# 错误信息, 已经发生错误, 影响了程序的运行
logging.error("error logging")

# logging模块默认日志等级是warning,所以上面几行的代码默认只会输出warning和error信息. 如果要修改
logging.basicConfig()

```

然后进去看`basicConfig`里的内容, 查看参数, 从`filename`, `filemode`到`format`, `datefmt`, `style`等等, 具体查看到`level`, 确定了level的含义, 这时候就可以写成:

```python
logging.basicConfig(level=)
```

但具体的值等于什么还不清楚, 继续往下查看该函数,当查看到:

```python
if level is not None:
  	root.setLevel(level)
```

然后就去跳转查看`setLevel`方法, 其中调用了`_checkLevel`方法, 并注意到方法的注释中有写: level must be an int or a str.

具体查看`_checkLevel`方法:

```python
def _checkLevel(level):
    if isinstance(level, int):
        rv = level
    elif str(level) == level:
        if level not in _nameToLevel:
            raise ValueError("Unknown level: %r" % level)
        rv = _nameToLevel[level]
    else:
        raise TypeError("Level not an integer or a valid string: %r" % level)
    return rv
```

解释:

如果level是一个整数,就把level赋值给rv, 如果level是一个字符串,继续判断level是否在`_nameToLevel`中,如果不在就会报错.现在继续进入`_nameToLevel`查看.

```python
_nameToLevel = {
    'CRITICAL': CRITICAL,
    'FATAL': FATAL,
    'ERROR': ERROR,
    'WARN': WARNING,
    'WARNING': WARNING,
    'INFO': INFO,
    'DEBUG': DEBUG,
    'NOTSET': NOTSET,
}
```

`_nameToLevel`是一个字典, 它的key是字符串, value继续点进去, 发现每个value都对应着一个数字.

如果要调试等级,那么既可以写字符串,也可以写数字.

这个时候就可以明确:

```python
logging.basicConfig(level="DEBUG")
logging.basicConfig(level=10)
```

这两种写法是等价的.

#### 1117自测结果

```python
# 1. 列举常见的日志等级
DEBUG, INFO, WARNING, ERROR

# 2. 默认情况下打印日志的等级是 warning

# 3. logging.basicConfig的三种配置等级的方式
import logging

logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level="info")
logging.basicConfig(level=30)

# 4.
```

##### 存在的问题

###  8-2 日志的多参数配置与解决中文问题

上一小节说了日志的基本使用,本小节看一看`logging`模块更多参数的应用,包括格式化的使用和中文的问题怎么办.

格式化很多时候都是一种固定的写法, 首先来看一下日志格式的格式化:

```python
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y/%m/%d %H:%M:%S"		# 日期的格式化 年月日只有年是大写,时分秒都是大写
```

`asctime`运行时时间

`levelname` 日志的等级

`message` 日志的信息

然后具体指定配置:

```python
logging.basicConfig(filename="my-first.log",
                   	level=10,
                    format=LOG_FORMAT,     # 如果指定了format但是没有指定datefmt
                   	datefmt=DATE_FORMAT)	 # 那么会把毫秒值都打印出来

logging.debug("debug info")
```

运行后控制台无输出, 当前目录新增`my-first.log`文件

将`logging.debug()`中的输出内容改为`这是debug的日志`, 运行后报错

```python
# UnicodeEncodeError: 'ascii' codec can't encode characters in position...
```

在`logging.basicConfig`中指定`encoding=‘UTF-8’`没有用因为并没有这个参数

通过查看报错信息的源代码, 查找到是`logging/__init__.py`下的994行`stream.write(msg)`报错:

如果是本地环境, 可以在write的时候添加`enconding`参数来强行指定一个字符编码

如果这里指定不了,那么必然有一个`open`的方法, 继续往上查看发现这句话隶属于`emit`方法, 其中传入了`record`方法, 然后全文查找`emit`看哪个里面会用到它, 然后在1069行 `self.stream = self._open()`, 大胆猜测一下`_open`就是调用打开本地文件的方法, 进入`_open`, 有一个`baseFilename`, `mode`, 这就是我们之前传入的文件名,写入方式,  `encoding=self.encoding` 简单粗暴的改成 `encoding=‘UTF-8’`可以解决中文的问题但是不能这么干.

回到`basicConfig`, 进到源代码里面, 它提供一个`handlers`参数, 表示最终要把日志往哪里输出. 一开始日志输出到控制台,后面又输出到文件, 现在想既输出到控制台又输出到文件, 这样的话就都可以看到.

而且既然`handlers`控制着输出流, 那是不是在这里面可以指定一些字符编码.

```python
import sys    # 输出到控制台用的

file_path = "my-second.log"
logger = logging.getLogger()  # 获取一个logger对象
logger.setLevel(logging.DEBUG)  # 到现在一共有三种指定level的方式了

# 文件日志的配置
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
fh = logging.FileHandler(file_path, encoding='utf-8')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)

# 控制台的日志配置
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

logger.info("这是我的日志信息")
```

运行的效果是: 控制台输出了, `my-second.log`中也会生成日志信息

扩展可以看一下`FileHandler`的源代码.

#### 1010自测结果

```python
LOG_FORMAT = "%(asctime)s - %(level)s - %(message)s"
DATE_FMT = "%Y-%m-%d %H:%M:%S"


import sys

logger = logging.getLogger()

filename = "my-first.log"
fh = logging.
```

##### 存在的问题


1. 日志和时间的格式化写出来了, 日志的第二个参数是levelname, 不过写成level也差不多. 一开始没有加引号, 是IDE提示报错才加的

2. 在回答第一个问题的时候, 还是没能理解具体的含义, 其实在这里已经把`basicConfig`的各个参数都已经讲过了,所以这时候就可以用`basicConfig`来配置一个日志并输出到文件:

   ```python
   logging.basicConfig(filename="my-first.log",
                      	level="DEBUG",
                      	format=LOG_FORMAT,
                      	datefmt=DATE_FMT)
   # 并用logging的信息来做验证
   ```

3. 在往文件和控制台同时输出的时候, 知道要找Handler, 但是怎么找都没找到. logger也已经生成了, 但是没有设置logger的level.

   ```python
   logger.setLevel(logging.DEBUG)
   ```

   Handler要直接在logging模块下找, 但是第一个字母是大写:

   ```python
   fh = logging.FileHandler()
   ```

   并同时指定`file_path`和`encoding`, 还要`setLevel`, `setFormatter`, 并把这个`Handler`加到logger里

   formatter的设置方式也要注意, 并不是直接写成常量了:

   ```python
   formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s ")
   ```

   控制台的写法也是如此:

   ```python
   formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
   ch = logging.StreamHander(sys.stdout)
   ch.setLevel(logging.DEBUG)
   ch.setFormatter(formatter)
   logger.addHandler(ch)
   ```


#### 1117自测结果

```python
# 1. 日志和日期的格式化
format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
datefmt = "%Y-%m-%d %H:%M:%S"

# 2. 使用basicConfig的各个参数输出
# logging.basicConfig(filename="my_basic_config_1117.log",
#                     filemode="a",
#                     format=format,
#                     datefmt=datefmt,
#                     level="debug")

# logging.info("这是输出测试")

# 3. 在控制台和文件中同时输出且输出中文
import sys

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
format = logging.Formatter(format, datefmt=datefmt)
ch = logging.StreamHandler(sys.stdout)
ch.setFormatter(format)
fh = logging.FileHandler("my_basic_file_log_1117", encoding="utf-8")
fh.setFormatter(format)
logger.addHandler(ch)
logger.addHandler(fh)

logger.info("这制次要同时输出到文件和控台，而且输出的是中文")
```

##### 存在的问题

### 8-3 日志解析引擎代码开发(1)

本小节咱们开始自己开发一个日志加载引擎.大家一般会用`properties`文件来进行配置.

创建一个新的`log.properties`, 一般都是按照如下格式进行配置:

```properties
# filename就是你要填写的日志路径及文件名称
filename = my-test.log

level=DEBUG   # 这是日志的等级设置

foramt=%(asctime)s - %(levelname)s - %(message)s
www.imooc.com = 123
```

1. 一种是`=`两边都有空格, 另外一种是按照要求`=`两边不空格
2. 注释分为两种情况: 一种是单独一行, 另外一种是写在了行末
3. 还有一种特别的情况是`www.imooc.com = 123`的配置的处理



新建`properties_utils.py`

```python
class Properties():
  	def __init__(self, file_name):
      	self.properties_file_name = file_name
        self.properties = {}
    
    def get_properties(self) -> dict:
      	"""
      	获取properties里所有的东西
      	"""
      	with open(self.properties_file_name, 'r', encoding='UTF-8') as pro_file:
          	for line in pro_file.readlines():
              	# 去掉两端的空格和\n
                line = line.strip().replace("\n", "")
                # 如果发现# , 就代表着这一行或者是它后面的内容是注释内容
                if line.find("#") != -1:  # != -1 也就是存在
                  	line = line[0:line.find("#")]
								
                # 如果包含等号, 我们就要进行字典类型的转换处理
                if line.find("=") > 0:
                  	# 我们就用等号进行切分, 形成了新的字典类型的list
                    strs = line.split("=")
                    # 获取字典
                    self.__get_dict(strs[0].strip(), self.properties, strs[1].strip())
        return self.properties
     
    def __get_dict(self, key_name, result_dict, value):
      	#首先检查key中是否包含. 包含的话我们就切分, 不包含就直接设置值
        if key_name.find(".") > 0:
          	k = key_name.split(".")[0]		# 用.切分,我拿第一个www作为一个key
            result_dict.setdefault(k, {})  # 把结果字典设置成 {www:{imooc:{com:value}}}
            return self.__get_dict(key_name[len(k)+1:], result_dict[k], value) # 递归的效果
        else:
          	result_dict[key_name] = value
```

#### 1010自测结果

```python
class Properties:
    def __init__(self, file_path):
        self.file_path = file_path
        self.properties = {}

    def get_properties(self):
        with open(self.file_path) as pro_file:
            for line in pro_file.readlines():
                # 首先排除空行的影响
                line = line.strip("\n")
                # 然后去掉注释行
                if line.find("#"):
                    # 然后取从这一行开头到发现#的位置
                # 还有等号两边的空格 去掉
                # 还有形如www.imooc.com这样的格式的处理
```

##### 存在的问题

1. 构造函数写的合格，即要传入一个properties文件，以及初始化一个字典

2. 在获取properties的时候思路不是很清晰：

  1. 在打开文件的时候最好指定一下mode和编码，就算mode不写，编码还是应该写，因为有中文

  2. 在去掉两端的空格和`\n`的时候对字符串内置方法不清晰，`strip()`方法是用来去掉两端空格的，然后换行符的去掉不是通过去掉，而是通过替换的方式，即使用`replace("\n", "")`

  3. 然后处理注释，在怎样获取从这行开头到发现#的位置的时候，写不出来

  4. 然后就是处理具体的内容了，即进行字典类型的转换，这里去掉等号两边的空格等思路不对，这属于具体转换过程中处理的内容，而且也不应该把这一行看做是整体，而是用等号进行切分后再去掉空格。

  5. 获取字典的方法没有写

  	具体思路：
  	
  	1. 在用等号进行切分后，获得到了一个包含两个元素的列表，分别取到这两个元素传给获取字典的方法
  	2. 首先还是对key的部分进行分解，value的部分没什么好说的
  	3. 判断key中是否包含.，如果包含.就以点进行切分，然后拿到第一个元素，把第一个元素放进结果字典里，并将这个元素的值设为{}
  	4. 递归调用获取字典的方法，返回的结果中，key的部分要去掉用.切分前的部分：就是`key_name[len(k)+1:]`，结果集的部分就是k的值：`result_dict[k]`,这样的话后续产生的所有结果就局限在了这个key的值里面，然后value没动 就继续传递。 
  	5. 这样切分直到key中没有`.`， 然后转到else， 把key和value绑定

#### 1013自测结果

```python
class Properties:
    def __init__(self, file_path):
        self.properties_file = file_path
        self.properties = {}

    def get_properties(self):
        with open(self.properties_file, encoding='utf-8') as f:
            for line in f.readlines():
                # 去除两端空格和换行符
                line.strip().replace("\n", "")
                # 去掉注释
                if "#" in line:
                    line = line[0: line.find("#")]
                # 使用=分割两边
                if "=" in line:
                    strs = line.split("=")
                # 检查参数合法性 "va"lue"
                value = self.do__check(strs[1])
                # 获取字典
                rs = self.__do_dict(strs[0], self.properties, value)
        return rs

    def __do_dict(self, key, result_dict, value):
        if "." in key:
            keys = key.split(".")[0]
            result_dict.setdefault(keys, {})
            return self.__do_dict(key[len(keys)+1:], result_dict[key], value)
        else:
            result_dict[key] = value


    def __do_check(self):
        pass
```

##### 存在的问题

1. `encoding`这次记得写了，但是更规范的应该是”UTF-8“？ 这个还存疑。
2. ==去掉两边的空格和换行符似乎用一句`line.strip()`就可以了，不需要`replace`==
3. ==不需要检查参数合法性，这里和orm混淆了==
4. 获取字典的方法叫`__get_dict`
5. 在递归调用的时候应该返回`result_dict[k]`
6. 获取字典的行缩进不对， 应该在“=”判断的下面，不应该和它平行
7. ==在往获取字典的方法里传参数时没有去掉参数两边的空格==
8. 在最后的时候不应该返回rs，因为`__get_dict`方法并没有返回值，我们只是把`self.properties`传给了`result_dict`, 这时候`result_dict`是我们想要的结果但并没有返回给调用者，所以rs的结果是None，所以这个时候要么是在`__get_dict`里返回`result_dict`, 要么在上一级方法中返回`self.properties`

#### 1112自测结果

```python
class Properties:
    def __init__(self, file_path):
        self.file_path = file_path
        self.properties = {}

    def get_properties(self):
        with open(self.file_path + "log.properties", "utf-8") as f:
            data = f.readlines()
            for line in data:
                # 去除两端空格

                # 去掉#后面的注释

                # 以=为分隔，获取key和value

                #
```

##### 存在的问题

1. 在构造方法传入文件路径的时候要把文件名称也直接传进去，分开传其实没什么意义，写到`get_properties`里更是写死了，更不灵活
2. 在编写`get_properties`方法的时候要始终明确，最终是要得到一个字典的。
3. ==在打开的文件中，要用`encoding`来指定编码格式，不是直接传的。==**<u>(该问题反复出现)</u>**
4. 在对每一行进行迭代的时候，可以变成一句写，不需要把`f.readlines()`返回的结果赋值给一个变量然后再for那个变量
5. 去掉两端空格和回车不会写了
6. 去掉注释不会写
7. 以=为分隔获取key和value的前提是先进行判断，先进行判断，然后获取字典

#### 1116自测结果

```python
class Properties:
    def __init__(self, properties_file_name):
        self.properties_file_name = properties_file_name
        self.properties = {}

    def get_properties(self) -> dict:
        with open(self.properties_file_name, 'r', encoding="utf-8") as f:
            for line in f.readlines():
                # 去除两端空格以及回车
                line = line.strip(" ").replace("\n", "")
                # 判断是否存在#
                if '#' in line:
                    line = line[:line.find('#')].strip()
                # 判断是否存在=，存在则以=进行分割
                if "=" in line:
                    strs = line.split('=')
                    result_dict = {}
                    rs = self.__get_dict(strs[0], result_dict, strs[1])
        return rs

    def __get_dict(self, keys, result_dict, values):
        for k in keys:
            if
```

##### 存在的问题

1. 去掉两端空格的`strip`方法就是专门用来去除空格的，不需要再传入空格了，如果是需要去除首尾的其他字符才需要传入
2. 字符串的`find`方法，如果找到对应字符就返回字符索引，否则返回-1，在这里可以不用去掉空格
3. 不需要再定义`result_dict`了，直接使用`self.properties`就行
4. 在往`__get_dict`方法里传入`key`和`value`时再去除空格不迟
5. 递归的获取字典的方法还是不会写。思路是，首先判断传入的`key`中是否有`“.”`，如果没有的话就
`result_dict[key_name]=value`；如果key中含有，就切分，然后把前面一部分作为result_dict中的一个元素的key值，对应的value为{}。

#### 1117自测结果

```python
class Properties:
    def __init__(self, filename):
        self.properties_filename = filename
        self.properties = {}

    def get_properties(self) -> dict:
        """
        获取properties 字典
        :return:
        """
        with open(self.properties_filename, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                # 去除两端空格和会车
                line = line.strip().replace("\n", "")
                # 去除#
                if "#" in line:
                    line = line[:line.find("#")]
                if "=" in line:
                    strs = line.split("=")
                    self.__get_dict(strs[0].strip(), self.properties,
                                    strs[1].strip())
        	return self.properties

    def __get_dict(self, key_name, result_dict, value):
        if "." in key_name:
            key = key_name.split(".")[0]
            result_dict.setdefault(key, {})
            return self.__get_dict(key_name[len(key) + 1:], result_dict[key],
                                   value)
        else:
            result_dict[key_name] = value

```

##### 存在的问题

1. 最后返回`self.properties`的时候应该在`with`的外面

### 8-4 日志解析引擎代码开发(2)

本小节主要看一下日志解析引擎怎么用.

新建`use_log.py`, 先来用直接写的方式写出来,然后再写到函数里.

```python
from part_eight.properties_utils import Properties

pro = Properties('log.properties').get_properties()

print(pro)
print(pro['filename'])
print(pro['www'])
print(pro['www']['imooc'])
print(pro['www']['imooc']['com'])

# 如果以上都可以打印出来,就说明我的值全部取成功了. 如果以后想用handlers的配置,就可以在配置文件里什么.什么,一顿点前边表示你自己的一些公共表示形式
# 假设说你中间想做一些判断,比如说之前的是文件日志啊,是控制台日志等等,或者说你用区分各个环境上的,比如说dev环境、生产环境等等的你怎么配,你可以分层取然后再做一个判断,能不能取到,取到完了以后再做一个判断,它就是来这样进行一个基本的使用
# 打印结果:
# {'filename': 'my-test.log', 'level': 'DEBUG', 'format': '%(asctime)s - '......}
# my-test.log
# {'imooc': {'com': '123'}}
# {'com': '123'}
# 123

# 确认可以取到以后就把上面注释掉 然后改写成方法
import logging

def set_log_config():
  	pro = Properties('log.properties').get_properties()
    log_config = {
      	"filename": pro['filename'],
      	"level": pro['level'],
    }
    logging.basicConfig(**log_config)



if __name__ == '__main__':
  	set_log_config()
    logging.info("info log")
```

运行, 在`part_eight`目录下生成`my-test.log`文件, 其中内容是`INFO:root:info log`

如果有另外一个文件, 那么另外的文件也可以用这个日志.

新建`use_log2.py`

```python
import logging

def use_log2_file():
  	logging.info("use log2 file log")
```

然后在`use_log.py`下运行

```python
from part_eight.use_log2 import use_log2_file

if __name__ == '__main__':
  	set_log_config()
    logging.info("info log")
  	use_log2_file()
```

说明别的文件的日志也可以输出到`my-test.log`. 这就说明配的这个日志一次加载全局运行.

这个配置如果想要进一步完善,就可以在`log.properties` 中继续添加配置就好了. 然后`set_log_config` 还可以丰富一下, 做一些多种判断,如果说哪个字段是否存在, 各种`handlers`存不存在然后你怎么去设置等等.

#### 1013自测结果

```python
from part_8.log_utils_1013 import Properties
import logging

# pro = Properties("log.properties").get_properties()

# print(pro['filename'])
# print(pro['level'])
# print(pro['format'])
# print(pro['www'])
# print(pro['www']['imooc'])
# print(pro['www']['imooc']['com'])

def log_settings(filename="log.properties"):
    pro = Properties(filename).get_properties()
    logging.basicConfig(filename=pro['filename'],
                        level=pro['level'],
                        format=pro['format'])

if __name__ == '__main__':
    log_settings()
    logging.info("这是1013的测试")
```

注意事项：

1. 在解析取回的properties结果时，应该构造一个字典，然后把字典以关键字参数的方式传入`basicConfig`
2. 这里的`basicConfig`只能输入英文，不能输入中文(和之前配置`basicConfig`一样的), 不然文件里会报乱码

### 8-5 企业中全局日志配置一种常见方式

在企业当中还有另外一种比较常用的日志方式, 就是config文件

新建`logging.conf`

```ini
[loggers]
keys=root,myAutoTest  # root必须写, myAutoTest是我们自己起的一个名字

[handlers]
keys=fileHandler,consoleHandler

[formatters]
keys=myFormatter

[logger_root]
level=DEBUG
handlers=fileHandler

[logger_myAutoTest]
level=DEBUG
handlers=consoleHandler,fileHandler
qualname=myAutoTest
propagate=0

[handler_consoleHandler]
class=StreamHandler
args=(sys.stdout,)   # 注意这里是个元祖
formatter=myFormatter
encoding=utf-8    # 注意这里的编码参数不能和fileHandler一样写在args里面

[handler_fileHandler]
class=FileHandler
args=('my_auto_test.log', 'a', 'utf-8')   
formatter=myFormatter

[formatter_myFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
datefmt=%Y-%m-%d %H:%M:%S
```

`root`必须写, `myAutoTest`是我们自己起的一个名字

`propagate=0`, 代表第一个handler是否传播到第二个handler(举例: 对于`logger_myAutoTest`来说第一个handler是consoleHandler, 第二个handler是fileHandler), 如果不配默认是1, 1就是传播,这样fileHandler(就是第二个handler)中的内容就会输出两遍

在`formatter`中的`name`指的就是logger的名字(这里就是`myAutoTest`)

新建`logging_setting.py`

```python
import logging.config
import logging
import os

def get_logger(name='myAutoTest'):
  	conf_log = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logging.conf')
    logging.config.fileConfig(conf_log)
    logger = logging.getLogger(name)
    return logger
  

logger = get_logger()
logger.info("info log")
```

运行, 控制台输出日志, 文件夹下生成`my_auto_test.log` 的日志文件

控制台和日志文件的输出日志的格式为:

```python
2020-03-14 20:55:02 - myAutoTest - INFO - info log
```

任意一个其它的文件调用`get_logger()`就可以实现一次配置全局使用这个logger对象了.

1110翻看问题的时候再补充一个: 在定义`[handler_fileHandler]`的时候文件名字还可以使用根据日期来生成. 来源:[logging.conf中的日志名称能否改成可以根据日期生成的名称？](https://coding.imooc.com/learn/questiondetail/133578.html)

网上找了一些文档但现在没时间看，整理在此：

[python logging模块使用教程](https://www.jianshu.com/p/feb86c06c4f4)

[Python日志处理logging模块](https://mp.weixin.qq.com/s/AWmEMcdf88u9UAVIrrtW8g)

[Python笔记：logging日志记录到文件及自动分割](https://beltxman.com/3195.html)

[python修改logging模块实现日志按天写入](https://blog.csdn.net/sdjzuch/article/details/39234465)

[python logging 模块之TimedRotatingFileHandler 实现每天一个日志文件](https://www.cnblogs.com/zhao-jie/archive/2013/06/03/3114961.html)

[python之配置日志的几种方式](https://www.cnblogs.com/yyds/p/6885182.html)

还有两个官网文档：

[Logging HOWTO](https://docs.python.org/3/howto/logging.html#configuring-logging)

[logging.config — Logging configuration](https://docs.python.org/3/library/logging.config.html#configuration-functions)



#### 1010自测结果

```shell
[logger]
key=root, myAutoTest



[logger_root]


[logger_myAutoTest]


[handler]
key=fh, ch

[handler_fh]
key=

[handler_ch]

[formatter]
key=

[formatter_myformatter]
key
```

##### 存在的问题

1. `[logger]`写的就不对， 应该是 `[loggers]`
2. 定义的思路是， loggers-> handlers -> formatters, 先指定各种类型的名字
3. `[logger_root]`不知道要写什么， 应该写`level`和`handlers`
4. `[logger_myAutoTest]`不知道要写什么， 应该写`level`， `handlers`，`qualname`和`propagate`
5. `[handler_ch]`不知道些什么，应该写`class`，`args`， `formatter`，`encoding`
6. 只有前面几个多的下的内容才是`keys`，其他都不是key。
7. `[formatter_myFormatter]`定义的内容不是key，而是format，datefmt

总的来说只记得要定义root的logger，其他就都毫无章法，不知道应该按什么顺序定义以及每个section里面定义什么。

```python
import logging
import logging.config
import os

def logging_setting():
    # 获取logging.conf
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "logging.conf")
    logger = logging.config.fileConfig(file_path)
    return logger
```

首先名字起的不好，这个文件的目的是获取logger

然后需要传进来一个自己定义的logger的名字，采用默认参数的方式

然后还要在函数里生成这个logger， `logging.config.fileConfig`这个~~并不会生成logger~~。(==现在觉得应该是会生成logger, 不仅会生成logger, 配置文件里的handler, formatter都会生成==, 只不过返回值不会返回一个logger), 然后在下一步里通过引用和`qualname`相同的`logger`名字来获取`logger`

最后缺少一步测试：测试的思路是：先调用这个函数生成一个`logger`。这个logger配置了文件里的各种东西。然后在调用`logger.info`， 往配置文件指定的日志文件中写东西测试结果。

#### 1013自测结果

```python
[loggers]
key=root, myAutoTest

[handlers]
key=FileHandler, StreamHandler

[formatters]
key=myFormatter

[logger_root]
level=DEBUG
handlers=StreamHandler
formatters=myFormatter

[logger_myAutoTest]
level=DEBUG
handlers=FileHandler, StreamHandler
formatters=myFormatter
propagate=0

[handler_FileHandler]
class=FileHandler
level=DEBUG
args=('myAutoTest.log', encoding='UTF-8')


[handler_StreamHandler]
class=StreamHandler
level=DEBUG
args=(sys.stdout, )
encoding='UTF-8'

[formatter_myFormatter]
format="%(asctime)s - %(user)s - %(levelname)s - %(message)s"
datfmt="%Y/%m/%d %H:%M:%S"
```

##### 存在的问题

1. 前面几个用到多个点section,关键字应该是`keys`, 而不是`key`, 即使只有一个`key`也应该是`keys`
2. handlers是我们自己起的名字, 不要起成`StreamHandler`, 应该写成`consoleHandler`
3. `logger_root`只需要添加`level`和`handlers`, 不需要写`formatters`
4. `logger_myAutoTest`还需要写`qualname`, `propagate`注意拼写
5. handler就不需要再定义`level`了, 但需要写`formatter`
6. `FileHandler`和`consoleHandler`的`encoding`参数的写法
7. `myFormatter`下参数的值不需要加引号

```python
import logging.config
import logging
import os


def set_logging_config(name):
    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "logging_1013.conf")
    logging.config.fileConfig(filepath)
    logger = logging.getLogger(name)
    return logger
```

基本没啥大问题, 就是写的时候不够肯定, 有点迷茫.

`logging.config.fileConfig(filepath)`返回了一个什么东西呢, 不知道, 为什么后面又定义了一个logger.

以及没有最终的验证代码:

```python
logger = set_logging_config()
logger.info("this is test")
```

在定义`set_logging_config`的时候, 需要将`name`设为默认参数`name=“myAutoTest”`,这个也没有写.

#### 1113自测结果

logging_1113.conf

```ini
[loggers]
keys=root,myAutoTest

[handlers]
keys=fileHandler,consoleHandler

[formatters]
keys=myFormatter

[logger_root]
level=DEBUG
handlers=fileHandler

[logger_myAutoTest]
level=DEBUG
handlers=fileHandler,consoleHandler
qualname=myAutoTest
propagate=0

[handler_consoleHandler]
class=StreamHandler
args=(sys.stdout,)
formatter=myFormatter
encoding=utf-8

[handler_fileHandler]
class=FileHandler
args=('my_auto_test_1113.log', 'a', 'utf-8')
formatter=myFormatter

[formatter_myFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
datefmt=%Y-%m-%d %H:%M:%S
```

logging_setting_1113.py

```python
import logging
import logging.config
import os


def get_logger(name="myAutoTest"):
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               "logging_1113.conf")
    print(config_file)
    logging.config.fileConfig(config_file)
    logger = logging.getLogger(name)
    return logger



logger = get_logger()
logger.info("this is a wenjian test")
```

##### 存在的问题

1. `qualname`和`propagate`是写在`logger`下面的，不是在`handler`下面，一开始记错了，后面才改对。
2. `formatter` 下的`format`中的`name`是指自定义的`logger`的名字，`levelname`和`message`必须写成`levelname`和`message`，不能写成其他的
3. :small_red_triangle: 在前面写formatter名字的时候写的是myFormatter，但是后面写的时候就误写成了MyFormatter，导致后面运行的时候报错。
4. 在调用logger的时候，应该使用`logger.info`来生成日志，而不是`logging`,这个地方前面思路不正确，因为已经生成了logger嘛，所以自然要用logger来做测试，如果用logging那就是root这个自动生成的logger了。而测试也无非是格式上的一个验证，还有输出到日志文件，看日志文件是否成成且格式是否正确。

### 8-6 从源代码层面分析日志配置文件的写法

核心代码就是`logging.config.fileConfig(conf_log)`这一句, 进到`fileConfig`中查看:

第一个参数是`fname`.就是传进来的那个文件

首先来判断传进来的文件是不是`configparser.RawConfigParser`, 最终就是把文件的内容读取出来了. 然后,

`formatters = _create_formatters(cp)`, 进入到`_create_formatters`中继续查看,

再继续往下看 `handlers = _install_handlers(cp, formatters)`, 进到`_install_handlers`中查看

再继续往下看`_install_loggers(cp, handlers, disable_existing_loggers)`

在192行的`llist.remove("root")`和下面的`section = cp["logger_root”]`都是写死的,所以在配置文件中一定要有`root`和`logger_root`, 没有就会报错.

## 第9章 面向对象思想的应用-PageObject

### 9-1 PO的简单解释和目录结构的说明

面向对象思想在UI自动化框架中,也就是selenium,我们管它叫PageObject.在面向对象当中有一句话叫「一切皆对象」. PO模式主要的思想就是:把每个页面当作一个对象来进行封装.

首先来看下京东整个页面的层级结构:

首页->左侧有商品列表页->一级筛选条件->二级筛选条件-> 弹出二级菜单页面->商品详情页

在京东的首页当中左侧有一个列表页面, 然后比如说一级的筛选我们选择“电脑”, 二级的筛选条件选择“笔记本”, 就会弹出来一个二级菜单页面,点击其中的一台电脑, 就会弹出来一个商品详情页面.

结论: 京东在商品的浏览这块一共有三个页面层次: 主页, 商品列表页, 商品详情页

工程的层次结构:

创建`part_nine`包, 然后创建`readme.txt`, 说一下项目的层级结构,在其中写入如下内容:

```python
part_nine:  项目名称 (下列都是文件夹)
  	config: 配置文件 包括Mysql的配置, 日志的配置
    logs: 日志写入的路径
    model: 数据库的对象模型
    orm: 对象关系映射逻辑代码
    pages: 页面对象的封装
    testcase: 我们所有的测试用例所在
    utils: 公共的工具方法
```

#### 1109自测结果

创建了readme.txt

```shell
config: 放置配置文件，包括mysql的配置文件，日志配置文件，一些常量
logs：日志输出文件夹
orm：对象关系映射，包括元类ModelMetaclass, Model, 各种Field，以及最终组装成的对象类
pages：页面
utils：工具类
test：测试代码（其实这个就是业务层了）
```

##### 存在的问题

1. 原课程中把ORM和Model分开放了，现在还没想好是不是要分开放，感觉数据库对象模型也算是ORM的一部分。（又：先按他写的来吧，分开放）
2. 测试用例文件夹最好叫testcase，不要叫test，可能会冲突。

### 9-2 目录内容的组织

首先在`part_nine`文件夹下创建包`config`, 在`config`包中首先创建一个基本配置:`basic_config.py`(也可以叫`basic_setting.py`).这个基本配置或基本设置就是在整个过程中需要我们定义的一些比如driver的路径,之前写的很辛苦,现在写在配置文件里然后直接读配置文件就可以了.

```python
# 页面元素最长等待时间
UI_WAIT_TIME = 2
# 本地chromedriver路径
EXECUTABLE_PATH = "XXX"
# 初始URL
START_URL = "https://www.jd.com"
# 远程driver服务地址
REMOTE_DRIVER_DICT = {
  	"linux": "http://192.168.1.35:4444/wd/hub",
  	"windows": "http://192.168.1.38:4444/wd/hub"
}
```

然后把之前`part_eight`创建的`logging_setting.py`和`logging.conf` 复制到当前的`part_nine`的`config`文件夹下

还可以创建一个`mysql`的基本配置: `mysql_config.py`, 强调一下环境隔离

```python
def set_mysql_config(env):
    if env == "dev":
      	db_config = {
          	'host': '192.168.1.35',
          	'user': 'admin',
          	'passwd': '123456',
          	'db': 'python_ui',
          	'port': 3306,
          	'charset': 'utf8'
        }
    if env == 'pro':
      	db_config = {
          	'host': '192.168.1.35',
          	'user': 'admin',
          	'passwd': '123456',
          	'db': 'python_ui',
          	'port': 3306,
          	'charset': 'utf8'
        }
    return db_config
```

新建==文件夹==: `/part_nine/logs/`,用来存放日志. 

新建`/part_nine/model`包, 在下面新建`jingdong_model.py`, 然后把`part_seven`下的`model.py`的内容复制过来.

新建包: `/part_nine/orm/`, 然后把`part_seven`下的`orm.py`的内容复制过来. `part_seven`下的`field.py`同样也复制到`orm`下. 对应的导包路径要修改一下

然后在`orm.py`中还有一个创建数据库连接池的操作,这个部分也需要弄进来:新建`utils`包, 然后在下面新建`my_database.py`, 其内容就是`part_seven`下的`my_database.py`, 同样需要修改导包路径

#### 1109自测结果

basic_config.txt

```shell
UI_WAIT_TIME = 10

START_URL = "https://www.jd.com"
```

my_log_config_1109.py

```python
import logging.config
import logging


def set_log_config(name):
    logging.config.fileConfig('log.conf')
    logger = logging.getLogger(name)
    return logger
```

log.conf

```ini
[loggers]
keys=root, myAutoTest

[handlers]
keys=StreamHandler, FileHandler

[formatters]
keys=myFormatter

[logger_root]
level=DEBUG
handler=StreamHandler

[logger_myAutoTest]
level=DEBUG
handlers=StreamHandler, FileHandler
propagate=1

[handler_StreamHandler]
level=DEBUG
args=(sys.stdout,)
formatters=myFormatter
encoding='utf-8'

[handler_FileHandler]
level=DEBUG
args=("myAutoTest.log", "utf-8")
formatters=myFormatter

[formatter_myFormatter]
format = "%(asctime) - %(level) - %(message)"
datefmt = "%Y%m%d %H:%M:%S"
```

my_mysql_config_1109.py

```python
def set_my_mysql_config(env):
    if env == "dev":
        db_config = {
            'host': '172.16.1.217',
            'port': 3306,
            'user': 'root',
            'passwd': '508956',
            'db': 'python_ui',
            'charset': 'utf8'
        }
    if env == "prod":
        db_config = {
            'host': '172.16.1.217',
            'port': 3306,
            'user': 'root',
            'passwd': '508956',
            'db': 'python_ui',
            'charset': 'utf8'
        }
    return db_config
```

##### 存在的问题

1. `basic_config`应该是`.py`文件，不是`txt`文件。
2. `basic_config`中还应定义`driver`的执行路径，即使用默认的也该定义，因为如果换机器运行，直接修改这里就行了，否则的话很麻烦
3. `basic_config`中还应定义远程服务器的地址，这个不记得了
4. `my_log_config_1109.py`反而倒是写的没什么大问题，首先是名字，原作是`loggging_setting.py`和`logging.conf`，我写的是`my_log_config.py`和`log.conf`，然后函数命名的时候原作是`get_logger`，我写的是`set_log_config`。文件的名字还好了，但是函数的名字，应该说不记得应该要从日志的配置中获取什么了，其实是要从这个日志配置中获取到一个logger，而且这个logger是我们在配置文件中写的，指定了名字的。而且函数的参数虽然记得要传一个logger的name，但应该把默认的参数名也写上`name=“myAutoTest”`
5. `my_log_config_1109.py`中文件的获取，因为是当前目录下，所以我那么写没有问题，但是不够标准，应该用`os.path.join(os.path.dirname(os.path.abspath(__file__)), "logging.conf")`来获取配置文件`logging.conf`
6. `log.conf`中：
	1. `handlers`的名字写的不对，handlers应该写自己定义的名字，所以要写成第一个字母小写的，然后StreamHandler应该是consoleHandler
	2. `[logger_root]`中应该是`handlers`，不是`handler`，而且应该是`fileHandler`,写到文件中，不是写到`StreamHandler`中
	3. `[logger_myAutoTest]`中忘写`qualname`别名，`propagate`应该写成0，不是1
	4. `[handler_StreamHandler]`中不是`formatters`，而是`formatter`，`encoding`不需要加引号
	5. `[handler_FileHandler]`handler中不用写`level`了，要写`class`是什么;`args`中少一个参数`'a’`追加方式写入
	6. `[formatter_myFormatter]`不需要加引号，format应该一共有4个列，后面几个也没加%和s
7. `mysql_config`没有问题，主要作用就是环境隔离

#### 1110自测结果

fields_1109.py

```python
class Field:
    def __init__(self, column_name, column_type):
        self.column_name = column_name
        self.column_type = column_type


class IntegerField(Field):
    def __init__(self, column_name):
        super(IntegerField, self).__init__(column_name, 'bigint')


class StringField(Field):
    def __init__(self, column_name):
        super(StringField, self).__init__(column_name, 'varchar(100)')


class TextField(Field):
    def __init__(self, column_name):
        super(TextField, self).__init__(column_name, 'text')
```

create_pool_1110.py

```python
from part_9.config.my_mysql_config_1109 import set_my_mysql_config
from dbutils.pooled_db import PooledDB
import pymysql


def create_pool():
    db_config = set_my_mysql_config()
    return PooledDB(pymysql,
                    5,
                    host=db_config['host'],
                    port=db_config['port'],
                    user=db_config['user'],
                    passwd=db_config['passwd'],
                    db=db_config['db'],
                    charset=db_config['charset']).connection()
```

orm.py

```python
from part_9.orm.fields_1109 import Field, StringField, TextField
from part_9.utils.create_pool_1109 import create_pool


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == "Model":
            return type.__new__(cls, name, bases, attrs)
        mappings = {}
        for k, v in attrs.items():
            if isinstance(v, Field):
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__table__'] = name.lower()
        attrs['__mappings__'] = mappings
        return type.__new__(cls, name, bases, attrs)


class Model(metaclass=ModelMetaclass):
    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)

    def insert(self, fields_list, values):
        # insert into table_name (fields) values()
        fields = []
        for f in fields_list:
            if f not in self.__mappings__.keys():
                raise RuntimeError("Field {} not found".format(f))
            fields.append(f)
        sql = "insert into {} () values()".format(self.__table__,
                                                  fields_list,
                                                  values)
        rs = self.__do_execute(sql)
        return rs

    def __do_execute(self, sql):
        conn = create_pool()
        cur = conn.Cursor()
        rs = cur.execute(sql)
        return rs
```

jingdong_model.py

```python
from part_9.orm.fields_1109 import StringField, TextField
from part_9.orm.orm_1109 import Model


class Goods(Model):
    computer_part = StringField("computer_part")
    computer_info = TextField("computer_info")
```

##### 存在的问题

1. Model 没有继承dict类

2. `insert`中对于字段的判断： 首先定义了一个fields列表，然后获取所有类中的fields，然后对于传入参数中的column_list,依次判断。

3. `insert`没有对参数的合法性进行判断

	```python
	args = self.check_params(params_list)
	
	def check_params(self, params_list):
	    args = []
	    for param in params_list:
	        if '"' in param:
	            param = param.replace('\"', '\\\"')
	         param = '\"' + param + '\"'
	         args.append(param)
	    return args
	```

	合法性的思路就是：首先新建一个结果列表，然后依次检查传入的参数列表中的每个参数：如果参数中含有\",那么就把前面再添加一个\\，这样实际的结果中就是显示\"了。然后我们再给每一个参数都加上一个带转义符的双引号，加到结果列表中，最后把结果列表返回。

4. 在拼接sql的时候，应该使用`join`方法，不是直接传递

5. `__do_execute`:

	1. `cursor` 的获取是`conn.cursor()`
	2. 在获取结果rs以后，还应该提交事务，关闭游标

6. sql的拼接只写了第一个{}，忘记写后面两个{}，导致拼接sql的时候不对，非常尴尬

#### 1111自测结果

orm.py 继续完成select, update和delete方法

```python
def select(self, columns_list, where_list):
    """
    select (columns_list) from table_name where column_a=value1, ...
    :return:
    """
    fields = []
    for k in self.__mappings__.keys():
        fields.append(k)
    for key in columns_list:
        if key not in fields:
            raise RuntimeError("field {} not found".format(key))
    args = self.__check_params(where_list)
    sql = "select ({}) from {} where {}".format(','.join(columns_list),
                                                self.__table__,
                                                args)
    rs = self.__do_execute(sql)
    return rs

def update(self, columns_list, params_list, where_list):
    """
    update table_name set column_a=value1, column_b=value2 where
    column_c=value3 and column_d=value4
    :param columns_list:
    :param where_list:
    :return:
    """
    pass

def delete(self, where_list):
    """
    delete from table_name where column_a = value1
    :param where_list:
    :return:
    """
    fields = []
    for k in self.__mappings__.keys():
        fields.append(k)
    for key in where_list:
```

##### 存在的问题

1. `select`方法：
	1. 不需要检查`where_list`的合法性，而且`where_list`里面也不是像`insert`方法中那种的`params_list`, 而是`[column_a=value1, column_b=value2,…]`这种形式，所以也无法使用`__check_params_`方法
	2. `select`在选择字段的时候不需要加括号
	3. `where`条件中多个条件需要用`and`连接，而且要用空格隔开
2. `udpate`方法：
	1. 传入的参数还是想的不对，应该传入`set_columns_list`和`where_list`就够了，不需要把`columns_list`和`params_list`分开
	2. 然后设定两个空的列表，然后把参数依次传入到列表里。
	3. 然后在拼接字段的时候用逗号，where条件用and和空格拼接，最后执行sql，返回结果
3. `delete`方法：
	1. 参数校验的方式也不对，不是对field进行校验，而是只是把参数中的列表导入到自己定义的一个空列表中；而不是从`__mappings__`中获取所有的fields，然后去校验fields。

#### 1118自测结果

##### 存在的问题

1. `basic_config.py`中还要定义初始URL。总结一下：`basic_config.py`中目前一共要定义四个东西：
	1. 页面元素最长等待时间
	2. 初始URL
	3. 本地chromedriver路径
	4. 远程driver服务地址

`logging_1118.conf`

```ini
[loggers]
keys=root,myAutoTest

[handlers]
keys=fileHandler,consoleHandler

[formatters]
keys=myFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[logger_myAutoTest]
level=DEBUG
handlers=fileHandler,consoleHandler
qualname=myAutoTest
propagate=0

[handler_consoleHandler]
class=StreamHandler
args=(sys.stdout,)
formatter=myFormatter
encoding=utf-8

[handler_fileHandler]
class=FileHandler
args=("../logs/my_auto_test.log", "a", "utf-8")
formatter=myFormatter

[formatter_myFormatter]
format=%(asctime)s - %(name)s -%(levelname)s - %(message)s
datefmt=%Y-%m-%d %H:%M:%S
```

`logging_setting_1118.py`

```python
import logging
import logging.config
import os


def get_logger(name="myAutoTest"):
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               "logging_1118.conf")
    logging.config.fileConfig(config_file)
    logger = logging.getLogger(name)
    return logger


if __name__ == '__main__':
    logger = get_logger()
    logger.info("1118的测试")
```

2. `[logger_root]`的`handlers`是`fileHandler`

`orm_1118.py`

```python
from part_9.orm.fields_1118 import Field
from part_9.utils.create_pool_1118 import create_pool


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == "Model":
            return type.__new__(cls, name, bases, attrs)
        mappings = {}
        for k, v in attrs.items():
            if isinstance(v, Field):
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name.lower()
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)

    def insert(self, columns_list, params_list):
        """
        insert into table_name (field_list) values(value_list)
        :return:
        """
        fields = []
        for k in self.__mappings__.keys():
            fields.append(k)
        for column in columns_list:
            if column not in fields:
                raise RuntimeError("field {} not found".format(column))
        # 合法性检查
        args = self.__check_params(params_list)
        sql = "insert into {} ({}) values({})".format(self.__table__,
                                                      ','.join(columns_list),
                                                      ','.join(args))
        rs = self.__do_execute(sql)
        return rs

    def __check_params(self, params_list):
        args = []
        for param in params_list:
            if '\"' in param:
                param = param.replace('\"', '\\\"')
            param = '\"' + param + '\"'
            args.append(param)
        return args

    def __do_execute(self, sql):
        conn = create_pool()
        cur = conn.cursor()
        print(sql)
        cur.execute(sql)
        if "select" in sql:
            rs = cur.fetchall()
        else:
            rs = cur.rowcount
        conn.commit()
        cur.close()
        return rs

    def select(self, columns_list, where_list):
        """
        select column_list from table_name where a=b and c=d
        :return:
        """
        fields = []
        args = []
        for k in self.__mappings__.keys():
            fields.append(k)
        for column in columns_list:
            if column not in fields:
                raise RuntimeError("field {} not found".format(column))
        for param in where_list:
            args.append(param)
        sql = "select {} from {} where {}".format(','.join(columns_list),
                                                  self.__table__,
                                                  ' and '.join(args))
        rs = self.__do_execute(sql)
        return rs

    def update(self, set_column_list, where_list):
        """
        update table_name set a=b, c=d where e=f and g=h
        :return:
        """
        args = []
        for param in where_list:
            args.append(param)
        fields = []
        for column in set_column_list:
            fields.append(column)
        sql = "update {} set {} where {}".format(self.__table__,
                                                 ','.join(set_column_list),
                                                 ' and '.join(args))
        rs = self.__do_execute(sql)
        return rs

    def delete(self, where_list):
        """
        delete from table_name where a=b and c=d
        :param where_list:
        :return:
        """
        args = []
        for param in where_list:
            args.append(param)
        sql = "delete from {} where {}".format(self.__table__,
                                               " and ".join(args))
        rs = self.__do_execute(sql)
        return rs
```

`fields_1118.py`

```python
class Field:
    def __init__(self, column_name, column_type):
        self.column_name = column_name
        self.column_type = column_type


class StringField(Field):
    def __init__(self, column_name):
        super(StringField, self).__init__(column_name, "varchar(200)")


class TextField(Field):
    def __init__(self, column_name):
        super(TextField, self).__init__(column_name, "text")
```

`jingdong_model_1118.py`

```python
from part_9.orm.fields_1118 import StringField, TextField
from part_9.orm.orm_1118 import Model


class Goods(Model):
    computer_part = StringField("computer_part")
    computer_info = TextField("computer_info")


goods = Goods()
rs = goods.insert(["computer_part", "computer_info"], ["1118组件",
                                                       "1118组\"件\"信息"])
# rs = goods.select(["computer_part", "computer_info"],
#                   ["computer_part='组件'"])
# rs = goods.update(["computer_part='组件1'"], ["computer_part='组件'"])
# rs = goods.delete(["computer_part='组件1'"])
print(rs)
```

`create_pool_1118.py`

```python
from part_9.config.mysql_config_1118 import set_mysql_config
from dbutils.pooled_db import PooledDB
import pymysql


def create_pool(env="test"):
    db_config = set_mysql_config(env)
    return PooledDB(pymysql,
                    5,
                    host=db_config['host'],
                    port=db_config['port'],
                    user=db_config['user'],
                    password=db_config['password'],
                    db=db_config['db'],
                    charset=db_config['charset']).connection()
```

捋下来正确的顺序应该是先建好fields字段，和创建数据库连接池，然后再新建元类，然后再新建Model类，然后在其中实现插入修改删除查找四种方法，最后新建Model，然后来进行测试。

### 9-3 浏览器引擎启动工具开发

在`/part_nine/utils`下新建`browser_engine.py`. 浏览器启动主要提供两种启动方法,一种是本地启动,一种是远程启动

```python
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from part_nine.config import basic_config

class BrowserEngine:
  	
    @staticmethod
    def init_local_driver():
      	"""
      	工具方法, 初始化本地的driver, 默认是谷歌浏览器
      	:return: 返回一个chrome driver
      	"""
      	option = webdriver.ChromeOptions()  # 浏览器启动时支持的一些选项
        option.add_argument('disable-infobars')
        driver = webdriver.Chrome(chrome_options=option,
                                  executable_path=basic_config.EXECUTABLE_PATH)
        return driver
      
    @staticmethod
    def init_remote_driver():
     	"""
     	初始化远程的driver, 具体启动哪些取决于在配置文件中的具体配置
     	详细配置在basic_config文件中
     	:return: result_dict 一个字典, 具体的结构是{"名字": driver}
     	"""
      	remote_browser_dict = basic_config.REMOTE_DRIVER_DICT
        # 用来存储返回结果, 结构是{"名字": driver}
        result_dict = {}
        for name, url in remote_browser_dict.items():
          	option = webdriver.ChromeOptions()
            option.add_argument('disable-infobars')
            driver = webdriver.Remote(
            		command_executor=url,
              		desired_capabilities=DesiredCapabilities.CHROME,
                	chrome_options=option
            )
        	result_dict[name] = driver
        return result_dict
```

如果是需要对不同浏览器进行测试, 那么需要修改为:

```python
def init_local_driver(driver_name):  # 接受一个浏览器名字
    # 然后进行一些if判断, 根据不同的浏览器来进行初始化
    # 然后driver可以在basic_config里写好, IE是什么路径, 火狐是什么路径等等
```

#### 1111自测结果

```python
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import ChromeOptions
from part_9.config import basic_config


class BrowserEngine:

    @staticmethod
    def webdriver_from_local():
        options = ChromeOptions()
        options.add_argument('disable-infobars')
        driver = webdriver.Chrome()
        return driver

    @staticmethod
    def start_webdriver_from_remote():
        remote_driver_dict = basic_config.REMOTE_DRIVER_DICT
        result_dict = {}
        for name, url in remote_driver_dict:
            options = ChromeOptions()
            options.add_argument("disable-infobars")
            driver = webdriver.Remote(
                command_executor=url,
                desired_capabilities=DesiredCapabilities.CHROME
            )
            result_dict[name] = driver
        return result_dict
```

##### 存在的问题

1. 导包： 
	1. DesiredCapabilities可以直接从`selenium.webdriver`中导入，不需要再到`common.desired_capabilities`中导入
	2. `ChromeOptions`不用专门导入了，直接用`webdriver.ChromeOptions`引用就好
2. 方法的命名：初始化本地driver-> `init_local_driver`， 初始化远程driver-> `init_remote_driver`
3. 在添加了options之后，还要把options加到driver的初始化中，同时要指定driver的路径，这样basic_config中的路径才没有白写
4. 启动远程driver中从配置文件中读取的是浏览器地址，不是driver地址，在命名上要做一个区分
5. 初始化远程driver的时候没有把options加入到driver的初始化中（原课件中也没有加）

#### 1118自测结果

```python
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from part_9.config import basic_config


class BrowserEngine:

    @staticmethod
    def init_local_driver():
        options = webdriver.ChromeOptions()
        options.add_argument("disable-infobars")
        driver = webdriver.Chrome(
            executable_path=basic_config.EXECUTABLE_PATH,
            options=options)
        return driver

    @staticmethod
    def init_remote_driver():
        remote_browser_dict = basic_config.REMOTE_DRIVER_DICT
        result_dict = {}
        for name, url in remote_browser_dict:
            options = webdriver.ChromeOptions()
            options.add_argument("disable_infobars")
            driver = webdriver.Remote(command_executor=url,
                                      desired_capabilities=DesiredCapabilities.CHROME,
                                      options=options)
            result_dict[name] = driver
        return result_dict
```

##### 存在的问题

1. 在添加options的时候参数写的是`options`, 但对于Chrome来说是`chrome_options`（udpate: `chrome_options`要被废弃了， 以后就只有`options`）
2. 在循环迭代`remote_browser_dict`的时候忘了加`items()`,
3. 注释的书写. 现在写注释写的不好

### 9-4 PageObject封装(1)

在`part_nine`下创建包`pages`,所有的页面对象都在这里.

pages从底层往上来进行封装, 一般有一个祖宗类, 新建`base_page.py`, 它是所有页面的父亲, 它来书写他们共有的方法:

```python
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_condition as EC
from selenium.webdriver.support.wait import WebDriverWait

from part_nine.config import basic_config


class BasePage(object):
  	def __init__(self, driver, url):
      	"""
      	BasePage的构造方法
      	:param driver: 启动具体哪个浏览器
      	:param url: 目标url地址
      	"""
      	self._driver = driver
        self._url = url
        
    def open(self):
      	"""
      	页面打开方法
      	:return: 浏览器的driver
      	"""
      	self._driver.get(url=self._url)
        return self._driver
      
    def find_element(self, 
                     *locator, 
                     element=None, 
                     timeout=None, 
                     wait_type="visibility",
                     when_failed_close_browser=True):
      	"""
      	发现元素方法,分别支持以driver或element之上来进行元素发现的两种定位方式
      	
      	:param locator: 元素定位方式, 数据类型是元组 例如(By.ID, "id_value")
      	:param element: 默认值为None, 如果有值, 那么这个值是一个页面元素, 这个方法将会在这个元素之上发现它的子元素
      	:param timeout: 默认值为None, 但是为None时, 将会取配置文件中的超时时间配置
      	:param wait_type: 等待的类型, 支持两种等待方式,一种是可见等待visibility, 另外一种是存在等待presence
      	:param when failed_close_browser: 当元素定位失败时,浏览器是否关闭
      	:return: 返回定位的元素
      	"""
      	if element is not None:
          	return self._init_wait(timeout).\
        		   until(EC.visibility_of(element.find_element(*locator)))
        try:
          	if wait_type == "visibility":
              	return self._init_wait(timeout).\
            		   until(EC.visibility_of_element_located(*locator))
            else:
              	return self._init_wait(timeout).\
            		   until(EC.presence_of_element_located(*locator))
       	except TimeoutException:
          	if when_failed_close_browser:
              	self._driver.quit()
            raise TimeoutException(msg="定位元素失败, 定位方式是:{}".format(locator))
        except NoSuchElementException:
          	if when_failed_close_browser:
              	self._driver.quit()
            raise NoSuchElementException(msg="定位元素失败, 定位方式是:{}".format(locator))
    
    def _init_wait(self, timeout):
        if timeout is None:
            return WebDriverWait(
                driver=self._driver, timeout=basic_config.UI_WAIT_TIME)
        else:
            return WebDriverWait(driver=self._driver, timeout=timeout)
        
	def find_elements(self, 
                     *locator, 
                     element=None, 
                     timeout=None, 
                     wait_type="visibility",
                     when_failed_close_browser=True):
      	"""
      	发现很多元素方法
      	:param locator: 元素定位方式和值, 支持的是元祖类型 例如(By.ID, "id_value")
      	:param element: 默认值为None, 如果有值, 那么这个值是一个页面元素, 这个方法将会在这个元素之上发现它的子元素
      	:param timeout: 默认值为None, 但是为None时, 将会取配置文件中的超时时间配置
      	:param wait_type: 等待的类型, 支持两种等待方式,一种是可见等待visibility, 另外一种是存在等待presence
      	:param when failed_close_browser: 当元素定位失败时,浏览器是否关闭
      	:return: 返回定位的元素们
      	"""
    	if element is not None:
          	return element.find_elements(*locator)
        try:
          	if wait_type == "visibility":
              	return self._init_wait(timeout).until(EC.visibility_of_all_elements_located(locator=locator))
            else:
              	return self._init_wait(timeout).until(EC.presence_of_all_elements_located(locator=locator))
        except TimeoutException:
          	if when_failed_close_browser:
              	self._driver.quit()
            raise TimeoutException(msg="定位元素失败, 定位方式是:{}".format(locator))
        except NoSuchElementException:
          	if when_failed_close_browser:
              	self._driver.quit()
            raise NoSuchElementException(msg="定位元素失败, 定位方式是:{}".format(locator))
```

其中还要说一下`visibility_of`: 查看源代码, `visibility_of`的构造函数接受一个`element`,说明`visibility_of`可以基于一个元素之内来定位元素,

`visibility_of_element_located`元素是否可见,可见是指在页面上是否可见. (可见一定存在)

`presence_of_element_located`: 元素是否存在, 但存在不一定可见.

在写`find_elements`的时候和`find_element`的小区别: `visibility_of`只接受一个`element`, 不接受`elements`, 所以应该有所区别

#### 1106自测结果

```python
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:
    def __init__(self, driver):
        self._driver = driver

    def open(self):
        url = config.START_URL
        driver = self._driver.open()
        return driver

    def __init_wait(self, driver, timeout):
        if timeout is None:
            return WebDriverWait(driver, timeout=config.WAIT_TIME)
        else:
            return WebDriverWait(driver, timeout=timeout)

    def find_element(self, locator, timeout, element=None, type="visibility",
                     when_failed_quit_browser=True):
        driver = self.open()
        if element != None:
            return self.__init_wait(driver, timeout).until(EC.visibility_of(
                element))
        try:
            if type == "visibility":
                return self.__init_wait(driver, timeout).until(
                    EC.visibility_of_element_located(locator))
            else:
                return self.__init_wait(driver, timeout).until(
                    EC.presence_of_element_located(locator))
        except TimeoutException:
            if when_failed_quit_browser:
                driver.quit()
            raise TimeoutException(msg="超时退出，当前定位元素是{}".format(locator))
        except NoSuchElementException:
            if when_failed_quit_browser:
                driver.quit()
            raise NoSuchElementException(msg="无法定位到元素：{}".format(locator))

```

##### 存在的问题

1. 在`__init__`方法中只传了driver，没有传url

	> 为什么要在`__init__`中传driver和url呢？
	>
	> ​		想了一下，答案应该是这样：drier当然是对应各种不同的浏览器驱动了，而url也是为了扩展适应性而传的，所以没有写死，而是根据传入的url来操作。（所以才没有从配置文件中读取）。而什么时候读取，是在实际测试页面的时候从配置文件中读取的。所以要区分出代码的功能和实际的业务。而至于为什么最长页面等待时间可以直接在代码中引用是因为这个本来就是一个selenium的常量，和业务无关。==所以要区分出业务层和页面层==

2. `open`方法中url是从self中获取，不是从配置文件中读取

3. `open`方法中，打开页面是`get`方法，不是`open`方法。返回的是driver没错，但是不需要起一个新变量来接收，直接挂在self上就行了。

4. `__init_wait__`的参数中只需要传self，通过self来引用driver，不需要再传一个driver了。（和3的后半段原因相同）

5. `find_element`传参：locator需要传成可变参数形式，timeout默认值为None，type名字应该是wait_type，

6. `find_element`不需要先通过open方法获取driver，还是那句话，注意区分功能，一个方法里只写对应功能的代码，这里是find_element,那么默认就是在某个页面上进行操作的

7. 如果元素不为None的写法是`if element is not None`不是`if element != None`

8. `EC.visibility_of()`中传入的是 `element.find_element(*locator)`，不是`element`

### 9-5 PageObject封装(2)

往上再封装一层商品列表页

在`pages`下新建一个`goods_list_page.py`

```python
from part_nine.pages.base_page import BasePage
from part_nine.config.logging_setting import get_logger
from part_nine.config import basic_config

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class GoodsListPage(BasePage):
  	logger = get_logger()
    
    def __init__(self, driver):
      	self._driver = driver
        super(GoodsListPage, self).__init__(driver, basic_config.START_URL)
        
    def get_goods_list_driver(self, first_list_name, second_list_name):
      	"""
      	获取商品列表的driver(就是京东首页点击商品跳转到商品列表页)
      	:param first_list_name: 一级菜单名字
      	:param second_list_name: 二级菜单名称
      	"""
      	driver = self.open()
        first_element = (By.LINK_TEXT, first_list_name)
        secone_element = (By.LINK_TEXT, second_list_name)
        
        first = self.find_element(*first_element)
        ActionChains(driver).move_to_element(first).perform()
        second = self.find_element(*second_element)
        second.click()
        # 切换句柄
        handles = driver.window_handles
        index_handle = driver.current_window_handle
        for handle in handles:   # 未来可以把切换句柄的方法放到工具类里
          	if handle != index_handle:
              	driver.close()   # 注意这句话和之前不一样, 要把原来的关掉
              	driver.switch_to.window(handle)
        self.logger.info("获取到页面" + second_list_name)
        self.logger.info("当前url是:" + driver.current_url)
        self._driver = driver
        return driver
        
    def get_selector_page(self, selector_condition_list):
      	"""
      	点击筛选条件
      	:param selector_condition_list: 筛选条件的list, 
      								比如 [(By.ID, "id_value"), (By.name, "name_value")]
      							   (为什么用list? 因为list顺序不会乱, 先放进去啥拿出来的就是啥)
      	:return: 
      	"""
        # 可以在这里对 selector_condition_list 做一个健壮性判断
        # if selector_condition_list isinstance() 或者
        # type(selector_condition_list)
        for condition in selector_condition_list:
          	element = self.find_element(*condition)
            element.click()
            
   	def get_goods_info_page(self, selector_condition):
      	"""
      	获取商品的详情页面
      	:param selector_condition: 具体商品的筛选条件, 例如: (By.ID, "id_value")
      	:return: 浏览器driver
      	"""
      	self.find_element(*selector_condition).click()
        handles = self._driver.window_handles
        index_handle = self._driver.current_window_handle
        for handle in handles:
          	if handle != index_handle:
              	self._driver.close()
              	self._driver.switch_to.window(handle)
        return self._driver    
```

#### 1124自测结果

```python
from part_9.pages.base_page_1119 import BasePage
from part_9.config import basic_config
from part_9.config.logging_setting_1118 import get_logger
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class GoodsListPage(BasePage):
    logger = get_logger()

    def __init__(self, driver):
        super(GoodsListPage, self).__init__(driver, basic_config.START_URL)


    def

```

##### 存在的问题

1. 不知道要导入什么, 除了BasePage, 其它就不知道了. 但至少应该知道的是要导入logger, 导入`basic_config`(因为其中有`START_URL`), 然后因为还会涉及到鼠标悬浮操作所以还应该导入`ActionChains`. 目前还不知道导入`By`有什么用.
2. logger的书写方式: 写成类变量, 这样的话实例也可以引用.
3. 重写构造方法, 只需要传入driver, 在给父类的构造方法传参数的时候直接传`START_URL`
4. 不知道要写什么方法在里面, 很迷茫.



### 9-6 PageObject封装(3)

新建`goods_info_page.py`

```python
from selenium.webdriver.common.by import By

from part_nine.config import basic_config
from part_nine.config.logging_setting import get_logger
from part_nine.model.jingdong_model import Goods
from part_nine.pages.base_page import BasePage


class GoodsInfoPage(BasePage):
  	logger = get_logger()
    
    def __init__(self, driver):
      	self._driver = driver
        super(GoodsInfoPage, self).__init__(driver, basic_config.START_URL)
        self.logger("初始化商品详情页面")
    
    def save_product_info(self):
      	js = "window.scrollTo(0, 1000)"
        self._driver.execute_script(js)
        # 定位到规格与包装
        product_element = (By.XPATH, "//*[@id='detail']/div[1]/ul/li[2]")
        self.find_element(*product_element).click()
        info_ele = (By.CLASS_NAME, "Ptable-item")
        info_elements = self.find_elements(*info_ele)
        result_list = []
        for info_element in info_elements:
          	info_element_dict = self.__get_info_element_dict(info_element)
            result_list.append(info_element_dict)
            # self.logger.debug(str(info_element_dict))
        self.__save_info_to_mysql(result_list)
        
    def __get_info_element_dict(self, info_list):
      	goods = Goods()
        for info in info_list:
          	for key, value in info.items():
              	goods.insert(["computer_part", "computer_info"], [str(key), str(value)])
                
      
      
    def __save_info_to_mysql(self, info_element):
      	# 计算机组成信息, 第一列的值
      	computer_part_element = (By.TAG_NAME, "h3")
        computer_part = self.find_element(*computer_part_element, element=info_element)
        
        # 计算机信息中的key值, 第二列的值
        computer_info_keys_element = (By.TAG_NAME, "dt")
        computer_info_keys = self.find_elements(*computer_info_keys_element, element=info_element)
        
        # 计算机信息中的值, 就是第三列的值
        computer_info_values_element = (By.XAPTH, "dl//dd[not(contains(@class, 'Ptable-tips'))]")
        computer_info_values = self.find_elements(*computer_info_values_element, element=info_element)
        
        self.logger.debug("获取到了所有的规格与包装信息")
        key_and_value_dict = {}
        parts_dict = {}
        
        for i in range(len(computer_info_keys)):
          	key_and_value_dict[computer_info_keys[i].text] = computer_info_values[i].text
            parts_dict[computer_part.text] = key_and_value_dict
        return parts_dict
```

#### 1124自测结果

```python

```



### 9-7 PageObject封装(4)

新建包`testcase`

新建`test.py`

```python
from part_nine.pages.goods_info_page import GoodsInfoPage
from part_nine.utils.browser_engine import BrowserEngine
from part_nine.config import logging_setting
from part_nine.pages.goods_list_page import GoodsListPage

from selenium.webdriver.common.by import By


class Test:
  	driver = BrowserEngine.init_local_driver()
	logger = logging_setting.get_logger()
    
    def test_save_info(self):
      	self.logger.debug("目标保存电脑详细信息, 触发")
        goods_list_page = GoodsListpage(self.driver)
        goods_list_page.get_goods_list_driver("电脑", "笔记本")
        brand_locator = (By.ID, "brand-11518")
        price_locator = (By.LINK_TEXT, "7000以上")
        comment_locator = (By.LINK_TEXT, "评论数")
        goods_list_page.get_selector_page([brand_locator, price_locator, comment_locator])
        self.logger.debug("开始获得具体的商品页面")
        goods = (By.XPATH, '//*[@id="plist"]/ul/li[1]/div/div[]')
        driver = goods_list_page.get_goods_info_page(goods)
        self.logger.info("当前的url地址是" + driver.current_url)
        
        goods_info = GoodsInfoPage(driver)
        goods_info.save_product_info()
        self.logger.info("保存商品信息成功")
        

t = Test()
t.test_save_info()
```

### 9-8 无页面的后台运行方式

打开`browser_engine.py`, 新建方法:

```python
@staticmethod
def init_local_driver_no_gui():
    """
    工具方法, 初始化本地的driver, 默认是谷歌浏览器
    :return: 返回一个chrome driver
    """
    option = webdriver.ChromeOptions()
    option.add_argument('--headless ')
    driver = webdriver.Chrome(chrome_options=option,
                              executable_path=basic_config.EXECUTABLE_PATH)
    return driver
```





### 9-9 远程Linux上的有界面和无界面启动测试

新建

```python
@staticmethod
def init_remote_driver_no_gui():
    remote_browser_dict = basic_config.REMOTE_DRIVER_DICT
    # 用来存储返回结果, 格式是{"名字": driver}
    result_dict = {}
    for name, url in remote_browser_dict.items():
        options = webdriver.ChromOptions()
        options.add_argument('--headless')
        driver = webdriver.Remote(command_executor=url,
                                  options=options,
                                  desired_capabilities=DesiredCapabilities.CHROME)
        reuslt_dict[name] = driver
    return result_dict
```

test里面就不能那么写了, 需要把`driver = BrowserEngine.init_local_driver_no_gui()`注释掉, 然后重写一个构造方法:

```python
class Test:
    logger = logging_setting.get_logger()
    
    def __init__(self):
        driver_dict = BrowserEngine.init_remote_driver()
        self.driver = driver_dict["linux"]
```

然后就可以右键启动, 然后运行.当然前提是把linux上的jar包先启动起来.

在数据库中确认数据是否成功写入.

然后再测试一下无头启动的方式: 修改构造函数:

```python
class Test:
    logger = logging_setting.get_logger()
    
    def __init__(self):
        driver_dict = BrowserEngine.init_remote_driver_no_gui()
        self.driver = driver_dict["linux"]
```



## 第10章 课程总结

课程框架总结

UI自动化框架

页面操作

页面对象: 面向对象的思想管理页面,使得页面操作容易且清晰

数据操作: 对象关系映射

ORM使得数据库的操作变得非常简单,并且有利于大家对框架封装产生兴趣

过程记录: 日志操作 比较容易忽略的一块,但日志的记录是项目开发中非常重要的一块



未来的技术进阶之路

完善测试代码: 学一个单元测试框架

测试用例: 抽象到数据库中进行管理

当你的用例量特别大的时候,怎么进行用例管理

框架学习





























