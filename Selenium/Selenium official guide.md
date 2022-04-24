# [The Selenium Browser Automation Project](https://www.selenium.dev/documentation/)

Selenium is an umbrella project for a range of tools and libraries that enable and support the automation of web browsers.

It provides extensions to emulate user interaction with browsers, a distribution server for scaling browser allocation, and the infrastructure for implementations of the W3C WebDriver specification that lets you write interchangeable code for all major web browsers.

This project is made possible by volunteer contributors who have put in thousands of hours of their own time, and made the source code freely available for anyone to use, enjoy, and improve.

Selenium brings together browser vendors, engineers, and enthusiasts to further an open discussion around automation of the web platform. The project organizes an annual conference to teach and nurture the community.

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

# [Overview](https://www.selenium.dev/documentation/overview/)

Is Selenium for you? See an overview of the different project components.

Selenium is not just one tool or API but it composes many tools.

**WebDriver**

If you are beginning with desktop website or mobile website test automation, then you are going to be using WebDriver APIs. WebDriver uses browser automation APIs provided by browser vendors to control browser and run tests. This is as if a real user is operating the browser. Since WebDriver does not require its API to be compiled with application code, it is not intrusive. Hence, you are testing the same application which you push live.

**IDE**

IDE is the tool you use to develop your Selenium test cases. It's an easy-to-use Chrome and Firefox extension and is generally the most efficient way to develop test cases. It records the user's actions in the browser for you, using existing Selenium commands, with parameters defined by the context of that element. This is not only a time-saver but also an excellent way of learning Selenium script syntax.

**Grid**

Selenium Grid allows you to run test cases in different machines across different platforms. The control of triggering the test cases is on the local end, and when the test cases are triggered, they are automatically executed by the remote end.

After the development of the WebDriver tests, you may face the need of running your tests on multiple browser and operating system combinations. This is where Grid comes into the picture.

## [Components](https://www.selenium.dev/documentation/overview/components/)

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

WebDriver has one job and one job only: communicate with the browser via any of the methods above. WebDriver does not know a thing about testing: it does not know how to compare things, assert pass or fail, and it certainly does not know a thing about reporting or Given/When/Then grammer.

This is where various frameworks come in to play. At a minimum you will need a test framework that matches the language binding, e.g. NUnit for .NET, JUnit for Java, Rspec for Ruby, etc.

The test framework is responsible for running and executing your WebDriver and related steps in your tests. As such, you can think of it looking akin to the following image.

