def send_email(message, recipient, sender = "university.help@gmail.com"):
    # print(message, recipient, sender)
    # Проверка адреса отправителя на коректность
    norm_mail_1 = False
    norm_mail_2 = False
    norm_mail_sender = False
    if ".net" in sender:
        norm_mail_1 = True
    elif ".com" in sender:
        norm_mail_1 = True
    elif ".ru" in sender:
        norm_mail_1 = True
    if '@' in sender:
        norm_mail_2 = True
    if norm_mail_1 == True and norm_mail_2 == True:
        norm_mail_sender = True
    # print(norm_mail_1, norm_mail_2, norm_mail_sender)
    # Проверка адреса получателя на коректность
    norm_mail_1 = False #
    norm_mail_2 = False
    norm_mail_recipient = False
    if ".net" in recipient:
        norm_mail_1 = True
    elif ".com" in recipient:
        norm_mail_1 = True
    elif ".ru" in recipient:
        norm_mail_1 = True
    if '@' in recipient:
        norm_mail_2 = True
    if norm_mail_1 == True and norm_mail_2 == True:
        norm_mail_recipient = True
    # print(norm_mail_1, norm_mail_2, norm_mail_recipient)
    # Теперь проверка всех условий
    if norm_mail_sender == False or norm_mail_recipient == False:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    elif sender != 'university.help@gmail.com':
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
