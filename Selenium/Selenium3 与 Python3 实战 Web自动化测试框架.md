### 第2章 环境搭建



邮箱		正确得到邮箱格式		错误给出提示

用户名	 18个英文或者9个汉字

密码		5到20位英文/数字/符号/区分大小写

验证码

---

expected_conditions 源码分析

#### 2-10 输入注册用户名字及获取用户信息

```python
print(email_element.get_attribute("value"))
```

#### 2-11 如何生成用户名

如何生成用户名

```python
import random

user_email = random.sample('1234567890abcdefg', 5)  # 输出结果是一个list
# 所以要再次修改为
user_email = ''.join(random.sample('1234567890abcdefg', 5))+"@163.com"
```

#### 2-12 如何解决验证码思路

然后把这个图标的坐标计算下来.

```python
driver.save_screenshot("E:/imooc.png")
code_element = driver.find_element_by_id("getcode_num")
code_element.location
left = code_element.location['x']
top = code_element.location['y']


pip install Pillow

im = Image.open("E:/imooc.png")
img = im.crop((left, top, right, height))
img.sage("E:/imooc1.png")
```

然后通过第三方库直接把它裁剪下来

#### 2-14 使用pytessseract 识别图片中的问题

如何去把图片里的文字来读取

`pip install pytesseract`

创建一个新的文件`read_image.py`

```python
import pytesseract
from PIL import Image

image = Image.open("E:/imooc1.png")
text = pytesseract.image_to_string(image)
print(text)
```

#### 2-15 showapiRequest 解决图片验证码识别

 ```python
from ShowapiRequest import ShowapiRequest

r = ShowapiRequest("http://route.showapi.com/184-4")
r.addBodyPara("typeId", 35)
r.addBodyPara("convert_to_jpg", "0")
r.addFilePara("image", r"E:/imooc1.png")
res = r.post()
text = res.json()["showapi_res_body"]["Result"]
print(text)
 ```

#### 2-16 注册输入验证码流程整合

整合进`start_browser.py`



#### 2-17 注册流程梳理及代码封装

创建文件`register_code.py`

```python
from selenium import webdriver
from PIL import Image
from Showapi


# 获取图片
def get_code_image():
    driver.save_screenshot(file_name)
    code_element = driver.find_element_by_id("getcode_num")
    
    
# 解析图片获取验证码
def code_online(file_name):
    r = Show
    
    
# 运行主程序
def run_main():
    user_name_info = get_range_user()
    user_email = get_range_user() + "@163.com"
    driver_init()
    get_element("register_email").send_keys(user_email)
    get_element("register_nickname").send_keys(user_name)
    get_element("register_password").send_keys()
    
```

#### 2-18 以配置文件形式实现定位设计思想

创建新文件`register_function.py`

以配置文件的信息存储

再创建一个文件夹:`config`,用来放置配置文件

创建一个`LocalElement.ini`

```ini
[RegisterElement]
user_email=id>register_email
user_name=id>register_nickname
password=id>register_password
code_image=id>getcode_num
code_text=id>captcha_code
```

#### 2-19 如何读取配置文件low代码

```shell
pip install configparser
```

创建`read_ini.py`

```python
import configparser


cf = configparser.ConfigParser()
cf.read("e:/Teacher/Imooc/SeleniumPython/Imooc_selenium/config/LocalElement.ini")
cf.get('RegisterElement', 'user_email' )
```

#### 2-20 重构封装读取配置文件方法

```python
import configparser


class ReadIni:
  
  	def __init__(self, file_name=None, node=None):
      	if file_name == None:
          	file_name = "e:/Teacher/Imooc/SeleniumPython/config/LocalElement.ini"
        if node == None:
            self.node = 'RegisterElement'
        else:
            self.node = node
        self.cf = self.load_ini(file_name)
        
    def load_ini(self, file_name):
        cf = configparser.ConfigParser()
				cf.read(file_name)
        return cf
      
    def get_value(self):
        self.cf.get(self.node, )
```

#### 2-22 如何将整个注册流程脚本进行模块化实战讲解

```python
from se


class RegistetFunction:
    def get_driver(self, url):
        driver = webdriver.Chrome()
        driver.get(url)
```

#### 2-23 注册失败进行截图处理

有“验证码错误”几个字

放到`localElement.ini`里面

#### 2-24 多浏览器跑case

```python
for i in range(3):
    
```

### 第3章 项目实战中PO模型的设计与封装

#### 3-1 po模型设计思想

#### 3-2 po模型如何设计操作层

```python
class RegisterBusiness:
    # 执行操作
    def 
```

#### 3-3 po模型设计之如何设计po及模块串联设计讲解

```python

```



第8章

根据当前的时间自动创建文件

```python
import datetime

# 文件名字
base_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = os.path.join(base_dir, 'logs')
log_file = datetime.datetime.now().strftime("")+".log"
log_name = log_dir + '/' + log_file


logging.FileHandler(log_name, 'a', encoding='utf-8')
```



```python
class Userlog:
  	
    def __init__(self)
```





```
8001
```



























































