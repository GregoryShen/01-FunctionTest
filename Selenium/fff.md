#### findElement(By by)

* ##### 通过id获取到元素

```javascript
WDS.browser.findElement(pkg.By.id('页面中元素的id'));
```

比如通过id获取登陆页面用户输入框，赋值给变量username

```javascript
var useranme = WDS.browser.findElement(pkg.By.id('j_username'));
```

之后操作username就会对用户名输入框进行操作

通过id获取登陆按钮，存到loginBtn中

```javascript
var loginBtn = WDS.browser.findElement(pkg.By.id('btnOk'));
```

* ##### 通过类名获取元素

```javascript
WDS.browser.findElement(pkg.By.className('kbs-logo-title'));
```

但可能不唯一，容易出现问题

* ##### 通过css选择器获取元素


```javascript
WDS.browser.findElement(pkg.By.cssSelector('div.right.dspib'));
```

* ##### 通过xpath获取元素

```javascript
WDS.browser.findElement(pkg.By.xpath("//div[@id='kbs-tab-menu']/a[@class='kbs-tab-menu-clear']"));
```

通过路径找到页面元素

比如通过div的id是test的话，表示如下：//div[@id='test']/p

多个属性可以在[ ]中用and隔开，或者用多个[ ]

父元素和子元素的应用

//div[@id='test']/parent::* 或者//div[@id='test']/..

元素包含文本时可以用//input['归属地']

如果不能获取到，尝试 [.='文本']

* ##### 通过partialLinkText获取元素

如果某个链接包含文字“文章同步”，要获取这个链接时可用

```javascript
WDS.browser.findElement(pkg.By.partialLinkText('文章同步'));
```

* ##### 通过xpath获取元素

```javascript
WDS.browser.findElement(pkg.By.xpath("//div[@id='kbs-tab-menu']/a[@class='kbs-tab-menu-clear']"));
```

#### 鼠标点击

有时候可能会遇到即使使用wait（等待元素加载或显示等）等待元素显示之后，进行点击（click或其他操作）也无法点击到元素的情形，可能是因为上层有元素（蒙版）从可见变为不可见需要时间，可以用暂停线程的方法，等待它消失后再点击

#### 输入文本

在输入框里输入文本时候使用：元素.sendKeys('[要输入的文本]');

比如获取到一个id是btnSearchCon的文本框

```javascript
var keyword = WDS.browser.findElement(pkg.By.id('btnSearchCon'));
```

在文本框中输入文本"文章同步"

```javascript
keyword.sendKeys(['文章同步']);
```

也可以不定义变量直接写

#### 切换框架

如果页面上包含iframe，可能在获取元素的时候出现获取不到的情况，需要使用switchTo()切换到iframe中，之后才能用上述的方法获取到元素并进行操作

##### frame

切换到一个iframe的方法是

```javascript
WDS.browser.switchTo().frame('iframe的id');
```

切换框架后，可以获取到这个iframe中的元素并进行操作。之后如果需要操作最外层或其他iframe的元素，需要先使用

##### defaultContent

切换到最外层，包括第一个iframe

```javascript
WDS.browser.switchTo().defaultContent();
```

#### 动态页面问题

定义一个变量

```javascript
var wait = new pkg.WebDriverWait(WDS.browser, 10);
```

之后用wait.until(某个条件)，直到某个条件出现，才执行下一步

```javascript
wait.until(pkg.ExpectedConditions.presenceOfElementLocated(pkg.By.id('kbsTabName')));
```

##### presenceOfElementLocated

用click()点击了登陆按钮，可以等待页面上出现登陆后才出现的某个元素，再进行下一步操作，

```javascript
var wait = new pkg.WebDriverWait(WDS.browser,10);
wait.until(pkg.ExpectedConditions.presenceOfElementLocated(pkg.By.id('kbsTabName')));
```

##### visibilityOfElementLocated

```javascript
var wait = new pkg.WebDriverWait(WDS.broswer,10);
wait.unti(pkg.ExpectedConditions.visibilityOfElementsLocated(pkg.By.id('navLogout')));
```

##### frameToBeAvailableAndSwitchTolt

页面上本来没有的iframe变得可用时，可用

```javascript
var wait = new pkg.WebDriverWait(WDS.browser, 10);
wait.until(pkg.ExpectedCondtions.frameToBeAvailableAndSwitchToIt('SearchResultPanel'));
```

```javascript
var wait2 = new pkg.WebDriverWait(WDS.driver,10);
wait2.until(pkg.ExpectedConditions.visibilityOfElementLocated(pkg.By.partialLinkText('文章同步')));
```

#### 鼠标悬停

定义一个动作

```javascript
var actions = new pkg.Actions(WDS.browser);
```

移动到某个元素（移动到这个元素的中心时），如下

```javascript
actions.moveToElement(元素).build().perform();
```

#### 鼠标右键

方法为：

```javascript
contextClick(元素)
```

获取id为  AdvSearchResult的元素

```javascript
var advSearchTab = WDS.browser.findElement(pkg.By.id('advSearchResult'));
```

定义一个变量 actions

```javascript
var actions = new org.openqa.selenium.interactions.Actions(WDS.browser);
```

对这个元素进行右键点击

```javascript
actions.contextClick(advSearchTab).build().perform();
```

#### 断言

```javascript
// 设置一个webdriver sampler在结果树中显示为断言成功用
WDS.sampleResult.setSuccessful(true);
WDS.sampleResult.successful = true;
// 类似的，要其断言失败时用
WDS.sampleResult.setSuccessful(false);
WDS.sampleResult.successful = false;
// 同时可以用（也可以不设置）
WDS.sampleResult.responseMessage = "消息内容"; 
WDS.sampleResult.setResponseMessage('消息内容');
```

jmeter变量

```javascript
WDS.vars.get("jmeter变量名");
WDS.vars.put('jmeter变量名', 脚本中的变量);
```

#### 响应时间

在需要开始计时的操作前添加WDS.sampleResult.sampleStart();

在需要计时结束的操作后添加WDS.sampleResult.sampleEnd();





























