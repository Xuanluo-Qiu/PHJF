# PHJF Alpha v0.1.2
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

**>>注意<<：所依赖的第三方库**
* BeautifulSoup
* Flask  
* lxml

**请记得安装这些库，直接pip3下载即可**
***
**正如你所见到的**,当你下载下来打开包时就会发现，它看起来不像是一个“正常的”库，你甚至可以直接复制粘贴
到自己的项目里，事实上，这也是我想见到的，您可以随意添加，修改，来进行属于你的定制。
## 我提供了一个实例，``example``文件夹就是实例。希望它能帮助你更好地了解这个库
### **实例** 得到并解析[3DM的游戏新闻](https://www.3dmgame.com/news/game/)的标题，时间，正文和简文保存为json后挂载到本地服务器

**
***

### Data.py和Main.py
**打开** *main.py*
打开后，你会看到两个函数，一个是 ``get_page() ``
另一个则是被注释掉的 ``run_compile_page()``

**关于``get_page()``**
我们先说第一个，``get_page()`` 为您提供了基础的爬虫需要，和不同的工作环境(也就是说，如果您的某个项目里需要这个，你可以直接复制粘贴)
``get_page()`` 您只需要以 *网页链接*，*编码格式*，*工作环境* 三个分别填入即可，如果您想以默认编码（*utf-8*）来使用的话，直接填``""``即可

**工作环境的调配**
我提供了三个工作环境，能覆盖大多数时候的应用，分别是
* ``let``--当你将工作环境设为 *let* 时，将会加载一个对接数据，用来对接``run_compile_page()``
* ``save`` --将会保存抓取的网页数据,一路无需修改代码
* ``""`` --或者是任何什么不是上面两个的数据，它将会返回爬取的数据

**实例**
比如我想要得到百度的网站数据并且保存就可以这么写

```python3
from data import *


def main():
  get_page("https://www.baidu.com", "", "save")


if __name__ == "__main__":
  main()
```

**关于 ``run_compile_page()``**，``run_compile_page()``是一个启动函数，也算是一个Debug，当您的工作模式选为``"let"``时 ，它将会对接您获取的数据然后对接到``compile_page()``
进行解析，如果你选错了模式或者出现了什么奇怪的，我还不知道的bug，它会告诉你没有找到数据，这时候请查看您的工作环境是否选择正确

**关于 ``compile_page()``** 打开``data.py``您会在``run_compile_page()``的下面发现这个函数，
顾名思义，它的作用就是解析您获取的``HTMl``，它有两种工作环境，一种是``txt``模式，将会在`templates`内创建文件，还有一种是`json`模式，会把格式化后的json文件存储在``data``文件夹，(**⚠️注意：如果您想要测试新的连接，请删除原有的，您已经得到的文件，不然的话新的数据只会被写入，旧数据不会被覆盖**) ️您也可以编辑它来达到您需要的目的（简称我很菜），内置的可以解析[3DM的游戏新闻](https://www.3dmgame.com/news/game/)。

**关于 ``run_server()``** 它会在您的本地端制造一个服务器，你可以在网页上浏览它(**⚠️注意：当你运行该函数时，你不会立刻在``templates``文件夹里发现``data.json``，但网页仍可以正常打开和查看，当你打开网页查看时，或者停止服务器时文件才会被加载出来**)

### open_web.py
进入后你就会明白它的作用，查看`return jsonify(render_template("GameNews.txt"))`语句，``GameNews.txt``是要挂载到网页上的Json文件名，程序将自动将其转换成Json文件，您可能已经发现了``<json_name>``这个变量，这意味着您可以在目录下放更多的文件互不干扰

## ⚠️注意：在开始一切工作之前，请翻阅代码与注释，这会帮助你更好的理解它

**常见问题**
* Q:爬虫爬不动了  
  A:重新启动程序
***
*来自 邱璇洛 2022 ©*️