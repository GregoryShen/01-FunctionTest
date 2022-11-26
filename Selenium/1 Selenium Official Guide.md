# [The Selenium Browser Automation Project](https://www.selenium.dev/documentation/)

Selenium is an umbrella[^0-1] project for a range of tools and libraries that enable and support the automation of web browsers.

It provides extensions to emulate[^0-2] user interaction with browsers, a distribution server for scaling browser allocation, and the infrastructure for implementations of the [W3C WebDriver specification](https://www.w3.org/TR/webdriver/) that lets you write interchangeable[^0-3] code for all major web browsers.

This project is made possible by volunteer contributors who have put in thousands of hours of their own time, and made the source code freely available for anyone to use, enjoy, and improve.

Selenium brings together browser vendors, engineers, and enthusiasts[^0-4] to further an open discussion around automation of the web platform. The project organizes an annual conference to teach and nurture the community.

At the core of Selenium is WebDriver, an interface to write instruction sets that can be run interchangeably in many browsers. Once you've installed everything, only a few lines of code get you inside a browser. You can find a more comprehensive example in Writing your first Selenium script

```c#
using OpenQA.Selenium.Chrome;

namespace SeleniumDocs.Hello
{
    public class HelloSelenium
    {
        public static void main()
        {
            var driver = new ChromeDriver();
            driver.Navigate().GoToUrl("https://selenium.dev");
            driver.Quit();
        }
    }
}
```

See the Overview to check the different project components and decide if Selenium is the right tool for you.

You should continue on to Getting Started to understand how you can install Selenium and successfully use it as a test automation tool, and scaling simple tests like this to run in large, distributed environments on multiple browsers, on several different operating systems.

**<u>Selenium overview</u>**

Is Selenium for you? See an overview of the different project components.

**<u>WebDriver</u>**

WebDriver drives a browser natively, learn more about it.

**<u>Selenium Grid 4</u>**

Want to run tests in parallel across multiple machines? Then Grid is for you.

**<u>IE Driver Server</u>**

The Internet Explorer Driver is a standalone server that implements the WebDriver specification.

**<u>Selenium IDE</u>**

The Selenium IDE is a browser extension that records and plays back a user's actions.

**<u>Test Practices</u>**

Some guidelines and recommendations on testing from the Selenium project.

**<u>Legacy</u>**

Documentation related to the legacy components of Selenium. Meant to be kept purely for historical reasons and not as a incentive to use deprecated components.

**<u>About this documentation</u>**

# [1 Overview](https://www.selenium.dev/documentation/overview/)

Is Selenium for you? See an overview of the different project components.

Selenium is not just one tool or API but it composes many tools.

**WebDriver**

If you are beginning with desktop website or mobile website test automation, then you are going to be using WebDriver APIs. WebDriver uses browser automation APIs provided by browser vendors to control browser and run tests. This is as if a real user is operating the browser. Since WebDriver does not require its API to be compiled with application code, it is not intrusive. Hence, you are testing the same application which you push live.

**IDE**

IDE is the tool you use to develop your Selenium test cases. It's an easy-to-use Chrome and Firefox extension and is generally the most efficient way to develop test cases. It records the user's actions in the browser for you, using existing Selenium commands, with parameters defined by the context of that element. This is not only a time-saver but also an excellent way of learning Selenium script syntax.

**Grid**

Selenium Grid allows you to run test cases in different machines across different platforms. The control of triggering the test cases is on the local end, and when the test cases are triggered, they are automatically executed by the remote end.

After the development of the WebDriver tests, you may face the need of running your tests on multiple browser and operating system combinations. This is where Grid comes into the picture.

## [1-1 Components](https://www.selenium.dev/documentation/overview/components/)

Building a test suite using WebDriver will require you to understand and effectively use a number of different components. As with everything in software, different people use different terms for the same idea. Below is a breakdown of how terms are used in this description.

### Terminology

* **API**: Application Programming Interface. This is the set of "commands" you use to manipulate WebDriver.
* **Library**: A code module which contains the APIs and the code necessary to implement them. Libraries are specific to each language binding, eg .jar files for Java, .dll files for .NET, etc.
* **Driver**: Responsible for controlling the actual browser. Most drivers are created by the browser vendors themselves. Drivers are generally executable modules that run on the system with the browser itself, not on the system executing the test suite.(Although those may be the same system.) NOTE: *Some people refer to the drivers as proxies*.
* **Framework**: An additional library used as a support for WebDriver suites. These frameworks may be test frameworks such as JUnit or NUnit. They may also be frameworks supporting natural language features such as Cucumber or Robotium. Frameworks may also be written and used for things such as manipulating or configuring the system under test, data creation, test oracles, etc.

### The Parts and Pieces

At its minimum, WebDriver talks to a browser through a driver. Communication is two way: WebDriver passes commands to the browser through the driver, and receives information back via the same route.

![](https://www.selenium.dev/images/documentation/webdriver/basic_comms.png)

The driver is specific to the browser, such as ChromeDriver for Google's Chrome/Chromium, GeckoDriver for Mozilla's Firefox, etc. The driver runs on the same system as the browser. This may, or may not be, the same system where the tests themselves are executing.

This simple example above is *direct* communication. Communication to the browser may also be *remote* communication through Selenium Server or RemoteWebDriver. RemoteWebDriver runs on the same system as the driver and the browser.

![](https://www.selenium.dev/images/documentation/webdriver/remote_comms.png)

Remote communication can also take place using Selenium Server or Selenium Grid, both of which in turn talk to the driver on the host system.

![](https://www.selenium.dev/images/documentation/webdriver/remote_comms_server.png)

### Where Frameworks fit in

WebDriver has one job and one job only: communicate with the browser via any of the methods above. WebDriver does not know a thing about testing: it does not know how to compare things, assert pass or fail, and it certainly does not know a thing about reporting or Given/When/Then grammar.

This is where various frameworks come in to play. At a minimum you will need a test framework that matches the language binding, e.g. NUnit for .NET, JUnit for Java, Rspec for Ruby, etc.

The test framework is responsible for running and executing your WebDriver and related steps in your tests. As such, you can think of it looking akin to the following image.

![](https://www.selenium.dev/images/documentation/webdriver/test_framework.png)

Natural language framework/tools such as Cucumber may exist as part of that Test Framework box in the figure above, or they may wrap the Test Framework entirely in their own implementation.

## [1-2 Details](https://www.selenium.dev/documentation/overview/details/)

**A deeper look at Selenium**

Selenium is an umbrella project for a range of tools and libraries that enable and support the automation of web browsers.

### Selenium controls web browsers

Selenium is many things but at its core, it is a toolset for web browser automation that uses the best techniques available to remotely control browser instances and emulate a user's interaction with the browser.

It allows users to simulate common activities performed by end-users; entering text into fields, selecting drop-down values and checking boxes, and clicking links in documents. It also provides many other controls such as mouse movement, arbitrary JavaScript execution, and much more.

Although used primarily for front-end testing of websites, Selenium is at its core a browser user agent library. The interfaces are ubiquitous to their application, which encourages composition with other libraries to suit your purpose.

### One interface to rule them all

One of the project's guiding principles is to support a common interface for all(major) browser technologies. Web browsers are incredibly complex, highly engineered applications, performing their operations in completely different ways but which frequently look the same while doing so. Even though the text is rendered in the same fonts, the images are displayed in the same place and the links take you to the same destination. What is happening underneath is as different as night and day. Selenium "abstracts" these differences, hiding their details and intricacies from the person writing the code. This allows you to write several lines of code to perform a complicated workflow, but these same lines will execute on Firefox, Internet Explorer, Chrome, and all other supported browsers.

### Tools and support

Selenium's minimalist design approach gives it the versatility to be included as a component in bigger applications. The surrounding infrastructure provides under the Selenium umbrella gives you the tools to put together your grid of browsers so tests can be run on different browsers and multiple operating systems across a range of machines.

Imagine a bank of computers in your server room or data center all firing up browsers at the same time hitting your site's links, forms, and tables -- testing your application 24 hours a day. Through the simple programming interface provides for the most common languages, these tests will run tirelessly in parallel, reporting back to you when errors occur.

It is an aim to help make this a reality for you, by providing users with tools and documentation to not only control browsers but to make it easy to scale and deploy such grids.

### Who uses Selenium

Many of the most important companies in the world have adopted Selenium for their browser-based testing, often replacing years-long efforts involving other proprietary tools. As it has grown in popularity, so have its requirements and challenges multiplied.

As the web becomes more complicated and new technologies are added to websites, it's the mission of this project to keep up with them where possible. Being an open source project, this support is provided through the generous donation of time from many volunteers, every one of which has a "day job".

Another mission of the project is to encourage more volunteers to partake in this effort, and build a strong community so that the project can continue to keep up with emerging technologies and remain a dominant platform for functional test automation.

# [2 WebDriver](https://www.selenium.dev/documentation/webdriver/)

WebDriver drives a browser natively, learn more about it.

WebDriver drives a browser natively, as a user would, either locally or on a remote machine using the Selenium server, marks a leap forward in terms of browser automation.

Selenium WebDriver refers to both the language bindings and the implementations of the individual browser controlling code. This is commonly referred to as just *WebDriver*.

Selenium WebDriver is a W3C Recommendation

* WebDriver is designed as a simple and more concise programming interface.
* WebDriver s a compact object-oriented API.
* It drives the browser effectively.

**<u>Getting started</u>**

If you are new to Selenium, we have a few resources that can help you get up to speed right away.

**<u>WebDriver Capabilities</u>**

**<u>Browser</u>**

**<u>Web elements</u>**

Identifying and working with element objects in the DOM.

**<u>Remote WebDriver</u>**

**<u>Configuring driver parameters</u>**

**<u>Waits</u>**

**<u>Actions API</u>**

A low-level interface for providing virtualized device input to the web browser.

**<u>BiDirectional functionality</u>**

**<u>Additional features</u>**

Set of packages and functionalities to simplify automation with Selenium.

## [2-1 Get Started](https://www.selenium.dev/documentation/webdriver/getting_started/)

If you are new to Selenium, we have a few resources that can help you get up to speed right away.

Selenium supports automation of all the major browsers in the market through the use of WebDriver. WebDriver is an API and protocol that defines a language-neutral interface for controlling the behavior of web browsers. Each browser is backed by a specific WebDriver implementation, called a driver. The driver is the component responsible for delegating down to the browser, and handles communication to and from Selenium and the browser.

This separation is part of a conscious effort to have browser vendors take responsibility for the implementation for their browsers. Selenium makes use of these third party drivers where possible, but also provides its own drivers maintained by the project for the cases when this is not a reality.

The Selenium framework ties all of these pieces together through a user-facing interface that enables the different browser backends to be used transparently, enabling cross-browser and cross-platform automation.

Selenium setup is quite different from the setup of other commercial tools. Before you can stat writing Selenium code, you have to install the language bindings libraries for your language of choice, the browser you want to use, and the driver for that browser.

### 2-1-1 Install Library

Setting up the Selenium library for your favorite programming language.

Fist you need to install the Selenium bindings for your automation project. The installation process for libraries depends on the language you choose to use. Make sure you check the Selenium downloads page to make sure you are using the latest version.

##### Requirements by language

Installation of Selenium libraries for C# can be done using NuGet in one of two ways

* Using a Packet Manager:

  ```c#
  Install-Package Selenium.WebDriver
  ```

* Using .NET CLI

  ```c#
  dotnet add package Selenium.WebDriver
  ```

##### Supported .NET Versions

Make sure to use the .NET SDK version compatible with relevant Selenium package. Check the dependencies section to find out the supported .NET version. At the time of this update, .NET 5.0 (Visual Studio 2019) is known to be supported, and .NET 6.0 is not supported. You can download MSBuild Tools 2019 from here to install the needed components and dependencies such as .NET SDK and NuGet Package Manager.

##### Using Visual Studio Code(vscode) and C#

This is a quick guide to help you get started with vscode and C#, however, more research may be required. Install the compatible .NET SDK as per the section above. Also install the vscode extensions (Ctrl-Shift-X) for C# and NuGet. Follow the instruction here to create and run the "Hello World" console project using C#. You may also create a NUnit starter project using the command line `dotnet new NUnit`. Make sure the file `%appdatat%\NuGet\nuget.config` is configured properly as some developers reported that it will be empty due to some issues. If `nuget.config` is empty, or not configured properly, then .NET builds will fail for Selenium Projects. Add the following section to the file `nuget.config` if it is empty:

```yaml
<configuration>
  <packageSources>
    <add key="nuget.org" value="https://api.nuget.org/v3/index.json" protocolVersion="3" />
    <add key="nuget.org" value="https://www.nuget.org/api/v2/" />   
  </packageSources>
...
```

For more info about `nuget.config` [click here](https://docs.microsoft.com/en-us/nuget/reference/nuget-config-file). You may have to customize `nuget.config` to meet your needs.

Now go back to vscode, press Ctrl-Shift-P, and type "NuGet Add Package", and enter the required Selenium packages such as `Selenium.WebDriver`. Press enter and select the version. Now you can use the examples in the documentation related to C# with vscode.

### 2-1-2 Install Drivers

Setting up your system to allow a browser to be automated.

Through WebDriver, Selenium supports all major browsers on the market such as Chrome/Chromium, Firefox, Internet Explorer, Edge, Opera, and Safari. Where possible, WebDriver drives the browser using the browser's built-in support for automation.

Since all the driver implementations except for Internet Explorer are provided by the browser vendors themselves, they are not included in the standard Selenium distribution. This section explains the basic requirements for getting you started with the different browsers.

Read about more advanced options for starting a driver in your [driver configuration](https://www.selenium.dev/documentation/webdriver/drivers/) documentation.

##### Quick Reference

|      Browser      |        Supported OS         |  Maintained by   |                           Download                           |                        Issue Tracker                         |
| :---------------: | :-------------------------: | :--------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|  Chromium/Chrome  |     Windows/macOS/Linux     |      Google      | [Downloads](https://chromedriver.storage.googleapis.com/index.html) | [Issues](https://bugs.chromium.org/p/chromedriver/issues/list) |
|      Firefox      |     Windows/macOS/Linux     |     Mozilla      | [Downloads](https://github.com/mozilla/geckodriver/releases) |   [Issues](https://github.com/mozilla/geckodriver/issues)    |
|       Edge        |        Windows/macOS        |    Microsoft     | [Downloads](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) | [Issues](https://github.com/MicrosoftDocs/edge-developer/issues) |
| Internet Explorer |           Windows           | Selenium Project |       [Downloads](https://www.selenium.dev/downloads)        | [Issues](https://github.com/SeleniumHQ/selenium/labels/D-IE) |
|      Safari       | macOS High Sierra and newer |      Apple       |                           Built in                           |         [Issues](https://bugreport.apple.com/logon)          |

Note: The Opera driver does not support w3c syntax, so we recommend using chromedriver to work with Opera. See the code example for [opening and Opera browser]().

##### Three Ways to Use Drivers

1. ###### Driver Management Software

   Most machines automatically update the browser, but the driver does not. To make sure you get the correct driver for your browser, there are many third party libraries to assist you.

   **<u>Python</u>**

   1. Import [WebDriver Manager for Python](https://github.com/SergeyPirogov/webdriver_manager)

      ```python
      from webdriver_manager.chrome import ChromeDriverManager
      ```

   2. Use `install()` to get the location used by the manager and pass it into service class

      ```python
      service = Service(executable_path=ChromeDriverManager().install())
      ```

   3. Use `Service` instance when initializing the driver:

      ```python
      driver = webdriver.Chrome(service=service)
      ```

   [See full example on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/dev/examples/python/tests/getting_started/test_install_drivers.py)

   **<u>CSharp</u>**

   1. Import [WebDriver Manager Package](https://github.com/rosolko/WebDriverManager.Net)

      ```c#
      using WebDriverManager;
      using WebDriverManager.DriverConfigs.Impl;
      ```

   2. Use the `SetUpDriver()` which requires a config class:

      ```c#
      new DriverManager().SetUpDriver(new ChromeConfig());
      ```

   3. Initialize your driver as you normally would:

      ```c#
      var driver = new ChromeDriver()
      ```

   [See full example on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/dev/examples/dotnet/SeleniumDocs/GettingStarted/InstallDriversTest.cs)

2. ###### The `PATH`  Environment Variable

   This option first requires manually downloading the driver(See [Quick Reference Section](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/#quick-reference) for links).

   This is a flexible option to change location of drivers without having to update your code, and will work on multiple machines without requiring that each machine put the drivers in the same place.

   You can either place the drivers in the directory that is already listed in `PATH`, or you can place them in a directory and add it to `PATH`

   **<u>Bash</u>**

   To see what directories are already on `PATH`, open a Terminal and execute:

   ```bash
   echo $PATH
   ```

   If the location to your driver is not already in a directory listed, you can add a new directory to PATH:

   ```bash
   echo 'export PATH=$PATH:/path/to/driver' >> ~/.bash_profile
   source ~/.bash_profile
   ```

   You can test if it has been added correctly by starting the driver:

   ```bash
   chromedriver
   ```

   **<u>Zsh</u>**

   To see what directories are already on `PATH`, open a Terminal and execute:

   ```bash
   echo $PATH
   ```

   If the location to your driver is not already in a directory listed, you can add a new directory to PATH:

   ```bash
   echo 'export PATH=$PATH:/path/to/driver' >> ~/.zshenv
   source ~/.zshenv
   ```

   You can test if it has been added correctly by starting the driver:

   ```bash
   chromedriver
   ```

   **<u>Windows</u>**

   To see what directories are already on `PATH`, open a Command Prompt and execute:

   ```shell
   echo %PATH%
   ```

   If the directory to your driver is not already in a directory listed, you can add a new directory to PATH:

   ```shell
   setx PATH "%PATH%;C:\WebDriver\bin"
   ```

   You can test if it has been added correctly by starting the driver:

   ```shell
   chromedriver.exe
   ```

   ---

   if your `PATH` is configured correctly above, you will see some output relating to the startup of the driver:

   ```bash
   Starting ChromeDriver 95.0.4638.54 (d31a821ec901f68d0d34ccdbaea45b4c86ce543e-refs/branch-heads/4638@{#871}) on port 9515
   Only local connections are allowed.
   Please see https://chromedriver.chromium.org/security-considerations for suggestions on keeping ChromeDriver safe.
   ChromeDriver was started successfully.
   ```

   You can regain control of  your command prompt by pressing `Ctrl+C`

3. ###### Hard Coded Location

   Similar to Option 2 above, you need to manually downloaded the driver. Specifying the location in the code itself has the advantage of not needing to figure out Environment Variables on your system, but has the drawback of making the code much less flexible.

   **<u>Python</u>**

   ```python
   service = Service(executable_path="/path/to/chromedriver")
   driver = webdriver.Chrome(service=service)
   ```

   **<u>CSharp</u>**

   ```c#
   var driver = new ChromeDriver(@"C:\WebDriver\bin");
   ```

##### Advanced Configuration

More information on how you can change the driver behavior can be found on the [Configuring driver parameters](https://www.selenium.dev/documentation/webdriver/drivers/) page

### 2-1-3 Open Browser

Code examples for starting and stopping a session with each browser.

Once you have a Selenium library installed, and your desired browser driver, you can start and stop a session with a browser.

Typically, browsers are started with specific options that describe which capabilities the browser must support, and how the browser should behave during the session. Some capabilities are shared by all browsers, and some will be specific to the browser being used. This page will show examples of starting a browser with the default capabilities.

After learning how to start a session, check out the next session on how to write your first Selenium script.

##### Chrome

By default, Selenium 4 is compatible with Chrome v75 and greater. Note that the version of the Chrome browser and the version of chromedriver must match the major version.

In addition to the shared capabilities, there are specific Chrome capabilities that can be used.

**<u>Python</u>**

```python
options = ChromeOptions()
driver = webdriver.Chrome(options=options)

driver.quit()
```

**<u>CSharp</u>**

```c#
var options = new ChromeOptions();
var driver = new ChromeDriver(options);

driver.Quit();
```

##### Edge

Microsoft Edge is implemented with Chromium, with the earliest supported version of v79. Similar to Chrome, the major version number of edgedriver must match the major version of the Edge browser.

**<u>Python</u>**

```python
options = EdgeOptions()
driver = webdriver.Edge(options=options)

driver.quit()
```

**<u>CSharp</u>**

```c#
var options = new EdgeOptions();
var driver = new EdgeDriver(options);

driver.Quit();
```

##### Firefox

Selenium 4 requires Firefox 78 or greater. It is recommended to always use the latest version of geckodriver.

**<u>Python</u>**

```python
options = FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.quit()
```

**<u>CSharp</u>**

```c#
var options = new FirefoxOptions();
var driver = new FirefoxDriver(options);

driver.Quit();
```

##### Internet Explorer

no need to learn now

##### Opera

no need to learn now

##### Safari

###### Desktop

Unlike Chromium and Firefox drivers, the safaridriver is installed with the Operating System. To enable automation on Safari, run the following command from the terminal:

```bash
safaridriver --enable
```

**<u>Python</u>**

```python
driver = webdriver.Safari();

driver.quit()
```

**<u>CSharp</u>**

```c#
var options = new SafariOptions();
var driver = new SafariDriver(options);

driver.Quit();
```

###### Mobile

Those looking to automate Safari on iOS should look to the [Appium project](https://appium.io/).

### [2-1-4 First Script](https://www.selenium.dev/documentation/webdriver/getting_started/first_script/)

Step-by-step instructions for constructing a Selenium script

Once you have Selenium installed and Drivers installed, you're ready to write Selenium code.

##### Eight Basic Components

Everything Selenium does is send the browser commands to do something or send requests for information. Most of what you'll do with Selenium is a combination of these basic commands:

1. ###### Start the session

   For more details on starting a session read our documentation on [opening and closing a browser](https://www.selenium.dev/documentation/webdriver/getting_started/open_browser/)

   **<u>Python</u>**

   ```python
   driver = webdriver.Chrome()
   ```

   **<u>CSharp</u>**

   ```c#
   var driver = new ChromeDriver();
   ```

2. ###### Take action on browser

   In this example we are [navigating](https://www.selenium.dev/documentation/webdriver/browser/navigation/) to a web page.

   **<u>Python</u>**

   ```python
   driver.get("https://www.google.com")
   ```

   **<u>CSharp</u>**

   ```c#
   driver.Navigate().GoToUrl("https://www.google.com")
   ```

3. ###### Request browser information

   There are a bunch of types of [information about the browser](https://www.selenium.dev/documentation/webdriver/browser/) you can request, including window handles, browser size/position, cookies, alerts, etc.

   **<u>Python</u>**

   ```python
   driver.title # => "Google"
   ```

   **<u>CSharp</u>**

   ```c#
   driver.Title; // => "Google"
   ```

4. ###### Establish Waiting Strategy

   Synchronizing the code with the current state of the browser is one of the biggest challenges with Selenium, and doing it well is an advanced topic.

   Essentially you want to make sure that the element is on the page before you attempt to locate it and the element is in an interactable state before you attempt to interact with it.

   An implicit wait is rarely the best solution, but it's the easiest to demonstrate here, so we'll use it as a placeholder.

   Read more about [Waiting strategies](https://www.selenium.dev/documentation/webdriver/waits/)

   **<u>Python</u>**

   ```python
   driver.implicitly_wait(0.5)
   ```

   **<u>CSharp</u>**

   ```c#
   driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromMilliseconds(500);
   ```

5. ###### Find an element

   The majority of commands in most Selenium sessions are element related, and you can't interact with one without first [finding an element](https://www.selenium.dev/documentation/webdriver/elements/)

   **<u>Python</u>**

   ```python
   search_box = driver.find_element(By.NAME, "q")
   search_button = driver.find_element(By.NAME, "btnK")
   ```

   **<u>CSharp</u>**

   ```c#
   var searchBox = driver.FindElement(By.Name("q"));
   var searchButton = driver.FindElement(By.Name("btnK"))
   ```

6. ###### Take action on element

   There are only a handful of [actions to take on an element](https://www.selenium.dev/documentation/webdriver/elements/interactions/), but you will use them frequently.

   **<u>Python</u>**

   ```python
   search_box.send_keys("Selenium")
   search_button.click()
   ```

   **<u>CSharp</u>**

   ```c#
   searchBox.SendKeys("Selenium");
   searchButton.Click();
   ```

7. ###### Request element information

   Elements store a lot of [information that can be requested](https://www.selenium.dev/documentation/webdriver/elements/information/). Notice that we need to relocate the search box because the DOM has changed since we first located it.

   **<u>Python</u>**

   ```python
   driver.find_element(By.NAME, "q").get_attribute("value") # => "Selenium"
   ```

   **<u>CSharp</u>**

   ```c#
   driver.FindElement(By.Name("q")).GetAttribute("value"); // => "Selenium"
   ```

8. ###### End the session

   This ends the driver process, which by default closes the browser as well. No more commands can be sent to this driver instance.

   **<u>Python</u>**

   ```python
   driver.quit()
   ```

   **<u>CSharp</u>**

   ```c#
   driver.Quit();
   ```

##### Putting everything together

Let's combine these 8 things into a complete script.

Follow the link at the bottom of the tab to see an example of the code as it would be executed with a test runner instead of a standalone file.

**<u>Python</u>**

   ```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.title	# => "Google"
driver.implicitly_wait(0.5)
search_box = driver.find_element(By.NAME, "q")
search_button = driver.find_element(By.NAME, "btnK")

search_box.send_keys("Selenium")
search_box.click()

driver.find_element(By.NAME, "q").get_attribute("value") # => "Selenium"

driver.quit()
   ```

 **<u>CSharp</u>**

   ```c#
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

class HelloSelenium{
    static void Main() {
        var driver = new ChromeDriver();
        driver.Navigate().GoToUrl("https://www.google.com");
        driver.Title;
        driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromMilliseconds(500);
        
        var searchBox = driver.FindElement(By.Name("q"));
        var searchButton = driver.FindElement(By.Name("btnK"))
            
        searchBox.SendKeys("Selenium");
        searchButton.Click();
        
        driver.FindElement(By.Name("q")).GetAttribute("value");  // => "Selenium"
        driver.Quit();
        
    }
}
   ```

### [2-1-5 Upgrade to Selenium 4](https://www.selenium.dev/documentation/webdriver/getting_started/upgrade_to_selenium_4/)

Upgrading to Selenium 4 should be a painless process if you are using one of the officially supported languages(Ruby, JavaScript, C#, Python and Java). There might be some cases where a few issues can happen, and this guide will help you to sort them out. We will go through the steps to upgrade your project dependencies and understand the major deprecations and changes the version upgrade brings.

There are the steps we will follow to upgrade to Selenium 4:

* Preparing our test code
* Upgrading dependencies
* Potential errors and deprecation messages

Note: while Selenium 3.x versions were being developed, support for the W3C WebDriver standard was implemented. Both this new protocol and the legacy JSON Wire Protocol were supported. Around version 3.11, Selenium code became compliant with the level W3C 1 specification. The W3C compliant code in the latest version of Selenium 3 will work as expected in Selenium 4.

##### Preparing our test code

Selenium 4 removes for the legacy protocol and uses the W3C WebDriver standard by default under the hood. For most things, this implementation will not affect end users. The major exceptions are `Capabilities` and the `Actions` class.

###### Capabilities

If the test capabilities are not structured to be W3C compliant, may cause a session to not be started. Here is the list of W3C WebDriver standard capabilities:

* `browserName`
* `browserVersion`(replaces `version`)
* `platformName`(replaces `platform`)
* `acceptInsecureCerts`
* `pageLoadStrategy`
* `proxy`
* `timeouts`
* `unhandledPromptBehavior`

An up-to-date list of standard capabilities can be found at [W3C WebDriver](https://www.w3.org/TR/webdriver1/#capabilities).

Any capability that is not contained in the list above, needs to include a vendor prefix. This applies to browser specific capabilities as well as cloud vendor specific capabilities. For example, if your cloud vendor uses `build` and `name` capabilities for your tests, you need to wrap them in a `cloud:options` block(check with your cloud vendor for the appropriate prefix).

###### Before

**<u>Python</u>**

```python
caps = {}
caps['browserName'] = 'firefox'
caps['platform'] = 'Windows 10'
caps['version'] = '92'
caps['build'] = my_test_build
caps['name'] = my_test_name
driver = webdriver.Remote(cloud_url, desired_capabilities=caps)
```

**<u>CSharp</u>**

```c#
DesciredCapabilities caps = new DesiredCapabiliites();
caps.SetCapability("browserName", "firefox");
caps.SetCapability("platform", "Windows 10");
caps.SetCapability("version", "92");
caps.SetCapability("build", myTestBuild);
caps.SetCapability("name", myTestName);
var driver = new RemoteWebDriver(new Uri(CloudURL), caps)
```

###### after

**<u>Python</u>**

```python
from selenium.webdriver.firefox.options import Options as FirefoxOptions
options = FirefoxOptions()
options.browser_version = '92'
options.platform_name = 'Windows 10'
cloud_options = {}
cloud_options['build'] = my_test_build
cloud_options['name'] = my_test_name
options.set_capability('cloud:options', cloud_options)
driver = webdriver.Remote(cloud_url, options=options)
```

**<u>CSharp</u>**

```c#
var browserOptions = new FirefoxOptions();
browserOptions.PlatformName = "Windows 10";
browserOptions.BrowserVersion = "92";
var cloudOptions = new Dictionary<string, object>();
cloudOptions.Add("build", myTestBuild);
cloudOptions.Add("name", myTestName);
browserOptions.AddAdditionalOption("cloud:options", cloudOptions);
var driver = new RemoteWebDriver(new Uri(Cloud_URL), browserOptions);
```

###### Find element(s) utility methods in Java

##### Upgrading dependencies

Check the subsections below to install Selenium 4 and have your project dependencies upgraded.

###### C#

The place to get updates for Selenium 4 in C# is [NuGet](https://www.nuget.org/). Under the [`Selenium.WebDriver`](https://www.nuget.org/packages/Selenium.WebDriver/4.0.0) package you can get the instructions to update to the latest version. Inside of Visual Studio, through the NuGet Package Manager you can execute:

```shell
PM> Install-Package Selenium.WebDriver -Version 4.0.0
```

###### Python

The most important change to use Python is the minimum required version. Selenium 4 will require a minimum Python 3.7 or higher. More details can be found at the [Python Package Index](https://pypi.org/project/selenium/4.0.0/). To upgrade from the command line, you can execute:

```shell
pip install selenium==4.0.0
```

##### Potential errors and deprecation messages

Here is a set of code examples that will help to overcome the deprecation messages you might encounter after upgrading to Selenium 4.

###### C#

**`AddAdditionalCapability` is deprecated**

Instead of it, `AddAdditionalOption` is recommended. Here is an example showing this:

**Before**

```c#
var browserOptions = new ChromeOptions();
browserOptions.PlatformName = 'Windows 10';
browserOptions.BrowserVersion = 'latest';
var cloudOptions = new Dictionary<string, object>();
browserOptions.AddAdditionalOptionCapability("cloud:options", cloudOptions, true);
```

**After**

```c#
var browserOptions = new ChromeOptions();
browserOptions.PlatformName = 'Windows 10';
browserOptions.BrowserVersion = 'latest';
var cloudOptions = new Dictionary<string, object>();
browserOptions.AddAdditionalOptions("cloud:options", cloudOptions);
```

###### Python

<u>executable_path has been deprecated, please pass in a Service object</u>

In Selenium 4, you'll need to set the driver's `executable_path` from a Service object to prevent deprecation warmings.(Or don't set the path and instead make sure that the driver you need is on the System PATH).

**Before**

```python
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)
```

**After**

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable_automation"])
options.add_experimental_options("useAutomationExtension", False)
service = ChromeService(executable_path=CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)
```

##### Summary

We wen through the major changes to be taken into consideration when upgrading to Selenium 4. Covering the different aspects to cover when test code is prepared for the upgrade, including suggestions on how to prevent potential issues that can show up when using the new version of Selenium. To finalize, we also covered a set of possible issues that you can be bump into after upgrading, and we shared potential fixes for those issues.

*This was originally posted at https://saucelabs.com/resources/articles/how-to-upgrade-to-selenium-4*

## [2-2 Capabilities](https://www.selenium.dev/documentation/webdriver/capabilities/)

**<u>Shared capabilities</u>**

These capabilities are shared by all browsers.

**<u>Capabilities specific to Chromium browsers</u>**

These capabilities are specific to Chromium based browsers.

**<u>Capabilities specific to Firefox browser</u>**

These capabilities are specific to Firefox.

<u>**Capabilities specific to Internet Explorer browser**</u>

These capabilities are specific to Internet Explorer.

**<u>Capabilities specific to Safari browser</u>**

These capabilities are specific to Safari.

### [2-2-1 Shared](https://www.selenium.dev/documentation/webdriver/capabilities/shared/)

<u>These capabilities are shared by all browsers.</u>

In order to create a new session by Selenium WebDriver, the local end should provide the basic capabilities to the remote end. The remote end uses the same set of capabilities to create a session and describes the current session features.

WebDriver provides capabilities that each remote end will/should support the implementation. The following capabilities are supported by WebDriver:

#### browserName

This capability is used to set the `browserName` for a given session. If the specified browser is not installed at the remote end, the session creation will fail.

#### browserVersion

This capability is optional, this is used to set the available browser version at remote end. For example, if ask for Chrome version 75 on a system that only has 80 installed, the session creation will fail.

#### pageLoadStrategy

When navigating to a new page via URL, by default Selenium will wait until the Document's Ready State is "complete". The `document.readyState` property of a document describes the loading state of the current document. By default, WebDriver will hold off on completing a navigation method(e.g. `driver.navigate().get()`) until the document ready state is `complete`. This does not necessarily mean that the page has finished loading, especially for sites like Single Page Applications that use a lot of JavaScript to dynamically load content after the Ready State returns complete. Note also that this behavior does not apply to navigation that is a result of clicking an element or submitting a form.

If a page takes a long time to load as a result of downloading assets(e.g images, css, js) that aren't important to the automation, you can change from the default parameter of `normal` to `eager` or `none` to speed up the session. This value applies to the entire session, so make sure that your waiting strategy is sufficient to minimize flakiness.

The page load strategy queries the [`document.readyState`](https://developer.mozilla.org/en-US/docs/Web/API/Document/readyState) as described in the table below:

| Strategy | Ready State |                            Notes                             |
| :------: | :---------: | :----------------------------------------------------------: |
|  normal  |  complete   |     Used by default, waits for all resources to download     |
|  eager   | interactive | DOM access is ready, but other resources like images may still be loading |
|   none   |     any     |               Does not block WebDriver at all                |

##### normal

This will make Selenium WebDriver to wait for the entire page is loaded. When set to normal, Selenium WebDriver waits until the [load](https://developer.mozilla.org/en-US/docs/Web/API/Window/load_event) event is returned.

By default normal is set to browser if none is provided.

**<u>Python</u>**

```python
from selenium import WebDriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)
driver.get("http://www.google.com")
driver.quit()
```

**<u>CSharp</u>**

```c#
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

namespace pageLoadStrategy{
    class pageLoadStrategy{
        public static void Main(string[] args){
            var chromeOptions = new ChromeOptions();
            chromeOptions.PageLoadStrategy = PageLoadStrategy.Normal;
            IWebDriver driver = new ChromeDriver(chromeOptions);
            try{
                driver.Navigate().GoToUrl("https://example.com");
            } finally{
                driver.Quit();
            }
        }
    }
}
```

##### eager

This will make Selenium WebDriver to wait until the initial HTML document has been completely loaded and parsed, and discards loading of stylesheets, images and subsframes.

When set to eager, Selenium WebDriver waits until [DOMContentLoaded](https://developer.mozilla.org/en-US/docs/Web/API/Document/DOMContentLoaded_event) event fire is returned.

**<u>Python</u>**

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com")
driver.quit()
```

**<u>CSharp</u>**

```c#
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

namespace pageLoadStrategy{
    class pageLoadStrategy{
        public static void Main(string[] args){
            var chromeOptions = new ChromeOptions();
            chromeOptions.PageLoadStrategy = PageLoadStrategy.Eager;
            IWebDriver driver = new ChromeDriver(chromeOptions);
            try{
                driver.Navigate().GoToUrl("https://example.com");
            } finally{
                driver.Quit();
            }
        }
    }
}
```

##### none

When set to none Selenium WebDriver only waits until the initial page is downloaded.

**<u>Python</u>**

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.page_load_strategy = 'none'
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com")
driver.quit()
```

**<u>CSharp</u>**

```c#
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

namespace pageLoadStrategy{
    class pageLoadStrategy{
        public static void Main(string[] args){
            var chromeOptions = new ChromeOptions();
            chromeOptions.PageLoadStrategy = PageLoadStrategy.None;
            IWebDriver driver = new ChromeDriver(chromOptions);
            try{
                driver.Navigate().GoToUrl("https://example.com");
            } finally{
                driver.Quit();
            }
        }
    }
}
```

#### platformName

This identifies the operating system at the remote-end, fetching the `platformName` returns the OS name.

In cloud-based providers, setting `platformName` sets the OS at the remote-end.

#### acceptInsecureCerts

This capability checks whether an expired (or) invalid <u>TLS Certificate</u> is used while navigating during a session.

If the capability is set to `false`, an [insecure certificate error](https://developer.mozilla.org/en-US/docs/Web/WebDriver/Errors/InsecureCertificate) will be returned as navigation encounters any domain certificate problems. If set to `true`, invalid certificate will be trusted by the browser.

All self-signed certificates will be trusted by this capability by default. Once set, `acceptInsecureCerts` capability will have an effect for the entire session.

#### timeouts

A WebDriver <u>session</u> is imposed with a certain <u>session timeout</u> interval, during which the user can control the behavior of executing scripts or retrieving information from the browser.

Each session timeout is configured with combination of different <u>timeouts</u> as described below:

##### Script Timeout

Specifies when to interrupt an executing script in a current browsing context. The default timeout <u>30,000</u> is imposed when a new session is created by WebDriver.

##### Page Load Timeout

Specified the time interval in which web page needs to be loaded in a current browsing context. The default timeout <u>300,000</u> is imposed when a new session is created by WebDriver. If page load limits a given/default time frame, the script will be stopped by `TimeoutException`.

##### Implicit Wait Timeout

This specifies the time to wait for the implicit element location strategy when locating elements. The default timeout <u>0</u> is imposed when a new session is created by WebDriver.

#### unhandledPromptBehavior

Specifies the state of current session's `user prompt handler`. Defaults to <u>dismiss and notify state</u>

##### User Prompt Handler

This defines what action must take when a user prompt encounters at the remote-end. This is defined by `unhandledPromptBehavior` capability and has the following states:

* dismiss
* accept
* dismiss and notify
* accept and notify
* ignore

#### setWindowRect

This command alters the size and position of the current browsing context window. This command acts as setter to `getWindowRect` command which accepts width, height, x, y as optional arguments.

During automation, the current browsing context will be associated with window states, which describe the visibility of the browser window. The window states are

* maximized
* minimized
* normal
* fullscreen

Setting *Width* or *Height* does not guaranteed that the resulting window size will exactly match that which was requested. This is because some drivers may not be able to resize in single-pixel increments. Due to this, fetching the window state/details by `getWindowRect` may not match the values set in the browser.

#### strictFileInteractability

This new capability indicates if strict interactability checks should be applied to <u>input type=file</u> elements. As strict interactability checks are off by default, there is a change in behavior when using <u>Element Send Keys</u> with hidden file upload controls.

#### proxy

A proxy server acts as an intermediary for requests between a client and a server. In simple, the traffic flows through the proxy server on its way to the address you requested and back.

A proxy server for automation scripts with Selenium could be helpful for:

* Capture network traffic
* Mock backend calls made by the website
* Access the required website under complex network topologies or strict corporate restrictions/policies.

If you are in a corporate environment, and a browser fails to connect to a URL, this is most likely because the environment needs a proxy to be accessed.

Selenium WebDriver provides a way to proxy settings:

**<u>Python</u>**

```python
from selenium import webdriver

PROXY = "<HOST:PORT>"
webdriver.DesiredCapabilites.FIREFOX['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "proxyType": "MANUAL"
}

with webdriver.Firefox() as driver:
    driver.get("https://selenium.dev")
```

**<u>CSharp</u>**

```c#
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

public class ProxyTest{
    publich static void Main(){
        ChromeOptions options = new ChromeOptions()；
        Proxy proxy = new Proxy();
        proxy.Kind = ProxyKind.Manual;
        proxy.IsAutoDetect = false;
        proxy.SslProxy = "<HOST:PORT>";
        options.Proxy = proxy;
        options.AddArgument("ignore-certificate-errors");
        IWebDriver driver = new ChromeDriver(options);
        driver.Navigate().GoToUrl("https://www.selenium.dev/");
    }
}
```


### [2-2-2 Chromium](https://www.selenium.dev/documentation/webdriver/capabilities/chromium/)

These Capabilities are specific to Chromium based browsers.

These Capabilities apply to:

* Chrome
* Chromium
* Edge

### [2-2-3 Firefox](https://www.selenium.dev/documentation/webdriver/capabilities/firefox/)

These capabilities are specific to Firefox.

#### Define Capabilities using `FirefoxOptions`

`FirefoxOptions` is the new way to define capabilities for the Firefox browser and should generally be used in preference to DesiredCapabilities.

**<u>Python</u>**

```python
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
```

**<u>CSharp</u>**

```c#
var options = new FirefoxOptions();
options.Proxy.Kind = ProxyKind.Direct;
var driver = new FirefoxDriver(options);
```

#### Setting a custom profile

It is possible to create a custom profile for Firefox as demonstrated below.

**<u>Python</u>**

```python
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

options = Options()
firefox_profile = FirefoxProfile()
firefox_profile.set_preference("javascript.enabled", False)
options.profile = firefox_profile
```

**<u>CSharp</u>**

```c#
var options = new FirefoxOptions();
var profile = new FirefoxProfile();
options.Profile = profile;
var driver = new RemoteWebDriver(options);
```

### [2-2-4 Internet Explorer](https://www.selenium.dev/documentation/webdriver/capabilities/internet_explorer/)

暂略

### [2-2-5 Safari](https://www.selenium.dev/documentation/webdriver/capabilities/safari/)

These capabilities are specific to Safari.

## [2-3 Browser](https://www.selenium.dev/documentation/webdriver/browser/)

### Get browser information

#### Get title

**<u>Python</u>**

```python
driver.title
```

**<u>CSharp</u>**

```c#
driver.Title;
```

#### Get current URL

**<u>Python</u>**

```python
driver.current_url
```

**<u>CSharp</u>**

```c#
driver.Url;
```

### [Navigation](https://www.selenium.dev/documentation/webdriver/browser/navigation/)

#### Navigate to

The first thing you will want to do after launching a browser is to open your website. This can be achieved in a single line:

**<u>Python</u>**

```python
driver.get("https://selenium.dev")
```

**<u>CSharp</u>**

```c#
driver.Navigate().GoToUrl(@"https://selenium.dev");
```

#### Back

Pressing the browser's back button:

**<u>Python</u>**

```python
driver.back()
```

**<u>CSharp</u>**

```c#
driver.Navigate().Back();
```

#### Forward

Pressing the browser's forward button:

**<u>Python</u>**

```python
driver.forward()
```

**<u>CSharp</u>**

```c#
driver.Navigate().Forward();
```

#### Refresh

Refresh the current page:

**<u>Python</u>**

```python
driver.refresh()
```

**<u>CSharp</u>**

```c#
driver.Navigate().Refresh();
```

### [Alerts](https://www.selenium.dev/documentation/webdriver/browser/alerts/)

WebDriver provides an API for working with the three types of native popup messages offered by JavaScript. These popups are styled by the browser and offer limited customization.

#### Alerts

The simplest of these is referred to as an alert, which shows a custom message, and a single button which dismisses the alert, labelled in most browsers as OK. It can also be dismissed in most browsers by pressing the close button, but this will always do the same thing as the OK buton.

WebDriver can get the text from the popup and accept or dismiss these alerts.

**<u>Python</u>**

```python
# Click the link to activate the alert
driver.find_element(By.LINK_TEXT, "See an example alert").click()

# Wait for the alert to be displayed and store it in a variable
alert = wait.until(expected_conditions.alert_is_present())

# Store the alert text in a variable
text = alert.text

# Press the OK button
alert.accept()
```

**<u>CSharp</u>**

```c#
//Click the link to activate the alert
driver.FindElement(By.LinkText("See an example alert")).Click();

//Wait for the alert to be displayed and store it in a variable
IAlert alert = wait.Unti(ExpectedConditions.AlertIsPresent());

//Store the alert text in a variable
string text = alert.Text;

//Press the OK button
alert.Accept();
```

#### Confirm

A confirm box is similar to an alert, except the user can also choose to cancel the message.

This example also shows a different approach to storing an alert:

**<u>Python</u>**

```python
# Click the link to activate the alert
driver.find_element(By.LINK_TEXT, "See a sample confirm").click()

# Wait for the alert to be displayed
wait.until(exepcted_conditions.alert_is_present())

# Store the alert in a variable for reuse
alert = driver.swtich_to.alert

# Store the alert text in a variable
text = alert.text

# Press the Cancel button
alert.dismiss()
```

**<u>CSharp</u>**

```c#
//Click the link to activate the alert
driver.FindElement(By.LinkText("See a sample confirm")).Click();

//Wait for the alert to be displayed
wait.Until(ExpectedConditions.AlertIsPresent());

//Store the alert in a variable
IAlert alert = driver.SwitchTo().Alert();

//Store the alert in a variable for reuse
string text = alert.Text;

//Press the cancel button
alert.Dismiss();
```

#### Prompt

Prompts are similar to confirm boxes, except they also include a text input. Similar to working with form elements, you can use WebDriver's send keys to fill in a response. This will completely replace the placeholder text. Pressing the cancel button will not submit any text. See a sample prompt.

**<u>Python</u>**

```python
# Click the link to activate the alert
driver.find_element(By.LINK_TEXT, "See a sample prompt").click()

# Wait for the alert to be displayed
wait.until(expected_conditions.alert_is_present())

# Store the alert in a variable for reuse
alert = Alert(driver)

# Type your message
alert.send_keys("Selenium")

# Press the OK button
alert.accept()
```

**<u>CSharp</u>**

```c#
//Click the link to activate the alert
driver.FindElement(By.LinkText("See a sample prompt")).Click();

//Wait for the alert to be displayed and store it in a variable
IAlert alert = wait.Until(ExpectedConditions.AlertIsPresent());

//Type your message
alert.SendKeys("Selenium");

//Press the OK button
alert.Accept();
```

### [Cookies](https://www.selenium.dev/documentation/webdriver/browser/cookies/)

A cookie is a small piece of data that is sent from a website and stored in your computer. Cookies are mostly used to recognize the user and load the stored information.

WebDriver API provides a way to interact with cookies with built-in methods.

#### Add Cookie

It is used to add a cookie to the current browsing context. Add cookie only accepts a set of defined serializable JSON object. [Here](https://www.w3.org/TR/webdriver1/#cookies) is the link to the list of accepted JSON key values.

First of all, you need to be on the domain that the cookie will be valid for. If you are trying to preset[^1] cookies before you start interacting with a site and your homepage is large/takes a while to load an alternative is to find a smaller page on the site (typically the 404 page is small, e.g. http://example.com/some404page)

**<u>Python</u>**

```python
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.example.com")

# Adds the cookie into current browser context
driver.add_cookie({"name": "key", "value": "value"})
```

**<u>CSharp</u>**

```c#
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

namespace AddCookie {
    class AddCookie {
        public static void Main(string[] args){
            IWebDriver driver = new ChromeDriver();
            try{
                //Navigate to Url
                driver.Navigate().GoToUrl("https://example.com");
                // Adds the cookie into current browser context
                driver.Manage().Cookies.AddCookie(new Cookie("key", "value"));
            } finally{
                driver.Quit();
            }
        }
    }
}
```

#### Get Named Cookie

It returns the serialized cookie data matching with the cookie name among all associated cookies.

**<u>Python</u>**

```python
from selenium import webdriver

driver = webdriver.Chrome()

# Navigate to url
driver.get("http://www.example.com")

# Adds the cookie into current browser context
driver.add_cookie({"name": "foo", "value": "bar"})

# Get cookie details with named cookie 'foo'
print(driver.get_cookie("foo"))
```

**<u>CSharp</u>**

```c#
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

namespace GetCookieNamed{
    class GetCookieNamed{
        public static void Main(string[] args){
            IWebDriver driver = new ChromeDriver();
            try{
                // Navigate to Url
                driver.Navigate().GoToUrl("https://example.com");
                driver.Manage().Cookies.AddCookie(new Cookie("foo", "bar"));
                // Get cookie details with named cookie 'foo'
                var cookie = driver.Manage().Cookies.GetCookieNamed("foo");
                System.Console.WriteLine(cookie);
            } finally{
                driver.Quit();
            }
        }
    }
}
```

#### Get All Cookies

It returns a 'successful serialized cookie data' for current browsing context. If browser is no longer available it returns error.

**<u>Python</u>**

```python
from selenium import webdriver

drivr = webdriver.Chrome()

# Navigate to url
driver.get("http://www.example.com")

driver.add_cookie({"name": "test1", "value": "cookie1"})
driver.add_cookie({"name": "test2", "value": "cookie2"})

# Get all available cookies
print(driver.get_cookies())
```

**<u>CSharp</u>**

```c#
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

namespace GetAllCookies{
    class GetAllCookies{
        public static void Main(String[] args){
            IWebDriver driver = new ChromeDriver();
            try{
                // Navigate to Url
                driver.Navigate().GoToUrl("https://example.com");
                driver.Manage().Cookies.AddCookie(new Cookie("test1", "cookie1"));
                driver.Manage().Cookies.AddCookie(new Cookie("test2", "cookie2"));
                
                // Get All available cookies
                var cookies = driver.Manage().Cookies.AllCookies;
            } finally{
                driver.Quit();
            }
        }
    }
}
```

#### Delete Cookie

It deletes the cookie data matching with the provided cookie name.

**<u>Python</u>**

```python
from selenium import webdriver
driver = webdriver.Chrome()

# Navigate to url
driver.get("http://www.example.com")
driver.add_cookie({"name": "test1", "value": "cookie1"})
driver.add_cookie({"name": "test2", "value": "cookie2"})

# Delete a cookie with name 'test1'
driver.delete_cookie("test1")
```

**<u>CSharp</u>**

```c#
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

namespace DeleteCookie{
    class DeleteCookie{
        public static void Main(string[] args){
            IWebDriver driver = new ChromeDriver();
            try{
                // Navigate to Url
                driver.Navigate().GoToUrl("https://example.com");
                driver.Manage().Cookies.AddCookie(new Cookie("test1", "cookie1"));
                var cookie
            }
        }
    }
}
```

#### Delete All Cookies

It deletes all the cookies of the current browsing context.

**<u>Python</u>**

```python
from selenium import webdriver
driver = webdriver.Chrome()

# Navigate to url
driver.get("http://www.example.com")
driver.add_cookie({"name": "test1", "value": "cookie1"})
driver.add_cookie({"name": "test2", "value": "cookie2"})

# Delete all cookies
driver.delete_all_cookies()
```

**<u>CSharp</u>**

```c#
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

namespace DeleteAllCookies{
    class DeleteAllCookies{
        public static void Main(string[] args){
            IWebDriver driver = new ChromeDriver();
            try{
                // Navigate to Url
                driver.Navigate().GoToUrl("https://example.com");
                driver.Manage().Cookies.AddCookie(new Cookie("test1", "cookie1"));
                driver.Manage().Cookies.AddCookie(new Cookie("test2", "cookie2"));
                // deletes all cookies
                driver.Manage().Cookies.DeleteAllCookies();
            } finally{
                driver.Quit();
            }
        }
    }
}
```

#### Same-Site Cookie Attribute

It allows a user to instruct browsers to control whether cookies are sent along with the request initiated by third party sites. It is introduced to prevent CSRF(Cross-Site Request Forgery) attacks.

Same-site cookie attribute accepts two parameters as instructions.

##### Strict

When the sameSite attribute is set as <u>Strict</u>, the cookie will not be sent along with requests initiated by third party websites.

##### Lax

When you set a cookie sameSite attribute to <u>Lax</u>, the cookie will be sent along with the GET request initiated by third party website.

> Note: As of now this feature is landed in chrome(80+version), Firefox(79+version) and works with Selenium 4 and later versions.

**<u>Python</u>**

```python
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://example.com")
# Adds the cookie into current browser context with sameSite 'Strict' (or) 'Lax'
driver.add_cookie({"name": "foo", "value": "value", "sameSite": "Strict"})
driver.add_cookie({"name": "foo1", "value": "value", "sameSite": "Lax"})
cookie1 = driver.get_cookie('foo')
cookie2 = driver.get_cookie('foo1')
print(cookie1)
print(cookie2)
```

**<u>CSharp</u>**

```c#
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

namespace SameSiteCookie{
    class SameSiteCookie{
        static void Main(string[] args){
            IWebDriver driver = new ChromeDriver();
            try{
                driver.Navigate().GoToUrl("http://www.example.com");
                var cookie1Dictionary = new System.Collections.Generic.Dictionary<string, object>(){{"name", "test1"}, {"value", "cookie1"}, {"sameSite", "Strict"}};
                var cookie1 = Cookie.FromDictionary(cookie1Dictionary);
                var cookie2Dictionary = new System.Collections.Generic.Dictionary<string, object>(){{"name", "test2"}, {"value", "cookie2"}, {"sameSite", "Lax"}};
                var cookie2 = Cookie.FromDictionary(cookie2Dictionary);
                
                driver.Manage().Cookies.AddCookie(cookie1);
                driver.Manage().Cookies.AddCookie(cookie2);
                
                System.Console.WriteLine(cookie1.SameSite);
                System.Console.WriteLine(cookie2.SameSite);
            } finally{
                driver.Quit();
            }
        }
    }
}
```

### [Frames](https://www.selenium.dev/documentation/webdriver/browser/frames/)

Frames are a now deprecated means of building a site layout from multiple documents on the same domain. You are unlikely to work with them unless you are working with an pre HTML5 webapp. Iframes allow the insertion of a document from an entirely different domain, and are still commonly used.

If you need to work with frames or iframes, WebDriver allows you to work with them in the same way. Consider a button within an iframe. If we inspect the element using the browser development tools, we might see the following:

```html
<div id="modal">
  <iframe id="buttonframe" name="myframe"  src="https://seleniumhq.github.io">
   <button>Click here</button>
 </iframe>
</div>
```

If it was not for the iframe we would expect to click on the button using something like:

**<u>Python</u>**

```python
# This won't work
driver.find_element(By.TAG_NAME, 'button').click()
```

**<u>CSharp</u>**

```c#
// This won't work
driver.FindElement(By.TagName("button")).Click();
```

However, if there are no buttons outside of the iframe, you might instead get a *no such element* error. This happens because Selenium is only aware of the elements in the top level document. To interact with the button, we will need to first switch to the frame, in a similar way to how we switch windows. WebDriver offers three ways of switching to a frame.

#### Using a WebElement

Switching using a WebElement is the most flexible option. You can find the frame using your preferred selector and switch to it.

**<u>Python</u>**

```python
# Store iframe web element
iframe = driver.find_element(By.CSS_SELECTOR, "#modal > iframe")

# Switch to selected iframe
driver.switch_to.frame(iframe)

# Now click on button
driver.find_element(By.TAG_NAME, 'button').click()
```

**<u>CSharp</u>**

```c#
// Store the web element
IWebElement iframe = driver.FindElement(By.CssSelector("#modal>iframe"));

// Switch to the frame
driver.SwitchTo().Frame(iframe);

// Now we can click the button
driver.FindElement(By.TagName("button")).Click();
```

#### Using a name or ID

If your frame or iframe has an id or name attribute, this can be used instead. If the name or ID is not unique on the page, then the first one found will be switched to.

**<u>Python</u>**

```python
# Swtich frame by id
driver.switch_to.frame('buttonframe')

# Now click on the button
driver.find_element(By.TAG_NAME, 'button').click()
```

**<u>CSharp</u>**

```c#
// Using the ID
driver.SwitchTo().Frame("buttonframe");

// Or using the name instead
driver.SwitchTo().Frame("myframe");

// Now we can click the button
driver.FindElement(By.TagName("button")).Click();
```

#### Using an index

It is also possible to use the index of the frame, such as can be queried using `window.frames` in JavaScript.

**<u>Python</u>**

```python
# Switching to second iframe based on index
iframe = driver.find_elements_by_tag_name('iframe')[1]

# switch to selected iframe
driver.switch_to.frame(iframe)
```

**<u>CSharp</u>**

```c#
// Switch to the second frame
driver.SwitchTo().Frame(1);
```

#### Leaving a frame

To leave an iframe or frameset, switch back to the default content like so:

**<u>Python</u>**

```python
# switch back to default content
driver.switch_to.default_content()
```

**<u>CSharp</u>**

```c#
// Return to the top level
driver.SwitchTo().DefaultContent();
```

### [Windows](https://www.selenium.dev/documentation/webdriver/browser/windows/)

#### Windows and tabs

##### Get window handle

WebDriver does not make the distinction between windows and tabs. If your site opens a new tab or window, Selenium will let you work with it using a window handle. Each window has a unique identifier which remains persistent in a single session. You can get the window handle of the current window by using:

**<u>Python</u>**

```python
driver.current_window_handle
```

**<u>CSharp</u>**

```c#
driver.CurrentWindowHandle;
```

##### Switching windows or tabs

Clicking a link which opens in w new window will focus the new window or tab on screen, but WebDriver will now know which window the Operating System considers active. To work with the new window you will need to switch to it. If you have only two tabs or windows open, and you know which window you start with, by the process of elimination you can loop over both windows or tabs that WebDriver can see, and switch to the one which is not the original.

However, Selenium 4 provides a new API [NewWindow](https://www.selenium.dev/documentation/webdriver/browser/windows/#create-new-window-or-new-tab-and-switch) which creates a new tab (or) new window and automatically switches to it.

**<u>Python</u>**

```python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Firefox() as driver:
    # Open URL
    driver.get("https://seleniumhq.github.io")
    
    # Setup wait for later
    wait = WebDriverWait(driver, 10)
    
    # Store the ID of the original window
    original_window = driver.current_window_handle
    
    # Check we don't have other windows open already
    assert len(driver.window_handles) == 1
    
    # Click the link which opens in a new window
    driver.find_element(By.LINK_TEXT, "new window").click()
    
    # Wait for the new window or tab
    wait.until(EC.number_of_windows_to_be(2))
    
    # Loop through until we find a new window handle
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
            
    # Wait for the new tab to finish loading content
    wait.until(EC.title_is("SeleniumHQ Browser Automation"))
```

**<u>CSharp</u>**

```c#
// Store the ID of the original window
string originalWindow = driver.CurrentWindowHandle;

// Check we don't have other windows open already
Assert.AreEqual(driver.WindowHandles.Count, 1);

// Click the link which opens in a new window
driver.FindElement(By.LinkText("new window")).Click();

// Wait for the new window or tab
wait.Until(wd => wd.WindowHandles.Count == 2);

// Loop through until we find a new window handle
foreach(string window in driver.WindowHandles){
    if(originalWindow != window){
        driver.SwitchTo().Window(window);
        break;
    }
}

// Wait for the new tab to finish loading content
wait.Unti(wd => wd.Title == "Selenium documentation");
```

##### Create new window (or) new tab and switch

Creates a new window （or) tab and will focus the new window or tab on screen. You don't need to switch to work with the new window (or) tab. If you have more than two windows (or) tabs opened other than the new window, you can loop over both windows or tabs that WebDriver can see, and switch to the one which is not the original.

> Note: This feature works with Selenium 4 and later versions.

**<u>Python</u>**

```python
# Opens a new tab and switches to new tab
driver.switch_to.new_window('tab')

# Opens a new window and switches to new window
driver.switch_to.new_window('window')
```

**<u>CSharp</u>**

```c#
// Opens a new tab and switches to new tab
driver.SwitchTo().NewWindow(WindowType.Tab)
    
// Opens a new window and switches to new window
driver.SwitchTo().NewWindow(WindowType.Window)
```

##### Closing a window or tab

When you are finished with a window or tab and it is not the last window or tab open in your browser, you should close it and switch back to the window you were using previously. Assuming you followed the code sample in the previous section you will have the previous window handle stored in a variable. Put this together and you will get:

**<u>Python</u>**

```python
# Close the tab or window
driver.close()

# Switch back to the old tab or window
driver.switch_to.window(original_window)
```

**<u>CSharp</u>**

```c#
// Close the tab or window
driver.Close();

// Switch back to the old tab or window
driver.SwitchTo().Window(originalWindow);
```

Forgetting to switch back to another window handle after closing a window will leave WebDriver executing on the now closed page, and will trigger a *<u>No Such Window Exception</u>*. You must switch back to a valid window handle in order to continue execution.

##### Quitting the browser at the end of a session

When you are finished with the browser session you should call quit, instead of close:

**<u>Python</u>**

```python
driver.quit()
```

**<u>CSharp</u>**

```c#
driver.Quit();
```

Quit will;

* Close all the windows and tabs associated with that WebDriver session
* Close the browser process
* Close the background driver process
* Notify Selenium Grid that the browser is no longer in use so it can be used by another session(if you are using Selenium Grid)

Failure to call quit will leave extra background processes and ports running on your machine which could cause you problems later.

Some test frameworks offer methods and annotations which you can hook into tear down at the end of a test.

**<u>Python</u>**

```python
# unittest teardown
# https://docs.python.org/3/library/unittest.html?highlight=teardown#unittest.TestCase.tearDown
def tearDown(self):
    self.driver.quit()
```

**<u>CSharp</u>**

```c#
/* 
	Example using Visual Studio's UnitTesting
	https://msdn.microsoft.com/en-us/library/microsoft.visualstudio.testtools.unittesting.aspx
*/
[TestCleanup]
public void TearDown(){
    driver.Quit();
}
```

If not running WebDriver in a test context, you may consider using `try/finally` which is offered by most languages so that an exception will still clean up the WebDriver session.

**<u>Python</u>**

```python
try:
    # WebDriver code here...
finally:
    driver.quit()
```

**<u>CSharp</u>**

```c#
try{
    // WebDriver code here...
} finally{
    driver.Quit();
}
```

Python's WebDriver now supports the python context manager, which when using the `with` keyword can automatically quit the driver at the end of execution.

```python
with webdriver.Firefox() as driver:
    # WebDriver code here...
    
# WebDriver will automatically quit after indentation
```

#### Window management

Screen resolution can impact how your web application renders, so WebDriver provides mechanisms for moving and resizing the browser window.

##### Get window size

Fetches the size of the browser window in pixels.

**<u>Python</u>**

```python
# Access each dimension individually
width = driver.get_window_size().get("width")
height = driver.get_window_size().get("height")

# Or store the dimensions and query them later
size = driver.get_window_size()
width1 = size.get("width")
height1 = size.get("height")
```

**<u>CSharp</u>**

```c#
// Access each dimension individually
int width = driver.Manage().Window.Size.Width;
int height = driver.Manage().Window.Size.Height;

// Or store the dimensions and query them later
System.Drawing.Size size = driver.Manage().Window,Size();
int width1 = size.Width;
int height1 = size.Height;
```

##### Set window size

Restores the window and sets the window size.

**<u>Python</u>**

```python
driver.set_window_size(1024, 768)
```

**<u>CSharp</u>**

```c#
driver.Manage().Window.Size = new Size(1024, 768);
```

##### Get window position

Fetches the coordinates of the top left coordinate of the browser window.

**<u>Python</u>**

```python
# Access each dimension individually
x = driver.get_window_position().get('x')
y = driver.get_window_position().get('y')

# Or store the dimensions and query them later
position = driver.get_window_position()
x1 = position.get('x')
y1 = position.get('y')
```

**<u>CSharp</u>**

```c#
// Access each dimension individually
int x = driver.Manage().Window.Position.X;
int y = driver.Manage().Window.Position.Y;

// Or store the dimensions and query them later
Point position = driver.Manage().Window.Position;
int x1 = position.X;
int y1 = position.Y;
```

#### Set window position

Moves the window to the chosen position.

**<u>Python</u>**

```python
# Move the window to the top left of the primary monitor
driver.set_window_position(0, 0)
```

**<u>CSharp</u>**

```c#
// Move the window to the top left of the primary monitor
driver.Manage().Window.Position = new Point(0, 0);
```

##### Maximize window

Enlarges[^2] the window. For most operating systems, the window will fill the screen, without blocking the operating system's own menus and toolbars.

**<u>Python</u>**

```python
driver.maximize_window()
```

**<u>CSharp</u>**

```c#
driver.Manage().Window.Maximize();
```

##### Minimize window

Minimizes the window of current browsing context. The exact behavior of this command is specific to individual window managers.

Minimize Window typically hides the window in the system tray.

> Note: this feature works with Selenium 4 and later versions.

**<u>Python</u>**

```python
driver.minimize_window()
```

**<u>CSharp</u>**

```c#
driver.Manage().Window.Minimize();
```

##### Fullscreen window

Fills the entire screen, similar to pressing F11 in most browsers.

**<u>Python</u>**

```python
driver.fullscreen_window()
```

**<u>CSharp</u>**

```c#
driver.Manage().Window().FullScreen();
```

##### TakeScreenshot

Used to capture screenshot for current browsing context. The WebDriver endpoint [screenshot](https://www.w3.org/TR/webdriver/#dfn-take-screenshot) returns screenshot which is encoded in Base64 format.

**<u>Python</u>**

```python
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.example.com")
# Returns and base64 encoded string into image
driver.save_screenshot('./image.png')
driver.quit()
```

**<u>CSharp</u>**

```c#
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Support.UI;

var driver = new ChromeDriver();
driver.Navigate().GoToUrl("http://www.example.com");
Screenshot screenshot = (driver as ITakeScreenshot).GetScreenshot();
// Format values are Bmp, Gif, Jpeg, Png, Tiff
screenshot.SaveAsFile("screenshot.png", ScreenshotImageFormat.Png); 
```

##### TakeElementScreenshot

Used to capture screenshot of an element for current browsing context. The WebDriver endpoint [screenshot](https://www.w3.org/TR/webdriver/#take-element-screenshot) returns screenshot which is encoded in Base64 format.

**<u>Python</u>**

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.example.com")
ele = driver.find_element(By.CSS_SELECTOR, 'h1')
# Returns and base64 encoded string into image
ele.screenshot('./image.png')
driver.quit()
```

**<u>CSharp</u>**

```c#
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Support.UI;

// WebDriver
var driver = new ChromeDriver();
driver.Navigate().GoToUrl("http://www.example.com");

// Fetch element using FindElement
var webElement = driver.FindElement(By.CssSelector("h1"));

// Screenshot for the element
var elementScreenshot = (webElement as ITakeScreenshot).GetScreenshot();
elementScreenshot.SaveAsFile("screenshot_of_element.png");
```

##### Execute Script

Executes JavaScript code snippet[^3] in the current context of a selected frame or window.

**<u>Python</u>**

```python
# Stores the header element
header = driver.find_element(By.CSS_SELECTOR, "h1")

# Executing JavaScript to capture innerText of header element
driver.execute_script('return arguments[0].innerText', header)
```

**<u>CSharp</u>**

```c#
// creating ChromeDriver instance
IWebDriver driver = new ChromeDriver();
// Creating the JavaScriptExecutor interface object by Type casting
IJavaScriptExecutor js = (IJavaScriptExecutor) driver;
// Button Element
IWebElement button = driver.FindElement(By.name("btnLogin"));
// Executing JavaScript to click on element
js.ExecuteScript("arguments[0].click();", button);
// Get return value form script
String text = (String)js.ExecuteScript("return arguments[0].innerText", button);
// Executing JavaScript directly
js.ExecuteScript("console.log('hello world')");
```

##### Print Page

Prints the current page within the browser.

> Note: This requires Chromium browsers to be in headless mode

**<u>Python</u>**

```python
from selenium.webdriver.common.print_page_options import PrintOptions

print_options = PrintOptions()
print_options.page_ranges = ['1-2']

driver.get("printPage.html")
base64code = driver.print_page(print_options)
```

**<u>CSharp</u>**

```c#
// code sample not available
```

## [2-4 Elements](https://www.selenium.dev/documentation/webdriver/elements/)

Identifying and working with element objects in the DOM.

The majority of most people's Selenium code involves working with web elements.

### [Locators](https://www.selenium.dev/documentation/webdriver/elements/locators/)

<u>Ways to identify one or more specific elements in the DOM.</u>

A locator is a way to identify elements on a page. It is the argument passed to the [Finding element](https://www.selenium.dev/documentation/webdriver/elements/finders/) methods.

Check out our encouraged test practices for tips on [locators](https://www.selenium.dev/documentation/test_practices/encouraged/locators/), including which to use when and why to declare locators separately from the finding methods. 

#### Traditional Locators

Selenium provides support for these 8 traditional location strategies in WebDriver:

|      Locator      |                         Description                          |
| :---------------: | :----------------------------------------------------------: |
|    class name     | Locates elements whose class name contains the search value(compound class names are not permitted) |
|   css selector    |           Locates elements matching a CSS selector           |
|        id         | Locates elements whose ID attribute matches the search value |
|       name        | Locates elements whose NAME attribute matches the search value |
|     link text     | Locates anchor elements whose visible text matches the search value |
| partial link text | Locates anchor elements whose visible text contains the search value. If multiple elements are matching, only the first one will be selected. |
|     tag name      |   Locates elements whose tag name matches the search value   |
|       xpath       |        Locates elements matching an XPath expression         |

#### Relative Locators

Selenium 4 introduces Relative Locators(previously called as *<u>Friendly Locators</u>*). These locators are helpful when it is not easy to construct a locator for the desired element, but easy to describe spatially[^4] where the element is in relation to an element that does have an easily constructed locator.

##### How it works

Selenium uses the JavaScript function [`getBoundingClientRect()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect) to determine the size and position of elements on the page, and can use this information to locate neighboring elements.

Relative locator methods can take as the argument for the point of origin, either a previously located element reference, or another locator. In these examples we'll be using locators only, but you could swap the locator in the final method with an element object and it will work the same.

Let us consider the below example for understanding the relative locators.

![](https://www.selenium.dev/images/documentation/webdriver/relative_locators.png)

##### Available relative locators

###### Above

If the email text field element is not easily identifiable for some reason, but the password text field element is, we can locate the text field element using the fact that it is an "input" element "above" the password element.

**<u>Python</u>**

```python
email_locator = locate_with(By.TAG_NAME, "input").above({By.ID: "password"})
```

**<u>CSharp</u>**

```c#
var emailLocator = RelativeBy.WithLocator(By.tagName("input")).Above(By.Id("password"));
```

###### Below

If the password text field is not easily identifiable for some reason, but the email text field is, we can locate the text field element using the fact that it is an "input" element "below" the email element.

**<u>Python</u>**

```python
password_locator = locate_with(By.TAG_NAME, "input").below({By.ID: "email"})
```

**<u>CSharp</u>**

```c#
var passwordLocator = RelativeBy.WithLocator(By.tagName("input")).Below(By.Id("email"));
```

###### Left of

If the cancel button is not easily identifiable for some reason, but the submit button element is, we can locate the cancel button element using the fact that it is a "button" element to the "left of" the submit element.

**<u>Python</u>**

```python
cancel_locator = locate_with(By.TAG_NAME, "button").to_left_of({By.ID: "submit"})
```

**<u>CSharp</u>**

```c#
var cancelLocator = RelativeBy.WithLocator(By.tagName("button")).LeftOf(By.Id("submit"));
```

###### Right of

If the submit button is not easily identifiable for some reason, but the cancel button element is, we can locate the submit button element using the fact that it is a "button" element "to the right of" the cancel element.

**<u>Python</u>**

```python
submit_locator = locate_with(By.TAG_NAME, "button").to_right_of({By.ID: "cancel"})
```

**<u>CSharp</u>**

```c#
var submitLocator = RelativeBy.WithLocator(By.tagName("button")).RightOf(By.Id("cancel"));
```

###### Near

If the relative positioning is not obvious, or it varies based on window size, you can use the near method to identify an element an element that is at most 50px away from the provided locator. One great use case for this is to work with a form element that doesn't have an easily constructed locator, but its associated [input label element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label) does.

**<u>Python</u>**

```python
email_locator = locate_with(By.TAG_NAME, "input").near({By.ID: "lbl-email"})
```

**<u>CSharp</u>**

```c#
var emailLocator = RelativeBy.WithLocator(By.tagName("input")).Near(By.Id("lbl-email"));
```

##### Chaining relative locators

You can also chain locators if needed. Sometimes the element is most easily identified as being both above/below one element and right/left of another.

**<u>Python</u>**

```python
submit_locator = locate_with(By.TAG_NAME, "button").below({By.ID: "email"}).to_right_of({By.ID: "cancel"})
```

**<u>CSharp</u>**

```c#
var submitLocator = RelativeBy.WithLocator(By.tagName("button")).Below(By.Id("email")).RightOf(By.Id("cancel"));
```

### [Finders](https://www.selenium.dev/documentation/webdriver/elements/finders/)

> Locating the elements based on the provided locator values.

One of the most fundamental aspects of using Selenium is obtaining element references to work with. Selenium offers a number of built-in locator strategies to uniquely identify an element. There are many ways to use the locators in very advanced scenarios. For the purposes of this documentation, let's consider this HTML snippet:

```html
<ol id="vegetables">
 <li class="potatoes">…
 <li class="onions">…
 <li class="tomatoes"><span>Tomato is a Vegetable</span>…
</ol>
<ul id="fruits">
  <li class="bananas">…
  <li class="apples">…
  <li class="tomatoes"><span>Tomato is a Fruit</span>…
</ul>
```

#### First matching element

Many locators will match multiple elements on the page. The singular find element method will return a reference to the first element found within a given context.

##### Evaluating entire DOM

When the find element method is called on the driver instance, it returns a reference to the first element in the DOM that matches with the provided locator. This value can be stored and used for future element actions. In our example HTML above, there are two elements that have a class name of "tomatoes" so this method will return the element in the "vegetables" list.

**<u>Python</u>**

```python
vegetable = driver.find_element(By.CLASS_NAME, "tomatoes")
```

**<u>CSharp</u>**

```c#
var vegetable = driver.FindElement(By.ClassName("tomatoes"));
```

##### Evaluating a subset of the DOM

Rather than finding a unique locator in the entire DOM, it is often useful to narrow the search to the scope of another located element. In the above example there are two elements with a class name of "tomatoes" and it is a little more challenging to get the reference for the second one.

One solution is to locate an element with a unique attribute that is an ancestor[^5] of the desired element and not an ancestor of the undesired element, then call find element on that object:

**<u>Python</u>**

```python
fruits = driver.find_element(By.ID, "fruits")
fruit = fruits.find_elements_by_id("tomatoes")
```

**<u>CSharp</u>**

```c#
IWebElement fruits = driver.FindElement(By.Id("fruits"));
IWebElement fruit = fruits.FindElement(By.Id("tomatoes"));
```

> <u>Java and C#</u>
>
> `WebDriver`, `WebElement` and `ShadowRoot` classes all implement a `SearchContext` interface, which is considered a <u>role-based interface</u>. Role-based interfaces allow you to determine whether a particular driver implementation supports a given feature. These interfaces are clearly defined and try to adhere to having only a single role of responsibility.

##### Optimized locator

A nested lookup might not be the most effective location strategy since it requires two separate commands to be issued to the browser.

To improve the performance slightly, we can use either CSS or XPath to find this element in a single command. See the Locator strategy suggestions in our Encouraged test practices section.

For this example, we'll use a CSS selector:

**<u>Python</u>**

```python
fruit = driver.find_element_by_css_selector('#fruits .tomatoes')
```

**<u>CSharp</u>**

```c#
var fruit = driver.FindElement(By.CssSelector("#fruits .tomatoes"));
```

#### All matching elements

There are several use cases for needing to get references to all elements that match a locator, rather than just the first one. The plural elements methods return a collection of element references. If there are no matches, an empty list is returned. In this case, references to all fruits and vegetable list items will be returned in a collection.

**<u>Python</u>**

```python
plants = driver.find_elements(By.TAG_NAME, "li")
```

**<u>CSharp</u>**

```c#
IReadOnlyList<IWebElement> plants = driver.FindElements(By.TagName("li"));
```

##### Get element

Often you get a collection of elements but want to work with a specific element, which means you need to iterate over the collection and identify the one you want.

**<u>Python</u>**

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox();

# Navigate to Url
driver.get("https://www.example.com")

# Get all the elements available with tag name 'p'
elements = driver.find_elements(By.TAG_NAME, 'p')

for e in elements:
    print(e.text)
```

**<u>CSharp</u>**

```c#
using OpenQA.Selenium;
using OpenQA.Selenium.Firefox;
using System.Collections.Generic;

namespace FindElementsExample{
    class FindElementsExample{
        public static void Main(string[] args){
            IWebDriver driver = new FirefoxDriver();
            try{
                // Navigate to Url
                driver.Navigate().GoToUrl("https://example.com");
                // Get all the elements available with tag name 'p'
                IList <IWebElement> elements = driver.FindElements(By.TagName("p"));
                foreach(IWebElement e in elements){
                    System.Console.WriteLIne(e.Text);
                } 
             }finally{
              	driver.Quit();
            }
        }
    }
}
```

#### Find Elements From Element

It is used to find the list of matching child WebElements within the context of parent element. To achieve this, the parent WebElement is chained with 'findElements' to access child elements.

**<u>Python</u>**

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Get element with tag name 'div'
element = driver.find_element(By.TAG_NAME, 'div')

# Get all the elements available with tag name 'p'
elements = element.find_elements(By.TAG_NAME, 'p')
for e in elements:
    print(e.text)
```

**<u>CSharp</u>**

```c#
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using System.Collections.Generic;

namespace FindElementsFromElement{
    class FindElementsFromElement{
        public static void Main(string[] args){
            IWebDriver driver = new ChromeDriver();
            try{
                driver.Navigate().GoToUrl("https://example.com");
                // Get element with tag name 'div'
                IWebElement element = driver.FindElement(By.TagName('div'));
                // Get all the elements available with tag name 'p'
                IList <IWebElement> elements = element.FindElements(By.TagName("p"));
                foreach(IWebElement e in elements){
                    System.Console.WriteLine(e.Text);
                }
            } finally{
                driver.Quit();
            }
        }
    }
}
```

#### Get Active Element

It is used to track (or) find DOM element which has the focus in the current browsing context.

**<u>Python</u>**

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.find_element(By.CSS_SELECTOR， '[name="q"]').send_keys("webElement")

#　Get attribute of current active element
attr = driver.switch_to.active_element.get_attribute("title")
print(attr)
```

**<u>CSharp</u>**

```c#
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

namespace ActiveElement{
    class ActiveElement{
        public static void Main(string[] args){
            IWebDriver driver = new ChromeDriver();
            try{
                // Navigate to Url
                driver.Navigate().GoToUrl("https://www.google.com");
                driver.FindElement(By.CssSelector(["[name='q']"]).SendKeys("webElemen"));
                // Get attribute of current active element
                string attr = driver.SwitchTo().ActiveElement().GetAttribute("title");
                System.Console.WriteLine(attr);
            } finally{
                driver.Quit();
            }
        }
    }
}
```

### [Interactions](https://www.selenium.dev/documentation/webdriver/elements/interactions/)

> A high-level instruction set for manipulating form controls.

There are only 5 basic commands that can be executed on an element:

* [click](https://w3c.github.io/webdriver/#element-click) (applies to any element)
* [send keys](https://w3c.github.io/webdriver/#element-send-keys) (only applies to text fields and content editable elements)
* [clear](https://w3c.github.io/webdriver/#element-send-keys) (only applies to text fields and content editable elements)
* submit (only applies to form elements)
* select (see [Select List Elements](https://www.selenium.dev/documentation/webdriver/elements/select_lists/))

#### Additional validations

These methods are designed to closely emulate a user's experience, so, unlike the [Actions API](https://www.selenium.dev/documentation/webdriver/actions_api/), it attempts to perform two things before attempting the specified action.

1. If it determines the element is outside the viewport, it scrolls the element into view, specifically it will align the bottom of the element with the bottom of the viewport.
2. It ensures the element is [interactable](https://w3c.github.io/webdriver/#interactability) before taking the action. This could mean that the scrolling was unsuccessful, or that the element is not otherwise displayed. Determining if an element is displayed on a page was too difficult to [define directly in the webdriver specification](https://w3c.github.io/webdriver/#element-displayedness), so Selenium sends an execute command with a JavaScript atom that checks for things that would keep the element from being displayed. If it determines an element is not in the viewport, not displayed, not [keyboard-interactable](https://w3c.github.io/webdriver/#dfn-keyboard-interactable), or not [pointer-interactable](https://w3c.github.io/webdriver/#dfn-pointer-interactable), it returns an [element not interactable](https://w3c.github.io/webdriver/#dfn-element-not-interactable) error.

#### Click

The [element click command](https://w3c.github.io/webdriver/#dfn-element-click) is executed on the [center of the element](https://w3c.github.io/webdriver/#dfn-center-point). If the center of the element is [obscured](https://w3c.github.io/webdriver/#dfn-obscuring)[^6] for some reason, Selenium will return an [element click intercepted](https://w3c.github.io/webdriver/#dfn-element-click-intercepted) error.

#### Send keys

The [element send keys command](https://w3c.github.io/webdriver/#dfn-element-send-keys) types the provided keys into an [editable](https://w3c.github.io/webdriver/#dfn-editable) element. Typically, this means an element is an input element of a form with a `text` type or an element with a `content-editable` attribute. If it is not editable, an [invalid element state](https://w3c.github.io/webdriver/#dfn-invalid-element-state) error is returned.

[Here](https://www.w3.org/TR/webdriver/#keyboard-actions) is the list of possible keystrokes[^7] that WebDriver supports.

**<u>Python</u>**

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
# Navigate to url
driver.get("http://www.google.com")
# Enter "webdriver" text and perform "ENTER" keyboard action
driver.find_element(By.NAME, "q").send_keys("webdriver" + Keys.ENTER)
```

**<u>CSharp</u>**

```c#
using (var driver = new FirefoxDriver())
{
    // Navigate to Url
    driver.Navigate().GoToUrl("https://google.com");
    // Enter "webdriver" text and perform "ENTER" keyboard action
    driver.FindElement(By.Name("q")).SendKeys("webdriver" + Keys.Enter);
}
```

#### Clear

The [element clear command](https://w3c.github.io/webdriver/#dfn-element-clear) resets the content of an element. This requires an element to be [editable](https://w3c.github.io/webdriver/#dfn-editable), and [resettable](https://w3c.github.io/webdriver/#dfn-resettable-elements). Typically, this means an element is an input element of a form with a `text` type or an element with a `content-editable` attribute. If these conditions are not met, an [invalid element state](https://w3c.github.io/webdriver/#dfn-invalid-element-state) error is returned.

**<u>Python</u>**

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome();

# Navigate to url
driver.get("http://www.google.com")
# Store 'SearchInput' element
SearchInput = driver.find_element(By.NAME, "q")
SearchInput.send_keys("selenium")
# Clears the entered text
SearchInput.clear()
```

**<u>CSharp</u>**

```c#
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using System;

namespace SnippetProjectDelete{
    class Program{
        static void Main(String[] args){
            IWebDriver driver = new ChromeDirver();
            try{
                // Navigate to Url
                driver.Navigate().GoToUrl("https://www.google.com");
                // Store 'SearchInput' element
                IWebElement searchInput = driver.FindElement(By.Name('q'));
                searchInput.SendKeys("selenium");
                // Clears the entered text
                searchInput.Clear();
            } finally{
                driver.Quit();
            }
        }
    }
} 
```

#### Submit

In Selenium 4 this is no longer implemented with a separate endpoint and functions by executing a script. As such[^8], it is recommended not to use this method and to click the applicable form submission button instead.

### [Information](https://www.selenium.dev/documentation/webdriver/elements/information/)

> What you can learn about an element.

There are a number of details you can query about a specific element.

#### Is Displayed

This method is used to check if the connected element is displayed on a webpage. Returns a `Boolean` value, true if the connected element is displayed in the current browsing context else returns false.

This functionality is [mentioned in](https://w3c.github.io/webdriver/#element-displayedness), but not defined by the w3c specification due to the [impossibility of covering all potential conditions](https://www.youtube.com/watch?v=hTa1KI6fQpg). As such, Selenium cannot expect drivers to implement this functionality directly, and now relies on executing a large JavaScript function directly. This function makes many approximations about an element's nature and relationship in the tree to return a value.

**<u>Python</u>**

```python
# Navigate to the url
driver.get("https://www.google.com")

# Get boolean value for is element display
is_button_visible = driver.find_element(By.CSS_SELECTOR, "[name='login']").is_displayed()
```

**<u>CSharp</u>**

```c#
// no sample atm
```

#### Is Enabled

This method is used to check if the connected element is enabled or disabled on a webpage. Returns a boolean value, true if the connected element is enabled in the current browsing context else returns false.

**<u>Python</u>**

```python
# Navigate to url
driver.get("http://www.google.com")

# Returns true if element is enabled else returns false
value = driver.find_element(By.NAME, 'btnK').is_enabled()
```

**<u>CSharp</u>**

```c#
// Navigate to Url
driver.Navigate().GoToUrl("https://google.com");

// Store the WebElement
IWebElement element = driver.FindElement(By.Name("btnK"));

// Prints true if element is enabled else returns false
System.Console.WriteLine(element.Enabled);
```

#### Is Selected

This method determines if the referenced element is selected or not. This method is widely used on checkbox, radio buttons, input elements, and option elements.

Returns a boolean value, true if referenced element is selected in the current browsing context else returns false.

**<u>Python</u>**

```python
# Navigate to url
driver.get("https://the-internet.herokuapp.com/checkboxes")

# Returns true if element is checked else returns false
value = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']:first-of-type").is_selected()
```

**<u>CSharp</u>**

```c#
// Navigate to Url
driver.Navigate().GoToUrl("https://the-internet.herokuapp.com/checkboxes");
// Returns true if element is checked else returns false
bool value = driver.FindElement(By.CssSelector("input[type='checkbox']:last-fo-type")).Selected;
```

#### Tag Name

It is used to fetch the [TagName](https://www.w3.org/TR/webdriver/#dfn-get-element-tag-name) of the referenced element which has the focus in the current browsing context.

**<u>Python</u>**

```python
# Navigate to url
driver.get("https://www.example.com")

# Returns TagName of the element
attr = driver.find_element(By.CSS_SELECTOR, "h1").tag_name
```

**<u>CSharp</u>**

```c#
// Navigate to Url
driver.Navigate().GoToUrl("https://www.example.com");

// Returns TagName of the element
string attr = driver.FindElement(By.CssSelector("h1")).TagName;
```

#### Size and Position

It is used to fetch the dimensions and coordinates of the referenced element.

The fetched data body contain the following details:

* X-axis position from the top-left corner of the element
* Y-axis position from the top-left corner of the element
* Height of the element
* Width of the element

**<u>Python</u>**

```python
# Navigate to url
driver.get("https://www.example.com")
# Returns height, width, x and y coordinates referenced element
res = driver.find_element(By.CSS_SELECTOR, "h1").rect
```

**<u>CSharp</u>**

```c#
// Navigate to Url
driver.Navigate().GoToUrl("https://example.com");

var res = driver.FindElement(By.CssSelector("h1"));
// Return x and y coordinates referenced element
System.Console.WriteLine(res.Location);
// Returns height, width
System.Console.WriteLine(res.Size);
```

#### Get CSS Value

Retrieves the value of specified computed style property of an element in the current browsing context.

**<u>Python</u>**

```python
# Navigate to Url
driver.get("https://www.example.com")

# Retrieves the computed style property 'color' of linktext
cssValue = driver.find_element(By.LINK_TEXT, "More information...").value_of_css_property('color')
```

**<u>CSharp</u>**

```c#
// Navigate to url
driver.Navigate().GoToUrl("https://www.example.com");

// Retrieves the computed style property 'color' of linktext
String cssValue = driver.FindElement(By.LinkText("More information...")).GetCssValue("color");
```

#### Text Content

Retrieves the rendered text of the specified element.

**<u>Python</u>**

```python
# Navigate to url
driver.get("https://www.example.com")

# Retrieves the text of the element
text = driver.find_element(By.CSS_SELECTOR, "h1").text
```

**<u>CSharp</u>**

```c#
// Navigate to url
driver.Navigate().GoToUrl("https://www.example.com");

// Retrieves the text of the element
String text = driver.FindElement(By.CssSelector("h1")).Text;
```

#### Attributes and Properties

Attribute

DOM Attribute

DOM Property

### [Select Lists](https://www.selenium.dev/documentation/webdriver/elements/select_lists/)

> Select lists have special behaviors compared to other elements.

Select elements can require quite a bit of boilerplate[^9] code to automate. To reduce this, and make your tests cleaner, there is a `Select` class in the Selenium support package. To use it, you will need the following import statement:

**<u>Python</u>**

```python
from selenium.webdriver.support.select import Select
```

**<u>CSharp</u>**

```c#
using OpenQA.Selenium.Support.UI
```

You are then able to create a Select object using a WebElement that references a `<select>` element.

**<u>Python</u>**

```python
select_element = driver.find_element(By.ID, 'selectElementID')
select_object = Select(select_element)
```

**<u>CSharp</u>**

```c#
IWebElement selectElement = driver.FindElement(By.Id("selectElementID"));
var selectObject = new SelectElement(selectElement);
```

The Select object will now give you a series of commands that allow you to interact with a `<select>` element. First of all, there are different ways of selecting an option from the `<select>`element.

```html
<select>
    <option value=value1>Bread</option>
    <option value=value2 selected>Milk</option>
    <option value=value3>Cheese</option>
</select>
```

There are three ways to select the first option from the above element:

**<u>Python</u>**

```python
# Select an <option> based upon the <select> element's internal index
select_object.select_by_index(1)

# Select an <option> based upon its value attribute
select_object.select_by_value('value1')

# Select an <option> based upon its text
select_object.select_by_visible_text('Bread')
```

**<u>CSharp</u>**

```c#
// Select an <option> based upon the <select> element's internal index
selectObject.SelectByIndex(1);

// Select an <option> based upon its value attribute
selectObject.SelectByValue("value1");

// Select an <option> based upon its text
selectObject.SelectByText("Bread");
```

You can then check with options are selected by using:

**<u>Python</u>**

```python
# Return a list[WebElement] of options that have been selected
all_selected_options = select_object.all_selected_options

# Return a WebElement referencing the first selection option found by walking down the DOM
first_selected_option = select_object.first_selected_option
```

**<u>CSharp</u>**

```c#
// Return a List<WebElement> of options that have been selected
var allSelectedOptions = selectObject.AllSelectedOptions;

// Return a WebElement referencing the first selection option found by walking down the DOM
var firstSelectedOption = selectObject.AllSelectedOptions.FirstOrDefault();
```

Or you may just be interested in what `<option>` elements the `<select>` element contains:

**<u>Python</u>**

```python
# Return a list[WebElement] of options that the <select> element contains
all_available_options = select_object.options
```

**<u>CSharp</u>**

```c#
// Return a IList<IWebElement> of options that the <select> element contains
IList<IWebElement> allAvailableOptions = selectObject.Options;
```

If you want to deselect any elements, you now have four options:

**<u>Python</u>**

```python
# Deselect an <option> based upon the <select> element's internal index
select_object.deselect_by_index(1)

# Deselect an <option> based upon its value attribute
select_object.desclect_by_value('value1')

# Deselect an <option> based upon its text
select_object.deselect_by_visible_text('Bread')

# Deselect all selected <option> elements
select_object.deselect-all()
```

**<u>CSharp</u>**

```c#
// Deselect an <option> based upon the <select> element's internal index
selectObject.DeselectByIndex(1);

// Deselect an <option> based upon its value attribute
selectObject.DeselectByValue("value1");

// Deselect an <option> based upon its text
selectObject.DeselectByText("Bread");

// Deselect all selected <option> elements
selectObject.DeselectAll();
```

Finally, some `<select>` elements allow you to select more than one option. You can find out if your `<select>` element is one of these by using:

**<u>Python</u>**

```python
does_this_allow_multiple_selections = select_object.is_multiple
```

**<u>CSharp</u>**

```c#
bool doesThisAllowMultipleSelections = selectObject.IsMultiple;
```

## [2-5 Remote WebDriver](https://www.selenium.dev/documentation/webdriver/remote_webdriver/)

You can use WebDriver remotely the same way you would use it locally. The primary difference is that a remote WebDriver needs to be configured so that it can run your tests on a separate machine.

==A remote WebDriver is composed of two pieces: a client and a server.== <u>The client is your WebDriver test and the server is simply a Java servlet, which can be hosted in any modern JEE app server.</u>

To run a remote WebDriver client, we first need to connect to the RemoteWebDriver. We do this by **pointing the URL to the address of the server running our tests**. In order to customize our configuration, we set desired capabilities. Below is an example of instantiating a remote WebDriver object pointing to our remote web server, www.example.com, running our tests on Firefox.

**<u>Python</u>**

```python
from selenium import webdriver

firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Remote(
	command_executor='http://www.example.com',
	options=firefox_options)
driver.get("http://www.google.com")
driver.quit()
```

**<u>CSharp</u>**

```c#
FireFoxOptions firefoxOptions = new FirefoxOptions();
IWebDriver driver = new RemoteWebDriver(new Uri("http://www.example.com"), firefoxOptions);
driver.Navigate().GoToUrl("http://www.google.com");
driver.Quit();
```

To further customize our test configuration, we can add other desired capabilities.

### Browser options

For example, suppose you wanted to run Chrome on Windows XP, using Chrome version 67:

**<u>Python</u>**

```python
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.set_capability("browserVersion", "67")
chrome_options.set_capability("platformName", "Windows XP")
driver = webdriver.Remote(
	command_executor='http://www.example.com',
	options=chrome_options
)
driver.get("http://www.google.com")
driver.quit()
```

**<u>CSharp</u>**

```c#
var chromeOptions = new ChromeOptions();
chromeOptions.BrowserVersion = "67";
chromeOptions.PlatformName = "Windows XP";
IWebDriver driver = new RemoteWebDriver(new Uri("http://www.example.com"), chromeOptions);
driver.Navigate().GoToUrl("http://www.google.com");
driver.Quit();
```

### Local file detector

The local file detector allows the transfer of files from the client machine to the remote server. For example, if a test needs to upload a file to a web application, a remote WebDriver can automatically transfer the file from the local machine to the remote web server during runtime. This allows the file to be uploaded from the remote machine running the test. It is not enabled by default and can be enabled in the following way:

**<u>Python</u>**

```python
from selenium.webdriver.remote.file_detector import LocalFileDetector

driver.file_detector = LocalFileDetector()
```

**<u>CSharp</u>**

```c#
var allowDetection = this.driver as IAllowsFileDetection;
if (allowsDetection != null){
    allowsDetection.FileDetector = new LocalFileDetector();
}
```

Once the above code is defined, you can upload a file in your test in the following way:

**<u>Python</u>**

```python
driver.get("http://sso.dev.saucelabs.com/test/guinea-file-upload")

driver.find_element(By.ID, "myfile").send_keys("/Users/sso/the/local/path/to/darkbulb.jpg")
```

**<u>CSharp</u>**

```c#
driver.Navigate().GoToUrl("http://sso.dev.saucelabs.com/test/guinea-file-upload");
IWebElement upload = driver.FindElement(By.Id("myfile"));
upload.SendKeys(@"/Users/sso/the/local/path/to/darkbulb.jpg");
```

### Tracing client requests

This feature is only available for Java client binding (Beta onwards). The Remote WebDriver client sends requests to the Selenium Grid server, which passes them to the WebDriver. Tracing should be enabled at the server and client-side to trace the HTTP requests end-to-end. Both ends should have a trace exporter setup pointing to the visualization framework. By default, tracing is enabled for both client and server. To set up the visualization framework Jaeger[^2-5-1] UI and Selenium Grid 4, please refer to [Tracing Setup](https://github.com/SeleniumHQ/selenium/blob/selenium-4.0.0-beta-1/java/server/src/org/openqa/selenium/grid/commands/tracing.txt) for the desired version.

for client-side setup, follow the steps below.

#### Add the required dependencies

Installation of external libraries for tracing exporter can be done using Maven. Add the `opentelemetry-exporter-jaeger` and `grpc-netty` dependency in your project `pom.xml`:

```xml
<dependency>
	<groupId>io.opentelemetry</groupId>
    <artifactId>opentelemetry-exporter-jaeger</artifactId>
    <version>1.0.0</version>
</dependency>
<dependency>
	<groupId>io.grpc</groupId>
    <artifactId>grpc-netty</artifactId>
    <verion>1.35.0</verion>
</dependency>
```

#### Add/pass the required system properties while running the client

```java
System.setProperty("otel.traces.exporter", "jaeger");
System.setProperty("otel.exporter.jaeger.endpoint", "http://localhost:14250");
System.setProperty("otel.resource.attributes", "service.name=selenium-java-client");

ImmutableCapabilities capabilities = new ImmutableCapabilities("browserName", "chrome");

WebDriver driver = new RemoteWebDriver(new URL("http://www.example.com"), capabilities);
driver.get("http://www.google.com");
driver.quit();
```

Please refer to [Tracing Setup](https://github.com/SeleniumHQ/selenium/blob/selenium-4.0.0-beta-1/java/server/src/org/openqa/selenium/grid/commands/tracing.txt) for more information on external dependencies versions required for the desired Selenium version.

More information can be found at:

* OpenTelemetry: [https://opentelemetry.io](https://opentelemetry.io/)
* Configuring OpenTelemetry: https://github.com/open-telemetry/opentelemetry-java/tree/main/sdk-extensions/autoconfigure
* Jaeger: [https://www.jaegertracing.io](https://www.jaegertracing.io/)
* [Selenium Grid Observability](https://www.selenium.dev/documentation/grid/advanced_features/observability/)

## [2-6 Drivers](https://www.selenium.dev/documentation/webdriver/drivers/)

We learned how to [install drivers](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/) in the Getting Started section.

Selenium provides access to Service classes which are used to determine how the server is started.

## [2-7 Waits](https://www.selenium.dev/documentation/webdriver/waits/)

WebDriver can generally be said to have a blocking API. Because it is an out-of-process library that instructs browser what to do, and because the web platform has an intrinsically asynchronous nature, WebDriver does not track the active, real-time state of the DOM. This comes with some challenges that we will discuss here.

From experience, most intermittent[^2-7-1] issues that arise from use of Selenium and WebDriver are connected to <u>race conditions</u> that occur between the browser and the user's instructions. An example could be that the user instructs the browser to navigate to a page, then gets a <u>no such element</u> error when trying to find an element.

Consider the following document:

```html
<!doctype html>
<meta charset=utf-8>
<title>Race Condition Example</title>

<script>
	var initialised false;
    window.addEventListener("load", function(){
        var newElement = document.createElement("p");
        newElement.textContent = "Hello from JavaScript!";
        document.body.appendChild(newElement);
        initialised = true;
    });
</script>
```

The WebDriver instructions might look innocent enough:

**<u>Python</u>**

```python
driver.navigate("file://race_condition.html")
el = driver.find_element(By.TAG_NAME, "p")
assert el.text == "Hello from JavaScript!"
```

**<u>CSharp</u>**

```c#
driver.Navigate().GoToUrl("file://race_condition.html");
IWebElement element = driver.FindElement(By.TagName("p"));
assertEquals(element.Text, "Hello from JavaScript!");
```

The issue here is that the default [page load strategy](https://www.selenium.dev/documentation/webdriver/capabilities/shared/#pageloadstrategy) used in WebDriver listens for the `document.readyState` to change to "`complete`" before returning from the call to `navigate`. Because the `p` element is added after the document has completed loading, this WebDriver script might be intermittent. It "might" be intermittent because no guarantees can be made about elements or events that trigger asynchronously without explicitly waiting -- or blocking -- on those events.

Fortunately, the normal instruction set available on the [WebElement](https://www.selenium.dev/documentation/webdriver/elements/) interface -- such as `WebElement.click` and `WebElement.sendKeys` -- are guaranteed to be synchronous, in that the function calls will not return (or the callback will not trigger in callback-style languages) until the command has been completed in the browser. The advanced user interaction APIs, Keyboard and Mouse, are exceptions as they are explicitly intended as "do what I say" asynchronous commands.

Waiting is having the automated task execution elapse a certain amount of time before continuing with the next step.

To overcome the problem of race conditions between the browser and your WebDriver script, most Selenium clients ship with a wait package. When employing a wait, you are using what is commonly referred to as an <u>explicit wait</u>.

### Explicit wait

Explicit waits are available to Selenium clients for imperative[^2-7-2], procedural languages. They allow your code to halt program execution, or freeze the thread, until the condition you pass it resolves. The condition is called with a certain frequency until the timeout of the wait is elapsed. This means that for as long as the condition returns a falsy value, it will keep trying and waiting.

Since explicit waits allow you to wait for a condition to occur, they make a good fit for synchronizing the state between the browser and its DOM, and your WebDriver script.

To remedy[^2-7-3] our buggy instruction set from earlier, we could employ[^2-7-4] a wait to have the `findElement` call wait until the dynamically added element from the script has been added to the DOM:

**<u>Python</u>**

```python
from selenium.webdriver.support.ui import WebDriverWait

def document_initialized(driver):
    return driver.execute_script("return initialized")

driver.navigate("file://race_condition.html")
WebDriverWait(driver, timeout=10).until(document_initialized)
el = driver.find_element(By.TAG_NAME, "p")
assert el.text == "Hello from JavaScript!"
```

**<u>CSharp</u>**

```c#
driver = new ChromeDriver();
driver.Url = "https://www.google.com/ncr";
driver.FindElement(By.Name("q")).SendKeys("cheese" + Keys.Enter);

WebDriverWait wait = new WebDriverWait(driver, TimeSpan.FromSeconds(10));
IWebElement firstResult = wait.Until(e => e.FindElement(By.XPath("//a/h3")));

Console.WriteLine(firstResult.Text);
```

We pass in the condition as a function reference that the wait will return repeatedly until its return value is truthy. A "truthful" return value is anything that evaluates to boolean true in the language at hand, such as a string, number, a boolean, an object(including a WebElement), or a populated(non-empty) sequence or list. That means an empty list evaluates to false. When the condition is truthful and the blocking wait is aborted, the return value from the condition becomes the return value of the wait.

With this knowledge, and because the wait utility ignores <u>no such element</u> errors by default, we can refactor our instructions to be more concise:

**<u>Python</u>**

```python
from selenium.webdriver.support.ui import WebDriverWait

driver.navigate("file://race_condition.html")
el = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element_by_tag_name("p"))
assert el.text == "Hello from JavaScript!"
```

**<u>CSharp</u>**

```c#
using (var driver = new FirefoxDriver()){
    var foo = new WebDriverWait(driver, TimeSpan.FromSeconds(3)).until(drv => drv.FindElement(By.Name("q")));
    Debug.Assert(foo.Text.Equals("Hello from JavaScript!"));
}
```

In that example, we pass in an anonymous function(but we could also define it explicitly as we did earlier so it may be reused). The first and only argument that is passed to our condition is always a reference to our driver object, WebDriver. In a multi-threaded environment, you should be careful to operate on the driver reference passed in to the condition rather than the reference to the driver in the outer scope.

Because the wait will swallow <u>no such element</u> errors that are raised when the element is not found, the condition will retry until the element is found. Then it will take the return value, a WebElement, and pass it back through to our script.

If the condition fails, e.g. a truthful return value from the condition is never reached, the wait will throw/raise an error/exception called a <u>timeout error</u>.

#### Options

The wait condition can be customized to match your needs. Sometimes it is unnecessary to wait the full extent of the default timeout, as the penalty[^2-7-5] for not hitting a successful condition can be expensive.

The wait lets you pass in an argument to override the timeout:

**<u>Python</u>**

```python
WebDriverWait(driver, timeout=3).until(some_condition)
```

**<u>CSharp</u>**

```c#
new WebDriverWait(driver, TimeSpan.FromSeconds(3)).Until(ExpectedConditions.ElementToBeClickable(By.XPath("//a/h3")));
```

#### Expected conditions

Because it is quite a common occurrence to have to synchronize the DOM and your instructions, most clients also come with a set of predefined <u>expected conditions</u>. As might be obvious by the name, they are conditions that are predefined for frequent wait operations.

The conditions available in the different language bindings vary, but this is a non-exhaustive[^2-7-6] list of a few:

* alert is present
* element exists
* element is visible
* title contains
* title is
* element staleness
* visible text

You can refer to the API documentation for each client binding to find an exhaustive list of expected conditions.

* Java's [org.openqa.selenium.support.ui.ExpectedConditions](https://seleniumhq.github.io/selenium/docs/api/java/org/openqa/selenium/support/ui/ExpectedConditions.html) class
* Python's [selenium.webdriver.support.expected_conditions](https://seleniumhq.github.io/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html?highlight=expected) class
* .NET's [OpenQA.Selenium.Support.UI.ExpectedConditions](https://seleniumhq.github.io/selenium/docs/api/dotnet/html/T_OpenQA_Selenium_Support_UI_ExpectedConditions.htm) type
* JavaScript's [selenium-webdriver/lib/until](https://seleniumhq.github.io/selenium/docs/api/javascript/module/selenium-webdriver/lib/until.html) module

### Implicit wait

There is a second type of wait that is distinct from explicit wait called <u>implicit wait</u>. By implicitly waiting, WebDriver polls the DOM for a certain duration when trying to find any element. This can be useful when certain elements on the webpage are not available immediately and need some time to load.

Implicit waiting for elements to appear is disabled by default and will need to be manually enabled on a per-session basis. ==Mixing explicit waits and implicit waits will cause unintended consequences, namely waits sleeping for the maximum time even if the element is available or condition is true.==

Warning: Do not mix implicit and explicit waits. Doing so can cause unpredictable wait times. For example, setting an implicit wait of 10 seconds and an explicit wait for 15 seconds could cause a timeout to occur after 20 seconds.

An implicit wait is to tell WebDriver to poll the DOM for a certain amount of time when trying to find an element or elements if they are not immediately available. The default setting is 0, meaning disabled. Once set, the implicit wait is set for the life of the session.

**<u>Python</u>**

```python
driver = Firefox()
driver.implicitly_wait(10)
driver.get("http://somedomain/url_that_delays_loading")
my_dynamic_element = driver.find_element(By.ID, "myDynamicElement")
```

**<u>CSharp</u>**

```c#
IWebDriver driver = new ChromeDriver();
driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(10);
driver.Url = "http://somedomain/url_that_delays_loading";
IWebElement dynamicElement = driver.FindElement(By.Name("dynamicElement"));
```

### FluentWait

FluentWait instance defines the maximum amount of time to wait for a condition, as well as the frequency with which to check the condition.

Users may configure the wait to ignore specific types of exceptions whilst[^2-7-7] waiting, such as `NoSuchElementException` when searching for an element on the page.

**<u>Python</u>**

```python
driver = Firefox()
driver.get("http://somedomain/url_that_delays_loading")
wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div")))
```

**<u>CSharp</u>**

```c#
using (var driver = new FirefoxDriver()){
    WebDriverWait wait = new WebDriverWait(driver, timeout: TimeSpan.FromSeconds(30)){
        PollingInterval = TimeSpan.FromSeconds(5)
    };
    wait.IgnoreExceptionTypes(typeof(NoSuchElementException));
    var foo = wait.Until(drv => drv.FindElement(By.Id("foo")));
}
```

## [2-8 Actions API](https://www.selenium.dev/documentation/webdriver/actions_api/)

A low-level interface for providing virtualized device input to the web browser.

Unlike the high-level element interactions, which conducts additional validations, the Actions API provides granular[^18] control over input devices.

Selenium provides access to 3 input sources: key inputs for keyboard devices, pointer inputs for a mouse, pen or touch device, and a wheel inputs for scroll wheel support.

### [Keyboard](https://www.selenium.dev/documentation/webdriver/actions_api/keyboard/)

> A representation of any key input device for interacting with a web page.

Keyboard represents a KeyBoard event. KeyBoard actions are performed by using low-level interface which allows us to provide virtualized device input to the web browser.

#### Keys

In addition to the keys represented by regular unicode, unicode values have been assigned to other keyboard keys for use with Selenium. Each language has its own way to reference these keys; the full list can be found [here](https://www.w3.org/TR/webdriver/#keyboard-actions).

#### Key down

The KeyDown is used to simulate action of depressing a key

**<u>Python</u>**

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# Navigate to url
driver.get("http://www.google.com")

# Enter "webdriver" text and perform "ENTER" keyboard action
driver.find_element(By.NAME, "q").send_keys("webdriver" + Keys.ENTER)

# Perform action ctrl + A to select the page
webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()
```

**<u>CSharp</u>**

```c#
IWebDriver driver = new ChromeDriver();
try
{
    // Navigate to Url
    driver.Navigate().GoToUrl("https://google.com");
    
    // Enter "webdriver" text and perform "ENTER" keyboard action
    driver.FindElement(By.Name("q")).SendKeys("webdriver" + Keys.Enter);
    
    // Perform action ctrl + A(modifer CONTROL + Alphabe A) to select the page
    Actions actionProvider = new Actions(driver);
    IAction keydown = actionProvider.KeyDown(Keys.Control).SendKeys("a").Build();
    keydown.Perform();
}
finally
{
    driver.Quit();
}
```

#### Key up

The KeyUp is used to simulate key-up (or) key-release action.

**<u>Python</u>**

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# Navigate to url
driver.get("http://www.google.com")

# Store google search box WebElement
search = driver.find_element(By.NAME, "q")
action = webdriver.ActionChains(driver)

# Enter text "qwerty" with keyDown SHIFT key and after keyUp SHIFT key(QWERTYqwerty)
actions.key_down(Keys.SHIFT).send_keys_to_element(search, "qwerty").key_up(Keys.SHIFT).send_keys("qwerty").perform()
```

**<u>CSharp</u>**

```c#
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Interactions;

namespace HelloSelenium
{
    class HelloSelenium
    {
        public static void Main(string[] args)
        {
            IWebDriver driver = new ChromeDriver();
            try
            {
                // Navigate to Url
                driver.Navigate().GoToUrl("https://google.com");
                Actions action = new Actions(driver);
                
                // Store google search box WebElement
                IWebElement search = driver.FindElement(By.Name("q"));
                
                // Enters text "qwerty" with KeyDown SHIFT key and after keyUp SHIFT key(QWERTYqwerty)
                action.KeyDown(Keys.Shift).SendKeys(search, "qwerty").KeyUp(Keys.Shift).SendKeys("qwerty").Perform();
            }
            finally
            {
                driver.Quit();
            }
        }
    }
}
```

#### Send keys

This is a convenience method in the Actions API that combines keyDown and keyUp commands in one action. Executing this command differs slightly from using the element method.

**<u>Python</u>**

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.selenium.dev/selenium/docs/api/py/genindex.html")

search = driver.find_element(By.NAME, "q")

action = webdriver.ActionChains(driver)
action.move_to_element(search).click().send_keys("send_keys", Keys.ENTER).perform()
```

**<u>CSharp</u>**

```c#
# Help us with a PR for code sample
```

### [Mouse](https://www.selenium.dev/documentation/webdriver/actions_api/mouse/)

> A representation of any pointer device for interacting with a web page.

#### Click and hold

It will move to the element and clicks (without releasing) in the middle of the given element.

**<u>Python</u>**

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# Navigate to url
driver.get("http://www.google.com")
# Store 'google search' button web element
searchBtn = driver.find_element(By.LINK_TEXT, "Sign in")
# Perform click-and-hold action on the element
webdriver.ActionChains(driver).click_and_hold(searchBtn).perform()
```

**<u>CSharp</u>**

```c#
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Interactions;

namespace SeleniumApp
{
    public class ClickAndHold
    {
        public static void Main(string[] args)
        {
            IWebDriver driver = new ChromeDriver();
        	try
            {
                // Navigate to Url
                driver.Navigate().GoToUrl("https://google.com");
                // Store 'google search' button web element
                IWebElement searchBtn = driver.FindElement(By.LinkText("Sign in"));
                Actions actionProvider = new Actions(driver);
                // Perform click-and-hold action on the elment
                actionProvider.ChickAndHold(searchBtn).Build().Perform();
            }
            finally
            {
                driver.Quit();
            }    
        }
    }
}
```

#### Context click

This method firstly performs a mouse-move to the location of the element and performs the context-click (right click) on the given element.

**<u>Python</u>**

```python
from selenium import webdriver

driver = webdriver.Chrome()

# Navigate to url
driver.get("http://www.google.com")
# Store 'google search' button web element
searchBtn = driver.find_element(By.LINK_TEXT, "Sign in")
# Perform context-click action on the element
webdriver.ActionChains(driver).context_click(searchBtn).perform()
```

**<u>CSharp</u>**

```c#
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Interactions;

namespace SeleniumApp
{
    public class ContextClick
    {
        public static void Main(string[] args)
        {
            IWebDriver driver = new ChromeDriver();
            try
            {
                // Navigate to Url
                driver.Navigate().GoToUrl("https://google.com");
                // Store 'google search' button web element
                IWebElement searchBtn = driver.FindElement(By.LinkText("Sign in"));
                Actions actionProvider = new Actions(driver);
                // Perform context-click action on the element
                actionProvider.ContextClick(searchBtn).Build().Perform();
            }
            finally
            {
                driver.Quit();
            }
        }
    }
}
```

#### Double click

It will move to the element and performs a double-click in the middle of the given element.

**<u>Python</u>**

```python
from selenium import webdriver

driver = webdriver.Chrome()

# Navigate to url
driver.get("https://www.google.com")
# Store 'google search' button web element
searchBtn = driver.find_element(By.LINK_TEXT, "Sign in")
# Perform double-click action on the element
webdriver.ActionChains(driver).double_click(searchBtn).perform()
```

**<u>CSharp</u>**

```c#
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Interactions;

namespace SeleniumApp
{
    public class DoubleClick
    {
        public static void Main(string[] args)
        {
            IWebDriver driver = new ChromeDriver();
            try
            {
                // Navigate to url
                driver.Navigate().GoToUrl("https://google.com");
                // Store 'google search' button web element
                IWebElement searchBtn = driver.FindElement(By.LinkText("Sign in"));
                Actions actionProvider = new Actions(driver);
                // Perform double-click action on the element
                actionProvider.DoubleClick(searchBtn).Build().Perform();
            }
            finally
            {
                driver.Quit();
            }
        }
    }
}
```

#### Move to element

This method moves the mouse to the middle of the element. ==The element is also scrolled into the view on performing this action.==

**<u>Python</u>**

```python
from selenium import webdriver

driver = webdriver.Chrome()
# Navigate to url
driver.get("http://www.google.com")
# Store 'google search' button web element
gmailLink = driver.find_element(By.LINK_TEXT, "Gmail")
# Performs mouse move action onto the element
webdriver.ActionChains(driver).move_to_element(gmailLink).perform()
```

**<u>CSharp</u>**

```c#
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Interactions;

namespace SeleniumApp
{
    public class MoveToElement
    {
        public static void Main(string[] args)
        {
            IWebDriver driver = new ChromeDriver();
            try
            {
                // Navigate to Url
                driver.Navigate().GoToUrl("https://google.com");
                // Store 'google search' button web element
                IWebElement gmailLink = driver.FindElement(By.LinkText("Gmail"));
                Actions actionProvider = new Actions(driver);
                actionProvider.MoveToElement(gmailLink).Build().Perform();
            }
            finally
            {
                driver.Quit();
            }
        }
    }
}
```

#### Move by offset

This method moves the mouse from its current position(or 0, 0) by the given offset. ==If the coordinates are outside the view window, then the mouse will end up outside the browser window.==

**<u>Python</u>**

```python
from selenium import webdriver

driver = webdriver.Chrome()

# Navigate to url
driver.get("http://www.google.com")
# Store 'google search' button web element
gmailLink = driver.find_element(By.LINK_TEXT, "Gmail")
# Set x and y offset positions of element
xOffset = 100
yOffset = 100
# Performs mouse move action onto the element
webdriver.ActionChains(driver).move_by_offset(xOffset, yOffset).perform()
```

**<u>CSharp</u>**

```c#
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Interactions;

namespace SeleniumApp
{
    public class MoveByOffset
    {
        public static void Main(string[] args)
        {
            IWebDriver driver = new ChromeDriver();
            try
            {
                // Navigate to Url
                driver.Navigate().GoToUrl("https://google.com");
                // Store 'google search' button web element
                IWebElement gmailLink = driver.FindElement(By.LinkText("Gmail"));
                // Set x and y offset positions of element
                int xOffset = 100;
                int yOffset = 100;
                Actions actionProvider = new Actions(driver);
                // Perform mouse move action onto the offset position
                actionProvider.MoveByOffset(xOffset, yOffset).Build().Perform();
            }
            finally
            {
                driver.Quit();
            }
        }
    }
}
```

#### dragAndDrop

This method firstly performs a click-and-hold on the source element, moves to the location of the target element and then releases the mouse.

**<u>Python</u>**

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# Navigate to url
driver.get("https://corssbrowsertesting.github.io/drag-and-drop")
# Store 'box A' as a source element
sourceEle = driver.find_element(By.ID, "draggable")
# Store 'box B' as a target element
targetEle = driver.find_element(By.ID, "drappable")
# Performs drag and drop action of sourceEle onto the targetEle
webdriver.ActionChains(driver).drag_and_drop(sourceEle, targetEle).perform()
```

**<u>CSharp</u>**

```c#
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Interactions;

namespace SeleniumApp
{
    public class DragAndDrop
    {
        public static void Main(string[] args)
        {
            IWebDriver driver = new ChromeDriver();
            try
            {
                // Navigate to Url
                driver.Navigate().GoToUrl("https://crossbrowsertesting.github.io/drag-and-drop");
                // Store 'box A' as source element
                IWebElement sourceEle = driver.FindElement(By.Id("draggable"));
                // Store 'box B' as source element
                IWebElement targetEle = driver.FindElement(By.Id("drappable"));
                Actions actionProvider = new Actions(driver);
                // Performs drag and drop action of sourceEle onto the targetEle
                actionProvider.DragAndDrop(sourceEle, targetEle).Build().Perform();
            }
            finally
            {
                driver.Quit();
            }
        }
    }
}
```

#### dragAndDropBy

This method firstly performs a click-and-hold on the source element, moves to the given offset and then releases the mouse.

**<u>Python</u>**

```python
from selenium import webdriver

driver = webdriver.Chrome()

# Navigate to url
driver.get("https://crossbrowsertesting.github.io/drag-and-drop")
# Store 'box A' as source element
sourceEle = driver.find_element(By.ID, "draggable")
# Store 'box B' as target element
targetEle = driver.find_element(By.ID, "droppable")
targetEleXOffset = targetEle.location.get("x")
targetEleYOffset = targetEle.location.get("y")
# performs dragAndDropBy onto the target element offset position
webdriver.ActionChains(driver).drag_and_drop_by_offset(sourceEle, targetEleXOffset, targetEleYOffset).perform()
```

**<u>CSharp</u>**

```c#
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OPenQA.Selenium.Interactions;

namespace SeleniumApp
{
    public class DragAndDropToOffset
    {
        public static void Main(string[] args)
        {
            IWebDriver driver = new ChromeDriver();
            try
            {
                // Navigate to Url
                driver.Navigate().GoToUrl("https://crossbrowsertesting.github.io/drag-and-drop");
                // Store 'box A' as source element
                IWebElement sourceEle = driver.FindElement(By.Id("draggable"));
                // Store 'box B' as target element
                IWebElement targetEle = driver.FindElement(By.Id("droppable"));
                int targetEleXOffset = targetEle.Location.X;
                int targetEleYOffset = targetEle.Location.Y;
                Actions actionProvider = new Actions(driver);
                // Performs drag and drop action of sourceEle onto the targetEle
                actionProvider.DragAndDropToOffset(sourceEle, targetEleXOffset, targetEleYOffset).Build().Perform();
            }
            finally
            {
                driver.Quit();
            }
        }
    }
}
```

#### release

This action releases the depressed left mouse button. If WebElement is passed, it will release depressed left mouse button on the given WebElement.

**<u>Python</u>**

```python
from selenium import webdriver

driver = webdriver.Chrome()
# Navigate to url
driver.get("https://corssbrowsertesting.github.io/drag-and-drop")
# Store 'box A' as source element
sourceEle = driver.find_element(By.ID, "draggable")
# Store 'box B' as target element
targetEle = driver.find_element(By.ID, "droppable")
# Performs dragAndDropBy onto the target element offset position
webdriver.ActionChains(driver).click_and_hold(sourceEle).move_to_element(targetEle).perform()
# Performs release event
webdriver.ActionChains(driver).release().perform()
```

**<u>CSharp</u>**

```c#
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Interactions;

namespace SeleniumApp
{
    public class MoveByOffset
    {
        public static void Main(string[] args)
        {
            IWebDriver driver = new ChromeDriver();
            try
            {
                // Navigate to Url
                driver.Navigate().GoToUrl("https://google.com");
                // Store 'google search' button web element
                IWebElement gmailLink = driver.FindElement(By.LinkText("Gmail"));
                // Set x and y offset positions of element
                int xOffset = 100;
                int yOffset = 100;
                Actions actionProvider = new Actions(driver);
                // Performs mouse move action onto the offset position
                actionProvider.MoveByOffset(xOffset, yOffset).Build().Perform();
            }
            finally
            {
                driver.Quit();
            }
        }
    }
}
```

### [Wheel](https://www.selenium.dev/documentation/webdriver/actions_api/wheel/)

> A representation of a scroll wheel input device for interacting with a web page.

#### Scroll to element

Scrolls to the element by scroll the viewport[^19]. This way the element is at the bottom.

**<u>Python</u>**

```python
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://crossbrowsertesting.github.io/selenium_example_page.html")
element = driver.find_element(By.ID, "closepopup")

ActionChains(driver).scroll(0, 0, 0, 0, origin=element).perform()
driver.quit()
```

**<u>CSharp</u>**

```c#
// placeholder
```

#### Scroll by given amount from element

Scrolls to the element by scrolling the viewport. This way the element is at the bottom. Scrolls the viewport further by the given amount i.e. horizontal and vertical offsets.

**<u>Python</u>**

```python
from selenium import webdriver
form selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.set_window_size(500, 400)
driver.get("https://crossbrowsertesting.github.io/selenium_example_page.html")

element = driver.find_element(By.LINK_TEXT, "Go To Page 2")
ActionChains(driver).scroll(0, 0, 0, 300, origin=element).perform()
driver.quit()
```

**<u>CSharp</u>**

```c#
// placeholder
```

#### Scroll by given amount

Scrolls the viewport by the given amount i.e. horizontal and vertical offsets.

**<u>Python</u>**

```python
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.set_window_size(500, 400)
driver.get("https://crossbrowsertesting.github.io/selenium_example_page.html")

ActionChains(driver).scroll(0, 0, 0, 200).perform()
driver.quit()
```

**<u>CSharp</u>**

```c#
// placeholder
```

#### Scroll from an offset of origin (viewport) by given amount

The origin is the where the cursor is placed before the scroll is executed. For example, the position on the screen where the cursor is before scrolling a mouse wheel. For origin as viewport, the origin offset is calculated from the upper left corner of the viewport. Starting from this origin, the viewport is scrolled by the given amount i.e. horizontal and vertical offsets.

**<u>Python</u>**

```python
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.set_window_size(600, 600)
driver.get("https://crossbrowsertesting.github.io/selenium_example_page.html")

textarea = driver.find_element(By.NAME, "textarea")
textarea.send_keys("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" +
                   "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb" +
                   "cccccccccccccccccccccccccccccccc" +
                   "dddddddddddddddddddddddddddddddd" +
                   "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")

ActionChains(driver).scroll(20, 200, 0, -50).perform()
driver.quit()
```

**<u>CSharp</u>**

```c#
// placeholder
```

#### Scroll from an offset of origin (element) by given amount

The origin is the where the cursor is placed before the scroll is executed. For example, the position on the screen where the cursor is before scrolling a mouse wheel. For origin as element, the origin offset is calculated from the center of the element. Starting from this origin, the viewport is scrolled by the given amount i.e. horizontal and vertical offsets.

**<u>Python</u>**

```python
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://crossbrowsertesting.github.io/selenium_example_page.html")

textarea = driver.find_element(By.NAME, "textarea")
submit = driver.find_element(By.ID, "submitbtn")

textarea.send_keys("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" +
                   "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb" +
                   "cccccccccccccccccccccccccccccccc" +
                   "dddddddddddddddddddddddddddddddd" +
                   "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")

ActionChains(driver).scroll(0, -50, 0, -50, origin=submit).perform()
driver.quit()
```

**<u>CSharp</u>**

```c#
// placeholder
```

## [2-9 BiDirectional](https://www.selenium.dev/documentation/webdriver/bidirectional/)

Selenium is working with browser vendors to create the [WebDriver BiDirectional Protocol](https://w3c.github.io/webdriver-bidi/) as a means to provide a stable, cross-browser API that uses the bidirectional[^2-9-0-1] functionality useful for both browser automation generally and testing specifically. Before now, users seeking this functionality have had to rely on with all of its frustrations and limitations.

The traditional WebDriver model of strict request/response command will be supplemented[^2-9-0-2] with the  ability to stream events from the user agent to the controlling software via WebSockets, better matching the evented nature of the browser DOM.

Because it's a bad idea to tie your tests to a specific version of a specific browser, the Selenium project recommends using WebDriver BiDi wherever possible. However, until the spec is complete there are many useful things that the CDP[^2-9-0-3] offers. To help keep your tests independent and portable, Selenium offers some useful helper classes. At the moment, these use the CDP, but when we shall be using WebDriver BiDi as soon as possible.

### [2-9-1 BiDi API](https://www.selenium.dev/documentation/webdriver/bidirectional/bidi_api/)

The following list of APIs will be growing as the Selenium project works through supporting real world use cases. If there is additional functionality you'd like to see, please raise a [feature request](https://github.com/SeleniumHQ/selenium/issues/new?assignees=&labels=&template=feature.md).

#### Register Basic Auth

Some applications make use of browser authentication to secure pages. With Selenium, you can automate the input of basic auth credentials whenever they arise.

**<u>Python</u>**

```python
# placeholder
```

**<u>CSharp</u>**

```c#
NetworkAuthenticationHandler handler = new NetworkAuthenticationHandler()
{
    UriMatcher = (d) => d.Host.Contains("your-domain.com"),
    Credentials = new PasswordCredentials("admin", "password")
};

INetwork networkInterceptor = driver.Manage().Network;
networkInterceptor.AddAuthenticationHandler(handler);
await networkInterceptor.StartMonitoring();
```

#### Mutation Observation

Mutation observation is the ability to capture events via WebDriver BiDi when there are DOM mutations on a specific element in the DOM.

**<u>Python</u>**

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
async with driver.log.mutation_events() as event:
    pages.load("dynamic.html")
    driver.find_element(By.ID, "reveal").click()
    WebDriverWait(driver, 5)\
    	.until(EC.visibility_of(driver.find_element(By.ID, "revealed")))
        
assert event["attribute_name"] == "style"
assert event["current_value"] == ""
assert event["old_value"] == "display:none;"
```

**<u>CSharp</u>**

```c#
List<DomMutationData> attributeValueChanges = new List<DomMutationData>();
DefaultWait<List<DomMutationData>> wait = new DefaultWait<List<DomMutationData>>(attributeValueChanges);
wait.Timeout = TimeSpan.FromSeconds(3);

IJavaScriptEngine monitor = new JavaScriptEngine(driver);
monitor.DomMutated += (sender, e) =>
{
    attributeValueChanges.Add(e.AttributeData);
};
await monitor.StartEventMonitoring();

driver.Navigate().GoToUrl("http://www.google.com");
IWebElement span = driver.FindElement(By.CssSelector("span"));

await monitor.EnableDomMutationMonitoring();
((IJavaScriptExecutor) driver).ExecuteScript("arguments[0].setAttribute('cheese', 'gouda');", span);

wait.Unti((list) => list.Count > 0);
Console.WriteLine("Found {0} DOM mutation events", attributeValueChanges.Count);
foreach(var record in attributeValueChanges)
{
    Console.WriteLine("Attribute name: {0}", record.AttributeName);
    Console.WriteLine("Attribute value: {0}", record.AttributeValue);
}
await monitor.DisableDomMutationMonitoring();
```

#### Listen to `console.log` events

Listen to the `console.log` events and register callbacks to process the event.

**<u>Python</u>**

```python
async def printConsoleLogs():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome()
    driver.get("http://www.google.com")
    
    async with driver.bidi_connection() as session:
        log = Log(driver, session)
        from selenium.webdriver.common.bidi.console import Console
        async with log.add_listener(Console.ALL) as messages:
            driver.execute_script("console.log('I love cheese')")
        print(messages["message"])
        
    driver.quit()
```

**<u>CSharp</u>**

```c#
IJavaScriptEngine monitor = new JavaScriptEngine(driver);
List<string> consoleMessages = new List<string>();
monitor.JavaScriptConsoleApiCalled += (sender, e) =>
{
    Console.WriteLine("Log: {0}", e.MessageContent);
};
await monitor.StartEventMonitoring();
```

#### Listen to JS Exceptions

Listen to the JS exceptions and register callbacks to process the exception details.

**<u>Python</u>**

```python
async def catchJSException():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome()
    
    async with driver.bidi_connection() as session:
        driver.get("<your site url>")
        log = Log(driver, session)
        async with log.add_js_error_listener() as messages:
            # Operation on the website that throws an JS error
        print(messsages)
        
    driver.quit()
```

**<u>CSharp</u>**

```c#
List<string> exceptionMessages = new List<string>();
IJavaScriptEngine monitor = new JavaScriptEngine(driver);
monitor.JavaScriptExceptionThrown += (sender, e) =>
{
    exceptionMessages.Add(e.Message);
};

await monitor.StartEventMonitoring();

driver.Navigate.GoToUrl("<your site url>");

IWebElement link2click = driver.FindElement(By.LinkText("<your link text>"));
((IJavaScriptExecutor) driver).ExecuteScript("arguments[0].setAttribute(arguments[1], arguments[2]);", link2click, "onclick", "throw new Error('Hello, world!')");
lick2click.Click();

foreach (string message in exceptionMessages)
{
    Console.WriteLine("JS exception message: {0}", message);
}
```

#### Network Interception

If you want to capture network events coming into the browser and you want manipulate them you are able to do it with the following examples.

**<u>Python</u>**

```python
# Currently unavailable in python due the inability to mix certain async and sync commands
```

**<u>CSharp</u>**

```c#
// placeholder
```

### [2-9-2 Chrome DevTools](https://www.selenium.dev/documentation/webdriver/bidirectional/chrome_devtools/)

> While Selenium 4 provides direct access to the Chrome DevTools Protocol (CDP), it is highly encouraged that you use the WebDriver Bidi APIs instead.

Many browsers provide "DevTools" - a set of tools that integrated with the browser that developers can use to debug web apps and explore the performance of their pages. Google Chrome's DevTools make use of a protocol called the Chrome DevTools Protocol (or "CDP" for short). As the name suggests, this is not designed for testing, nor to have a stable API, so functionality is highly dependent on the version of the browser.

WebDriver Bidi is the next generation of the W3C WebDriver protocol and aims to provide a stable API implemented by all browsers, but it's not yet complete. Until it is, Selenium provides access to the CDP for those browsers that implement it (such as Google Chrome, or Microsoft Edge, and Firefox), allowing you to enhance your tests in interesting ways. Some examples of what you can do with it are given below.

#### Emulate Geo Location

Some applications have different features and functionalities across different locations. Automating such applications is different because it is hard to emulate the geo-locations in the browser using Selenium. But with the help of Devtools, we can easily emulate them. Below code snippet demonstrates that.

**<u>Python</u>**

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def geoLocationTest():
    driver = webdriver.Chrome()
    Map_coordinates = dict({
        "latitude": 41.8781,
        "longitude": -87.6298,
        "accuracy": 100
    })
    driver.execute_cdp_cmd("Emulation.setGeolocationOverride", Map_coordinates)
    driver.get("<your site url>")
```

**<u>CSharp</u>**

```c#
using System.Threading.Tasks;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.DevTools;
// Replace the version to match the Chrome version
using OpenQA.Selenium.DevTools.V87.Emulation;

namespace dotnet_test {
    class Program {
        public static void Main(string[] args) {
            GeoLocation().GetAwaiter().GetResult();
        }
        
        public static async Task GeoLocation() {
            ChromeDriver driver = new ChromeDriver();
            DevToolsSession devToolsSession = driver.CreateDevToolsSession();
            var geoLocationOverrideCommandSettings = new SetGeoLocationOverrideCommandSettings();
            geoLocationOverrideCommandSettings.Latitude = 51.507351;
            geoLocationOverrideCommandSettings.Longitude = -0.127758;
            geoLocationOverrideComamndSettings.Accuracy = 1;
            
            await devToolsSession
                .GetVersionSpecificDomains<OpenQA.Selenium.DevTools.V87.DevToolsSessionDomains>()
                .Emulation
                .SetGeolocationOverride(geoLocationOverrideCommandSettings);
            
            driver.Url = "<your site url>";
        }
    }
}
```

#### Emulate Geo Location with the Remote WebDriver

**<u>Python</u>**

```python
from selenium import webdriver
# Replace the version to match the Chrome version
import selenium.webdriver.common.devtools.v93 as devtools

async def geoLocationTest():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
    	command_executor='<grid-url>',
    	options=chrome_options
    )
    
    aysnc with driver.bidi_connection() as session:
        cdpSession = session.session
        await cdpSession.execute(devtools.emulation.set_geolocation_override(latitude=41.8781,longitude=-87.6298,accuracy=100))
        driver.get("https://my-location.org/")
        driver.quit()
```

**<u>CSharp</u>**

```c#
using System.Threading.Tasks;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.DevTools;
// Replace the version to match the Chrome version
using OpenQA.Selnium.DevTools.V87.Emulation;

namespace dotnet_test {
    class Program {
        public static void Main(string[] args) {
            GeoLocation().GetAwaiter().GetResult();
        }
        
        public static async Task GeoLocation() {
            ChromeOptions chromeOptions = new ChromeOptions();
            RemoteWebDriver driver = new RemoteWebDriver(new Uri("<grid-url>"), chromeOptions);
            DevToolsSession devToolsSession = driver.CreateDevToolsSession();
            var geoLocationOverrideCommandSettings = new SetGeolocationOverrideCommandSettings();
            
            geoLocationOverrideCommandSettings.Latitude = 51..507351;
            geoLocationOverrideCommandSettings.Longitude = -0.127758;
            geoLocationOverrideCommandSettings.Accuracy = 1;
            
            await devToolsSession
                .GetVersionSpecificDomains<OpenQA.Selenium.DevTools.V87.DevToolsSessionDomains>()
                .Emulation
                .SetGeolocationOverride(geoLocationOverrideCommandSettings);
            
            driver.Url = "https://my-location.org/";
        }
    }
}
```

#### Override Device Mode

Using Selenium's integration with CDP, one can override the current mode and simulate a new mode. Width, height, mobile, and deviceScaleFactor are required parameters. Optional parameters include `scale`, `screenWidth`, `screenHeight`, `positionX`, `positionY`, `dontsetVisible`, `screenOrientation`, `viewport`, and `displayFeature`.

**<u>Python</u>**

```python
# placeholder
```

**<u>CSharp</u>**

```c#
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.DevTools;
using System.Threading.Tasks;
using OpenQA.Selenium.DevTools.V91.Emulation;
using WebDriverManager;
using WebDriverManager.DriverConfigs.Impl;
using DevToolsSessionDomains = OpenQA.Selenium.DevTools.V91.DevToolsSessionDomains;

namespace Selenium4Sample {
    public class ExampleDevice {
        protected IDevToolsSession session;
        protected IWebDriver driver;
        protected DevToolsSessionDomains devToolsSession;
        
        public async Task DeviceModeTest() {
            new DriverManager().SetUpDriver(new ChromeConfig());
            ChromeOptions chromeOptions = new ChromeOptions();
            // Set ChromeDriver
            driver = new ChromeDriver();
            // Get DevTools
            IDevTools devTools = driver as IDevTools;
            // DevTools Session
            session = devTools.GetDevToolsSession();
            
            var deviceModeSetting = new SetDeviceMetricsOverrideCommandSettings();
            deviceModeSetting.Width = 600;
            deviceModeSetting.Height = 1000;
            deviceModeSetting.Mobile = true;
            deviceModeSetting.DeviceScaleFactor = 50;
            
            await session
                .GetVersionSpecificDomains<OpenQA.Selenium.DevTools.V91.DevToolsSessionDomains>()
                .Emulation
                .SetDeviceMetricsOverride(deviceModeSetting);
            
            driver.Url = "<your site url>";
        }
    }
}
```

#### Collect Performance Metrics

Collect various performance metrics while navigating the application.

**<u>Python</u>**

```python
# placeholder
```

**<u>CSharp</u>**

```c#
// File must contain the following using statements
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.DevTools;

// We must use a version-specific set of domains
using OpenQA.Selenium.DevTools.V94.Performance;

public async Task PerformanceMetricsExample(){
    IWebDriver driver = new ChromeDriver();
    IDevTools devTools = driver as IDevTools;
    DevToolsSession session = devTools.GetDevToolsSession();
    await session.SendCommand<EnableCommandSettings>(new EnableCommandSettings());
    var metricsResponse =
        await session.SendCommand<GetMetricsCommandSettings, GetMetricsCommandResponse>(new GetMetricsCommandSettings());
    driver.Navigate().GoToUrl("http://www.google.com");
    driver.Quit();
    
    var metrics = metricsResponse.Metrics;
    foreach (Metric metric in metrics)
    {
        Console.WriteLine("{0} = {1}", metric.Name, metric.Value);
    }
}
```

## [2-10 Additional Features](https://www.selenium.dev/documentation/webdriver/additional_features/)

Set of packages and functionalities to simplify automation with Selenium.

### [colors](https://www.selenium.dev/documentation/webdriver/additional_features/colors/)

You will occasionally want to validate the color of something as part of your tests; the problem is that color definitions on the web are not constant. Would it not be nice if there was an easy way to compare a HEX representation of a color with a RGB representation of a color, or a RGBA representation of a color with a HSLA representation of a color?

Worry not. There is a solution: the *Color* class!

First of all, you will need to import the class:

 **<u>Python</u>**

```python
from selenium.webdriver.support.color import Color
```

**<u>CSharp</u>**

```c#
// placeholder
```

You can now start creating color objects. Every color object will need to be created from a string representation of your color. Supported color representations are:

**<u>Python</u>**

```python
HEX_COLOR = Color.from_string('#2F7DE8')
RGB_COLOR = Color.from_string('rgb(255, 255, 255)')
RGB_COLOUR = Color.from_string('rgb(40%, 20%, 40%)')
RGBA_COLOUR = Color.from_string('rgba(255, 255, 255, 0.5)')
RGBA_COLOUR = Color.from_string('rgba(40%, 20%, 40%, 0.5)')
HSL_COLOUR = Color.from_string('hsl(100, 0%, 50%)')
HSLA_COLOUR = Color.from_string('hsla(100, 0%, 50%, 0.5)')
```

**<u>CSharp</u>**

```c#
// placeholder
```

The Color class also supports all of the base color definitions specified in [http://www.w3.org/TR/css3-color/#html4](https://www.w3.org/TR/css3-color/#html4).

**<u>Python</u>**

```python
BLACK = Color.from_string('black')
CHOCOLATE = Color.from_string('chocolate')
HOTPINK = Color.from_string('hotpink')
```

**<u>CSharp</u>**

```c#
// placeholder
```

Sometimes browsers will return a color value of "transparent" if no color has been set on an element. The Color class also supports this:

**<u>Python</u>**

```python
TRANSPARNET = Color.from_string('transparent')
```

**<u>CSharp</u>**

```c#
// placeholder
```

You can now safely query an element to get its color/background color knowing that any response will be correctly parsed and converted into a valid Color object:

**<u>Python</u>**

```python
login_button_color = Color.from_string(driver.find_element(By.ID, 'login').value_of_css_property('color'))
login_button_background_color = Color.from_string(driver.find_element(By.ID, 'login').value_of_css_property('background-color'))
```

**<u>CSharp</u>**

```c#
// placeholder
```

You can then directly compare color objects:

**<u>Python</u>**

```python
assert login_button_background_color == HOTPINK
```

**<u>CSharp</u>**

```c#
// placeholder
```

Or you can convert color into one of the following formats and perform a static validation:

**<u>Python</u>**

```python
assert login_button_background_color.hex == '#ff69b4'
assert login_button_background_color.rgba == 'rgba(255, 105, 180, 1)'
assert login_button_background_color.rgb == 'rgb(255, 105, 180)'
```

**<u>CSharp</u>**

```c#
// placeholder
```

### [ThreadGuard](https://www.selenium.dev/documentation/webdriver/additional_features/thread_guard/)

> This class is only available in the Java Binding

不需要看

# 3 Grid

暂时不需要看

# 4 IE Driver Server

不需要看

# 5 IDE

不需要看

# [6 Test Practices](https://www.selenium.dev/documentation/test_practices/)

> Some guidelines and recommendations on testing from the Selenium project.

A note on "Best Practices": We've intentionally avoided the phrase "Best Practices" in this documentation. No one approach works for all situations. We prefer the idea of "Guidelines and Recommendations". We encourage you to read through these and thoughtfully[^6-0-1] decide what approaches will work for you in your particular environment.

Functional testing is difficult to get right for many reasons. As if application state, complexity, and dependencies do not make testing difficult enough, dealing with browsers (especially with cross-browser incompatibilities) makes writing good tests a challenge.

Selenium provides tools to make functional user interaction easier, but does not help you write well-architected test suites. In this chapter we offer advice, guidelines, and recommendations on how to approach functional web page automation.

This chapter records software design patterns popular amongst many of the users of Selenium that have proven successful over the years.

## [6-1 Design Strategies](https://www.selenium.dev/documentation/test_practices/design_strategies/)

### Overview

Over time, project tend to accumulate large numbers of tests. As the total number of tests increases, it becomes harder to make changes to the codebase -- a single "simple" change may cause numerous tests to fail, even though the application still works properly. Sometimes these problems are unavoidable, but when they do occur you want to be up and running again as quickly as possible. The following design patterns and strategies have been used before with WebDriver to help make tests easier to write and maintain. They may help you too.

<u>DomainDrivenDesign</u>: Express your tests in the language of the end-user of the app.

<u>PageObjects</u>: A simple abstraction of the UI of your web app.

<u>LoadableComponent</u>: Modeling PageObjects as components.

<u>BotStyleTests</u>: Using a command-based approach to automating tests, rather than the object-based approach that PageObjects encourage.

### Loadable Component

#### What Is It?

The loadable component is a base class that aims to make writing PageObjects less painful. It does this by providing a standard way of ensuring that pages are loaded and providing hooks to make debugging the failure of a page to load easier. You can use it to help reduce the amount of boilerplate code in your tests, which in turn makes maintaining your tests less tiresome.

There is currently an implementation in Java that ships as part of Selenium 2, but the approach used is simple enough to be implemented in any language.

#### Simple Usage

As an example of a UI that we'd like to model, take a look at the [new issue](https://github.com/SeleniumHQ/selenium/issues/new) page. From the point of view of a test author, this offers the service of being able to file a new issue. A basic Page Object would look like:

```java
package com.example.webdriver;

import org.openqa.selenium.by;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class EditIssue {
    
    private final WebDriver driver;
    
    public EditIssue(WebDriver driver) {
        this.driver = driver;
    }
    
    public void setSummary(String summary) {
        WebElement field = driver.findElement(By.name("summary"));
        clearAndType(field, summary);
    }
    
    public void enterDescription(String description) {
        WebElement field = driver.findElement(By.name("comment"));
        clearAndType(field, description);
    }
    
    public IssueList submit() {
        driver.findElement(By.id("submit")).click();
        return new IssueList(driver);
    }
    
    private void clearAndType(WebElement field, String text) {
        field.clear();
        field.sendKeys(text);
    }
}
```

In order to turn this into a LoadableComponent, all we need to do is to set that as the base type:

```java
public class EditIssue extends LoadableComponent<EditIssue> {
    // rest of class ignored for now
}
```

This signature looks a little unusual, but all it means is that this class represents a LoadableComponent that loads the EditIssue page.

By extending this base class, we need to implement two new methods:

```java
@override
protected void load() {
    driver.get("https://github.com/SeleniumHQ/selenium/issues/new");
}

@override
protected void isLoaded() throws Error {
    String url = driver.getCurrentUrl();
    assertTrue("Not on the issue entry page: " + url, url.endsWith("/new"));
}
```

The `load` method is used to navigate to the page, whilst the `isLoaded` method is used to determine whether we are on the right page. Although the method looks like it should return a boolean, instead it performs a series of assertions using JUnit's assert class. There can be as few or as many assertions as you like. By using these assertions it's possible to give users of the class clear information that can be used to debug tests.

With a little rework, our PageObject looks like:

```java
package com.example.webdriver;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

import static junit.framework.Assert.assertTrue;

public class EditIssue extends LoadableComponent<EditIssue> {
    
    private final WebDriver driver;
    
    // By default the PageFactory will locate elements with the same name or id
    // as the field. Since the summary element has a name attribute of "summary"
    // we don't need any additional annotations.
    private WebElement summary;
    
    // Same with the submit element, which has the ID "submit"
    private WebElement submit;
    
    // But we'd prefer a different name in our code than "comment", so we use the
    // FindBy annotation to tell the PageFactory how to locate the element.
    @FindBy(name = "comment")
    private WebElement description;
    
    public EditIssue(WebDriver driver) {
        this.driver = driver;
        
        // This call sets the WebElement fields.
        PageFactory.initElements(driver, this);
    }
    
    @Override
    protected void load() {
        driver.get("https://github.com/SeleniumHQ/selenium/new");
    }
    
    @Override
    protected void isLoaded() throws Error {
        String url = driver.getCurrentUrl();
        assertTrue("Not on the issue entry page: " + url, url.endsWith("/new"));
    }
    
    public void setSummary(String issueSummary) {
        clearAndType(summary, issueSummary);
    }
    
    public void enterDescription(String issueDescription) {
        clearAndType(description, issueDescription);
    }
    
    public IssueList submit() {
        submit.click();
        return new IssueList(driver);
    }
    
    private void clearAndType(WebElement field, String text) {
        field.clear();
        field.sendKeys(text);
    }
}
```

This doesn't seem to have bought us much, right? One thing it has done is encapsulate the information about how to navigate to the page into the page itself, meaning that this information's not scattered[^6-1-1] through the code base. It also means that we can do this in our tests:

```java
EditIssue page = new EditIssue(driver).get();
```

This call will cause the driver to navigate to the page if that's necessary.

#### Nested Components

Loadable components start to become more useful when they are used in conjunction with other loadable components. Using our example, we could view the "edit issue" page as a component within a project's website (after all, we access it via a tab on that site). You also need to be logged in to file an issue. We could model this as a tree of nested components:

```shell
+ ProjectPage
+---+ SecuredPage
	+---+ EditIssue
```

What would this look like in code? For a start, each logical component would have its own class. The "load" method in each of them would "get" the parent. The end result, in addition to the EditIssue class above is:

`ProjectPage.java`:

```java
package com.example.webdriver;

import org.openqa.selenium.WebDriver;
import static org.junit.Assert.assertTrue;

public class ProjectPage extends LoadableComponent<ProjectPage> {
    
    private final WebDriver driver;
    private final String projectName;
    
    public ProjectPage(WebDriver driver, String projectName) {
        this.driver = driver;
        this.projectName = projectName;
    }
    
    @Override
    protected void load() {
        driver.get("http://" + projectName + ".googlecode.com/");
    }
    
    @Override
    protected void isLoaded() throws Error {
        String url = driver.getCurrentUrl();
        
        assertTrue(url.contains(projectName));
    }
}
```

and `SecuredPage.java`:

```java
package com.example.webdriver;

import org.openqa.selenium.By;
import org.openqa.selenium.NoSuchElementException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

import statc org.junit.Assert.fail;

public class SecuredPage extends LoadableComponent<SecuredPage> {
    private final WebDriver driver;
    private final LoadableComponent<?> parent;
    private final String username;
    private final String password;
    
    public SecuredPage(WebDriver driver, LoadableComponent<?> parent, String username, String password) {
        this.driver = driver;
        this.parent = parent;
        this.username = username;
        this.password = password;
    }
    
    @Override
    protected void load() {
        parent.get();
        
        String originalUrl = driver.getCurrentUrl();
        
        // Sign in
        driver.get("https://www.google.com/accounts/ServiceLogin?service=code");
        driver.findElement(By.name("Email")).sendKeys(username);
        WebElement passwordField = driver.findElement(By.name("Passwd"));
        passwordField.sendKeys(password);
        passwordField.submit();
        
        // Now return to the original Url
        driver.get(originalUrl);
    }
    
    @Override
    protected void isLoaded() throws Error {
        // If you're signed in, you have the option of picking a different login.
        // Let's check for the presence of that.
        
        try {
            WebElement div = driver.findElement(By.id("multilogin-dropdown"));
        } catch (NoSuchElementException e) {
            fail("Cannot locate user name link");
        }
    }
}
```

The "load" method in EditIssue now looks like:

```java
@Override
protected void load() {
    securedPage.get();
    
    driver.get("https://github.com/SeleniumHQ/selenium/issues/new");
}
```

This shows that the components are still "nested" within each other. A call to `get()` in EditIssue will cause all its dependencies to load too. The example usage:

```java
public class FooTest {
    private EditIssue editIssue;
    
    @Before
    public void prepareComponents() {
        WebDriver driver = new FirefoxDriver();
        
        ProjectPage project = new ProjectPage(driver, "selenium");
        SecuredPage securedPage = new SecuredPage(driver, project, "example", "top secret");
        editIssue = new EditIssue(driver, securedPage);
    }
    
    @Test
    public void demonstrateNestedLoadableComponents() {
        editIssue.get();
        
        editIssue.SetSummary("Summary");
        editIssue.enterDescription("This is an example");
    }
}
```

If you're using a library such as [Guiceberry](https://github.com/zorzella/guiceberry) in your tests, the preamble[^6-1-2] of setting up the PageObjects can be omitted leading to nice, clear, readable tests.

### Bot Pattern

> Previously located: https://github.com/SeleniumHQ/selenium/wiki/Bot-Style-Tests)

Although PageObjects are a useful way of reducing duplication in your tests, it's not always a pattern that teams fell comfortable following. An alternative approach is to follow a more "command-like" style of testing.

==A "bot" is an action-oriented abstraction over the raw Selenium APIs.== This means that if you find that commands aren't doing the right thing for your app, it's easy to change them. As an example:

```java
public class ActionBot {
    private final WebDriver driver;
    
    public ActionBot(WebDriver driver) {
        this.driver = driver;
    }
    
    public void click(By locator) {
        driver.findElement(locator).click();
    }
    
    public void submit(By locator) {
        driver.findElement(locator).submit();
    }
    /**
     * Type something into an input field. WebDriver doesn't normally clear these
     * before typing, so this method does that first. It also sends a return key
     * to move the focus out of the element.
     */
    public void type(By locator, String text) {
        WebElement element = driver.findElement(locator);
        element.clear();
        element.sendKeys(text + "\n");
    }
}
```

Once these abstractions have been built and duplication in your tests identified, it's possible to layer PageObjects on top of bots.

## [6-2 Overview](https://www.selenium.dev/documentation/test_practices/overview/)

First, start by asking yourself whether or not you really need to use a browser. Odds are that, at some point, if you are working on a complex web application, you will need to open a browser and actually test it.

Functional end-user tests such as Selenium tests are expensive to run, however. Furthermore, they typically require substantial infrastructure to be in place to be run effectively. It is a good rule to always ask yourself what you want to test can be done using more lightweight test approaches such as unit tests or with a lower-level approach.

Once you have made the determination that you are in the web browser testing business, and you have your Selenium environment ready to begin writing tests, you will generally perform some combination of three steps:

* Set up the data
* Perform a discrete set of actions
* Evaluate the results

You will want to keep these steps as short as possible; one or two operations should be enough most of the time. Browser automation has the reputation of being "flaky[^6-2-1]", but in reality, that is because users frequently demand too much of it. In later chapters, we will return to techniques you can use to mitigate[^6-2-2] apparent intermittent problems in tests, in particular on how to [overcome race conditions](https://www.selenium.dev/documentation/webdriver/waits/) between the browser and WebDriver.

By keeping your tests short and using the web browser only when you have absolutely no alternative, you can have many tests with minimal flake.

A distinct advantage of Selenium tests is their inherent ability to test all components of the application, from backend to frontend, from a user's perspective. So in other words, whilst functional tests may be expensive to run, they also encompass[^6-2-3] large business-critical portions at one time.

### Testing requirements

As mentioned before, Selenium tests can be expensive to run. To what extent[^6-2-4] depends on the browser you are running the tests against, but historically browsers' behavior has varied so much that it has often been a stated goal to cross-test against multiple browsers.

Selenium allows you to run the same instructions against multiple browsers on multiple operating systems, but the enumeration of all the possible browsers, their different versions, and the many operating systems they run on will quickly become a non-trivial undertaking[^6-2-5].

### Let's start with an example

Larry has written a website which allows users to order their custom unicorns.

The general workflow (what we will call the "happy path") is something like this:

* Create an account
* Configure the unicorn
* Add it to the shopping cart
* Check out and pay
* Give feedback about the unicorn

It would be tempting to write one grand[^6-2-6] Selenium script to perform all these operations -- many will try. Resist the temptation! Doing so will result in a test that

* takes a long time
* will be subject to some common issues around page rendering timing issues
* is such that if it fails, it will not give you a concise, "glanceable" method for diagnosing what went wrong.

The preferred strategy for testing this scenario would be to break it down to a series of independent, speedy tests, each of which has one "reason" to exist.

Let us pretend you want to test the second step:  Configuring your unicorn. It will perform the following actions:

* Create an account
* Configure a unicorn

Note that we are skipping the rest of these steps, we will test the rest of the workflow in other small, discrete test cases after we are done with this one.

To start, you need to create an account. Here you have some choices to make:

* Do you want to use an existing account?
* Do you want to create a new account?
* Are there any special properties of such a user that need to be taken into account before configuration begins?

Regardless of how you answer this question, the solution is to make it part of the "set up the data" portion of the test. If Larry exposed an API that enables you (or anyone) to create and update user accounts, be sure to use that to answer this question. If possible, you want to launch the browser only after you have a user "in hand", whose credentials you can just log in with.

If each test for each workflow begins with the creation of a user account, many seconds will be added to the execution of each test. Calling an API and talking to a database are quick, "headless" operations that don't require the expensive process of opening a browser, navigating to the right pages, clicking and waiting for the forms to be submitted, etc.

Ideally, you can address this set-up phase in one line of code, which will execute before any browser is launched:

**<u>Python</u>**

```python
# Create a user who has read-only permissions -- they can configure a unicorn,
# but they do not have payment information set up, nor do they have 
# administrative privileges. At the time the user is created, its email
# address and password are randomly generated -- you don't even need to
# know them.
user = user_factory.create_common_user() # This method is defined elsewhere.

# Log in as this user.
# Logging in on this site takes you to your personal "My Account" page, so the
# AccountPage object is returned by the loginAs method, allowing you to then
# perform actions from the AccountPage.
account_page = login_as(user.get_email(), user.get_password())
```

**<u>CSharp</u>**

```c#
// Create a user who has read-only permissions--they can configure a unicorn,
// but they do not have payment information set up, nor do they have
// administrative privileges. At the time the user is created, its email
// address and password are randomly generated--you don't even need to
// know them.
User user = UserFactory.CreateCommonUser(); // This method is defined elsewhere

// Log in as this user.
// Logging in on this site takes you to your personal "My Account" page, so the
// AccountPage object is returned by the loginAs method, allowing you to then
// perform actions from the AccountPage.
AccountPage accountPage = LoginAs(user.Email, user.Password);
```

As you can imagine, the `UserFactory` can be extended to provide methods such as `createAdminUser()`, and `createUserWithPayment()`. The point is, these two lines of code do not distract you from the ultimate purpose of this test: configuring a unicorn.

The intricacies[^6-2-7] of the <u>Page Object model</u> will be discussed in later chapters, but we will introduce the concept here:

Your tests should be composed of actions, performed from the user's point of view, within the context of pages in the site. These pages are stored as objects, which will contain specific information about how the web page is composed and how actions are performed -- very little of which should concern you as a tester.

What kind of unicorn do you want? You might want pink, but not necessarily. Purple has been quite popular lately. Does she need sunglasses? Star tattoos? Those choices, while difficult, are your primary concern as a tester -- you need to ensure that your order fulfillment center sends out the right unicorn to the right person, and that starts with these choices.

Notice that nowhere in that paragraph do we talk about buttons, fields, drop-downs, radio buttons, or web forms. Neither should your tests! You want to write your code like the user trying to solve their problem. Here is one way of doing this (continuing from the previous example): adornment[^6-2-8]

**<u>Python</u>**

```python
# The Unicorn is a top-level Object -- it has attributes, which are set here.
# This only stores the values; it does not fill not any web forms or interact
# with the browser in any way.
sparkles = Unicorn("Sparkles", UnicornColors.PURPLE, UnicornAccessories.SUNGLASSES, UnicornAdornments.STAR_TATTOOS)

# Since we're already "on" the account page, we have to use it to get to the
# actual place where you configure unicorns. Calling the "Add Unicorn" method
# takes us there.
add_unicorn_page = account_page.add_unicorn()

# now that we're on the AddUnicornPage, we will pass the "sparkles" object to
# its createUnicorn() method. This method will take Sparkles' attributes,
# fill out the form, and click submit.
unicorn_confirmation_page = add_unicorn_page.create_unicorn(sparkles)
```

**<u>CSharp</u>**

```c#
// The Unicorn is a top-level Object--it has attributes, which are set here. 
// This only stores the values; it does not fill out any web forms or interact
// with the browser in any way.
Unicorn sparkles = new Unicorn("Sparkles", UnicornColors.Purple, UnicornAccessories.Sunglasses, UnicornAdornments.StarTattos);

// Since we are already "on" the account page, we have to use it to get to the
// actual place where you configure unicorns. Calling the "Add Unicorn" method
// takes us there.
AddUnicornPage addUnicornPage = accountPage.AddUnicorn();

// Now that we're on the AddUnicornPage, we will pass the "sparkles" object to
// its createUnicorn() method. This method will take Sparkles' attributes,
// fill out the form, and click submit.
UnicornConfirmationPage unicornConfirmationPage = addUnicornPage.CreateUnicorn(sparkles);
```

Now that you have configured your unicorn, you need to move on to step 3: making sure it actually worked.

intact[^6-2-9]

**<u>Python</u>**

```python
# The exists() method from UnicornConfirmationPage will take the Sparkles
# object--a specification of the attributes you want to see, and compare
# them with the fields on the page.
assert unicorn_confirmation_page.exists(sparkles), "Sparkles should have been created, with all attributes intact"
```

**<u>CSharp</u>**

```c#
// The exists() method from UnicornConfirmationPage will take the Sparkles
// object -- a specification of the attributes you want to see, and compare
// them with the fields on the page.
Assert.True(unicornConfirmationPage.Exists(sparkles), "Sparkles should have been created, with all attributes intact");
```

Note that the tester still has not done anything but talk about unicorns in this code -- no buttons, no locators, no browser controls.  This method of ==modelling== the application allows you to keep these test-level commands in place and unchanging, even if Larry decides next week that he no longer likes Ruby-on-Rails and decides to re-implement the entire site in the latest Haskell bindings with a Fortran front-end.

Your page objects will require some small maintenance in order to conform[^6-2-10] to the site redesign, but these tests will remain the same. Taking this basic design, you will want to keep going through our workflows with the fewest browser-facing steps possible. Your next workflow will involve adding a unicorn to the shopping cart. You will probably want many iterations of this test in order to make sure the cart is keeping its state properly: Is there more than one unicorn in the cart before you start? How many can fit in the shopping cart? If you create more than one with the same name and/or features, will it break? Will it only keep the existing one or will it add another?

Each time you move through the workflow, you want to try to avoid having to create an account, login as the user, and configure the unicorn. Ideally, you will be able to create an account and pre-configure a unicorn via the API or database. Then all you have to do is log in as the user, locate Sparkles, and add her to the cart.

### To automate or not to automate?

Is automation always advantageous[^6-2-11]? When should one decide to automate test cases?

It is not always advantageous to automate test cases. There are times when manual testing may be more appropriate. For instance, if the application's user interface will change considerably in the near future, then any automation might need to be rewritten anyway. Also, sometimes there simply is not enough time to build test automation. For the short term, manual testing may be more effective. If an application has a very tight deadline, there is currently no test automation available, and it's imperative that the testing gets done within that time frame, then manual testing is the best solution.

## [6-3 Testing Types](https://www.selenium.dev/documentation/test_practices/testing_types/)

### Acceptance testing

This type of testing is done to determine if a feature or system meets the customer expectations and requirements. This type of testing generally involves the customer's cooperation or feedback, being a validation activity that answers the question:

<u>Are we building the ***right*** product?</u>

For web applications, the automation of this testing can be done directly with Selenium by simulating user expected behavior. This simulation could be done by record/playback or through the different supported languages as explained in this documentation. Note:

Acceptance testing is a subtype of *functional testing*, which some people might also refer to.

### Functional testing

This type of testing is done to determine if a feature or system functions properly without issues. It checks the system at different levels to ensure that all scenarios are covered and that the system does what it's supposed to do. It's a verification activity that answers the question:

<u>Are we building the product ***right***?</u>

This generally includes: the tests work without errors (404, exceptions,...), in a usable way (correct redirections), in an accessible way and matching its specifications (see acceptance testing above).

For web applications, the automation of this testing can be done directly with Selenium by simulation expected returns.

This simulation could be done by record/playback or through the different supported languages as explained in this documentation.

### Performance testing

As its name indicates, performance tests are done to measure how well an application is performing.

There are two main sub-types for performance testing:

#### Load testing

Load testing is done to verify how well the application works under different defined loads (usually a particular number of users connected at once).

#### Stress testing

Stress testing is done to verify how well the application works under stress (or above the maximum supported load).

Generally, performance tests are done by executing some Selenium written tests simulating different users hitting a particular function on the web app and retrieving some meaningful measurements.

This is generally done by other tools that retrieve the metrics. One such tool is JMeter.

For a web application, details to measure include throughput, latency, data loss, individual component loading times...

Note 1: All browsers have a performance tab in their developers' tools section (accessible by pressing F12)

Note 2: is a subtype of non-functional testing as this is generally measured per system and not per function/feature.

### Regression testing

This testing is generally done after change, fix or feature addition.

To ensure that the change has not broken any of the existing functionality, some already executed tests are executed again.

The set of re-executed tests can be full or partial and can include several different types, depending on the application and development team.

### Test driven development (TDD)

Rather than a test type per se[^6-3-1], TDD is an iterative development methodology in which tests drive the design of a feature.

Each cycle starts by creating a set of unit tests that the feature should eventually pass (they should fail their first time executed).

After this, development takes place to make the tests pass. The tests are executed again, starting another cycle and this process continues until all tests are passing.

This aims to speed up the development of an application based on the fact that defects are less costly the earlier they are found.

### Behavior-driven development (BDD)

BDD is also an iterative development methodology based on the above TDD, in which the goal is to involve all the parties in the development of an application.

Each cycle starts by creating some specifications (which should fail). Then create the failing unit tests (which should also fail) and then do the development.

This cycle is repeated until all types of tests are passing.

In order to do so, a specification language is used. It should be understandable by all parties and simple, standard and explicit. Most tools use *Gherkin* as this language.

The goal is to be able to detect even more errors than TDD, by targeting potential acceptance errors too and make communication between parties smoother.

A set of tools are currently available to write the specifications and match them with code functions, such as *Cucumber* or *SpecFlow*.

A set of tools are built on top of Selenium to make this process even faster by directly transforming the BDD specifications into executable code. Some of these are *JBehave*, *Capybara*[^6-3-2] and *Robot Framework*.

## [6-4 Encouraged](https://www.selenium.dev/documentation/test_practices/encouraged/)

Same with text under Test Practices, need to raise a bug.

### [6-4-1 Page object models](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)

Note: this page has merged contents from multiple sources, including the [Selenium wiki](https://github.com/SeleniumHQ/selenium/wiki/PageObjects)

**Overview**

Within your web app's UI there are areas that your tests interact with. A Page Object simply models these as objects within the test code. This reduces the amount of duplicated code and means that if the UI changes, the fix need only be applied in one place.

Page Object is a Design Pattern which has become popular in test automation for enhancing test maintenance and reducing code duplication. A page object is an object-oriented class that serves as an interface to a page of your AUT. The tests then use the methods of this page object class whenever they need to interact with the UI of that page. The benefit is that if the UI changes for the page, the tests themselves don't need to change, only the code within the page object needs to change. Subsequently all changes to support that new UI are located in one place.

* **Advantages**

  * There is a clean separation between test code and page specific code such as locators (or their use if you're using a UI Map) and layout.

  * There is a single repository for the services or operations offered by the page rather than having these services scattered[^6-4-1-1] throughout the tests.


In both cases this allows any modifications required due to UI changes to all be made in one place. Useful information on this technique can be found on numerous blogs as this 'test design pattern' is becoming widely used. We encourage the reader who wishes to know more to search the internet for blogs on this subject. Many have written on this design pattern and can provide useful tips beyond the scope of this user guide. To get you started, we'll illustrate page objects with a simple example.

* **Examples**

First, consider an example, typical of test automation, that does not use a page object:

```java
/***
 * Tests login feature
 */
public class Login {
    public void testLogin(){
        // fill login data on sign-in page
        driver.findElement(By.name("user_name")).sendKeys("userName");
        driver.findElement(By.name("password")).sendKeys("my supersecret password");
        driver.findElement(By.name("sign-in")).click();
        
        // verify h1 tag is "Hello userName" after login
        driver.findElement(By.tagName("h1")).isDisplayed();
        assertThat(driver.findElement(By.tagName("h1")).getText(), is("Hello username"));
    }
}
```

There are two problems with this approach.

* There is no separation between the test method and the AUT's locators (IDs in this example); both are intertwined[^6-4-1-2] in a single method. If the AUT's UI changes its identifiers, layout, or how a login is input and processed, the test itself must change.
* The ID-locators would be spread in multiple tests, in all tests that had to use this login page.

Applying the page object techniques, this example could be rewritten like this in the following example of a page object for a sign-in page.

```java
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

/**
 * Page Object encapsulates the Sign-in page.
 */
public class SignInPage{
    protected WebDriver driver;
    
    // <input name="user_name" type="text" value="">
    private By usernameBy = By.name("user_name");
    // <input name="password" type="password" value="">
    private By passwordBy = By.name("password");
    // <input name="sign_in" type="submit" value="SignIn">
    private By signinBy = By.name("sign_in");
    
    public SignInPage(WebDriver driver){
        this.driver = driver;
    }
    
    /**
      * Login as valid user
      *
      * @param userName
      * @param password
      * @return HomePage object
      */
    public HomePage loginValidUser(String userName, String password){
        driver.findElement(usernameBy).sendKeys(userName);
        driver.findElement(passwordBy).sendKeys(password);
        driver.findElement(signinBy).click();
        return new HomePage(driver);
    }
}
```

and page object for a Home page could look like this:

```java
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

/**
 * Page Object encapsulates the Home Page
 */

public class HomePage{
    protected WebDriver driver;
    
    // <h1>Hello userName</h1>
    private By messageBy = By.tagName("h1");
    
    public HomePage(WebDriver driver){
        this.driver = driver;
        if (!driver.getTitle().equals("Home Page of logged in user")){
            throw new IllegalStateException("Thians is not Home Page of logged in user," + " current page is: " + driver.getCurrentUrl());
        }
    }
    
    /**
      * Get message (h1 tag)
      * 
      * @return String message text
      */
    public String getMessageText(){
        return driver.findElement(messageBy).getText();
    }
    
    public HomePage manageProfile(){
        // Page encapsulation to manage profile functionality
        return new HomePage(driver);
    }
    /* More methods offering the services represented by Home Page
    of logged user. These methods in turn might return more Page Objects
    for example click on Compose mail button could return ComposeMail class object */
}
```

So now, the login test would use these two page objects as follows.

```java
/***
 * Tests login feature
 */
public class TestLogin{
    @Test
    public void testLogin(){
        SignInPage signInPage = new SignInPage(driver);
        HomePage homePage = SignInPage.loginValidUser("userName", "password");
        assertThat(homePage.getMessageText(), is("Hello userName"));
    }
}
```

There is a lot of flexibility in how the page objects may be designed, but there are a few basic rules for getting the desired maintainability of your test code.

==Page objects themselves should never make verifications or assertions.== This is part of your test and should always be within the test's code, never in an page object. ==The page object will contain the representation of the page, and the services the page provides via methods== but no code related to what is being tested should be within the page object.

==There is one, single, verification which can, and should, be within the page object and that is to verify that the page, and possibly critical elements on the page, were loaded correctly.== This verification should be done while instantiating the page object. In the examples above, both the SignInPage and HomePage constructors check the expected page is available and ready for requests from the test.

A page object does not necessarily need to represent all the parts of a page itself. The same principles used for page objects can be used to create "<u>**Page Component Objects**" that represent discrete chunks of the page and can be included in page objects.</u> These component objects can provide references to the elements inside those discrete chunks, and methods to leverage[^6-4-1-3] the functionality provided by them. You can even nest component objects inside other component objects for more complex pages. If a page in the AUT has multiple components, or common components used throughout the site (e.g. a navigation bar), then it may improve maintainability and reduce code duplication.

There are other design patterns that also may be used in testing. Some use a Page Factory for instantiating their page objects. Discussing all of these is beyond the scope of this user guide. Here, we merely want to introduce the concepts to make the reader aware of some of the things that can be done. As was mentioned earlier, many have blogged on this topic and we encourage the reader to search for blogs on these topics.

**Implementation Notes**

PageObjects can be thought of as facing in two directions simultaneously. Facing towards the developer of a test, they represent the **services** offered by a particular page. Facing away from the developer, they should be the only thing that has a deep knowledge of the structure of the HTML of a page (or part of a page). It's simplest to think of the methods on a page object as offering the "services" that a page offers rather than exposing the details and mechanics of the page. As an example, think of the inbox of any web-based email system. Amongst the services that it offers are typically the ability to compose a new email, to choose to read a single email, and to list the subject lines of the emails in the box. How these are implemented shouldn't matter to the test.

Because we're encouraging the developer of a test to try and think about the services that they're interacting with rather than the implementation, PageObjects should seldom expose the underlying WebDriver instance. To facilitate this, methods on the PageObject should return other PageObjects. This means that we can effectively model the user's journey through our application. ==It also means that should the way that pages relate to one another change (like when the login page asks the user to change their password the first time they log into a service, when it previously didn't do that) simply changing the appropriate method's signature will cause the tests to fail to compile.== Put another way, we can tell which tests would fail without needing to run them when we change the relationship between pages and reflect this in the PageObjects.

One consequence of this approach is that it may be necessary to model (for example) both a successful and unsuccessful login, or a click could have a different result depending on the state of the app. When this happens, it is common to have multiple methods on the PageObject:

```java
public class LoginPage{
    public HomePage loginAs(String username, String password){
        // ... clever magic happens here
    }
    
    public LoginPage loginAsExpectingError(String username, String password){
        // ... failed login here, maybe because one or both of the username and password are wrong
    }
    
    public String getErrorMessage(){
        // So we can verify that the correct error is shown
    }
}
```

The code presented above shows an important point: the tests, not the PageObjects, should be responsible 

for making assertions about the state of a page. For example:

```java
public void testMessagesAreReadOrUnread(){
    Inbox inbox = new Inbox(driver);
    inbox.assertMessageWithSubjectIsUnread("I like cheese");
    inbox.assertMessageWithSubjectIsNotUnread("I'm not fond of tofu");
}
```

could be re-written as:

```java
public void testMessagesAreReadOrUnread(){
    Inbox inbox = new Inbox(driver);
    assertTrue(inbox.isMessageWithSubjectIsUnread("I like cheese"));
    assertFalse(inbox.isMessageWithSubjectIsUnread("I'm fond of tofu"));
}
```

Of course, as with every guideline there are exceptions, and one that is commonly seen with PageObjects is to check that the WebDriver is on the correct page when we instantiate the PageObject. This is done in the example below.

Finally, a PageObject need not represent an entire page. It may represent a section that appears many times within a site or page, such as site navigation. The essential principle is that there is only one place in your test suite with knowledge of the structure of the HTML of a particular (part of a) page.

**Summary**

* The public methods represent the services that the page offers
* Try not to expose the internals of the page
* Generally don't make assertions
* Methods return other PageObjects
* Need not represent an entire page
* ==Different results for the same action are modelled as different methods==

**Example**

```java
public class LoginPage{
    private final WebDriver driver;
    
    public LoginPage(WebDriver driver){
        this.driver = driver;
        
        // Check that we're on the right page.
        if(!"Login".equals(driver.getTitle())){
            // Alternatively, we could navigate to the login page, perhaps logging out first
            throw new IllegalStateException("This is not the login page");
        }
    }
    
    // The login page contains several HTML elements that will be represented as WebElements.
    // The locators for these elements should only be defined once.
    	By usernameLocator = By.id("username");
    	By passwordLocator = By.id("passwd");
    	By loginButtonLocator = By.id("login");
    
    // The login page allows the user to type their username into the username field
    public LoginPage typeUsername(String username){
        // This is the only place that "knows" how to enter a username
        driver.FindElement(usernameLocator).sendKeys(username);
        
        // Return the current page object as this action doesn't navigate to a page represented by another PageObject
        return this;
    }
    
    // The login page allows the user to type their password into the password field
    public LoginPage typePassword(String password){
        // This is the only place that "knows" how to enter a password
        driver.findElement(passwordLocator).sendKeys(password);
        
        // Return the current page object as this action doesn't navigate to a page represented by another PageObject
        return this;
    }
    
    // The login page allows the user to submit the login form
    public Homepage submitLogin(){
        // This is the only place that submits the login form and expects the destination to to be the home page.
        // A seperate method should be created for the instance of clicking login whilst expecting a login failure.
        driver.findElement(loginButtonLocator).submit();
        
        // Return a new page object representing the destination. Should the login page ever
        // go somewhere else (for example, a legal disclaimer) then changing the method signature
        // for this method will mean that all tests that rely on this behavior won't compile.
        return new HomePage(driver);
    }
    
    // The login page allows the user to submit the login form knowing that an invaild username and/or password were entered
    public LoginPage submitLoginExpectingFailure(){
        // This is the only place that submits the login form and expects the destination to be the login page due to login 		// failure.
        driver.findElement(loginButtonLocator).submit();
        
        // Return a new page object representing the destination. Should the user ever be navigated to the homepage after
        // submitting a login with credentials expected to fail login, the script will fail when it attempts to instantiate
        // the LoginPage pageobject.
        return new LoginPage(driver);
    }
    
    // Consequently, the login page offers the user the service of being able to "log into"
    // the application using a user name and password.
    public HomePage loginAs(String username, String password){
        // The PageObject methods that enter username, password & submit login have already defined and should not be
        // repeated here.
        typeUsername(username);
        typePassword(password);
        return submitLogin();
    }
}
```

**Support in WebDriver**

There is a PageFactory in the support package that provides support for this pattern, and helps to remove some boilerplate code from your page objects at the same time.

### [6-4-2 Domain specific language](https://www.selenium.dev/documentation/test_practices/encouraged/domain_specific_language/)

A domain specific language (DSL) is a system which provides the user with an expressive means of solving a problem. It allows a user to interact with the system on their terms -- not just programmer-speak.

Your users, in general, do not care how your site looks. They do not care about the decoration, animations, or graphics. They want to user your system to push their new employees through the process with minimal difficulty; they want to book travel to Alaska; they want to configure and buy unicorns at a discount. Your job as tester is to come as close as you can to "capturing" this mind-set. With that in mind, we set about "modeling" the application you are working on, such that the test scripts (the user's only pre-release proxy) "speak" for, and represent the user.

The goal is to use <u>ubiquitous language</u>. Rather than referring to "load data into this table" or "click on the third column" it should be possible to use language such as "create a new account" or "order displayed results by name"

With Selenium, DSL is usually represented by methods, written to make the API simple and readable -- they enable a report between the developers and the stakeholders (users, product owners, business intelligence specialists, etc.).

**Benefits**

* Readable: Business stakeholders can understand it.
* Writable: Easy to write, avoids unnecessary duplication.
* Extensible: Functionality can (reasonably) be added without breaking contracts and existing functionality.
* Maintainable: By leaving the implementation details out of test cases, you are well-insulated[^6-4-2-1] against changes to the AUT*.

**Further Reading**

(previously located: https://github.com/SeleniumHQ/selenium/wiki/Domain-Driven-Design)

There is a good book on Domain Driven Design by Eric Evans http://www.amazon.com/exec/obidos/ASIN/0321125215/domainlanguag-20

And to whet[^6-4-2-2] your appetite there's a useful smaller book available online for download at http://www.infoq.com/minibooks/domain-driven-design-quickly

**Java**

Here is an example of a reasonable DSL method in Java. For brevity[^6-4-2-3]'s sake, it assumes the driver object is pre-defined and available to the method.

```java
/**
 * Takes a username and password, fills out the fields, and clicks "login".
 * @return An instance of the AccountPage
 */

public AccountPage loginAsUser(String username, String password){
    WebElement loginField = driver.findElement(By.id("loginField"));
    loginField.clear();
    loginField.sendKeys(username);
    
    // Fill out the password field. The locator we're using is "By.id", and we should
    // have it defined elsewhere in the class.
    WebElement passwordFiled = driver.findElement(By.id("password"));
    passwordField.clear();
    passwordField.sendKeys(password);
    
    // Click the login button, which happens to have the id "submit".
    driver.findElement(By.id("submit")).click();
    
    // Create and return a new instance of the AccountPage (via the built-in 
    // Selenium PageFactory).
    return PageFactory.newInstance(AccountPage.class);
}
```

This method completely abstracts the concepts of input fields, buttons, clicking, and even pages from your test code. Using this approach, all a tester has to do is call this method. This gives you a maintenance advantage: if the login fields ever changed, you would only ever have to change this method - not your tests.

```java
public void loginTest(){
    loginAsUser("cbrown", "cl0wn3");
    
    // Now that we're logged in, do some other stuff--since we used a DSL to support
    // our testers, it's as easy as choosing from available methods.
    do.something();
    do.somethingElse();
    Assert.assertTrue("Something should have been done!", something.wasDone());
    
    // Note that we still haven't referred to a button or web control anywhere in
    // this script...
}
```

It bears[^6-4-2-4] repeating: one of your primary goals should be writing an API that allows your tests to address <u>**the problem at hand, and NOT the problem of the UI**</u>. The UI is a secondary concern for your users - they do not care about the UI, they just want to get their job done. Your test scripts should read like a laundry list of things the user wants to DO, and the things they want to KNOW. The tests should not concern themselves with HOW the UI requires you to go about it.

### [6-4-3 Generating application state](https://www.selenium.dev/documentation/test_practices/encouraged/generating_application_state/)

Selenium should not be used to prepare a test case. All repetitive[^6-4-3-1] actions and preparations for a test case, should be done through other methods. For example, most web UIs have authentication (e.g. a login form). Eliminating logging in via web browser before every test will improve both the speed and stability[^6-4-3-2] of the test. A method should be created to gain access to the AUT[^6-4-3-3] (e.g. using an API to login and set a cookie). Also, creating methods to pre-load data for testing should not be done using Selenium. As mentioned previously, existing APIs should be leveraged to create data for the AUT.

### [6-4-4 Mock external services](https://www.selenium.dev/documentation/test_practices/encouraged/mock_external_services/)

Eliminating the dependencies on external services will greatly improve the speed and stability of your tests.

### [6-4-5 Improved reporting](https://www.selenium.dev/documentation/test_practices/encouraged/improved_reporting/)

Selenium is not designed to report on the status of test cases run. Taking advantage of the built-in reporting capabilities of unit test frameworks is a good start. Most unit test frameworks have reports that can generate xUnit or HTML formatted reports. ==xUnit reports are popular for importing results to a Continuous Integration (CI) server== like Jenkins, Travis, Bamboo, etc. Here are some links for more information regarding report outputs for several languages.

[NUnit 3 Console Runner](https://github.com/nunit/docs/wiki/Console-Runner)

[NUnit 3 Console Command Line](https://github.com/nunit/docs/wiki/Console-Command-Line)

[xUnit getting test results in TeamCity](https://xunit.net/docs/getting-test-results-in-teamcity)

[xUnit getting test results in CruiseControl.NET](https://xunit.net/docs/getting-test-results-in-ccnet)

[xUnit getting test results in Azure DevOps](https://xunit.net/docs/getting-test-results-in-azure-devops)

### [6-4-6 Avoid sharing state](https://www.selenium.dev/documentation/test_practices/encouraged/avoid_sharing_state/)

Although mentioned in several places it is worth mentioning again. Ensure tests are isolated from one another.

* Do not share test data. Imagine several tests that each query the database for valid orders before picking one to perform an action on. Should two tests pick up the same order you are likely to get unexpected behavior.
* Clean up stale[^6-4-6-1] data in the application that might be picked up by another test e.g. invalid order records.
* Create a new WebDriver instance per test. This helps ensure test isolation and makes parallelization simpler.

### [6-4-7 Locators](https://www.selenium.dev/documentation/test_practices/encouraged/locators/)

> When to use which locators and how best to manage them in your code.

Take a look at examples of the <u>supported locator strategies</u>.

In general, if HTML IDs are available, unique, and consistently predictable, they are the preferred method for locating an element on a page. They tend to work very quickly, and forego[^6-4-7-1] much processing that comes with complicated DOM traversals.

If unique IDs are unavailable, a well-written CSS selector is the preferred method of locating an element. XPath works as well as CSS selectors, but the syntax is complicated and frequently difficult to debug. Though XPath selectors are very flexible, they are typically not performance tested by browser vendors and tend to be quite slow.

Selection strategies based on `linkText` and `partialLinkText` have drawbacks in that they only work on link elements. Additionally, they call down to [`querySelectorAll`](https://www.w3.org/TR/webdriver/#link-text)  selectors internally in WebDriver.

Tag name can be a dangerous way to locate elements. There are frequently multiple elements of the same tag present on the page. This is mostly useful when calling the `findElements(By)` method which returns a collection of elements.

The recommendation is to keep your locators as compact and readable as possible. Asking WebDriver to traverse the DOM structure is an expensive operation, and the more you can narrow the scope of your search, the better. 

### [6-4-8 Test independency](https://www.selenium.dev/documentation/test_practices/encouraged/test_independency/)

Write each test as its own unit. Write the tests in a way that will not be reliant on other tests to complete:

Let us say there is a content management system with which you can create some custom content which then appears on your website as a module after publishing, and it may take some time to sync between the CMS and the application.

A wrong way of testing your module is that the content is created and published in one test, and then checking the module in another test. This is not feasible[^6-4-8-1] as the content may not be available immediately for the other test after publishing.

Instead, you can create a stub[^6-4-8-2] content which can be turned on and off within the affected test, and use that for validating the module. However, for content creation, you can still have a separate test.

### [6-4-9 Consider using a fluent API](https://www.selenium.dev/documentation/test_practices/encouraged/consider_using_a_fluent_api/)

Martin Fowler coined[^6-4-9-1] the term "[Fluent API](https://www.martinfowler.com/bliki/FluentInterface.html)". Selenium already implements something like this in their `FluentWait` class, which is meant as an alternative to the standard `Wait` class. You could enable the Fluent API design pattern in your page object and then query the Google search page with a code snippet like this one:

```java
driver.get("http://www.google.com/webhp?hl=en&amp;tab=ww");
GoogleSearchPage gsp = new GoogleSearchPage();
gsp.withFluent().setSearchString().clickSearchButton();
```

The Google page object class with this fluent behavior might look like this:

```java
public class GoogleSearchPage extends LoadableComponent<GoogleSearchPage>{
    private final WebDriver driver;
    private GSPFluentInterface gspfi;
    
    public class GSPFluentInterface{
        private GoogleSearchPage gsp;
        
        public GSPFluentInterface(GoogleSearchPage googleSearchPage){
            gsp = googleSearchPage;
        }
        
        public GSPFluentInterface clickSearchButton(){
            gsp.searchButton.click();
            return this;
        }
        
        public GSPFluentInterface setSearchString(String sstr){
            clearAndType(gsp.searchField, sstr);
            return this;
        }
    }
    
    @FindBy(id="gbqfq") private WebElement searchField;
    @FindBy(id="gbqfb") private WebElement searchButton;
    public GoogleSearchPage(WebDriver driver){
        gspfi = new GSPFluentInterface(this);
        this.get(); // if load() fails, calls isLoaded() until page is finished loading
        PageFactory.initElements(driver, this);  // Initialize WebElements on page
    }
    
    public GSPFulentInterface withFluent(){
        return gspfi;
    }
    
    public void clickSearchButton(){
        searchButton.click();
    }
    
    public void setSearchString(String sstr){
        clearAndType(searchField, sstr);
    }
    
    @Override
    protected void isLoaded() throws Error{
        Assert.assertTrue("Google search page is not yet loaded.", isSearchFieldVisible());
    }
    
    @Override
    protected void load() {
        if ( isSFieldPresent ) {
            Wait<WebDriver> wait = new WebDriverWait( driver, Duration.ofSeconds(3) );
            wait.until( visibilityOfElementLocated( By.id("gbqfq") ) ).click();
        }
    }
}
```

### [6-4-10 Fresh browser per test](https://www.selenium.dev/documentation/test_practices/encouraged/fresh_browser_per_test/)

Start each test from a clean known state. Ideally, spin[^6-4-10-1] up a new virtual machine for each test. If spinning up a new virtual machine is not practical, at least start a new WebDriver for each test. For Firefox, start a WebDriver with you known profile.

```java
FirefoxProfile profile = new FirefoxProfile(new File("pathToFirefoxProfile"));
WebDriver driver = new FirefoxDriver(profile);
```

## [6-5 Discouraged](https://www.selenium.dev/documentation/test_practices/discouraged/)

Things to avoid when automating browsers with Selenium.

### [6-5-1 Captchas](https://www.selenium.dev/documentation/test_practices/discouraged/captchas/)

CAPTCHA, short for <u>*Completely Automated Public Turing test to tell Computers and Humans Apart*</u>, is explicitly designed to prevent automation, so do not try! There are two primary strategies to get around[^6-5-1-1] CAPTCHA checks:

* Disable CAPTCHAs in your test environment
* Add a hook to allow tests to bypass the CAPTCHA

### [6-5-2 File downloads](https://www.selenium.dev/documentation/test_practices/discouraged/file_downloads/)

Whilst it is possible to start a download by clicking a link with a browser under Selenium's control, the API does not expose download progress, making it less than ideal for testing downloaded files. This is because downloading files is not considered an important aspect of emulating user interaction with the web platform. Instead, find the link using Selenium (and any required cookies) and pass it to a HTTP request library like [libcurl](https://curl.haxx.se/libcurl/).

The [HtmlUnit driver](https://github.com/SeleniumHQ/htmlunit-driver) can download attachments by accessing them as input streams by implementing the [AttachmentHandler](https://htmlunit.sourceforge.io/apidocs/com/gargoylesoftware/htmlunit/attachment/AttachmentHandler.html) interface. The AttachmentHandler can then be added to the [HtmlUnit](https://htmlunit.sourceforge.io/) WebClient.

### [6-5-3 HTTP response codes](https://www.selenium.dev/documentation/test_practices/discouraged/http_response_codes/)

For some browser configurations in Selenium RC, Selenium acted as a proxy between the browser and the site being automated. This meant that all browser traffic passed through Selenium could be captured or manipulated. The `captureNetworkTraffic()` method purported[^6-5-3-1] to capture all of the network traffic between the browser and the site being automated, including HTTP response codes.

Selenium WebDriver is a completely different approach to browser automation, preferring to act more like a user. This is represented in the way you write tests with WebDriver. In automated functional testing, checking the status code is not a particularly important detail of a test's failure; the steps that preceded[^6-5-3-2] it are more important.

The browser will always represent the HTTP status code, imagine for example a 404 or a 500 error page. A simple way to "fail fast" when you encounter one of these error pages is to check the page title or content of a reliable point (e.g. the `<h1>` tag) after every page load. If you are using the page object model, you can include this check in your class constructor or similar point where the page load is expected. Occasionally[^6-5-3-3], the HTTP code may even be represented in the browser's error page and you could use WebDriver to read this and improve your debugging output.

Checking the webpage itself is in line with[^6-5-3-4] WebDriver's ideal practice of representing and asserting upon the user's view of the website.

If you insist, an advanced solution to capturing HTTP status codes is to replicate the behavior of Selenium RC by using a proxy. WebDriver API provides the ability to set a proxy for the browser, and there are a number of proxies that will programmatically[^6-5-3-5] allow you to manipulate the contents of requests sent to and received from the web server. Using a proxy lets you decide how you want to respond to redirection response codes. Additionally, not every browser makes the response codes available to WebDriver, so opting[^6-5-3-6] to use a proxy allows you to have a solution that works for every browser.

### [6-5-4 Gmail, email and Facebook](https://www.selenium.dev/documentation/test_practices/discouraged/gmail_email_and_facebook_logins/)

For multiple reasons, logging into sites like Gmail and Facebook using WebDriver is not recommended. Aside from being against the usage terms for these sites (where you risk having the account shut down), it is slow and unreliable.

The ideal practice is to use the APIs that email providers offer, or in the case of Facebook the developer tools service which exposes an API for creating test accounts, friends and so forth. Although using an API might seem like a bit of extra hard work, you will be paid back in speed, reliability, and stability. The API is also unlikely to change, whereas webpages and HTML locators change often and require you to update your test framework.

Logging in to third party sites using WebDriver at any point of your test increases the risk of your test failing because it makes your test longer. A general rule of thumb is that longer tests are more fragile and unreliable.

WebDriver implementations that are [W3C conformant[^6-5-4-1]](https://w3c.github.io/webdriver/webdriver-spec.html) also annotate the `navigator` object with a `WebDriver` property so that Denial of Service[^6-5-4-2] attacks can be mitigated.

### [6-5-5 Test dependency](https://www.selenium.dev/documentation/test_practices/discouraged/test_dependency/)

A common idea and misconception[^6-5-5-1] about automated testing is regarding a specific test order. Your tests should be able to run in **any** order, and not rely on other tests to complete in order to be successful.

### [6-5-6 Performance testing](https://www.selenium.dev/documentation/test_practices/discouraged/performance_testing/)

Performance testing using Selenium and WebDriver is generally not advised. Not because it is incapable, but because it is not optimized for the job and you are unlikely to get good results.

It may seem ideal to performance test in the context of the user but a suite of WebDriver tests are subjected to many points of external and internal fragility[^6-5-6-1] which are beyond your control; for example browser startup speed, speed of HTTP servers, response of third party servers that host JavaScript or CSS, and the instrumentation[^6-5-6-2] penalty[^6-5-6-3] of the WebDriver implementation itself. Variation at these points will cause variation in your results. It is difficult to separate the difference between the performance of your website and the performance of external resources, and it is also hard to tell what the performance penalty is for using WebDriver in the browser, especially if you are injecting scripts.

The other potential attraction is "saving time" -- carrying out functional and performance tests at the same time. However, functional and performance tests have opposing objectives. To test functionality, a tester may need to be patient and wait for loading, but this will cloud the performance testing results and vice versa.

To improve the performance of your website, you will need to be able to analyze overall performance independent of environment differences, identify poor code practices, breakdown of performance of individual resources (i.e. CSS or JavaScript), in order to know what to improve. There are performance testing tools available that can do this job already, that provide reporting and analysis, and can even make improvement suggestions.

Example (open source) packages to use are: JMeter.

### [6-5-7 Link spidering](https://www.selenium.dev/documentation/test_practices/discouraged/link_spidering/)

Using WebDriver to spider[^6-5-7-1] through links is not recommended practice. Not because it cannot be done, but because WebDriver is definitely not the most ideal tool for this. WebDriver needs time to start up, and can take several seconds, up to a minute depending on how your test is written, just to get to the page and traverse through the DOM.

Instead of using WebDriver for this, you could save a ton of time by executing a [curl](https://curl.haxx.se/) command, or using a library such as BeautifulSoup since these methods do not rely on creating a browser and navigating to a page. You are saving tones of time by not using WebDriver for this task.

### [6-5-8 Two Factor Authentication](https://www.selenium.dev/documentation/test_practices/discouraged/two_factor_authentication/)

Two factor authentication (2FA) is an authorization mechanism where a One Time Password (OTP) is generated using "Authenticator" mobile apps such as "Google Authenticator", "Microsoft Authenticator" etc., or by SMS, email to authenticate. Automating this seamlessly[^6-5-8-1] and consistently is a big challenge in Selenium. There are some ways to automate this process. But that will be another layer on top of our Selenium tests and not as secure. So , you should avoid automating 2FA.

There are few options to get around 2FA checks:

* Disable 2FA for certain users in the test environment, so that you can use those user credentials in the automation.
* Disable 2FA in your test environment.
* Disable 2FA if you login from certain IPs. That way we can configure our test machine IPs to avoid this.

# 7 Legacy

不需要看

# 8 About






[^0-1]: something which covers or includes a wide range of different parts
[^0-2]: to do something or behave in the same way as someone else, especially because you admire them  SYN: imitate
[^0-3]: things that are interchangeable can be used instead of each other
[^0-4]: /ɪnˈθjuːziæst $ ɪnˈθuː-/
[^1]: vt. 预先布置; 事先调整; 预先决定; 事先安排
[^2]: v. 扩大，增大; 放大; 详细说明
[^3]: [ˈsnɪpɪt] n. 小片，片段; 不知天高地厚的年轻人
[^4]: ['speɪʃəlɪ] adv. 空间地，存在于空间地
[^5]: [ˈænsestər]
[^6]: vt. 使…模糊不清，掩盖; 隐藏; 使难理解 adj. 昏暗的，朦胧的; 晦涩的，不清楚的; 隐蔽的; 不著名的，无名的
[^7]: n. 键击，按键
[^8]: as the word is usually understood; in the exact sense of the word
[^9]: n. 样板文件; 公式化，陈词滥调
[^2-5-1]: /ˈjeɪɡə $ -gər/
[^2-7-1]: stopping and starting often over a period of time, but not regularly
[^2-7-2]: extremely important and needing to be done or dealt with immediately. SYN: urgent, essential, pressing, vital
[^2-7-3]: vt. (remedied, remedying, remedies) to deal with a problem or improve a bad situation. SYN: put right
[^2-7-4]: to use a particular object, method, skill etc in order to achieve something. *employ a method/technique/tactic etc*. In everyday English, people usually say **use** a method rather than **employ** a method.
[^2-7-5]: a punishment for breaking a law, rule, or legal agreement
[^2-7-6]: adj. 详尽的，彻底的 extremely thorough and complete
[^2-7-7]: conj. 在…期间; 与…同时; 然而; 尽管
[^18]: [ˈɡrænjələr] adj. 颗粒状的 consisting of granules
[^19]: *(computing)* an area inside a frame on a screen, for viewing information
[^2-9-0-1]: adj. 双向的 reactive or functioning or allowing movement in two usually opposite directions
[^2-9-0-2]: vt. 增补，补充  to add something, especially to what you earn or eat, in order to increase it to an acceptable level
[^2-9-0-3]: Customer data platform (CDP) definition. A customer data platform (CDP) is packaged software that creates a comprehensive customer database accessible by other systems to analyze, track, and manage customer interactions.
[^6-0-1]: adj. 沉思的; 体贴的; 缜密思考过的，深思熟虑的 3 well planned and carefully thought about
[^6-1-1]: v. 撒播; 散开; （使）分散 if someone scatters a lot of things, or if they scatter, they are thrown or dropped over a wide area in an irregular way
[^6-1-2]: n. 序; 绪言; （法令、文件等的）序文; 前言 a statement at the beginning of a book, document, or talk, explaining what it is about
[^6-2-1]: adj. 薄片的; 成片的; 薄而易剥落的; <美俚>极古怪的 *informal especially* <u>American English</u> a flaky person is slightly strange or often forgets things
[^6-2-2]: vt.使缓和，使减轻; 使平息 vi.减轻，缓和下来 to make a situation or the effects of something less unpleasant, harmful, or serious
[^6-2-3]: vt.围绕，包围; 包含或包括某事物; 完成 to include a wide range of ideas, subjects, etc
[^6-2-4]: n.程度; 大小; 范围 how large, important, or serious something is, especially something such as a problem or injury
[^6-2-5]: n.企业; 事业; 殡仪事业; 保证 an important job, piece of work, or activity that you are responsible for
[^6-2-6]: adj.宏伟的; 壮丽的; 不可一世的; 快乐的; 了不起的; 总括的; 大的 aiming or intended to achieve something impressive
[^6-2-7]: n. 错综复杂; （因复杂而产生的）难以理解; （常复数）错综复杂的事物 *the intricacies of something*: the complicated details of something
[^6-2-8]: n. 装饰，装饰品 something that you use to decorate something

[^6-2-9]: adj. 完整无缺的，未经触动的，未受损伤的; 原封不动的; 完好无缺; 完好无损 not broken, damaged, or spoiled
[^6-2-10]: v. 遵守，符合; 一致; 顺应（大多数人或社会）to obey a law, rule etc
[^6-2-11]: [ˌædvənˈteɪdʒəs] adj.有利的; 有好处的 helpful and likely to make you successful
[^6-3-1]: adv. 本身，本质上 used to say that something is being considered alone, not with other connected things
[^6-3-2]: [ˌkæpəˈberə] n.水豚（产于南美洲湖泊溪流间的啮齿动物）
[^6-4-1-1]: if someone scatters a lot of things, or if they scatter, they are thrown or dropped over a wide area in an irregular way
[^6-4-1-2]: [ˌɪntərˈtwaɪn] vt.缠结在一起; 使缠结 vi.纠缠; 编结 if two things intertwine, or if they are intertwined, they are twisted together
[^6-4-1-3]: n.杠杆作用; 优势，力量; 影响力 v.举债经营; 发挥杠杆作用; 施加影响; 利用 to get as much advantage or profit as possible from something that you have
[^6-4-2-1]: adj.绝缘的，隔热的 v.使绝缘; 使隔离; 使免除（不愉快的经历）; 使免受（不良影响）to keep someone apart from particular experiences or influences, especially unpleasant ones
[^6-4-2-2]: /wet/ vt.（在石头上）磨（刀、斧等）; 引起，刺激（食欲、欲望、兴趣等）whet somebody’s appetite (for something);*literary* to make the edge of a blade sharp
[^6-4-2-3]: [ˈbrɛvɪti] n.短暂; 简洁 the quality of expressing something in very few words
[^6-4-2-4]: to bravely accept or deal with a painful, difficult, or upsetting situation SYN stand
[^6-4-3-1]: [ rɪˈpetətɪv] done many times in the same way, and boring
[^6-4-3-2]: [stəˈbɪləti]
[^6-4-3-3]: **AUT**: Application under test
[^6-4-6-1]: adj.陈腐的; 不新鲜的; 走了味的 bread or cake that is stale is no longer fresh or good to eat **OPP** fresh
[^6-4-7-1]: vt.摒弃; 摒绝; 放弃; 在......之前 to not do or have something pleasant or enjoyable **SYN** go without
[^6-4-8-1]: adj.可行的; 做得到的 a plan, idea, or method that is feasible is possible and is likely to work **SYN** possible
[^6-4-8-2]: n.树桩; 铅笔头，烟蒂; 票根，存根 the short part of something long and thin, such as a cigarette or pencil, that is left when the rest has been used
[^6-4-9-1]: v.创造（新词语）; 很快地赚（钱）to invent a new word or expression, especially one that many people start to use
[^6-4-10-1]: v.使旋转; 急转弯; 疾驰; 甩干衣服; 有倾向性陈述; 纺纱; 吐丝 to turn around and around very quickly, or to make something do this
[^6-5-1-1]: 传播; 绕开; 随意走走; 说服 **get around something** to avoid something that is difficult or causes problems for you
[^6-5-3-1]: vt.声称; 意图; 意味着; 打算 n.意义，要旨; 目的，意图 *formal* to claim to be or do something, even if this is not true
[^6-5-3-2]: vt.& vi.在…之前发生或出现，先于; 在…之上，优于; 给…作序; 处于…前面的位置 to happen or exist before something or someone, or to come before something else in a series
[^6-5-3-3]: adv.偶尔; 偶然; 有时候 sometimes, but not regularly and not often. *In everyday English, people often say **once in a while** rather than **occasionally***
[^6-5-3-4]: 跟…一致，符合; 本着 if something changes in line with something else, it changes in the same way and at the same rate as it
[^6-5-3-5]: 以编程方式
[^6-5-3-6]: vi.选择，挑选 to choose one thing or do one thing instead of another
[^6-5-4-1]: n.顺应，一致 to behave in the way that most other people in your group or society behave
[^6-5-4-2]: Denial of Service (DoS) 拒绝服务攻击. 分布式拒绝服务攻击（ 英文: Distributed Denial of Service，缩写：DDoS ）亦称洪水攻击。 顾名思义，即是利用网络上已被攻陷的电脑作为“僵尸 ”，向某一特定的目标电脑发动密集式的“拒绝服务”式攻击，用以把目标电脑的网络资源及系统资源耗尽，使之无法向真正正常请求的用户提供服务。黑客通过将一个个“丧尸”或者称为“肉鸡”组成僵尸网络 ，就可以发动大规模DDoS或SYN洪水网络攻击，或者将“丧尸”们组到一起进行带有利益的刷网站流量、Email垃圾邮件群发，瘫痪预定目标受雇攻击竞争对手等商业活动。A denial-of-service (DoS) attack is a cyberattack on devices, information systems, or other network resources that prevents legitimate users from accessing expected services and resources. This is usually accomplished by flooding the targeted host or network with traffic until the target can't respond or crashes.
[^6-5-5-1]: n.误解; 错觉; 错误想法 an idea which is wrong or untrue, but which people believe because they do not understand the subject properly
[^6-5-6-1]: [frə'dʒɪlətɪ] n.脆弱，虚弱; 易碎性; 脆性; 脆弱性
[^6-5-6-2]: n.使用仪器，装设仪器; 乐器法; 乐曲研究; 手段 the set of instruments used to help in controlling a machine
[^6-5-6-3]: n.惩罚; 刑罚; 害处; 足球点球 a punishment for breaking a law, rule, or legal agreement
[^6-5-7-1]: *technical* a computer program that searches the Internet for the best websites with the information you want, so that you can find it quickly **SYN**: crawler, bot
[^6-5-8-1]: done or made so smoothly that you cannot tell where one thing stops and another begins