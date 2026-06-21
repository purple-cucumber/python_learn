# 怎么使用pytest
## 怎么更新和下载
python怎么更新和下载捏？
``` bash
python -m pip install --upgrade pip
```
（1）调用你电脑上的 Python 解释器。

（2）-m 是“module”的缩写，意思是把后面的名字当成一个 Python 模块来运行。
所以 python -m pip 就是告诉 Python：“去找到 pip 这个模块，并且运行它。”

（3）这是传给 pip 模块的参数，意思是“安装某个包，并且如果已经装了，就把它升级到最新版”。
--upgrade 可以简写成 -U，效果相同。

（4）这里的 pip 是要安装/升级的包的名字。也就是让 pip 自己升级自己。
整句话串起来就是：“用 Python 运行 pip 模块，然后让它安装最新版的 pip 包（覆盖掉旧版）。”

```bash
python -m pip install --user package_name
```

告诉 pip 把包安装到用户专属的 site-packages 目录（比如 Windows 上通常在 C:\Users\<用户名>\AppData\Roaming\Python\Python311\site-packages），而不是系统范围的 Python 安装目录。

## 怎么使用pytest？
```
python -m pytest
```