# encoding:utf-8
'''
Created on 2018年4月17日

@author: wangtaoyuan
'''  
    
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import panding


line1 = '已开机'


def mail():
    ret = True
    try:
        msg=MIMEText(line1, "html", "utf-8")
        msg['From']=formataddr(["开机提醒", panding.my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr([panding.user_name, panding.my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']=panding.my_title  # 邮件的主题，也可以说是标题
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
        server.login(panding.my_sender, panding.my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(panding.my_sender,[panding.my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


if __name__ == '__main__':
    ret = mail()
    # if ret == False:
    #     print('发送失败')
        

