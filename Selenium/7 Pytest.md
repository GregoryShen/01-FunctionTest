# [【软件测试教程】自动化测试入门教程-pytest测试框架](https://www.bilibili.com/video/BV1JC4y147XK)

* pytest是一个非常成熟的全功能的Python测试框架,第三方插件丰富,可扩展性强,兼容性强,越来越多的项目开始放弃unittest和nose以及robotframework
  * 能够支持简单的单元测试和复杂的功能测试,还可以用来做selenium/appnium等自动化测试,接口自动化测试(pytest+requests)
  * 简单灵活,容易上手
  * 支持参数化
  * 测试用例的skip和xfail,自动失败重试等处理
  * pytest具有很多第三方插件,并且可以自定义扩展,比较好用的如pytest-allure(完美html测试报告生成),pytest-xdist(多CPU分发)等
  * 可以很好的和jenkins集成
  * 不依赖特定的python版本,python2和python3都可以使用最新的版本
* pytest官方文档:https://docs.pytest.org/en/latest/contents.html#toc
* 第三方库:https://pypi.org/search/?q=pytest

## pytest安装与依赖

* pytest安装

​	`pip install -U pytes`t  U表示升级

* pytest常用的插件
  * pytest-selenium 集成selenium
  * pytest-allure-adaptor 生成漂亮的allure报告
  * `pip install pytest-sugar` 优化运行效果
  * `pip install pytest-rerunfailures` 重新运行错误用例
  * `pip install pytest-xdist` 多CPU分发分布式执行
  * `pip install pytest-assume` 断言
  * `pip install pytest-html` 测试报告

* pip list 查看

* pytest -h 帮助

## 测试用例的识别与运行

* 测试文件
  * test_*.py
  * \*\_test.py
* 用例识别
  * Test*类包含的所有test\_\*的方法(测试类不能带有\__init__方法)
  * 不在class中的所有的test\_\*方法
* pytest也可以执行unittest框架写的用例和方法

* 终端执行
  
  * `pytest / py.test`
  
  * `pytest -v` (最高级别信息 —verbose) 打印详细运行日志信息
  * `pytest -v -s` 文件名(s是带控制台输出结果,也是输出详细)
  * `pytest 文件名.py` 执行单独一个pytest模块
  * `pytest 文件名.py::类名`  运行某个模块里面某个类
  * `pytest 文件名.py::类名::方法名` 运行某个模块里面某个类里面的方法

* 报错停止运行
  * `pytest -x 文件名` 一旦运行到报错,就停止运行(可用在回归测试或不希望有任何报错的用例里面)
  * `pytest —maxfail=[num]` 当运行错误达到num的时候就停止运行

* 跳过某条用例或者只运行某些用例
  * `pytest -k "类名 and not 方法名"` 跳过运行某个用例
  * `pytest -m [标记名]`    `@pytest.mark.[标记名]` 将运行有这个标记的测试用例

### pytest 执行用例出错时停止

* 场景:

* 正常全部执行完成后才能停止:

  * 如果想遇到错误时停止测试: [-x] 参数
  * 也可以当用例错误个数n达到指定数量时,停止测试: [—maxfail=n]

* `pytest -x -v -s test_class_01.py`

  `pytest -x -v -s test_class_01.py --maxfail=2`

### pytest 执行-失败重新运行

* 场景
* 测试失败后要重新运行n次,要在重新运行之间添加延时时间,间隔n秒在运行
* 安装:
  * `pip install pytest-rerunfailures`
* 执行:
  * `pytest --reruns=3 -v -s test_class.py`
  * `pytest -v --reruns=5 --reruns-delay=1`

### pytest 执行-多条断言有失败也都运行

* 场景:一个方法中写多条断言,通常第一条过不去,下面就不执行了,我们想报错也都执行一下
* 安装:
  * `pip install pytest-assume`
* 执行:
  * `pytest.assume(1==4)`
  * `pytest.assume(2==4)`

### 测试用例的识别与运行

* pycharm配置与执行pytest测试框架
* 运行方式: `pytest.main([‘-v’],'**.py::TestClass')`(列表里面所有的参数和pytest命令行方式是一样的)

是说的在脚本上如何执行:

```python
if __name__ == '__main__':
  	pytest.main(['-v', '-s', 'test_sample.py::test_one'])
```

## pytest框架结构

* import pytest 类似的`setup`, `teardown` 同样更灵活
  * 模块级(setup_module/teardown_module)模块始末,全局的(优先最高)
  * 函数级(setup_function/teardown_function)只对函数用例生效(不在类中)
  * 类级(setup_class/teardown_class)只在类中前后运行一次(在类中)
  * 方法级(setup_method/teardowm_method)开始于方法始末(在类中)
  * 类里面的(setup/teardown) 运行在调用方法的前后

```python
def seup_module():
  print("模块级别的setup")
  
def teardown_module()
```

## pytest fixture使用

