from flask import Flask, render_template

app = Flask(__name__)

print("\033[34m%s" % "PHJF:" + "\033[32m%s" % "服务器已启动")
print("\033[34m%s" % "PHJF:" + "\033[35m%s" % "请打开启动网址中的" + "\033[36m%s" % " /data " + "\033[35m%s" % "目录" + "\033[30m")


@app.route('/data')
def rt_data():
    return render_template('data.json')


if __name__ == "__main__":
    app.run()
