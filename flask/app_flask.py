from flask import Flask, render_template

app = Flask(__name__)

@app.route('/user/<username>')  # 注意：<> 代表动态参数
def show_user(username):
    # 假设我们从数据库查到了这个用户的信息
    return render_template('index.html', name=username)  # 把 username 传给 index.html 里的 {{ name }}
#render_template 是专门用来处理 templates 文件夹里那些 HTML 文件的工具。注意，这不是 Python 自带的，是安装 Flask 后才有的。
if __name__ == '__main__':
    app.run(debug=True)