* fixture 是pytest 特有的功能,它用`@pytest.fixture()`标识,定义在函数前面
* 在你编写测试函数的时候,你可以将这个函数名称作为传入参数,pytest将会以依赖注入方式,将该函数的返回值作为测试函数的传入参数
* fixture有明确的名字,在其他函数、模块、类或整个工程调用它时会被激活
* fixture主要的目的是为了提供一种可靠和可重复性的手段去运行那些最基本的测试内容
* 比如在测试网站的功能时,每个测试用例都要登录和退出,利用fixture就可以只做一次,否则每个测试用例都要做这两步也是冗余

## pytest前端自动化中应用-fixture

* fixture 可以当作参数传入,也可以传入多个fixture

* fixture 的作用范围(function<class<module<session)

* `fixture(scope=“function”, params=None, autouse=False, ids=None, name=None)`
* scope有四个级别,function(默认),class, module, session(fixture为session级别是可以跨.py模块调用的,也就是当我们有多个.py文件的用例的时候,如果多个用例只需调用一次fixture,那就可以设置为scope=“session”,并且写到conftest.py文件里)
  * params:可选参数,它将导致多个参数调用fixture功能,在所有的测试使用
  * autouse:True 则为所有测试激活fixture功能
  * ids:每个字符串id的列表,每个字符串对应于params这样他们就是测试ID的一部分,如果没有提供ID它们将从params自动生成
  * name:fixture的名称
  
## pytest 前端自动化中应用-conftest

* 场景

  * 你与其他测试工程师合作一起开发时,公共模块要在不同文件中,要在大家都访问到的地方

* 解决

  * `conftest.py`这个文件进行数据共享,并且他可以放在不同位置起着不同的范围共享作用

* 执行:

  * 系统执行到参数login时先从本文件中查找是否有这个名字的变量,之后在conftest.py中找是否有

* 步骤:

  * 将登录模块带@pytest.fixture写在conftest.py

* conftest.py配置需要注意:

  * conftest文件名是不能换的 
  * conftest.py与运行的用例要在同一个package下,并且有`__init.py__`文件
  * 不需要import倒入conftest.py,pytest用例会自动查找
  * 全局的配置和前期工作都可以写在这里,放在某个包下,就是这个包数据共享的地方

  

  





# [Junit结合下一代测试报告框架Allure2](https://www.bilibili.com/video/BV1jb41177zF)

### xUnit体系

Java: JUnit4, TestNG, JUnit5

python: Unittest, pytest

测试用例的管理概念

测试用例 testcase

测试用例核心元素

测试用例名字

测试用例标签

测试用例描述

测试过程

单元测试

Web自动化测试Selenium

App

定义测试套件

RunWith

SuiteClasses

测试套

用例分组标签

方法级别的标签

基于标签运行

include

## 数据驱动

### 参数化

JUnit

RunWith

Parameterized

### 数据驱动

数据来源: csv, yaml, xml, db, excel, json

读取数据源返回数组:

* 基于shcema: `List<Class>`
* 纯数据: `Array<Array<String, Object>>`

利用参数化进行数据与变量的对应

第一级能力: 参数化

第二级能力: 测试数据数据化

第三级能力: 业务逻辑数据化

第四级能力: 测试框架数据化

数据格式的选择

| 数据格式 | 优点            | 缺点                       |
| -------- | --------------- | -------------------------- |
| Excel    | 生成数据方便    | 二进制文件不利于版本管理   |
| CSV      | 可使用Excel编辑 | 文本格式方便版本管理       |
| YAML     | 格式完备        | 格式简单                   |
| XML      | 格式完备        | 冗长复杂                   |
| JSON     | 格式完备        | 不能编写注释, 格式相对复杂 |

### 汇总断言失败

```java
@Rule
public ErrorCollector collector = new ErrorCollector();

@Test
public void assertions(){
    collector.checkThat( value: 1, equalTo( operand: 2));
    collector.checkThat( value: 2, equalTo( operand: 2));
    collector.checkThat( value: 3, equalTo( operand: 2));
}
```

## jenkins

allure历史报告对比

allure generate allure



# [【软件测试教程】自动化测试pytest实战案例](https://www.bilibili.com/video/BV1wZ4y1H7Fi)





# [【软件测试教程】一节课掌握超好用的软件测试框架pytest](https://www.bilibili.com/video/BV1b54y1q7Cj)





# [小鱼老师讲pytest测试框架1-强大的Fixture功能](https://www.bilibili.com/video/BV1Kt41157qg)

## fixture 是干什么用的

fixture是在测试函数运行前后,由pytest执行的外壳函数;代码可以定制,满足多变的测试需求;包括定义传入测试中的数据集(比如接口测试需要很多不同的测试数据源,可以通过fixture进行传入),配置测试系统的初始状态(比如在测试用例中需要验证数据是否插入了mysql,因而需要连接mysql,这些步骤可以不在测试用例里实现,可以在fixture里实现),为==批量测试提供数据源==等等...

