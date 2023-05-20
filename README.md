# ***金太阳考试服务云平台成绩爬虫**

## 环境配置

1.安装Python 3.7+

2.使用pip为你的Python安装selenium模块(用于自动化执行web操作)

```
pip install selenium
```

3.安装浏览器驱动，驱动版本尽量与你的浏览器版本号一致

```
各浏览器驱动下载地址
Chrome:
https://chromedriver.chromium.org/downloads

Edge:
https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

Firefox:
https://github.com/mozilla/geckodriver/releases

Safari:
https://webkit.org/blog/6900/webdriver-support-in-safari-10/
```

## 修改代码

因为本程序默认使用Edge浏览器，如果需要修改浏览器，请将msedgedriver.exe替换为想要使用的浏览器驱动，并修改main.py中的

```python
options = webdriver.浏览器名Options()
```

```python
wd = webdriver.浏览器名(service=Service('驱动程序名.exe'), options=options)
```

## 考号获取

你可以在你的浏览器中输入一段url，获取想要获取的学校学生考号(仅限21届学生)，例如:

```
https:/alipic.onlyets.cn/pic2t/jty/ScoreFile/1821/0/省/河北/市/保定市/县/涿州市/校/物探一分校/物理_原始分_物探一分校xlsx
```

如果不行，可以尝试更换学校名称或科目，后续我也会尝试获取其他年级的考号

## 导入考号

将获取到的考号粘贴到student_numbers.txt中，一个考号占一行

## 运行

准备工作完成后执行main.py即可，程序默认输出SQL语句，如果需要以其他格式输出，可自行在main.py中修改