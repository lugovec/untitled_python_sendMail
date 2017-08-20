from django.shortcuts import render
from django.template import RequestContext, loader

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def landing(request):
    return render(request, 'landing/landing.html', locals())


def index(request):

    # smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    # smtpObj.starttls()
    # smtpObj.login('lugovecfox@gmail.com', '8powerlifting8')
    # #отправка письма
    # smtpObj.sendmail("From Lugovets Andrey, Ekaterinburg", "lugovec-fox@yandex.ru", "I am happy")
    # smtpObj.quit()
    toaddr = 'lugovec-fox@yandex.ru'
    me = 'From: Lugooooooooovets!'
    #you = 'To: ' + toaddr

    server = 'smtp.gmail.com'  # Сервер
    port = 587  # Порты
    user_name = '*********@gmail.com'  # Отправитель
    user_passwd = '******************'  # Пароль отправителя

    # Формируем заголовок письма
    msg = MIMEMultipart('mixed')
    msg['Subject'] = 'Lugooooooooovets!'
    msg['From'] = me
    msg['To'] = toaddr

    # Формируем письмо
    part = MIMEText('Мы хотим заниматься на Ваших курсах.', 'Plain email')
    msg.attach(part)

    # Подключение
    s = smtplib.SMTP(server, port)
    s.ehlo()
    s.starttls()
    s.ehlo()
    # Авторизация
    s.login(user_name, user_passwd)
    # Отправка письма
    s.sendmail(me, toaddr, msg.as_string())
    s.quit()

    return render(request, 'landing/index.html')