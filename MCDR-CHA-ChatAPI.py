import json

import requests
from flask import Flask

# 设置一个Flask程序
bot_server = Flask(__name__)


# 发送私聊消息
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


# 发送群消息
def seed_group_message(group_id, message, auto_escape):
    data = {
        'group_id': group_id,
        'message': message,
        'auto_escape': auto_escape
    }
    api_url = 'http://127.0.0.1:5700/send_group_msg'
    # 酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    r = requests.post(api_url, data=data)
    return r


# send_discuss_msg 发送讨论组消息
def seed_discuss_msg(discuss_id, message, auto_escape):
    data = {
        'discuss_id': discuss_id,
        'message': message,
        'auto_escape': auto_escape
    }
    api_url = 'http://127.0.0.1:5700/send_discuss_msg'
    # 酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    r = requests.post(api_url, data=data)
    return r


# /send_msg 发送消息
def send_msg(message_type, user_id, group_id, discuss_id, message, auto_escape):
    data = {
        'message_type': message_type,
        'user_id': user_id,
        'group_id': group_id,
        'discuss_id': discuss_id,
        'message': message,
        'auto_escape': auto_escape
    }
    api_url = 'http://127.0.0.1:5700/send_msg'
    # 酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    r = requests.post(api_url, data=data)
    return r


# delete_msg 撤回消息
def delete_msg(message_id):
    data = {
        'message_id': message_id,
    }
    api_url = 'http://127.0.0.1:5700/delete_msg'
    # 酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    r = requests.post(api_url, data=data)
    return r


# /send_like 发送好友赞
def send_like(user_id, times):
    data = {
        'user_id': user_id,
        'times': times
    }
    api_url = 'http://127.0.0.1:5700/send_like'
    # 酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    r = requests.post(api_url, data=data)
    return r


# /set_group_kick 群组踢人
def set_group_kick(group_id, user_id, reject_add_request):
    data = {
        'group_id': group_id,
        'user_id': user_id,
        'reject_add_request': reject_add_request
    }
    api_url = 'http://127.0.0.1:5700/set_group_kick'
    # 酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    r = requests.post(api_url, data=data)
    return r


# /set_group_ban 群组单人禁言
def set_group_ban(group_id, user_id, duration):
    data = {
        'group_id': group_id,
        'user_id': user_id,
        'duration': duration,
    }
    api_url = 'http://127.0.0.1:5700/set_group_ban'
    # 酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    r = requests.post(api_url, data=data)
    return r


# /set_group_whole_ban 群组全员禁言
def set_group_whole_ban(group_id, enable):
    data = {
        'group_id': group_id,
        'enable': enable,
    }
    api_url = 'http://127.0.0.1:5700/set_group_whole_ban'
    # 酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    r = requests.post(api_url, data=data)
    return r


# /set_group_anonymous 群组匿名
def set_group_anonymous(group_id, enable):
    data = {
        'group_id': group_id,
        'enable': enable,
    }
    api_url = 'http://127.0.0.1:5700/set_group_anonymous'
    # 酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    r = requests.post(api_url, data=data)
    return r


# /set_group_card 设置群名片（群备注）
def set_group_card(group_id, user_id, card):
    data = {
        'group_id': group_id,
        'user_id': user_id,
        'card': card
    }
    api_url = 'http://127.0.0.1:5700/set_group_card'
    # 酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    r = requests.post(api_url, data=data)
    return r


# /set_group_leave 退出群组
def set_group_leave(group_id, is_dismiss):
    data = {
        'group_id': group_id,
        'is_dismiss': is_dismiss,
    }
    api_url = 'http://127.0.0.1:5700/set_group_leave'
    # 酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    r = requests.post(api_url, data=data)
    return r


# /set_group_special_title 设置群组专属头衔
def set_group_special_title(group_id, user_id, special_title, duration):
    data = {
        'group_id': group_id,
        'user_id': user_id,
        'special_title': special_title,
        'duration': duration,
    }
    api_url = 'http://127.0.0.1:5700/set_group_special_title'
    # 酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    r = requests.post(api_url, data=data)
    return r


# /set_friend_add_request 处理加好友请求
def set_friend_add_request(flag, approve, remark):
    data = {
        'flag': flag,
        'approve': approve,
        'remark': remark,
    }
    api_url = 'http://127.0.0.1:5700/set_friend_add_request'
    # 酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    r = requests.post(api_url, data=data)
    return r


# /set_group_add_request 处理加群请求／邀请
def set_group_add_request(flag, sub_type, approve, reason):
    data = {
        'flag': flag,
        'sub_type': sub_type,
        'approve': approve,
        'reason': reason,
    }
    api_url = 'http://127.0.0.1:5700/set_group_add_request'
    # 酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    r = requests.post(api_url, data=data)
    return r


