#!/usr/bin/env python
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2016 All rights reserved.
#
#   Author        : bbxytl
#   Email         : bbxytl@gmail.com
#   File Name     : config.py
#   Last Modified : 2016-08-31 19:40
#   Describe      :
#
#   Log           :
#
# ====================================================

#  import sys
import os

config_data = {
# host="TODO: 填写SMTP, eg:smtp.xxx.com"
	"host":"TODO: 填写SMTP, eg:smtp.xxx.com"
	,
# user="TODO: 改成自己的邮箱,eg: xyz@gmail.com"
	"user":"TODO: 改成自己的邮箱,eg: xyz@gmail.com"
	,
# show_user_name = "TODO: 改成自己的名字"
	"show_user_name" : "TODO: 改成自己的名字"
	,
# postfix="TODO:改成邮箱后缀,eg: gamil.com"
	"postfix":"TODO:改成邮箱后缀,eg: gamil.com"
	,
# server_type='TODO: 如果是user中需要带@的全称的，此处为 eim， 否则，为邮箱后缀'
	"server_type" : "eim"
	,
# pwd="TODO:改成自己的密码"
	"pwd":"TODO:改成自己的密码"
	,
# 是否备份邮件(发给自己一份)
	"backup" : 1
	,
# 默认的收件人列表
	"receivers" : [
			# TODO:添加收件人 eg: "xxxx@gmail.com",
			]
	,
# 邮件log
	"log_path" : os.path.dirname(os.path.abspath(__file__)) + '/send_mail.log'
}

def get_config():
	config_data["subject"] = "subject:_from:" + config_data["show_user_name"] + "(" + config_data["user"] + ")"
	config_data["content"] = "Content____"
	return config_data
