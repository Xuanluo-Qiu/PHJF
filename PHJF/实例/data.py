import requests
import json
import os
import atexit
from bs4 import BeautifulSoup

PHJF_text = ("\033[34m%s" % "PHJF:")
page_text = ""
all_file_name = ""

unicode = "utf-8"

web_name = ""
lists_info = []


def compile_data():
    soup = BeautifulSoup(page_text, 'lxml')
    page_list = soup.select('.Revision_list > ul > li')
    for each in page_list:
        image = each.find("img")
        image_url = image['data-original']
        title = each.find("a", attrs={"class": "bt"})
        text = each.find("div", attrs={"class": "miaoshu"}).text
        data = each.find("span", attrs={"class": "time"}).text
        lists_info.append({"image": image_url, "title": title.text, "text": text, "data": data})


def get_page(url, encoding, ish):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/52.0.2743.116 Safari/537.36'}
    print(PHJF_text + "\033[33m%s" % "开始抓取网页数据")
    page_back = requests.get(url, headers=headers)
    if page_back.status_code == requests.codes.ok:
        print(PHJF_text + "\033[32m%s" % "抓取成功")
    else:
        print(PHJF_text + "\033[31m%s" % "抓取失败")

    if ish == "save":
        write_page = page_back.text
        file_name = input(PHJF_text + "\033[35m%s" % "输入文件名称（包括后缀）")
        if encoding == "":
            encoding = unicode
        else:
            encoding = encoding
        with open(file_name, 'w', encoding=encoding) as save:
            save.write(write_page)
            print(PHJF_text + f"\033[32m%s \033[33m{file_name}" % "文件已保存")
    elif ish == "let":
        global page_text
        page_text = page_back.text
        print(PHJF_text + "\033[35m%s" % "对接数据已加载")
    else:
        print(PHJF_text + "\033[35m%s" % "页面数据已返回")
        return page_back.text


def run_compile_page(ish, file_name):
    if page_text != "":
        print(PHJF_text + "\033[36m%s" % "已对接数据")
        compile_page(ish, file_name)
    else:
        print(PHJF_text + "\033[31m%s" % "未查找到数据")


# 抓取特别页面数据
def compile_page(ish, file_name):
    global all_file_name
    all_file_name = file_name
    with open("var.txt", "a", encoding=unicode) as save:
        save.write(file_name)
    with open("page_text.txt", "a", encoding=unicode) as save:
        save.write(page_text)
    print(PHJF_text + "\033[33m%s" % "正在编译数据...")
    compile_data()
    if ish == "json":
        with open(f"{file_name}.json", 'a', encoding=unicode) as save:
            json_file = json.dumps(lists_info, sort_keys=False, ensure_ascii=False, indent=4, separators=(',', ': '))
            save.write(json_file + "\n")
        print(PHJF_text + "\033[32m%s" % "数据已保存")
    elif ish == "data":
        with open(f"templates/{file_name}.txt", 'a', encoding=unicode) as save:
            json_file = lists_info
            save.write(str(json_file))
        print(PHJF_text + "\033[32m%s" % "数据已对接")
    else:
        print(PHJF_text + "\033[31m%s" % "请输入正确的指令")
        exit()


def run_server():
    print(PHJF_text + "\033[33m%s" % "正在启动本地服务器...")
    os.system("python3 open_web.py")


@atexit.register
def clean_file():
    os.remove('var.txt')
    os.remove('page_text.txt')
    os.remove(f'templates/{all_file_name}.txt')
    print(PHJF_text + "\033[33m%s" % "超级全局变量和页面内容已清除")


'''
 ______     _     _      _____    _______ 
(_____ \   | |   | |    (_____)  (_______)
 _____) )  | |__ | |       _      _____   
|  ____/   |  __)| |      | |    |  ___)  
| |        | |   | |   ___| |    | |      
|_|        |_|   |_|  (____/     |_|      

2022 by CCAil                                          
'''