![](https://www.selenium.dev/images/documentation/webdriver/test_framework.png)

Natural language framework/tools such as Cucumber may exist as part of that Test Framework box in the figure above, or they may wrap the Test Framework entirely in their own implementation.

## [Details](https://www.selenium.dev/documentation/overview/details/)

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

# [WebDriver](https://www.selenium.dev/documentation/webdriver/)

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

## [Get Started](https://www.selenium.dev/documentation/webdriver/getting_started/)

If you are new to Selenium, we have a few resources that can help you get up to speed right away.

Selenium supports automation of all the major browsers in the market through the use of WebDriver. WebDriver is an API and protocol that defines a language-neutral interface for controlling the behavior of web browsers. Each browser is backed by a specific WebDriver implementation, called a driver. The driver is the component responsible for delegating down to the browser, and handles communication to and from Selenium and the browser.

This separation is part of a conscious effort to have browser vendors take responsibility for the implementation for their browsers. Selenium makes use of these third party drivers where possible, but also provides its own drivers maintained by the project for the cases when this is not a reality.

The Selenium framework ties all of these pieces together through a user-facing interface that enables the different browser backends to be used transparently, enabling cross-browser and cross-platform automation.

Selenium setup is quite different from the setup of other commercial tools. Before you can stat writing Selenium code, you have to install the language bindings libraries for your language of choice, the browser you want to use, and the driver for that browser.

#### Install Library

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

#### Install Drivers

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

#### Open Browser

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

#### First Script

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

#### [Upgrade to Selenium 4](https://www.selenium.dev/documentation/webdriver/getting_started/upgrade_to_selenium_4/)

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

## [Capabilities](https://www.selenium.dev/documentation/webdriver/capabilities/)

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

### [Shared](https://www.selenium.dev/documentation/webdriver/capabilities/shared/)

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


### [Chromium](https://www.selenium.dev/documentation/webdriver/capabilities/chromium/)

These Capabilities are specific to Chromium based browsers.

These Capabilities apply to:

* Chrome
* Chromium
* Edge

### [Firefox](https://www.selenium.dev/documentation/webdriver/capabilities/firefox/)

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

### [Internet Explorer](https://www.selenium.dev/documentation/webdriver/capabilities/internet_explorer/)

暂略

### [Safari](https://www.selenium.dev/documentation/webdriver/capabilities/safari/)

These capabilities are specific to Safari.

## [Browser](https://www.selenium.dev/documentation/webdriver/browser/)

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

First of all, you need to be on the domain that the cookie will be valid for. If you are trying to preset[^ 1] cookies before you start interacting with a site and your homepage is large/takes a while to load an alternative is to find a smaller page on the site (typically the 404 page is small, e.g. http://example.com/some404page)

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

**<u>Python</u>**

```python
```

**<u>CSharp</u>**

```c#
```

##### Switching windows or tabs

**<u>Python</u>**

```python
```

**<u>CSharp</u>**

```c#
```

##### Create new window (or) new tab and switch

**<u>Python</u>**

```python
```

**<u>CSharp</u>**

```c#
```

##### Closing a window or tab

**<u>Python</u>**

```python
```

**<u>CSharp</u>**

```c#
```

##### Quitting the browser at the end of a session

**<u>Python</u>**

```python
```

**<u>CSharp</u>**

```c#
```

#### Window management

##### Get window size

**<u>Python</u>**

```python
```

**<u>CSharp</u>**

```c#
```

##### Set window size

**<u>Python</u>**

```python
```

**<u>CSharp</u>**

```c#
```

##### Get window position

**<u>Python</u>**

```python
```

**<u>CSharp</u>**

```c#
```

#### Set window position

**<u>Python</u>**

```python
```

**<u>CSharp</u>**

```c#
```

##### Maximize window

**<u>Python</u>**

```python
```

**<u>CSharp</u>**

```c#
```

##### Minimize window

**<u>Python</u>**

```python
```

**<u>CSharp</u>**

```c#
```

##### Fullscreen window

**<u>Python</u>**

```python
```

**<u>CSharp</u>**

```c#
```

##### TakeScreenshot

**<u>Python</u>**

```python
```

**<u>CSharp</u>**

```c#
```

##### TakeElementScreenshot

**<u>Python</u>**

```python
```

**<u>CSharp</u>**

```c#
```

##### Execute Script

**<u>Python</u>**

```python
```

**<u>CSharp</u>**

```c#
```

##### Print Page

**<u>Python</u>**

```python
```

**<u>CSharp</u>**

```c#
```

## [Elements](https://www.selenium.dev/documentation/webdriver/elements/)

[Locators](https://www.selenium.dev/documentation/webdriver/elements/locators/)

Finders

Interactions

Information

Select Lists

## [Remote WebDriver](https://www.selenium.dev/documentation/webdriver/remote_webdriver/)



## [Drivers](https://www.selenium.dev/documentation/webdriver/drivers/)



## [Waits](https://www.selenium.dev/documentation/webdriver/waits/)



## [Actions API](https://www.selenium.dev/documentation/webdriver/actions_api/)

Keyboard

Mouse

Wheel

## [BiDirectional](https://www.selenium.dev/documentation/webdriver/bidirectional/)

BiDi API

Chrome DevTools

## [Additional Features](https://www.selenium.dev/documentation/webdriver/additional_features/)

colors

ThreadGuard

# Grid

暂时不需要看

# IE Driver Server

不需要看

# IDE

不需要看

# [Test Practices](https://www.selenium.dev/documentation/test_practices/)

## Design Strategies

## Overview

## Testing Types

## Encouraged

## Discouraged

# Legacy

不需要看

# About



[^ 1]: vt. 预先布置; 事先调整; 预先决定; 事先安排

