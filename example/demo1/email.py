from random import Random
from django.core.mail import send_mail
from example.settings import EMAIL_FROM


def random_str(randomlength = 8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


def send_register_email(email, send_type = "register"):
    code = random_str(16)
    email_title = "注册激活链接"
    email_body = "请点击下面的链接激活你的账号:http://127.0.0.1:8000/active/{0}".format(code)
    send_mail(email_title, email_body, EMAIL_FROM, [email])
    return code


def send_remind_email(email, content):
    email_title = "缴费通知"
    email_body = content
    send_mail(email_title, email_body, EMAIL_FROM, [email])
    return