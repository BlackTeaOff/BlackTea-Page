from flask import Flask, render_template, request, redirect, url_for, jsonify
import numpy as np;

app = Flask(__name__)

count = 0

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/counterpage", methods=["GET", "POST"])
def counterpage():
    global count
    return render_template("counter.html", count=count)

@app.route("/counter", methods=["GET", "POST"])
def counter():
    global count
    if request.method == "GET":
        return jsonify(count=count)
    else:
        count += 1
        return jsonify(count=count)

matrix = np.array([[3683, 4311, 4508, 5147, 5362, 5961, 6195], 
                   [7000, 7602, 7877, 8417, 8653, 9271, 9487],
                   [12762, 12969, 13165, 13370, 13566, 13773, 13970],
                   [14413, 14609, 14806, 15002, 15198, 15395, 15591],
                   [16074, 16270, 16466, 16663, 16859, 17056, 17252],
                   [17730, 17927, 18123, 18320, 18516, 18713, 18909],
                   [19380, 19796, 20211, 20627, 21042, 21458, 21873],
                   [22698, 23313, 23526, 24134, 24347, 24975, 25177],
                   [29323, 29526, 29729, 29942, 30154, 30358, 30560],
                   [30979, 31184, 31391, 31598, 31805, 32012, 32219],
                   [32631, 32840, 33050, 33228, 33464, 33638, 33852],
                   [34263, 34473, 34677, 34884, 35095, 35298, 35502],
                   [35916, 36540, 36740, 37365, 37569, 38198, 38394]]
                    )

@app.route("/rythem")
def rythem():
    return render_template("rythem_doctor.html", matrix=matrix.tolist()) #使用tolist()将numpy数组转换为普通Python列表

@app.route("/window_move")
def window_move():
    return render_template("window_move.html")

@app.route("/bonus")
def bonus():
    return render_template("bonus.html")

names = []

@app.route("/data_bonus", methods=["POST"])
def data_bonus():
    global names
    name = request.form.get("name")
    if name:
        names.append(name)
        return render_template("bonus.html", status="成功")
    return render_template("bonus.html", status="失败")

@app.route("/show_names")
def show_names():
    global names
    return render_template("show_names.html", names=names)

@app.route("/rickroll")
def rickroll():
    return render_template("rickroll.html")

@app.route("/move")
def move():
    return render_template("rythem_move.html")

if __name__ == '__main__': # 只有在该文件作为主程序执行时才会运行，而不是在它被其他脚本导入时执行
    app.run(host='0.0.0.0', port=5000)