fixture是pytest用于将测试前后进行预备,清理工作的代码分离出核心测试逻辑的一种机制

举例:

```python
import pytest

@pytest.fixture()
def some_data():
    return 42
  
def test_some_data(some_data):
    assert some_data == 42
```

`@pytest.fixture()`装饰器用于声明函数是一个fixture,如果测试函数的参数列表中包含fixture名字,那么pytest会检测到.

检测顺序是:优先搜索该测试所在的模块,然后搜索`conftest.py`并在测试函数运行之前执行该fixture.

fixture可以完成测试任务,也可以返回数据给测试函数.

如果我们想看看fixture具体是怎么执行的,可以运行:

`pytest --setup-show test_example1.py`

```python
@pytest.fixture()
def some_data():
 		print("222222")
    yield
    print("hhhh")
    
    
def test_some_data(some_data):
    print("test")
```

执行顺序是先打印“222222”,然后打印“test”, 最后打印“hhhhh”

## fixture函数放在哪里合适

1. 可以放在单独的测试文件里
2. 如果希望多个测试文件共享fixture,可以放在某个公共目录下新建一个`conftest.py`文件,将fixture放在里面

```python
# 作者之前写的一个fixture函数,类似切换mysql的游标的
import pytest

@pytest.fixture(scope="session", autouse=False)
def mysql(request, env):
    """
    初始化各个data_base的cursor
    :param request
    :param env
    :return
    """
    mysql_cursor = {}
    for config in env.get('mysql_config', []):
        mysql_curosr.setdefault(config['database'], MysqlManager(**config))
        
    def fin():
        for c in mysql_cursor:
            mysql_cursor[c].close()
    request.addfinalizer(fin)
    return mysql_cursor
```

## 使用fixture传递测试数据

fixture非常适合存放测试数据,并且他可以返回任何数据

```python
@pytest.fixture()
def a_list():
    return [1,2,3,4,5]
  
def test_a_list(a_list):
    assert a_list[2] == 3
```

## 指定fixture 作用范围

fixture 里面有个scope参数可以控制fixture的作用范围: session>module>class>function

1. function 每一个函数或方法都会调用

```python
@pytest.fixture
def first():
    print("\n获取用户名")
    a = "xiaoyulaoshi"
    return a
  
@pytest.fixture(scope="function")
def second():
    print("\n获取密码")
    b = "123456"
    return b
  
  
```



1. 

## fixture 的参数化

pytest支持在多个完整测试参数化方法

1. `pytest.fixture()`:在fixture级别的function处参数化
2. `@pytest.mark.parametrize`:允许在function或class级别的参数化,为特定的测试函数或类提供了多个argument/fixture设置
3. `pytest_generate_tests`:可以实现自己的自定义动态参数化方案或扩展

# [pytest测试框架2-深入讲解pytest的配置文件](https://www.bilibili.com/video/BV1Gt411u7nb)

本节课深入讲解pytest的配置文件,分析它们是如何改变pytest的运行方式的

## pytest里都有哪些非测试文件

1. `pytest.ini`:pytest的主配置文件,放在项目的根目录下,可以改变pytest的默认行为,其中有很多可配置的选项
2. `conftest.py`:是本地的插件库,其中的hook函数和fixture将作用于该文件所在的目录以及所有子目录
3. `__init__.py`:每个测试子目录都包含该文件时,那么在多个测试目录中可以出现同名测试文件

## 如何查看ini文件选项

使用`pytest —-help`命令查看`pytest.ini`的所有设置选项

`.` 在pytset中表示测试通过的意思. 但是在控制台中看`.`并不直观,想要输出详细信息,所以加`-v`参数, 为了一劳永逸,以后每次都能加`-v`,可以在`pytest.ini`文件中添加: `addopts = -v`

## 更改默认命令行选项

我们已经用过很多pytest命令行选项了, 比如 `-v` `-—verbose`可以输出详细信息

```python
[pytest]
addopts = -v --alluredir ./allure-results
```

常用的命令行选项:

`-v`:输出详细信息

`-—collect-only`:展示在给定的配置下哪些测试用例会被执行,但并不会真的执行这些测试

示例: `pytest -v -k "baidu" —-collect-only test.py` 可以查看根据`-k`具体筛选出了哪些用例(但并不会执行这些用例, 只是把在这个条件下的用例展示出来)

`-k`:允许使用表达式指定希望运行的测试用例(是指测试用例(==就是测试方法==)的名字中含有相应的“关键字”)

示例: `pytest -v -k "baidu" test.py`

`-m`:mark用于标记测试并分组(筛选测试用例的另一种方法)

示例:

```python
@pytest.mark.smoke
def test_baidu_search(class_scope):
    ...
    ...
```

