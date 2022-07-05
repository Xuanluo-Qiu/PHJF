from flask import Flask, render_template, jsonify


super_var = open("var.txt", "r")
File_name = super_var.read()
name = f"{File_name}.txt"

print("\033[34m%s" % "PHJF:" + "\033[32m%s" % "服务器已启动")
print("\033[34m%s" % "PHJF:" + "\033[35m%s" % "请打开启动网址中的" + "\033[36m%s" % f" /read_json/{File_name} " + "\033[35m%s" % "目录" + "\033[30m")

app = Flask(__name__)  # 实例化flask


# json_name是客户端传来的json文件名，根据传来的文件名从本地读取
@app.route('/read_json/<json_name>', methods=['GET'])
# 如果你改了名字，改变这里的名字，它是目录的名字
def game_json(json_name=File_name):
    try:
        # 如果你改了名字，改变这里的名字，它是更改的名字
        return jsonify(render_template(name))
    except Exception as e:
        return jsonify({"code": "Error", "message": "{}".format(e)})


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"  # 指定浏览器渲染的文件类型，和解码格式；
    app.run()