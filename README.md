## 项目说明

随着个人项目的不断增加，管理这些脚本和独立项目变得越来越困难。尤其是当我需要快速找到之前编写的某个项目时，经常会浪费很多时间在搜索和浏览文件夹中。

为了更高效地管理这些项目路径，我决定开发一个本地项目路径管理工具。这个工具可以帮助我添加项目录和项目描述信息，并支持根据项目描述快速搜索，以便在需要时迅速定位和访问相关代码，从而节省时间并提高工作效率。


第一版本基于AI（GPT4）生成，还有很多要完善的，后面会持续迭代，可能的问题：
- 每次运行都要加载一遍模型，比较耗时
- 目前数据库是json文件管理，不是很方便
- 目前向量数据库查找是遍历比较，比较耗时
- 模型向量匹配查找效果不好
等等，后续会一一优化。

下一个版本应该会分为：
- server端：使用fastapi 搭建一套服务api，这样服务可以部署到任意地方，而且不用重复加载模型
- webui端：使用flask+html 搭建一套简单的ui管理页面，方便非开发者使用
- cli端：就基于现在这套代码，编写一个简单的cli程序，方便开发者在terminal下使用

## 运行说明

安装环境，并赋予运行脚本可执行权限，然后创建一个软链接到系统环境变量路径下，比如`/usr/local/bin/pv`

```bash
cd /usr/local
git clone https://github.com/XksA-me/PathVec
conda create -n pv python=3.10
conda activate pv
cd PathVec
pip install -r requirements.txt
chmod +x ./pv.sh
ln -sf ./pv.sh /usr/local/bin/pv
```

修改代码文件路径：
- pv.py 中设置 DB_PATH 路径，注意是绝对路径，随便设置一个路径即可，比如`"/usr/local/PathVec/db.json"`
- pv.sh 中设置 CODE_PATH 路径，请按自己clone项目所在实际路径填写，比如`"/usr/local/PathVec/pv.py"`

修改好，即可在terminal 任意位置执行 pv 指令来添加项目文件信息或者查询项目文件信息了。

### 添加项目路径和项目信息
```bash
pv add -p /usr/local/PathVec -m "基于向量数据库的本地项目路径管理系统"
```
 `-p` 是可选参数，不指定的话默认会获取当前路径作为项目路径，`-m`是必填参数，含义为项目描述内容，方便日后查找。
 
 ### 根据描述查找项目路径
 
 ```bash
 pv search -s "路径管理"
 ```
 `-s`是必填参数，模糊查找使用的项目描述。
 


## 与我交流

对项目感兴趣，或者想了解AI使用的欢迎加我微信，邀请你加入项目使用交流群。
我的微信：pythonbrief
我的QQ：820553471