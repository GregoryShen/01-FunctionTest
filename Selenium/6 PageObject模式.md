[Selenium中Page Object设计模式](https://cloud.tencent.com/developer/article/1492150)

[selenium自动化,关于PageObject设计模式](https://www.imooc.com/article/17580)

[Page Object设计模式](https://juejin.im/post/5caef9cef265da03775c3f05)

[page object模式](https://blog.csdn.net/JOJOY_tester/article/details/55045393)

## Page Object是什么

是selenium自动化测试项目开发最佳测试设计模式，主要体现在对界面交互细节的封装，这样使得测试案例更加注重页面而不是界面细节，提高了测试用例的可读性。

Page Object 模式主要是将<u>每个页面设计为一个类class</u>，这个类包含页面中需要的测试元素（按钮、输入框、URL、标题等）和实际操作方法，这样在写测试用例时可以通过调用页面类的方法和属性来获取页面元素和操作元素，这样优点是避免当页面元素的ID或位置改变时需要更改测试用例代码的情况。当页面元素定位发生改变时只要通过更改页面类的属性即可。

* 一个类中，一个方法调用另一个方法时，需要加入self.被调用的方法(self.入参)
* 在Python方法中入参是元组时，需要加*，因为Python存在这种特性，将入参放进元组里，入参是元组的元素需要加\*
* 把操作方法封装为函数时，return返回就是这个操作方法的具体操作，return返回值可以给其他函数直接使用的

## Page Object的优点

* 提高测试用例的可读性
* 减少了代码的重复
* 提高测试用例的可维护性，特别是针对UI频繁变动的项目

## Page Object使用例子

base.py

定义页面基础类，用于所有页面的基础，封装所有测试页面的公共方法。

```python
class Page:
    '''基础类，用于所有页面的继承'''
    login_url = "http://www.126.com"
    #实例化Page 类时会执行__init__方法，该方法的入参是Page类的入参
    #__init__()构造函数不能只返回None
    def __init__(self, driver, base_url=login_url):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 30
    #on_page()方法是URL地址的断言部分
    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)
    
    # 单下划线_开头表示是私有的，就是通过import *时私有的方法不会被导入
    # _open()方法用于打开URL网站，并检验页面链接加载是否正确
    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), "Did not land on %s" % url
    
    # open()方法通过调用_open()方法打开URL网站
    def open(self):
        self._open(self.url)
        
    # 重写定位元素的方法，Loc==(By.NAME, "email"),是一个元组，Python方法中入参是元组时需要在前面加*
    def find_element(self, *loc):
        return self.driver.find_element(*loc)
    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)
```

login_object.py

每个测试页面元素定位和操作方法都在这层定义，一旦UI发生改变只需要在该层修改对象属性即可



[XPath 教程](https://www.w3school.com.cn/xpath/index.asp)

[如何使用PageFactory](https://www.iteye.com/blog/libin0019-1260090)

[在Python中实现PageFactory模式](https://yq.aliyun.com/articles/36335)

[Selenium PageFactory](https://www.cnblogs.com/tman/p/4397860.html)

[Category Archives: 使用说明](http://www.selenium.org.cn/category/use)

[selenium 实战二_PO代码重构](https://www.kancloud.cn/guanfuchang/python_selenium/714652)

[Selenium的PO模式（Page Object Model）[python版]](https://cloud.tencent.com/developer/article/1200220)

[Selenium的PO模式（Page Object Model）[python版]](https://www.bbsmax.com/A/RnJW1xwdqY/)

[selenium自动化测试框架之PO设计模式](https://blog.51cto.com/starpoint/2285046)

[基于Python Selenium Unittest PO设计模式详解](https://www.cnblogs.com/snailrunning/p/10163159.html)

[Selenium的PO模式（Page Object Model）|(Selenium Webdriver For Python)](https://www.cnblogs.com/tsbc/p/4080301.html)

[Selenium PO模式实现](https://blog.csdn.net/qq_24373725/article/details/80436121)

[全网最详细的selenium支po模式讲解（全集)](https://www.bilibili.com/video/av76601326/)



[【Python自动化测试公开课】Selenium自动化中如何玩转PO模式-51CTO](https://www.bilibili.com/video/av18885836/)

[Automation in Selenium: Page Object Model and Page Factory](https://www.toptal.com/selenium/test-automation-in-selenium-using-page-object-model-and-page-factory)

[你用错 Page Object 了吗？](https://mp.weixin.qq.com/s/Bv5zLzkmraoKK_1bcNFyLg)

[UI 自动化到底要不要用 Page Object 模式？(续 - 深入了解 PO 模式, 并改造 PO 模式](https://testerhome.com/topics/19900)

# [Selenium WdbDriver: The Architecture of Open Source Applications](http://aosabook.org/en/selenium.html)

## 16.1. History

Because Selenium was written in pure Javascript, its initial design required developers to host Core and their tests on the same server as the application under test(AUT) in order to avoid falling foul of the browser’s security polices and the Javascript sandbox. This was not always practical or possible. Worse, althouth a developer’s IDE gives them the ability to swiftly manipulate code and navigate a large codebase, there is no such tool for HTML. It rapidly became clear that maintaining even a medium-sized suite of tests was an unwieldly and painful proposition.

To resolve this and other issues, an HTTP proxy was written so that every HTTP request could be intercepted by Selenium. Using this proxy made it possible to side-step many of the constraints of the “same host origin” policy, where a browser won’t allow Javascript to make calls to anything other than the server from which the current page has been served, allowing the first weakness to be mitigated. The design opened up the possiblity of writing Selenium bindings in multiple languages: they just needed to be able to send HTTP requests to a particular URL. The wire format was closely modeled on the table-based syntax of Selenium Core and it, along with the table-based syntax, became known as “Selenese”. Because the language bindings were controlling the browser at at distance, the tool was called “Selenium Remote Control”, or “Selenium RC”.

While Selenium was being developed, another browser automation framework was brewing at ThoughtWorks: WebDriver. The initial code for this was released early in 2007. WebDriver was derived from work on projects which wanted to isolate their end-to-end tests from the underlying test tool. Typically, the way that this isolation is done is via the Adapter pattern. WebDriver grew out of insight developed by applying this approach consistently over numerous projects, and initially was a wrapper around HtmlUnit. Internet Explorer and Firefox support followed rapidly after release.

When WebDriver was released there were significant differences between it and Selenium RC, though they sat in the same software niche of an API for browser automation. The most obvious difference to a user was the Selenium RC had a dictionary-based API, with all methods exposed on a single class, whereas WebDriver had a more object-oriented API. In addition, WebDriver only supported Java, whereas Selenium RC offered support for a wide-range of languages. There were also strong technical differences: Selenium Core(on which RC was based) was essentially a Javascript application, running inside the browser’ s security sandbox. WebDriver attempted to bind natively to the browser, side-stepping the browser’s security model at the cost of significantly increased development effort for the framework itself.

In August, 2009, it was annouced that the two projects would merge, and Selenium WebDriver is the result of those merged projects. As I write this, WebDriver supports language bindings for Java, C#, Python and Ruby. It offers support for Chrome, Firefox, Internet Explorer, Opera, and he Android and iPhone browsers. There are sister projects, not kept in the same source code repo but working closely with the main project, that provide Perl bindings, an implementation for BlackBerry browser, and for “headless” WebKit — useful for those times where tests need to run on a continuous integration server without a proper display. The original Selenium RC mechanism is still maintained and allows WebDriver to provide support for browsers that would otherwise be unsupported.

## 16.2. A Digression About Jargon

Unfortunately, the selenium project uses a lot of jargon. To recap what we’ve already come across:

* *Selenium Core* is the heart of the original Selenium implementation, and is a set of Javascript scripts that control the browser. This is sometimes referred to as “Selenium” and sometimes as “Core”.
* *Selenium RC* was the name given to the language bindings for Selenium Core, and is commonly, and confusingly, referred to as just “Selenium” or “RC”. It has now been replaced by Selenium WebDriver, where RC’s API is referred to as the “Selenium 1.x API”.
* *Selenium WebDriver* fits in the same niche as RC did, and has subsumed the original 1.x bindings. It refers to both the language bindings and the implementations of the individual browser controlling code. This is commonly referred to as just “WebDriver” or sometimes as Selenium 2. Doubtless, this will be contracted to “Selenium” over time.

The astute reader will have noticed that “Selenium” is used in a fairly general sense. Fortunately, context normally makes it clear which particular Selenium people are referring to.

## 16.3. Architectural Themes

### 16.3.5. Lower the Bus Factor

There’s a (not entirely serious) concept in software development called the “bus factor”. It refers to the number of key developers who would need to meet some grisly end- presumably by being hit by a bus - to leave the project in a state where it couldn’t continue. Something as complex as browser automation could be especially prone to this, so a lot of our architectural decisions are made to raise this number as high as possible.

### 16.3.7. Every Call Is an RPC Call

WebDriver controls browsers that are running in other processes. Although it’s easy to overlook it, this means that every call that is made through its API is an RPC call and therefore the performance of the framework is at the mercy of network lantency. In normal operation, this may not be terribly noticeable — most OSes optimize routing to localhost — but as the network latency between the browser and the test code increases, what may have seemed efficient becomes less so to both API designers and users of that API.

This introduces some tension into the design of APIs. A larger API, with coarser functions would help reduce latency by collapsing multiple calls, but this must be balanced by keeping the API expressive and easy to use. For example, there are several checks that need to be made to determine whether an element is visible to an end-user. Not only do we need to take into account various CSS properties, which may need to be inferred by looking at parent elements, but we should probably also check the dimensions of the element. A minimalist API would require each of these checks to be made individually. WebDriver collapses all of them into a single `isDisplayed` method.

## 16.4. Coping with Complexity

Think of a simplified `Shop` class. Every day, it needs to be restocked, and it collaborates with a `Stockist` to deliver this new stock. Every month, it needs to pay staff and taxes. For the sake of argument, let’s assume that it does this using an `Accountant`.One way of modeling this looks like:

```java
public interface Shop {
    void addStock(StockItem item, int quantity);
    Money getSalesTotal(Date startDate, Date endDate);
}
```

We have two choices about where to draw the boundaries when defining the interface between the Shop, the Accountant and the Stockist. We could draw a theoretical line as shown in Figure 16.1.

This would mean that both Accountant and Stockist would accept a Shop as an argument to their respective methods. The drawback here, though, is that it’s unlikely that the Accountant really wants to stack shelves, and it’s probably not a great idea for the Stockist to realize the vast mark-up on prices that the Shop is adding. So, a better place to draw the line is shown in Figure 16.2.

We’ll need two interfaces that the Shop needs to implement, but these interfaces clearly define the role that the Shop fulfills for both the Accountant and the Stockist. They are role-based interfaces:

```java
public interface HasBalance {
    Money getSalesTotal(Date startDate, Date endDate);
}

public interface Stockable {
    void addStock(StockItem item, int quantity);
}

public interface Shop extends HasBalance, Stockable {
    
}
```

I find `UnsupportedOpreationExceptions` and their ilk deeply displeasing, but there needs to be something that allows functionality to be exposed for the subset of users who might need it without cluttering the rest of the APIs for the majority of users. To this end, WebDriver makes extensive use of role-based interfaces. For example, there is a JavascriptExecutor interface that provides the ability to execute arbitrary chunks of Javascript in the context of the current page. A successful cast of a WebDriver instance to that interface indicates that you can expect the methods on it to work.

### 16.4.2. Dealing with the Combinatorial Explosion



### 16.4.3. Flaws in the WebDriver Design

The downside of the decision to expose capabiliites in this way is that until someone knows that a particular interface exists they may not realize that WebDriver supports that type of functionality; there’s a loss of explorability in the API. (以这种方式决定暴露能力的负面意义是:在明确的知道一个确定的接口存在前, 人们是不知道WebDriver支持这种类型的功能的, 这对于探索API的能力是一种损失)Certainly when WebDriver was new we seemed to spend a lof of time just pointing people towards particular interfaces. We’ve now put a lot more effort into our documentation and as the API gets more widely used it becomes easier and easier for users to find the information they need.

From an implementor’s point of view, binding tightly to a browser is also a design flaw, albeit an inescapable one. It takes significant effort to support a new browser, and often several attempts need to be made in order to get it right. As a concrete example, the Chrome driver has gone through four complete rewrites, and the IE driver has had three major rewrites too. The advantage of binding tightly to a browser is that it offers more control.

## 16.5. Layers and Javascript

A browser automation tool is essentially built of three moving parts:

* A way of interrogating the DOM
* A mechanism for executing Javascript
* Some means of emulating user input

This section focuses on the first part: providing a mechanism to interrogate the DOM. The lingua franca of the browser is Javascript, and this seems like the ideal language to use when interrogating the DOM. Although this choice seems obvious, making it leads to some interesting challenges and competing requirements that need balancing when thinking about Javascript.

Like most large projects, Selenium makes use of a layered set of libraries.The bottom layer is Google’s Closure Library, which supplies primitives and a modularization mechanism allowing source files to be kept focused and as small as possible. Above, this, there is a utility library providing functions that range from simple tasks such as getting the value of an attribute, through determining whether an element would be visible to an end user, to far more complex actions such as simulting a click using synthesized automation, and so are called Browser Automation Atoms or atoms. Finally, there are adapter layers that compose atoms in order to meet the API contracts of both WebDriver and Core.

 The Closure Library was chosen for several reasons. “Compilation” can be as simple as ordering input files in dependency order, concatenating and pretty printing them, or as complex as doing advanced minification and dead code removal.

Although this seems like a strange thing to do, it allows the Javascript to be pushed into the underlying driver without needing to expose the raw source in multiple places.

Because the atoms normalize return values between browsers, there can also be unexpected return values. For example, consider this HTML:

```html
<input name="example" checked>
```

The value of the `checked` attribute will depend on the browser being used. The atoms normalize this, and other Boolean attributes defined in the HTML5 spec, to be “true” or “false”. While the value was now consistent there was an extended period where we explained to the community what had happened and why.

## 16.6. The Remote Driver, and the Firefox Driver in Particular

The remote WebDriver was originally a glorified RPC mechanism. It has since evolved into one of the key mechanisms we use to reduce the cost of maintaining WebDriver by providing a uniform interface that languange bindings can code against.

## 16.8. Selenium RC

It’s not always possible to bind tightly to a particular browser. In those cases, WebDriver falls back to the original mechanism used by Selenium.