在方法前加上装饰器`@pytest.mark.smoke`(`somke`可以自己随便取名), 比如想把一些测试用例作为冒烟测试, 在开发提测后先跑一遍, 只想跑这些冒烟, 这时候就可以用这种方法:

`pytest -v -m "smoke" test.py`

> 如何注册marker?

[Registering custom markers](https://docs.pytest.org/en/latest/writing_plugins.html#registering-custom-markers)

If your plugin uses any markers, you should register them so that they appear in pytest’s help text and do not cause spurious warnings. For example, the following plugin would register `cool_marker` and `mark_with` for all users:

```python
def pytest_configure(config):
    config.addinivale_line("markers", "cool_markder: this one is for cool tests.")
    config.addinivalue_line(
        "markers", "mark_with(arg, arg2): this marker takes arguments."
    )
```

## 注册标记来防范拼写错误

自定义标记可以简化测试工作,但是标记容易拼写错误(比如`@pytest.mark.smoke`写成了`@pytest.mark.smoke1`),这种情况下不会引起错误,pytest以为这是另外一个标记.为了避免拼写错误,可以在`pytest.ini`文件里注册标记

```ini
markers = 
	smoke: run the smoke test functions for test project
```

可以通过命令查看:

`pytest --markers`

没有注册的标记不会出现在 `--markers`列表里, 同时还需要使用 `—strict`选项(在`addopts`里),遇到拼写错误的标记或未注册的标记就会报错

## 如何使用allure生成报告

1. `brew install allure`

2. 安装`pytest-allure`

3. 运行case时增加命令行选项 `pytest -v  —-alluredir ./allure-results test.py`

   `./allure-results`指生成allure结果的文件夹地址,生成结果是一些json文件

4. 生成测试报告: `allure generate allure-results -o allure`

   在第3步生成了数据文件后,还要执行这句话来生成html格式的报告, 其中allure-results是数据文件夹名称, allure是html报告文件夹名称, 可根据需要自行编写

## 指定pytest的最低版本号

`minversion = 5.0`

`minversion`选项可以指定运行测试用例的pytest的最低版本

## 指定pytest忽略某些目录

pytest执行用例搜索时,会递归遍历所有子目录,包括某些你明知没必要遍历的目录

`norecursedirs = .* data config utils`

可以使用`norecursedirs`缩小`pytest`的搜索范围

指定访问目录

`testpaths = tests`

## 避免文件名冲突

增加`__init__.py`文件

## Pytest 官网文档

### [Marking test functions with attributes](https://docs.pytest.org/en/stable/mark.html)

### [Using markers to pass data to fixtures](https://docs.pytest.org/en/stable/fixture.html#using-markers-to-pass-data-to-fixtures)

### [Using marks with parametrized fixtures](https://docs.pytest.org/en/stable/fixture.html#using-marks-with-parametrized-fixtures)



# [pytest测试框架3-如何将测试代码与测试数据分离？](https://www.bilibili.com/video/BV1M4411o7vV/)

本节课主要讲解参数化测试

参数化测试允许传递多组数据,一旦发现测试失败, pytest会及时报告

`@pytest.mark.parametrize(argnames, argvalues)`装饰器可以达到批量传送参数的目的

这个装饰器是放在测试用例前, 一个参数是argnames, 就是在case里调用的名字, 第二个就是这个名字对应的值.

首先来看一个不用装饰器的例子:

## 不用装饰器

第一步: 用python的requests请求一个接口:

```python
import requests
import pytest
import allure

class TestParam1:
    """
    """
    @pyest.fixture(scope="class", autouse=True)
    def prepare(self, request):
        with allure.step("测试数据准备:"):
            pass
          
        @allure.step("测试数据数据清理:")
        def fin():
            """
            Clean up test environment after testing
            """
            pass
        request.addfinalizer(fin)
        
    def test_param_1(self):
        with allure.step("发起API请求"):
            url = "http://127.0.0.1:8000/add_message/"
            headers = {
                'Content-Type': "application/x-www-form-urlencoded",
            }
            payload = {
                "mid": "104",
                "name": "adroid3",
                "content": "8",
                "status": "1",
                "author": "xixi"
            }
            response = requests.request("POST", url, data=payload, headers=headers)
            print(response.json())
            assert response.json()['message'] == "add message success"
```

执行这个脚本,返回的数据为:

`{'message': 'add message success', 'status': 200}`

## 测试数据与测试用例相分离

第二步: 把测试数据和测试case相分离

```python
import requests
import pytest
import allure

param = [
  	({'Content-Type': "application/x-www-form-urlencoded"}, {"mid": "104","name": "adroid3", "content": "8", "status": "1", "author": "xixi"}),
  	({'Content-Type': "application/x-www-form-urlencoded"}, {"mid": "104","name": "adroid3", "content": "8", "status": "1", "author": "xixi"}),
  	({'Content-Type': "application/x-www-form-urlencoded"}, {"mid": "104","name": "adroid3", "content": "8", "status": "1", "author": "xixi"})
]

class TestParam2:
    """
    """
    @pyest.fixture(scope="class", autouse=True)
    def prepare(self, request):
        with allure.step("测试数据准备"):
            pass
          
        @allure.step("测试数据数据清理:")
        def fin():
            """
            Clean up test environment after testing
            """
            pass
        request.addfinalizer(fin)
        
    @pytst.mark.parametrize("headers, payload", param)
    def test_param_2(self, headers, payload):
        url = "http://127.0.0.1:8000/add_message/"
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.json())
        assert response.json()['message'] == "add message success"
```

使用`@pytst.mark.parametrize`有两个要点:

1. 在装饰器里列出要取的字段的名字(这部分是说在方法中的参数, 比如上例, 方法中的参数是headers和payload, 所以要写在第一个参数的位置, 并且要用引号包裹), 以及从哪取(就是param, 相当于数据源)
2. 在测试用例里把这两个参数传进去(这个地方还要注意: 并不是在装饰器里写了参数名字方法就可以直接用了, 而是要在方法的入参中再显式地写一下, 才能够顺利引用)

## 测试数据独立成文件

再下一步就是把测试数据单拎出来成为一个文件 ,实现真正的与测试用例相分离.

data下的层级目录要和测试样例下面的一样,这样好找测试数据.测试数据存成json格式.

怎么找:

我们要写两个函数,

1. 找到测试数据所在的目录

   测试数据和测试case地址的区别:

   测试case: `/Users/echo/Documents/python/untitled11/tests/test_params/test1.py`

   测试数据: `/Users/echo/Documents/python/untitled11/data/test_params/test1.json`

   一共有两处不同, 一个是要把tests目录变成data, 另一个是要把py变成json, 所以我们就可以根据测试用例所在的目录获取测试数据所在的目录

2. 用python读取文件的方法读取每条测试数据(获取测试数据的函数是放在utils下面的)

```python
# 在utils下新建get_data.py

import os

def get_data_path(case_path):
	file_name = os.path.dirname(case_path).split(os.sep+'tests'+os.sep, 1)
    print(file_name)
    test_data = os.sep.join([filename[0],'data',file_name[1], os.path.basename(case_path).replace('.py', '.json')])
    return test_data
```

case_path 传入的是像 `/Users/echo/Documents/python/untitled11/tests/test_params/test1.py` 这种绝对路径. `os.path.dirname` 获取的是该文件所在目录, `os.path.basename` 获取的是该文件的名字, 去掉前面的所有路径信息.

`os.path.dirname(case_path)`获取到case的目录后, 是一个字符串, 然后使用字符串的`str.split`的方法对这个字符串进行分割, 其中 `os.sep+"tests"+os.sep`是使用`\tests\`作为分隔符, 然后分割1次, 最终得到的启示就是`tests`的父级目录和在`tests`下的子目录名字. 然后就是用`os.sep`来进行`join`, 包括tests的父级目录+data+tests的子目录+文件名.

文件名这里用到了`os.path.basename`, 得到文件名后再使用字符串的`replace`方法对文件名后缀进行替换.

> 之前可能和`os.path.split`方法有点混淆了. `os.path.split`是用来分割一个绝对路径的文件目录和文件名的, 只要把一个绝对路径传进去就行了, 不需要传分隔符和最大分割几次这些参数, 默认就是分割最后一个slash之前和之后的内容, 得到一个元组.
>
> 而字符串的`str.split`方法是来分割一个字符串的, 需要传入分隔符和最大分割几次.
>
> 还有一个`os.path.splitext`, 是用来得到文件的扩展名的, 也是只需要传入一个路径地址就行了.

测试数据是一个json文件: json文件里有一个字典, 字典里有一个key叫test, test的value值就是多组测试用例,都存在一个列表里, 列表里有一个个字典, 每一个字典就是一组测试数据, 字典里有几个key就是接口需要的测试数据, case就是接口测试用例名,

json文件格式:

```json
{
  "test": [
    {
      "case": "this is name1",
      "cookies": {
        "JSESSIONID": "1g8git7dix5q51oblwxblipy7v"
      },
      "params": {
        "fetchRoles": true,
        "_dc": 1607844270887,
        "statusType": -1
      },
      "expected": {
      }
    },
    
    {
      "case": "this is name2",
      "cookies": {
        "JSESSIONID": "1g8git7dix5q51oblwxblipy7v"
      },
      "params": {
        "fetchRoles": true,
        "_dc": 1607844270887,
        "statusType": -1
      },
      "expected": {
      }
    },
    
    {
      "case": "this is name3",
      "cookies": {
        "JSESSIONID": "1g8git7dix5q51oblwxblipy7v"
      },
      "params": {
        "fetchRoles": true,
        "_dc": 1607844270887,
        "statusType": -1
      },
      "expected": {
      }
    }
  ]
}
```

然后就是想办法把他们提取出来, 提取成之前param的样子, 就是一个列表里包含多个元组, 然后每个元组里包含多个字典, 每个字典对应一个参数.

```python
def get_test_data(test_data_path):
    case = []
    headers = []
    querystring = []
    payload = []
    expected =[]
    with open(test_data_path, encoding='utf-8') as f:
        dat = json.loads(f.read())
        test = dat['test']  # 得到的是一个列表
        for td in test: # 循环列表里的每个字典
          case.append(td['case'])  # 取到每个字典里的对应关键字的值后存到对应的列表里
          headers.append(td.get('headers', {}))
          querystring.append(td.get('querystring', {}))
          payload.append(td.get('payload', {}))
          expected.append(td.get('expected', {}))
   list_parameters = list(zip(case, headers, querystring, payload, expected))
   return case, list_parameters
```

zip解释:

```python
case = [1, 2, 3]
headers = [4, 5, 6]
query= [7, 8, 9]
zip(case, headers, query)
<zip object at 0x102199848>
```

意思就是取了1,4,7为一个元组, 2,5,8为一个元组

然后再`list()`变成列表格式

```python
>>> list(zip(case, headers, query))
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
```

这个形式和之前param的形式是一样的.

到这一步就可以把测试case中的数据删掉了, 替换为

```python
import pytest
import requests

from utils.get_data import get_data_path
from utils.get_data import get_test_data

param = get_test_data(get_data_path(__file__))
```

然后为了区分每组数据跑的测试用例,我们加入id, 

```python
# 在get_test_data 里多返回一个case
return case, list_parameters

# 然后在测试样例的py文件里添加:
case, param = get_test_data(get_data_path(__file__))

# 在测试样例的parametrize装饰器里添加ids
@pytest.mark.parametrize("case,headers,querystring,payload,expected", param, ids=case)
def test_param_2(self, case, headers, querystring, payload, expected):
```

## 1213自测结果

## Pytest 官网

### [Parametrizing fixtures and test functions](https://docs.pytest.org/en/stable/parametrize.html)

Pytest enables test parametrization at several levels:

* pytest.fixture() allows one to parametrize fixture functions.
* @pytest.mark.parametrize allows one to define multiple sets of arguments and fixtures at the test function or class.
* pytest_generate_tests allows one to define custom parametrization schemes or extensions

#### @pytest.mark.parametrize: parametrizing test functions

The builtin `pytest.mark.parametrize` decorator enables parametrization of arguments for a test function. Here is a typical example of a test function that implements checking that a certain input leads to an expected output:

### [Parametrizing tests](https://docs.pytest.org/en/stable/example/parametrize.html#paramexamples)



# [pytest测试框架4-插件与hook函数](https://www.bilibili.com/video/BV1k4411C7X4)

## 简介

pytest的自带功能很强大,通过添加插件可以扩展功能,pytest 的代码结构适合定制和扩展插件,可以借助hook函数来实现.

把fixture 函数或者hook函数添加到conftest文件里,就已经创建了一个本地的conftest插件

## pytest plugin 加载的几种方式

1. 内置plugins: 从代码内部的`_pytest`目录加载

2. 外部插件(第三方插件): 通过setuptools entry points 机制发现的第三方插件模块

   推荐的第三方的pytest插件: https://docs.pytest.org/en/latest/plugins.html

3. `conftest.py`形式的本地插件: 测试目录下的自动模块发现机制

通过`pytest -—trace-config` 命令可以查看当前pytest 中所有的plugin

在pytest中,所谓plugin其实就是能被pytest发现的一些带有pytest hook方法的文件或对象.

## What is a hook

要理解pytest hook, 首先要知道什么是hook方法(钩子函数)

这里举一个简单的例子,比如说你写了一个框架类的程序, 然后你希望这个框架可以“被代码注入”, 即别人可以加入代码对你这个框架进行定制化, 该如何做比较好? 一种很常见的方式就是约定一个规则,框架初始化时会收集满足这个规则的所有代码(文件), 然后把这些代码加入到框架中来,在执行时一并执行即可.所以这一规则下可以被框架收集到的方法就是hook方法.

## 编写自己的插件

插件可以改变pytest行为,可用的hook函数很多,详细的定义:

http://doc.pytest.org/en/latest/_modules/_pytest/hookspec.html

1. `pytest_addoption`为例, 基本每个pytest plugin 都会有这个hook方法, 它的作用是为pytest命令行添加自定义的参数.

   `parser`: 用户命令行参数与ini文件值的解析器

```python
def pytest_addoption(parser):
  	group = parser.getgroup('xiaoyulaoshi auto test')
    group.addoption("--env", 
                    default="test",
                    dest="env",
                    help="set test run env")
    
@pytest.fixture(scope="session")
def cmdopt(request):
    return request.config.getoption("--env", default='test')
  
@pytest.fixture(scope="session", autouse=True)
def env(request, cmdopt):
    # load remote config settings
    request.config.base_data = collect_static_data(cmdopt, str(request.config.rootdir))
    return request.config.base_data
```

测试case如何使用env:

```python
import requests
from utils.get_data import get_data_path
from utils.get_data import get_test_data
import logging
case, par_to_test = get_test_data(get_data_path(__file__))


class TestFixture:
   	def test_fixture(self, param, env):
        url = env["host"]["local"] + env["APIs"]["add_message"]
        response = requests.request("POST", url, data=param[3], headers=param[1])
        res = response.json()
        print(res)
```



`pytest_addoption`:hook function, 这里创建了一个argparser的group, 通过addoption方法添加option, 使得显示help信息时相关option 显示在一个group下面,更加友好

2. 修改`pytest_collection_modifyitems`

能解决什么实际问题?

测试case中case名字为中文时,显示的是乱码

完成所有测试项的收集后, pytest调用的钩子

```python
def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时,将收集到的item的name和nodeid的中文显示在控制台上,所有的测试用例收集完毕后调用,可以再次过滤或者对他们重新排序
    items (收集的测试项目列表)
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")   
```

3. 可以实现自己的自定义动态参数化方案或扩展

```python
# 也是写在conftest.py里的
def pytest_generate_tests(metafunc):
    """generate (multiple) parametrized calls to a test function"""
    if "param" in metafunc.fixturenames:
        metafunc.parametrize("param", 
                             metafunc.module.par_to_test,ids=metafunc.module.case,  		
                             scope="function")
```

使用的例子看上面, 其中`par_to_test`和`case`都是定义好的返回数据

## 总结

pytest通过这种plugin的方式,大大增强了这个测试框架的实用性,可以看到pytest本身的许多组件也是通过plugin的方式加载的,可以说pytest就是由许许多多个plugin组成的.另外,通过定义好一些hook spec, 可以有效地控制plugin的“权限”, 再通过类似pytest.hookimpl这样的装饰器又可以增强了各种plugin的“权限”.这种设计对于pytest这样复杂的框架而言无疑是非常重要的,这可能也是pytest相比于其他测试框架中越来越火的原因吧.



[incremental testing - test steps](https://docs.pytest.org/en/latest/example/simple.html#incremental-testing-test-steps)

Sometimes you may have a testing situation which consists of a series of test steps. If one step fails it makes no sense to execute further steps as they are all expected to fail anyway and their tracebacks add no insight. Here is a simple `conftest.py` file which introduces an `incremental` marker which is to be used on classes:

```python
from typing import Dict, Tuple
import pytest

# store history of failures per test class name and per index in parametrize(if parametrize used)
_test_failed_incremental: Dict[str, Dict[Tuple[int, ...], str]] = {}
  
def pytest_runtest_makereport(item, call):
    if "incremental" in item.keywords:
        # incremental marker is used
        if call.excinfo is not None:
            # the test has failed
            # retrieve the class name of the test
            cls_name = str(item.cls)
            # retrieve the index of the test (if parametrize is used in combination 							with incremental)
            parametrize_index = (
            	  tuple(item.callspec.indices.values()))
                if hasattr(item, "callspec")
                else()
            )
            # retrieve the name of the test function
            test_name = item.originalname or item.name
            # store in _test_failed_incremental the original name of the failed test
            _test_failed_incremental.setdefault(cls_name, {}).setdefault(
                parametrize_index, test_name    
            )
            

            
