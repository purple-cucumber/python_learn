# 📚 Flask 动态网页入门 - 完整复习笔记

> 适用场景：复习 Flask 基础路由、动态参数传递、模板渲染。
> 对应文件：`app_flask.py` + `templates/index.html`

---

## 1. 项目目录结构（这是重点！）

Flask 默认会自动寻找 `templates` 文件夹来存放 HTML 文件，**名字绝对不能拼错**（末尾必须带 `s`）。

```text
python_test/                     # 项目根目录
└── num1/
    └── flask/                   # 核心代码文件夹
        ├── app_flask.py         # Python 后端入口文件
        └── templates/           # ⚠️ 固定文件夹名（末尾有 s）
            └── index.html       # 前端页面模板
```
## 2.怎么写简单的py代码
```
# 1. 导入 Flask 核心类 和 模板渲染函数
from flask import Flask, render_template

# 2. 创建 Flask 应用实例
#    __name__ 是当前模块名，Flask 靠它定位 templates 文件夹
app = Flask(__name__)

# 3. 定义路由（网址入口）
#    动态路由：<username> 是变量占位符，能捕获网址 /user/ 后面的所有内容
@app.route('/user/<username>')
def show_user(username):
    # 4. 视图函数（业务逻辑）
    #    这里本应查询数据库，现在我们直接把捕获到的 username 传进模板
    
    # 5. 渲染并返回 HTML
    #    render_template(文件名, 模板变量名=Python变量值)
    #    将 username 的值填充到 index.html 里的 {{ name }} 位置
    return render_template('index.html', name=username)

# 6. 程序入口（门卫）
if __name__ == '__main__':
    # 7. 启动开发服务器
    #    debug=True 开启调试模式：代码修改后自动重启，报错时显示详细错误
    app.run(debug=True)
```
## 3.前端模板：templates/index.html
这是网页的“皮肤”，负责展示数据。注意 {{ name }} 是挖好的坑位。
```<!-- 1. 文档类型声明：告诉浏览器这是 HTML5 页面 -->
<!DOCTYPE html>

<!-- 2. HTML 根标签 -->
<html>

<!-- 3. 头部：存放页面元数据 -->
<head>
    <!-- 设置字符编码为 UTF-8，让中文正常显示 -->
    <meta charset="UTF-8">
    <!-- 浏览器标签页上显示的文字 -->
    <title>我的动态网页</title>
</head>

<!-- 4. 身体：网页的可见内容 -->
<body>
    <!-- 
        5. Jinja2 模板语法：{{ 变量名 }}
        这是 Flask 的渲染引擎（Jinja2）提供的功能。
        它会自动被 Python 中 render_template 传过来的同名变量替换。
        这里加了 style 内联样式，让字体又红又大，方便看清效果。
    -->
    <h1 style="color: red; font-size: 40px;">你好，{{ name }}！</h1>
    
    <p>当前访问的网址是 /user/ 后面的名字</p>
</body>

</html>
```
## 4.运行与访问流程
### 启动服务：
在项目目录下打开终端（或 PyCharm 底部 Terminal），执行：
```
python app_flask.py
```
查看状态：命令行显示 Running on http://127.0.0.1:5000 即表示成功。

### 打开浏览器，在地址栏输入：
```
http://127.0.0.1:5000/user/小明
```
观察结果：浏览器页面显示 “你好，小明！”。
## 5.核心概念速查表（面试/复习高频考点）

| 概念 | 代码示例 | 一句话解释（人话版） |
| :--- | :--- | :--- |
| **Flask 实例** | `app = Flask(__name__)` | 创建你的网站应用对象。 |
| **路由装饰器** | `@app.route('/path')` | 给下面的函数绑定一个访问网址（挂门牌号）。 |
| **动态路由** | `@app.route('/user/<username>')` | 尖括号 `<>` 是捕手，能抓取网址后面的数据当参数。 |
| **视图函数** | `def show_user(username):` | 处理请求、拿数据、返回网页的函数。函数参数名必须和尖括号里一致。 |
| **模板渲染** | `render_template('index.html', name=username)` | 将 Python 数据（右边）传给 HTML 模板中的变量（左边 `{{ name }}`）。 |
| **模板变量** | `{{ name }}` | HTML 里的占位符，运行时会变成具体的值。 |
| **调试模式** | `debug=True` | 改了代码自动重启，报错显示详情（开发必备神器）。 |
 ### 什么是静态路由？
静态路由 vs 动态路由（生死对比）
|类型	|代码写法	|能响应的网址	|局限|
| :--- | :--- | :--- | :--- |
|**静态路由**|	@app.route('/about')	|只有 http://.../about 这一个网址	|写死了一个页面，来 100 个用户就得写 100 个函数
|**动态路由**	|@app.route('/user/<username>')	|/user/小明、/user/小红、/user/张三……无穷多个|一个函数，通吃所有！