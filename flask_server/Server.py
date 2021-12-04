# @Time    : 2021-12-01 11:54
# @Author  : Peisong Li
# @FileName: py-server.py
from flask import Flask, request
import os
from werkzeug.utils import secure_filename
import time


os.environ['TZ'] = 'Asia/Shanghai'
time.tzset()
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker container!'


# 添加路由
@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        # 通过file标签获取文件
        f = request.files['file']
        pro = request.form['pro']
        ph = request.form['phone']
        datatime = time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime())
        # 当前文件所在路径
        basepath = os.path.dirname(__file__)
        # 一定要先创建该文件夹，不然会提示没有该路径
        upload_path = os.path.join(basepath, 'Audio', pro+'-'+datatime+'-'+ph+'-'+secure_filename(f.filename))
        # 保存文件
        f.save(upload_path)
        # 返回上传成功界面
        return 'Success.'
        # return render_template('upload_ok.html')
    # 重新返回上传界面
    # return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
