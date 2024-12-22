
import streamlit as t
#import time

def check(password):
    #current_time = time.localtime()
    #date_time = time.strftime("%X", current_time)
    count_spec_symbol = 0
    count_numbers = 0
    count_upper = 0
    count_lower = 0
    sum = 0
    if len(password) < 7:
        t.text("Пароль должен содержать минимум 7 символов")
    elif count_numbers > 300:
        t.text("Ваш пароль не должен содержать больше 300 символов")
    elif "A" in password:
        t.text("Пароль не должен содержать букву: A")
    elif "8" in password:
        t.text("Пароль не должен содержать символ: 8")
    elif "@" in password:
       t.text("Ваш пароль не должен содержать символ @")
    elif "%" in password:
       t.text("Ваш пароль не должен содержать символ %")
    elif "&" in password:
        t.text("Ваш пароль не должен содержать символ &")
    elif "*" in password:
        t.text("Ваш пароль не должен содержать символ *")
    elif "67" in password:
        t.text("Ваш пароль не должен содержать символы: 67")
    elif "%%2F" in password:
        t.text("Ваш пароль должен содержать символ ;")
    elif "!" in password:
        t.text("Ваш пароль не должен содержать символ !")
    #elif "90" in password:
        #t.write("Ваш пароль должен содержать цифры из даты", date_time)
    elif "2024" in password:
        t.text("Ваш пароль не должен содержать 2024")
    elif "01." in password:
        t.text(sum)
        t.text("Ваш пароль не должен включать поллученную сумму 2037")
    elif "." in password:
        t.text("Ваш пароль не должен содержать .")
    elif "ю" in password:
        t.text("Ваш пароль должен содержать день недели")
    elif "Воскресенье" in password:
        t.text("Ваш парорль должен содержать ссылку на картинку бравл старс")
    elif " " in password:
        t.text("https://ya.ru/images/search?pos=0&from=tabbar&img_url=https%3A%2F%2Fstatic.g2board.com%2Fuploads%2Fimages%2Fcategory_icon%2Ficon%2F26%2Fbrawl.jpg&text=ссылка+на+картинку+бравл+старс&rpt=simage&lr=2")
    elif "№" in password:
        t.text("Ваш пароль не должен содержать №, ваш пароль должен содержать игру шахматы и кто выигрыл белые или черные")
    for symbol in password:
        if symbol in "ЙСЖДВДМПЗЧЮБВЪКЕАЛЩЩВAО":
            count_upper += 1
        if symbol in "@%$#!)(&^=+":
            count_spec_symbol += 1
        if symbol in "01122024":
            count_numbers += 1
            sum += int(symbol)
        if symbol in "йрчцчпцзывся":

            if count_spec_symbol < 6:
                print("Ваш пароль должен содержать минимум 5 спец символов")
            if count_upper < 7:
                print("Ваш пароль должен содержать хотя бы не меньше 6 заглавных")

t.title("Добро пожаловать")
t.subheader("")
t.markdown("center; color: red")
r = t.text_input('Введите пароль', max_chars=300, type="Пароль")
check(r)
