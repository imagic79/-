import linecache
import random
import smtplib
from email.mime.text import MIMEText
import weather


def send_email(email_r, email, email_s, password, sender, Theme):
    # 从文件中随机读取一行情话
    originFile = 'qinghua.txt'
    lineNumber = random.randint(1, 3998)  # 随机数作为行数
    line = linecache.getline(originFile, lineNumber)  # 随机读取一行
    if len(line) == 0:  # 过滤为空的内容
        lineNumber = random.randint(1, 3998)  # 随机数作为行数
        line = linecache.getline(originFile, lineNumber)  # 随机读取一行
        
    # 爬取天气信息
    today_weather = weather.Weather()

    # 设置email信息
    # 邮件内容设置
    context = line + today_weather
    message = MIMEText(context, 'plain', 'utf-8')
    # 邮件主题
    message['Subject'] = Theme
    # 发送方信息
    message['From'] = sender
    # 接受方信息
    message['To'] = email_r

    # 登录并发送邮件
    try:
        smtpObj = smtplib.SMTP()
        # 连接到服务器
        smtpObj.connect(email, 25)
        # 登录到服务器
        smtpObj.login(email_s, password)
        # 发送
        smtpObj.sendmail(
            sender, email_r, message.as_string())
        # 退出
        smtpObj.quit()
        print('success')
    except smtplib.SMTPException as e:
        print('error', e)  # 打印错误


if __name__ == '__main__':
    email = 'smtp.163.com'  # 使用邮箱 这里是163 可更改   # 设置服务器所需信息 # 163邮箱服务器地址
    email_r = ['XXXX@qq.com', 'XXXXX@126.com']  # 自行更改 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
    email_s = "xxx@163.com"  # 自行更改 邮箱用户名，这里是163用户名 要和上面的邮箱服务器地址对应
    password = "xxxxx"  # 自行更改 密码(部分邮箱为smtp授权码)
    sender = 'XXX@xxx.com'  # 自行更改 即备注发件人
    Theme = 'XXXX'  # 自行更改 邮箱主题
    send_email(email_r, email, email_s, password, sender, Theme)
