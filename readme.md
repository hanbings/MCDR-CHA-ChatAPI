# 针对MCDR简单封装CoolQ-Http-API 



### Install / 安装它

1.安装Flask包（pip install flask）

2.到 [CoolQ](https://cqp.cc/) 网站下载和安装CoolQ 并且安装CoolQ-Http-API插件 [CoolQ-Http-API](https://github.com/richardchien/coolq-http-api) 

启动一次CoolQ和CoolQ-Http-API插件，生成配置文件

它一般位于 ./data/app/io.github.richardchien.coolqhttpapi/config/ 内

双击打开它，并将port设置为5700，将port_url设置为http://127.0.0.1:5701/api/message

前者为端口号，请务必不要更改，后者为插件转发链接地址，可视情况更改

3.下载本Github仓库的API文件，将它放到MCDR的插件文件夹内并启动，若未出现报错即可视为成功

4.若对以上描述存有疑问，您可以来主动联系我 3219065882@qq.com

或参考我编写此插件前参考的文章 https://zhuanlan.zhihu.com/p/96892167

以及CoolQ-Http-API的相关教程 https://richardchien.gitee.io/coolq-http-api/docs/4.12/#/



### Use / 使用它

此插件仅仅是对CoolQ-Http-API进行了最基本的封装

```
def send_private_msg(user_id, message, auto_escape):
    data = {
        'user_id': user_id,
        'message': message,
        'auto_escape': auto_escape
    }
    api_url = 'http://127.0.0.1:5700/send_private_msg'
    # 酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    r = requests.post(api_url, data=data)
    return r
```

将CoolQ-Http-API的API封装为一个独立的方法，参数将被直接传递，每个方法执行完成后将返回CoolQ-Http-API返回的内容（返回内容并未处理）



因为本插件仅仅为封装此API，并未对API本身做出更改，所有的方法都可参考CoolQ-Http-API的官方文档

API列表：https://richardchien.gitee.io/coolq-http-api/docs/4.12/#/API

方法名与CoolQ-Http-API无差别，去掉 / 后即本项目方法名



### Get the content received by QQ / 获取QQ接收到的内容

在处理QQ接收到的内容的方法前添加

**@bot_server.route('/api/message',methods=['POST'])**

（此情况针对安装文档来设置port_url的用户，请自行根据配置文件变更[POST]参数需更改项目源码，请自行更改）

例子：

```text
@bot_server.route('/api/message',methods=['POST'])
def server():
    data = request.get_data().decode('utf-8')
    data = loads(data)
    print(data)
    return ''
```

在接收到传来的消息时将执行@符号下的方法