# /get_login_info 获取登录号信息
def get_login_info(user_id, nickname):
    data = {
        'user_id': user_id,
        'nickname': nickname,
    }
    api_url = 'http://127.0.0.1:5700/get_login_info'
    # 酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    r = requests.post(api_url, data=data)
    return r


# /get_stranger_info 获取陌生人信息
def get_stranger_info(user_id, no_cache):
    data = {
        'user_id': user_id,
        'no_cache': no_cache,
    }
    api_url = 'http://127.0.0.1:5700/get_stranger_info'
    # 酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    r = requests.post(api_url, data=data)
    return r


# /get_friend_list 获取好友列表
def get_friend_list():
    api_url = 'http://127.0.0.1:5700/get_friend_list'
    # 酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    r = requests.post(api_url)
    return r


# /get_group_list 获取群列表
def get_group_list():
    api_url = 'http://127.0.0.1:5700/get_group_list '
    # 酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    r = requests.post(api_url)
    return r


# /get_group_info 获取群信息
def get_group_info(group_id, no_cache):
    data = {
        'group_id': group_id,
        'no_cache': no_cache,
    }
    api_url = 'http://127.0.0.1:5700/get_group_info'
    # 酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    r = requests.post(api_url, data=data)
    return r


# /get_group_member_info 获取群成员信息
def get_group_member_info(group_id, user_id, no_cache):
    data = {
        'group_id': group_id,
        'user_id': user_id,
        'no_cache': no_cache,
    }
    api_url = 'http://127.0.0.1:5700/get_group_member_info'
    # 酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    r = requests.post(api_url, data=data)
    return r


# /get_group_member_list 获取群成员列表
def get_group_member_list(group_id):
    data = {
        'group_id': group_id,
    }
    api_url = 'http://127.0.0.1:5700/get_group_member_list'
    # 酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    r = requests.post(api_url, data=data)
    return r


# /get_cookies 获取 Cookies
def get_cookies(domain):
    data = {
        'group_id': domain,
    }
    api_url = 'http://127.0.0.1:5700/get_cookies'
    # 酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    r = requests.post(api_url, data=data)
    return r


# /get_csrf_token 获取 CSRF Token
def get_csrf_token():
    api_url = 'http://127.0.0.1:5700/get_csrf_token'
    # 酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    r = requests.post(api_url)
    return r


# /get_credentials 获取 QQ 相关接口凭证
def get_credentials():
    api_url = 'http://127.0.0.1:5700/get_credentials'
    # 酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    r = requests.post(api_url)
    return r


# /get_record 获取语音
def get_record(file, out_format, full_path):
    data = {
        'file': file,
        'out_format': out_format,
        'full_path': full_path
    }
    api_url = 'http://127.0.0.1:5700/get_record'
    # 酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    r = requests.post(api_url, data=data)
    return r


# /get_image 获取图片
def get_image(file):
    data = {
        'file': file,
    }
    api_url = 'http://127.0.0.1:5700/get_image'
    # 酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    r = requests.post(api_url, data=data)
    return r


# /can_send_image 检查是否可以发送图片
def can_send_image():
    api_url = 'http://127.0.0.1:5700/can_send_image'
    # 酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    r = requests.post(api_url)
    return r


# /can_send_record 检查是否可以发送语音
def can_send_record():
    api_url = 'http://127.0.0.1:5700/can_send_record'
    # 酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    r = requests.post(api_url)
    return r


# /get_status 获取插件运行状态
def get_status():
    api_url = 'http://127.0.0.1:5700/get_status'
    # 酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    r = requests.post(api_url)
    return r


# /get_version_info 获取 酷Q 及 HTTP API 插件的版本信息
def get_version_info():
    api_url = 'http://127.0.0.1:5700/get_version_info'
    # 酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    r = requests.post(api_url)
    return r


# /set_restart_plugin 重启 HTTP API 插件
def set_restart_plugin(delay):
    data = {
        'delay': delay,
    }
    api_url = 'http://127.0.0.1:5700/set_restart_plugin'
    # 酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    r = requests.post(api_url, data=data)
    return r


# /clean_data_dir 清理数据目录
def clean_data_dir(data_dir):
    data = {
        'data_dir': data_dir,
    }
    api_url = 'http://127.0.0.1:5700/clean_data_dir'
    # 酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700
    r = requests.post(api_url, data=data)
    return r


# /clean_plugin_log 清理插件日志
def clean_plugin_log():
    return ' '


# on_load方法加载flask实例
def on_load(server, old_module):
    bot_server.run(port=5701)
    # 端口也是你在酷Q配置文件里自定义的
