# [Allure一自动化测试报告](https://www.bilibili.com/video/BV1Hz4y1Q7Xu)

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

# [Allure 官网介绍](https://docs.qameta.io/allure/)

Allure Framework is a flexible lightweight multi-language test report tool that not only shows a very concise representation of what have been tested in a neat web report form, but allows everyone participating in the development process to extract maximum of useful information from everyday execution of tests.

From the dev/qa perspective Allure reports shorten common defect lifecycle: test failures can be divided on bugs and broken tests, also logs, steps, fixtures, attachments, timings, history and integrations with TMS and bug-tracking systems can be configured, so the responsible developers and testers will have all information at hand.

From the managers perspective Allure provides a clear 'big picture' of what features have been covered, where defects are clustered, how the timeline of execution looks like and many other convenient things. Modularity and extensibility of Allure guarantees that you will always be able to find-tune[^0-0-0-1] something to make Allure suit you better.

## 1. About

### 1.1 Copyright

The Allure reference guide is available as HTML documents. The latest copy is available at https://docs.qameta.io/allure/

Copies of this document may be made for your own use and for distribution to others, provided that you do not charge any fee for such copies and further provided that each copy contains this Copyright Notice, whether distributed in print or electronically.

### 1.2 Get Help

There are several places to get help:

* Contact the community on [Gitter](https://gitter.im/allure-framework/allure-core). We also have a Russian-speaking room.
* Ask a question on [Stack Overflow](https://stackoverflow.com/questions/ask?tags=allure) or Stack Overflow in Russian.
* Report bugs in [GitHub issues](https://github.com/allure-framework/allure2/issues/new?).

### 1.3 How to Proceed

* Open the [demo version](http://demo.qameta.io/allure/latest/) to see what an Allure report looks like.
* Go to <u>Get started</u> to build a report for an existing project.
* Learn more about [report structure and features](https://docs.qameta.io/allure/latest/#_report_structure).
* Integrate your favorite testing framework with Allure. Supported frameworks are grouped by language: Java, Python, JavaScript, Ruby, Groovy, PHP, .Net and Scala.

## 2. Get Started

To generate your first report you will need to go through just a few simple steps:

* Downloading and installing Allure commandline application suitable for your environment.
* Locating test execution data that you have to build a report on.

### 2.1 Installing a commandline

Several options for Allure installation are currently supported:

#### 2.1.1. Linux

For Debian-based repositories a PPA is provided:

```shell
sudo apt-add-repository ppa:qameta/allure
sudo apt-get update
sudo apt-get install allure
```

#### 2.1.2. Mac OS X

For Mac OS, automated installation is available via [Homebrew](https://brew.sh/)

```shell
brew install allure
```

#### 2.1.3. Windows

For Windows, Allure is available from the [Scoop](http://scoop.sh/) commandline-installer.

To install Allure, download and install Scoop and then execute in the PowerShell:

```powershell
scoop install allure
```

Also Scoop is capable of updating Allure distribution installations. To do so navigate to the Scoop installation directory and execute

```powershell
\bin\checkver.ps1 allure -u
```

This will check for newer versions of Allure, and update the manifest file. Then execute

```powershell
scoop update allure
```

to install a newer version. ([documentation](https://github.com/lukesampson/scoop/wiki/App-Manifest-Autoupdate))

#### 2.1.4. Manual installation

1. Download the latest version as zip archive from [Maven Central](https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/).
2. Unpack the archive to allure-commandline directory.
3. Navigate to <u>bin</u> directory.
4. Use <u>allure.bat</u> for Windows or allure for other Unix platforms.
5. Add allure to system PATH.

> To run commandline application, Java Runtime Environment must be installed.

#### 2.1.5. Check the installation

Execute `allure --version` in console to make sure that allure is now available:

```shell
$ allure --version
2.0.1
```

### 2.2 Test execution

> If you are using IDE to run tests locally it may ignore Allure configuration specified in build file (as IntelliJ IDEA does). In order to make it work consider using `allure.properties`  file to configure Allure. Check out configuration section for more information.

Before building a report you need to run your tests to obtain some basic test report data. Typically it might be a junit-style xml report generated by nearly every popular test framework. For example, suppose you have test reports automatically created by surefire maven plugin stored in the `target/surefire-reports`:

![](https://docs.qameta.io/allure/images/get_started_surefire-report.png)

### 2.3 Report generation

This is already enough to see the Allure report in one command:

`allure serve /home/path/to/project/target/surefire-reports/`

Which generates a report in temporary folder from the data found in the provided path and then creates a local Jetty server instance, serves generated report and opens it in the default browser. It is possible to use a `--profile` option to enable some pre-configured allure setting. junit profile is enabled by default, you will learn more about profiles in the following section.

This would produce a report with a minimum of information extracted from the xml data that will lack nearly all of the advanced allure features but will allow you to get a nice visual representation of executed tests.

![](https://docs.qameta.io/allure/images/get_started_report_overview.png)

## 3. Report structure

Once you’ve got the idea what the report does look like. You will probably want to get more data-rich reports. You might have to consider using one of the Allure adaptors for your testing framework, which will allow to collect much more information. Jump to the integrations section to learn more about integration with testing frameworks.

Typical report consists of ‘Overview’ tab, navigation bar, several tabs for different kinds of test data representation and test case pages for each individual test. ==Each Allure report is backed by a tree-like data structure, that represents a test execution process.== Different tabs allow to switch between the views of the original data structure thus giving a different perspective. Note that all tree-like representations including Behaviors, Categories, xUnit and Packages support filtering and are sortable.

### 3.1. Overview page

Entry point for every report would be the ‘Overview’ page with dashboards and widgets:

![](https://docs.qameta.io/allure/images/tab_overview.png)

Overview page hosts several default widgets representing basic characteristics of your project and test environment.

* Statistics - overall report statistics.
* Launches[^3-1-1] - if this report represents several test launches, statistics per launch will be shown here.
* Behaviors - information on results aggregated according to stories and features
* Executors - information on test executors that were used to run the tests.
* History Trend - if tests accumulated some historical data, it’s trend will be calculated and shown on the graph.
* Environment - information on test environment (see [how to define environment](https://docs.qameta.io/allure/#_environment)).

Home page widgets are draggable and configurable. Also, Allure supports it’s own plugin system, so quite different widget layouts are possible.

Navigation bar is collapsible and enables you to switch into several of the basic results overview modes.

### 3.2 Categories

Categories tab gives you the way to [create custom defects classification](https://docs.qameta.io/allure/#_categories_2) to apply for test results.

![](https://docs.qameta.io/allure/images/tab_categories.png)

### 3.3 Suites

On the Suites tab a standard structural representation of executed tests, grouped by suites and classes can be found.

![](https://docs.qameta.io/allure/images/tab_suites.png)

### 3.4 Graphs

Graphs allow you to see different statistics collected from the test data: statuses breakdown or severity and duration diagrams.

![](https://docs.qameta.io/allure/images/tab_graphs.png)

### 3.5 Timeline

Timeline tab visualizes retrospective of tests execution, allure adaptors collect precise timings of tests, and here on this tab they are arranged accordingly to their sequential or parallel timing structure.

![](https://docs.qameta.io/allure/images/tab_timeline.png)

### 3.6 Behaviors

For Behavior-driven approach, this tab groups test results according to Epic, Feature and Story tags.

![](https://docs.qameta.io/allure/images/tab_behaviors.png)

### 3.7 Packages

Packages tab represents a tree-like layout of test results, grouped by different packages.

![](https://docs.qameta.io/allure/images/tab_packages.png)

### 3.8 Test case page

From some of the results overview pages described above you can go to the test page after clicking on the individual tests. ==This page will typically contain a lot of individual data related to the test case: steps executed during the test, timings, attachments, test categorization labels, descriptions and links.==

## 4. Features

This section describes the main features of Allure. For example, you can group your tests by stories or features, attach files, and distribute assertions over a set of custom steps, among other features. All features are supported by Java test frameworks, so we only provide Java examples here. For details on how a particular adapter works with the test framework of your choice, refer to the adapter guide.

### 4.1 Flaky tests

In real life not all of your tests are stable and always green or always red. A test might start to “blink” i.e. it fails from time-to-time without any obvious reason. you could disable such a test, that is a trivial[^4-1-1] solution. However what if you do not want to do that? Say you would like to get more details on possible reasons or the test is so critical that even being flaky it provides helpful information? You have an option now to mark such tests in a special way, so the resulting report will clearly show them as unstable:

```java
@Flaky
public void aTestWhichFailsFromTimeToTime {
    ...
}
```

Here is what you get in the report if such a test failed:

![](https://docs.qameta.io/allure/images/flaky_failed.png)

> you can mark a whole test class as flaky as well.

### 4.2 Environment

To add information to Environment widget just create `environment.properties`(or `environment.xml`) file to `allure-results` directory before report generation.

*environment.properties*

```properties
Browser=Chrome
Browser.Version=63.0
Stand=Production
```

*environment.xml*

```xml
<environment>
	<parameter>
    	<key>Browser</key>
        <value>Chrome</value>
    </parameter>
    <parameter>
    	<key>Browser.Version</key>
        <value>63.0</value>
    </parameter>
    <parameter>
    	<key>Stand</key>
        <value>Production</value>
    </parameter>
</environment>
```

### 4.3 Categories

There are two categories of defects by default:

* ==Product defects (failed tests)==
* ==Test defects(broken tests)==

To create custom defects classification add `categories.json` file to `allure-results` directory before report generation.

*categories.json*

```json
[
  {
    "name": "Ignored tests", 
    "matchedStatuses": ["skipped"]
  },
  {
    "name": "Infrastructure problems",
    "matchedStatuses": ["broken", "failed"],
    "messageRegex": ".*bye-bye.*"
  },
  {
    "name": "Outdated tests",
    "matchedStatuses": ["broken"],
    "traceRegex": ".*FileNotFoundException.*"
  },
  {
    "name": "Product defects",
    "matchedStatuses": ["failed"]
  },
  {
    "name": "Test defects",
    "matchedStatuses": ["broken"]
  }  
]
```

:one: (mandatory) category name

:two: (optional) list of suitable test statuses. Default `["failed", "broken", "passed", "skipped", "unkonwn"]`

:three: (optional) regex pattern to check test error message. Default `".*"`

:four: (optional) regex pattern to check stack trace. Default `".*"`

Test result falls into the category if its status is in the list and both error message and stack trace match the pattern.

> `categories.json` file can be stored in test resources directory in case of using [allure-maven](https://docs.qameta.io/allure/#_maven_5) or [allure-gradle](https://docs.qameta.io/allure/#_gradle_4) plugins.

## 6.1 Pytest

### 6.1.1. Installation

Pytest is available for installation from the [PyPI](https://pypi.python.org/pypi/allure-pytest), therefore installation with pip is recommended. To install the latest version, execute from the command line:

```shell
$ pip install allure-pytest
```

That will install allure-pytest and allure-python-commons packages to produce report data compatible with Allure 2. If you are using a previous version of adapter for the first generation of Allure reports then you will need to uninstall it first.

### 6.1.2. Usage

To enable Allure listener to collect results during the test execution simply add `–-alluredir` option and provide path to the folder where results should be stored. E.g.:

```shell
$ pytest --alluredir=/tmp/my_allure_results
```

To see the actual report after your tests have finished, you need to use Allure commandline utility to generate report from the results.

```shell
$ allure serve /tmp/my_allure_results
```

This command will show you generated report in your default browser.

### 6.1.3. Basic Reporting

Your can see all default pytest statuses in the Allure report: <u>only tests that were not succeeded due to one of the assertion errors will be marked as ==failed==, any other exception will cause a test to have a ==broken== status.</u>

```python
import pytest

def test_success():
    """This test succeeds"""
    assert True

def test_failure():
    """This test fails"""
    assert False
    
def test_skip():
    """This test is skipped"""
    pytest.skip('for a reason!')
    
def test_broken():
    raise Exception('oops')
```

### 6.1.4. Supported Pytest features

Some of the common Pytest features that the Allure report supports include xfails, fixtures and finalizers, marks, conditional skips and parametrization.

#### xfail

This is pytest way of marking expected failures: ([Pytest docs](https://docs.pytest.org/en/latest/skipping.html))

```python
@pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
def test_xfail_expected_failure():
    """this test is an xfail that will be marked as expected failure"""
    assert False
    
@pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
def test_xfail_unexpected_pass():
    """this test is an xfail that will be marked as unexpected success"""
    assert True
```

Which results in test being skipped and marked with a special tag when it is expected to fail.

![](https://docs.qameta.io/allure/images/pytest_xpass_expected_failure.png)

And special marking in description and a special tag when it unexpectedly passed.

![](https://docs.qameta.io/allure/images/pytest_xpass_unexpected_pass.png)

#### Conditional mark

In Pytest you can conditionally mark a test to not be executed under some specific conditions ([Pytest docs](https://docs.pytest.org/en/latest/skipping.html)):

```python
@pytest.mark.skipif('2 + 2 != 5', reason='This test is skipped by a triggered condition in @pytest.mark.skipif')
def test_skip_by_triggered_condition():
    pass
```

When condition is evaluated to true, test receives a 'Skipped' status in report, a tag and a description from the decorator.

![](https://docs.qameta.io/allure/images/pytest_conditional_skip.png)

#### Fixtures and Finalizers

Fixtures and finalizers are the utility functions that will be invoked by Pytest before your test starts and after your test ends respectively. Allure tracks invocations of every fixture and shows in full details what methods with what arguments were invoked, preserving the correct sequence of the calls that were made. ([Pytest docs](https://docs.pytest.org/en/latest/reference.html#id30))

You don’t need to mark your fixtures to make them visible in the report, they will be detected automatically for different scopes.

```python
@pytest.fixture(params=[True, False], ids=['param_true', 'param_false'])
def function_scope_fixture_with_finalizer(request):
    if request.param:
        print('True')
    else:
        print('False')
    def function_scope_finalizer():
        function_scope_step()
    request.addfinalizer(function_scope_finalizer)

    
@pytest.fixture(scope='class')
def class_scope_fixture_with_finalizer(request):
    def class_finalizer_fixture():
        class_scope_step()
  	request.addfinalizer(class_finalizer_fixture)
    

@pytest.fixture(scope='module')
def module_scope_fixture_with_finalizer(request):
    def module_finalizer_fixture():
        module_scope_step()
    request.addfinalizer(module_finalizer_fixture)
    
    
@pytest.fixture(scope='session')
def session_scope_fixture_with_finalizer(request):
    def session_finalizer_fixture():
        session_scope_step()
    request.addfinalizer(session_finalizer_fixture)
    
    
class TestClass:
    
    def test_with_scoped_finalizers(self,
                                    function_scope_fixture_with_finalizer,
                                   	class_scope_fixture_with_finalizer,
                                    module_scope_fixture_with_finalizer,
                                    session_scope_fixture_with_finalizer):
        stpe_inside_test_body()
```

![](https://docs.qameta.io/allure/images/pytest_skoped_finalizers.png)

Depending on an outcome of a fixture execution, test that is dependent on it may receive a different status. <u>Exception in the fixture would make all dependent tests broken, `pytest.skip()` call would make all dependent test skipped.</u>

```python
import pytest

@pytest.fixture
def skip_fixture():
    pytest.skip()
    
@pytest.fixture
def fail_fixture():
    assert False
    
@pytest.fixture
def broken_fixture():
    raise Exception("Sorry, it's broken")
    
def test_with_pytest_skip_in_the_fixture(skip_fixture):
    pass

def test_with_failure_in_the_fixture(fail_fixture):
    pass

def test_with_broken_fixture(broken_fixture):
    pass
```

![](https://docs.qameta.io/allure/images/pytest_fixture_effect.png)

#### Parametrization

You can generate many test cases from the sets of input parameters using `@pytest.mark.parametrize`.([Pytest docs](https://docs.pytest.org/en/latest/skipping.html))

All argument names and values will be captured in the report, optionally argument names will be replaced with provided string descriptions in the `ids` kwarg.

```python
import allure
import pytest


@allure.step
def simple_step(step_param1, step_param2 = None):
    pass

@pytest.mark.parametrize('param1', [True, False], ids=['id explaining value 1', 'id explaining value 2'])
def test_parameterize_with_id(param1):
    simple_step(param1)
    
@pytest.mark.parameterize('param1', [True, False])
@pytest.mark.parameterize('param2', ['value 1', 'value 2'])
def test_parameterize_with_two_parameters(param1, param2):
    simple_step(param1, param2)
    
@pytest.mark.parameterize('param1', [True], ids=['boolean parameter id'])
@pytest.mark.parameterize('param2', ['value 1', 'value 2'])
@pytest.mark.parameterize('param3', [1])
def test_parameterize_with_uneven_value_sets(param1, param2, param3):
    simple_step(param1, param3)
    simple_step(param2)
```

Example of captured test invocations with different sets of named and unnamed parameters.

![](https://docs.qameta.io/allure/images/pytest_parameterized_tests.png)

Details of test execution for a parameterized test with a named parameter.

![](https://docs.qameta.io/allure/images/pytest_parameterized_with_id.png)

### 6.1.5. Allure Features

Allure currently supports almost every available feature except for environment with Pytest.

#### Steps

The first and probably most important aspect of the Allure report is that it allows to get a very detailed step-by-step representation of every test invocation[^6-1-5-1]. This is made possible with `@allure.step` decorator that adds invocation of the annotated[^6-1-5-2] method or function with provided arguments to the report.

Methods annotated with `@step` can be stored aside[^6-1-5-3] from your tests and just imported when needed. Step methods can have an arbitrarily deep nested structure.

```python
import allure
import pytest

from .steps import imported_step


@allure.step
def passing_step():
    pass

@allure.step
def step_with_nested_steps():
    nested_step()
    
@allure.step
def nested_step():
    nested_step_with_arguments(1, 'abc')
    
@allure.step
def nested_step_with_arguments(arg1, arg2):
    pass

def test_with_imported_step():
    passing_step()
    imported_step()
    
def test_with_nested_steps():
    passing_step()
    step_with_nested_steps()
```

Status of every step is shown in a small icon on the right from the name. Nested steps are organized in a tree-like collapsible structure.

![](https://docs.qameta.io/allure/images/pytest_nested_steps_and_args.png)

Steps can have a description line that supports placeholders for passed positional and keyword arguments. Default parameters of the keyword arguments will be captured as well.

```python
import allure

@allure.step('Step with placeholders in the title, positional: "{0}", keyword: "{key}"')
def step_with_title_placeholders(arg1, key=None):
    pass

def test_steps_with_placeholders():
    step_with_title_placeholders(1, key='something')
    step_with_title_placeholders(2)
    step_with_title_placeholders(3, 'anything')
```

![](https://docs.qameta.io/allure/images/pytest_step_arguments.png)

Steps are supported in fixtures as well. Here is an example of a test using a fixture defined in `conftest.py` module (such fixtures will be resolved by Pytest even when not directly imported):

*conftest.py*

```python
import allure
import pytest

@allure.step('step in conftest.py')
def conftest_step():
    pass

@pytest.fixture
def fixture_with_conftest_step():
    conftest_step()
```

```python
import allure

from .steps import imported_step

@allure.step
def passing_step():
    pass

def test_with_step_in_fixture_from_conftest(fixture_with_conftest_step):
    passing_step()
```

Steps in fixtures are shown in separate trees for setup and teardown.

![](https://docs.qameta.io/allure/images/pytest_step_in_fixture.png)

#### Attachments

Reports can display many different types of provided attachments that can complement a test, step or fixture result. Attachments can be created either with invocation of `allure.attach(body, name, attachment_type, extension)`:

1. `body` - raw content to be written into the file.
2. `name` - a string with name of the file
3. `attachment_type` - one of the `allure.attachment_type` values
4. `extension` - is provided will be used as an extension for the created file.

or `allure.attach.file(source, name, attachment_type, extension)`:

1.  `source` - a string containing path to the file.

(other arguments are the same)

```python
import allure
import pytest


@pytest.fixture
def attach_file_in_module_scope_fixture_with_finalizer(request):
    allure.attach('A text attachment in module scope fixture', 'blah blah blah', allure.attachment_type.TEXT)
    def finalizer_module_scope_fixture():
        allure.attach('A text attachment in module scope finalizer', 'blah blah blah blah',
                      allure.attachment_type.TEXT)
    request.addfinalizer(finalizer_module_scope_fixture)
    
def test_with_attachments_in_fixture_and_finalizer(attach_file_in_module_scope_finalizer):
    pass

def test_multiple_attachments():
    allure.attach.file('./data/totally_open_source_kitten.png', attachment_type=allure.attachment_type.PNG)
    allure.attach('<head></head><body> a page </body>', 'Attach with HTML type', allure.attachment_type.HTML)
```

Attachments are shown in the context of a test entity they belong to. Attachments of HTML type are rendered and displayed on the report page. This is a convenient way to provide some customization for your own representation of a test result.

![](https://docs.qameta.io/allure/images/pytest_attachments.png)

#### Descriptions



#### Titles



#### Links



### 6.1.6. Retries



### 6.1.7. Tags



#### BDD markers



#### Severity markers



[^0-0-0-1]: vt. 调整，使有规则; 对进行微调 to make very small changes to something such as a machine, system, or plan, so that it works as well as possible
[^3-1-1]: an occasion at which a new product is shown or made available for sale or use for the first time
[^4-1-1]: adj. not serious, important, or valuable
[^6-1-5-1]: n. 祈祷; 乞求; 乞灵; 乞求神助 *literary* a request for help, especially from a god
[^6-1-5-2]: vt.& vi. 注解，注释 to add short notes to a book or piece of writing to explain parts of it
[^6-1-5-3]: adv. 到旁边; 留出; 不顾，撇开; 除…外 1 kept to be used later

