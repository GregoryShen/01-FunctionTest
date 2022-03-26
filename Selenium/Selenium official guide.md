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

## [Overview](https://www.selenium.dev/documentation/overview/)

Is Selenium for you? See an overview of the different project components.

Selenium is not just one tool or API but it composes many tools.

**WebDriver**

If you are beginning with desktop website or mobile website test automation, then you are going to be using WebDriver APIs. WebDriver uses browser automation APIs provided by browser vendors to control browser and run tests. This is as if a real user is operating the browser. Since WebDriver does not require its API to be compiled with application code, it is not intrusive. Hence, you are testing the same application which you push live.

**IDE**

IDE is the tool you use to develop your Selenium test cases. It's an easy-to-use Chrome and Firefox extension and is generally the most efficient way to develop test cases. It records the user's actions in the browser for you, using existing Selenium commands, with parameters defined by the context of that element. This is not only a time-saver but also an excellent way of learning Selenium script syntax.

**Grid**

Selenium Grid allows you to run test cases in different machines across different platforms. The control of triggering the test cases is on the local end, and when the test cases are triggered, they are automatically executed by the remote end.

After the development of the WebDriver tests, you may face the need of running your tests on multiple browser and operating system combinations. This is where Grid comes into the picture.

### Components

Building a test suite using WebDriver will require you to understand and effectively use a number of different components. As with everything in software, different people use different terms for the same idea. Below is a breakdown of how terms are used in this description.

#### Terminology

* **API**: Application Programming Interface. This is the set of "commands" you use to manipulate WebDriver.
* **Library**: A code module which contains the APIs and the code necessary to implement them. Libraries are specific to each language binding, eg .jar files for Java, .dll files for .NET, etc.
* **Driver**: Responsible for controlling the actual browser. Most drivers are created by the browser vendors themselves. Drivers are generally executable modules that run on the system with the browser itself, not on the system executing the test suite.(Although those may be the same system.) NOTE: *Some people refer to the drivers as proxies*.
* **Framework**: An additional library used as a support for WebDriver suites. These frameworks may be test frameworks such as JUnit or NUnit. They may also be frameworks supporting natural language features such as Cucumber or Robotium. Frameworks may also be written and used for things such as manipulating or configuring the system under test, data creation, test oracles, etc.

#### The Parts and Pieces

At its minimum, WebDriver talks to a browser through a driver. Communication is two way: WebDriver passes commands to the browser through the driver, and receives information back via the same route.

![](https://www.selenium.dev/images/documentation/webdriver/basic_comms.png)

The driver is specific to the browser, such as ChromeDriver for Google's Chrome/Chromium, GeckoDriver for Mozilla's Firefox, etc. The driver runs on the same system as the browser. This may, or may not be, the same system where the tests themselves are executing.

This simple example above is *direct* communication. Communication to the browser may also be *remote* communication through Selenium Server or RemoteWebDriver. RemoteWebDriver runs on the same system as the driver and the browser.

![](https://www.selenium.dev/images/documentation/webdriver/remote_comms.png)

Remote communication can also take place using Selenium Server or Selenium Grid, both of which in turn talk to the driver on the host system.

![](https://www.selenium.dev/images/documentation/webdriver/remote_comms_server.png)

#### Where Frameworks fit in

WebDriver has one job and one job only: communicate with the browser via any of the methods above. WebDriver does not know a thing about testing: it does not know how to compare things, assert pass or fail, and it certainly does not know a thing about reporting or Given/When/Then grammer.

This is where various frameworks come in to play. At a minimum you will need a test framework that matches the language binding, e.g. NUnit for .NET, JUnit for Java, Rspec for Ruby, etc.

The test framework is responsible for running and executing your WebDriver and related steps in your tests. As such, you can think of it looking akin to the following image.

![](https://www.selenium.dev/images/documentation/webdriver/test_framework.png)

Natural language framework/tools such as Cucumber may exist as part of that Test Framework box in the figure above, or they may wrap the Test Framework entirely in their own implementation.

### [Details](https://www.selenium.dev/documentation/overview/details/)

**A deeper look at Selenium**

Selenium is an umbrella project for a range of tools and libraries that enable and support the automation of web browsers.

#### Selenium controls web browsers

Selenium is many things but at its core, it is a toolset for web browser automation that uses the best techniques available to remotely control browser instances and emulate a user's interaction with the browser.

It allows users to simulate common activities performed by end-users; entering text into fields, selecting drop-down values and checking boxes, and clicking links in documents. It also provides many other controls such as mouse movement, arbitrary JavaScript execution, and much more.

Although used primarily for front-end testing of websites, Selenium is at its core a browser user agent library. The interfaces are ubiquitous to their application, which encourages composition with other libraries to suit your purpose.

#### One interface to rule them all

One of the project's guiding principles is to support a common interface for all(major) browser technologies. Web browsers are incredibly complex, highly engineered applications, performing their operations in completely different ways but which frequently look the same while doing so. Even though the text is rendered in the same fonts, the images are displayed in the same place and the links take you to the same destination. What is happening underneath is as different as night and day. Selenium "abstracts" these differences, hiding their details and intricacies from the person writing the code. This allows you to write several lines of code to perform a complicated workflow, but these same lines will execute on Firefox, Internet Explorer, Chrome, and all other supported browsers.

#### Tools and support

Selenium's minimalist design approach gives it the versatility to be included as a component in bigger applications. The surrounding infrastructure provides under the Selenium umbrella gives you the tools to put together your grid of browsers so tests can be run on different browsers and multiple operating systems across a range of machines.

Imagine a bank of computers in your server room or data center all firing up browsers at the same time hitting your site's links, forms, and tables -- testing your application 24 hours a day. Through the simple programming interface provides for the most common languages, these tests will run tirelessly in parallel, reporting back to you when errors occur.

It is an aim to help make this a reality for you, by providing users with tools and documentation to not only control browsers but to make it easy to scale and deploy such grids.

#### Who uses Selenium

Many of the most important companies in the world have adopted Selenium for their browser-based testing, often replacing years-long efforts involving other proprietary tools. As it has grown in popularity, so have its requirements and challenges multiplied.

As the web becomes more complicated and new technologies are added to websites, it's the mission of this project to keep up with them where possible. Being an open source project, this support is provided through the generous donation of time from many volunteers, every one of which has a "day job".

Another mission of the project is to encourage more volunteers to partake in this effort, and build a strong community so that the project can continue to keep up with emerging technologies and remain a dominant platform for functional test automation.

## [WebDriver](https://www.selenium.dev/documentation/webdriver/)

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

### [Get Started](https://www.selenium.dev/documentation/webdriver/getting_started/)

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

   

##### Advanced Configuration



#### Open Browser

#### First Script

#### Upgrade to Selenium 4



### [Capabilities](https://www.selenium.dev/documentation/webdriver/capabilities/)

Shared

Chromium

Firefox

Internet Explorer

Safari





### Browser

### Elements

### Remote WebDriver

### Drivers

### Waits

### Actions API

### BiDirectional

### Additional Features

## Grid

暂时不需要看

## IE Driver Server

不需要看

## IDE

不需要看

## Test Practices

### Design Strategies

### Overview

### Testing Types

### Encouraged

### Discouraged

## Legacy

不需要看

## About