```



https://docs.pytest.org/en/latest/mark.html

https://www.jianshu.com/p/4c214fa3e0f3

https://docs.pytest.org/en/latest/example/markers.html

https://www.jianshu.com/p/54b0f4016300

https://docs.pytest.org/en/latest/fixture.html

https://docs.pytest.org/en/latest/_modules/_pytest/hookspec.html

https://docs.pytest.org/en/latest/example/simple.html#incremental-testing-test-steps

# [Pytest 官网补充](https://docs.pytest.org/en/stable/contents.html)

## Installation and Getting Started

### Install pytest

### Create your first test

### Run multiple tests

### Assert that a certain exception is raised

### Group multiple tests in a class

### Request a unique temporary directory for functional tests

### Continue reading

## Usage and Invocations

### Calling pytest through `python -m pytest`

### Possible exit codes

### Getting help on version, option names, environment variables

### Stopping after the first (or N) failures

### Specifying tests / selecting tests

### Modifying Python tracebck printing

### Detailed summary report

### Dropping to PDB (Python Debugger) on failures

### Dropping to PDB (Python Debugger) at the start of a test

### Setting breakpoints

### Using the bulitin breakpoint function

### Profiling test execution duration

### Fault Handler

### Warning about unraisable exceptions and unhandled thread exceptions

### Creating JUnitXML format files

### Creating resultlog format files

### Sending test report to online pastebin service

### Early loading plugins

### Disabling plugins

### Calling pytest from Python code

## Using pytest with an existing test suite

### Running an existing test suite with pytest

## The writing and reporting of assertions in tests

### Asserting with the assert statement

### Assertions about expected exceptions

### Assertions about expected warnings

### Making use of context-sensitive comparisons

### Defining your own explanation for failed assertions

### Assertion introspection details

## pytest fixtures: explicit, modular, scalable

### Fixtures as Function arguments

### Fixtures: a prime example of dependency injection

### conftest.py: sharing fixture functions

### Sharing test data

### Scope: sharing fixtures across classes, modules, packages or session

### Order: Higher-scoped fixtures are instantiated first

### Fixture finalization / executing teardown code

### Fixtures can introspect the requestiong test context

### Using markers to pass data to fixutures

### Factories as fixtures

### Parametrizing fixtures

### Using marks with parametrized fixtures

## Good Integration Practices

### Install package with pip

For deveopment, we recommend you use venv for virtual environments and pip for installing your application and any dependencies, as well as the pytest package itself. This ensures your code and dependencies are isolated from your system Python installation.

Next, place a `setup.py` file in the root of your package with the following minimum content:

```python
from setuptools import setup, find_packages

