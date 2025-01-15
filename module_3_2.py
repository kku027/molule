message = "Proba"


def send_email(message: str, recipient: str, *, sender: str = "university.help@gmail.com"):
    if '@' not in recipient or not recipient.endswith(".com") or recipient.endswith(".ru") or recipient.endswith(
            ".net"):
        return f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}"
    elif recipient == sender:
        return f"Нельзя отправить письмо самому себе!"
    elif sender == "university.help@gmail.com":
        return f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}."
    else:
        return f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}."


print(send_email('Проверка', "asdfgh.help@gmail.com", sender="lkjhgfd@gmail.com"))
