#!/usr/bin/env python
# encoding: utf-8

import os
import sys

g_mail_core_path = "TODO: 给出mail_core.py 文件位置, 最好是绝对位置"

def main(argv):
	#=======================================================
	# 设置服务器，用户名、口令以及邮箱的后缀, 【可修改部分】
	#=======================================================
	host="TODO: 填写SMTP"
	# 企业邮箱,需要全称
	user="TODO: 改成自己的邮箱,eg: xyz@gmail.com"
	show_user_name = "TODO: 改成自己的名字"
	# 非QQ企业邮箱,只需要用户名
	# user="TODO:@前面的部分,eg: xyz"
	pwd="TODO:改成自己的密码"
	postfix="TODO:改成邮箱后缀,eg: gamil.com"
	server_type='TODO: 如果是user中需要带@的全称的，此处为 eim， 否则，为邮箱后缀'
	#=========================================
	# 设置邮件内容, 【修改部分】
	#=========================================
	# 收件人
	receivers = [
			# TODO:添加收件人 eg: "xxxx@175game.com",
			]
	# 主题
	subject = 'TODO: 添加主题'
	# 邮件正文
	content = '''
		TODO: 添加邮件内容
		'''

	# 是否备份邮件(发给自己一份)
	backup = 1
	# 邮件log
	log_path = './send_mail.log'
	# 附件文件列表
	attachments = [
			# TODO: 添加附件文件，或者通知参数传入
			#  "./mail_core.py",
			#  "./send_mail.py"
			]
	for a in argv:
		attachments.append(a)

	#=========================================
	# 处理命令，勿改动
	#=========================================
	receivers_str = ''
	for rc in receivers:
		receivers_str = receivers_str + ' -r "' + rc + '"'
	attachments_str = ''
	for at in attachments:
		attachments_str = attachments_str + ' -a "' + at + '"'
	# 生成命令
	if len(show_user_name):
		show_user_name = '-n "' + show_user_name +'"'
	if len(subject):
		subject = '-s "' + subject + '"'
	if len(content):
		content = '-c "' + content + '"'
	if len(log_path):
		log_path = '-l "' + log_path + '"'
	if len(server_type):
		server_type = '-t ' + server_type
	if backup > 0:
		backup = '-b '

	cmd = "python {mail_core} -h {h} -u {u} -p {p} -f {f} {sname} {rs} {s} {c} {ats} {t} {b} {l}".format(
			mail_core=g_mail_core_path,
			h=host, u=user, p=pwd, f=postfix, sname=show_user_name, rs=receivers_str,
			s=subject, c=content, ats=attachments_str,
			t=server_type, b=backup, l=log_path)
	# 执行命令
	os.system(cmd)
	#=========================================

if __name__ == "__main__":
	# 这里如果传入了参数，只能是用做附件发送的文件。
	main(sys.argv[1:])