setup(name="PACKAGENAME", packages=find_packages())
```

Where `PACKAGENAME` is the name of your package. You can then install your package in “editable” mode by running from the same directory:

```python
pip install -e .
```

which lets you change your source code (both tests and application) and return tests at will. This is similar to running python setup.py develop or conda develop in that it installs your package using a symlink to your development code.

扩展阅读：https://stackoverflow.com/questions/19048732/python-setup-py-develop-vs-install

https://zhuanlan.zhihu.com/p/162842824

### Conventions for Python test discovery

pytest implements the following standard test discovery:

* if no arguments are specified then collection starts from testpaths(if configured) or the current directory. Alternatively, command line arguments can be used in any combination of directories, file names or node ids.
* Recurse into directories, unless match norecursedirs.
* In those directories, search for `test_*.py` or `*_test.py` files, imported by their test package name.
* From those files, collect test items:
	* test prefixed test functions or methods outside of class
	* test prefixed test functions or methods inside Test prefixed test classes(without an `__init__` method)

For examples of how to customize your test discovery Changing stardard(Python) test discovery.

Within Python modules, pytest alos discovers tests using the standard unittest.TestCase subclassing technique.

### Choosing a test layout / import rules

### tox

## Flaky tests

### Why flaky tests are a problem

### Potential root causes

### Pytest features

### Other general strategies

### Research

### Resources



# allure 介绍

Allure Framework is a flexible lightweight multi-language test report 

# [【软件测试教程】Allure一节课学会生成业内最优秀的自动化测试报告](https://www.bilibili.com/video/BV1Hz4y1Q7Xu)

Allure 实现自动化测试用例与手工测试用例关联的作用

## allure介绍

* allure 是一个轻量级, 灵活的, 支持多语言的测试报告工具
* 多平台的, 奢华的report框架
* 可以为dev/qa 提供详尽的测试报告、测试步骤、log
* 也可以为管理层提供high level统计报告
* java语言开发的,支持pytest, javascript, PHP, ruby等
* 可以集成到Jenkins

## allure安装

## pytest-allure插件

## Allure 报告的生成

## allure 特性分析

### 场景:

​			希望在报告中看到测试功能, 子功能或场景, 测试步骤, 包括测试附加信息

### 解决:

​			`@feature`, `@story`, `@step,` `@attach`

### 步骤:

* import allure
* 功能加上`@allure.feature(“功能名称”)`
* 子功能上加`@allure.story(“子功能名称”)`
* 步骤上加`@allure.step(“步骤细节”)`
* `@allure.attach(“具体文本信息”)`, 需要附加的信息, 可以是数据, 文本, 图片, 视频, 网页
* 如果只测试登录功能运行的时候可以加限制过滤:
  * `pytest 文件名 --allure-features='购物车功能' --alure-stories='加入购物车'`

示例:

```python
def test_search(""):
    with allure.step("第一步: 打开搜索页面")
    
```

清理存在的目录使用 `--clean-alluredir`

## 按feature, story运行

注解`@allure.feature` 与 `@allure.story` 的关系

feature相当于一个功能, 一个大的模块, 将case分类到某个feature中, 报告中behavior中显示, 相当于testsuite

story相当于对应这个功能或者模块下的不同场景, 分支功能, 属于feature之下的结构, 报告在features中显示, 相当于testcase

feature与story类似于父子关系

```python
@allure.feature("登录类")
class TestLoginDemo:
    def test_login1(self):
        allure.attach('<img>...', attachment_type=allure.attachment_type.HTML)
        allure.attach.file('路径地址', attachment_type=allure.attachment_type.PNG)
        allure.attach.file()
    
```

Allure 生成包含日志, html代码片段, 图片, 视频

关联测试用例, 



## allure+pytest+selenium 实战演示



















