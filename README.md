# PHJF Alpha v0.1.5
* 简单易懂的爬虫
* 使用python将html转化成json并部署到服务器
-----------------
**>>注意<<**: 如果想使用本库的全部内容，请至少达到能知道大多数Python3基础知识并且知道BeautifulSoup的基本用法和爬虫的概念和Flask库的基本知识

*立志于用最简单的工作*
***
 **为什么选择PHJF？**  
 * *简单* 
 * *轻便*
 * *超强的可塑性*
 * *一键部署*
 
 

 **实现的功能**  
 + 模块化
 + 算是debug
 + 保存为json并且格式化
 + 键部署到本地服务器

**未实现的功能**
+ 部署到真正意义上的互联网服务器
+ 爬虫未响应自动结束程序
+ 部署到服务器时进行格式化
 
 ---

## __迅速开始__

**注意：所依赖的第三方库**
* BeautifulSoup
* Flask
***
## 快速入门
### **最简单的项目**  
**打开``PHJF/main.py``**
 ### **get_page(url, encoding, 工作模式)**
 获取页面，拥有三种工作模式
 * *url* : 输入您所需要爬虫的网页 
 * *encoding* : 编码格式，默认为 utf-8  
 * **工作模式** : 见下文

**工作模式的选择**
* *let* : 对接页面数据，解析时使用
* *save* : 保存页面到当前目录

### 玩法实例
**爬取``baidu.com``的数据并保存**
```python3
from data import *

def main():
  get_page("https://baidu.com", "", "save")

if __name__ == "__main__"
  main()
```
### run_compile_page(工作模式, 文件名字)
**工作模式**
* *json* : 保存页面到当前目录
* *data* : 为运行本地服务器对接数据

**文件名字**
* 为你的本地服务器设置目录名称与保存文件时的名称

### run_server()
* 启动本地服务器
## **进阶玩法**
```python3
from data import *


def main():
    get_page("https://www.3dmgame.com/news/game/", "", "let")
    run_compile_page("data", "GameNews")
    run_server()


if __name__ == "__main__":
    main()
```
## **打开``data.py``**  
### 编辑``compile_data()``函数来定制你的工作需要


***
**常见问题**
* Q:爬虫爬不动了  
  A:重新启动程序
***
*来自 邱璇洛 2022 ©*️