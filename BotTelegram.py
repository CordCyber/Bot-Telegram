import telebot
from telebot import types
import os

client = telebot.TeleBot("Ваш токен")

@client.message_handler(commands=["info"])
def info(message):
    client.send_message(message.chat.id, message)


@client.message_handler(commands=["start"])
def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    money = types.KeyboardButton("Спонсировать")
    video = types.KeyboardButton("Kali Linux и т.д")
    talk = types.KeyboardButton("Отправить что-то автору")
    library = types.KeyboardButton("Книги по информационой безопасности!")
    markup.add(video, talk, money, library)
    client.send_message(message.chat.id, "Выберай все что тебе по душе! Бот дополняется каждую неделю!", reply_markup=markup)


@client.message_handler(content_types=["text"])
def get_text(message):
    # def money(message):
    if message.text == "Спонсировать":
        client.send_message(message.chat.id, "Вот моя карта: . Если, что - это MonoBank")

    # def message_talk(message):
    if message.text == "Отправить что-то автору":
        send_message = client.send_message(message.chat.id,
                                           "Следующее сообщение увидет автор. Также можно отправлять фото, документ и видео размером до 20 мегабайт.")
        client.register_next_step_handler(send_message, talk_with1)

    #def library_one(message):
    markup_library = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    library = types.KeyboardButton("Список книг")
    say_library = types.KeyboardButton("Предложить книгу")
    home0 = types.KeyboardButton("Назад")

    markup_library.add(library, say_library, home0)
    if message.text == "Книги по информационой безопасности!":
        client.send_message(message.chat.id, "Что хотите найти?", reply_markup=markup_library)

    #def library_two(message):
    markup_library_new = types.InlineKeyboardMarkup(row_width=1)
    book_new1 = types.InlineKeyboardButton("Книга «Этичный хакинг. Практическое руководство по взлому»", url="https://drive.google.com/file/d/1vrB4WbiHjpwe3QYw_bJ7VqlWhRNKYnV6/view?usp=sharing")
    book_new2 = types.InlineKeyboardButton("Книга «Kali Linux. Тестирование на проникновение и безопасность»", url="https://drive.google.com/file/d/1erEjCMhMfbvWCACBVMn628f8KOXkfCkI/view?usp=sharing")
    book_new3 = types.InlineKeyboardButton("Kali Linux от разработчиков", url="https://ru.pdfdrive.com/kali-linux-%D0%BE%D1%82-%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA%D0%BE%D0%B2-e176231371.html")
    book1 = types.InlineKeyboardButton("Програмирование на C++", url="https://drive.google.com/file/d/1Kce4coybF_Q62OaKh2fDzT8Apzyb3GNQ/view?usp=sharing")
    markup_library_new.add(book_new1, book_new2, book_new3, book1)

    if message.text == "Список книг":
        client.send_message(message.chat.id, "Книги для абсолютных новичков по Python:", reply_markup=markup_library_new)
    elif message.text == "Предложить книгу":
        send_book = client.send_message(message.chat.id, "Отправьте название книги")
        client.register_next_step_handler(send_book, send_book_txt)

    #def python_project_one(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    game = types.KeyboardButton("Беспроводные сети.")
    project = types.KeyboardButton("Этиный хакинг")
    module = types.KeyboardButton("Практика")
    home = types.KeyboardButton("Назад")
    markup.add(game, project, module, home)
    if message.text == "Kali Linux и т.д":
        client.send_message(message.chat.id, "Что хотите найти?", reply_markup=markup)

    markup_game = types.InlineKeyboardMarkup(row_width=1)
    wifivzlom = types.InlineKeyboardButton("Проверка wifi сети на защищеность!", url="https://telegra.ph/Vzlom-besprovodnoj-seti-Wifi-s-pomoshchyu-Kali-Linux-Aircrck-ng-04-07")
    zloy = types.InlineKeyboardButton("Злой двойник", url="https://telegra.ph/Zloj-dvojnik-04-07")
    markup_game.add(wifivzlom, zloy)

    markup_gam = types.InlineKeyboardMarkup(row_width=1)
    crypt = types.InlineKeyboardButton("Криптовка вирусов", url="https://lolz.guru/threads/2218408/")
    sbor = types.InlineKeyboardButton("Сбор данных", url="https://telegra.ph/Sbor-dannyh-04-07")
    soc = types.InlineKeyboardButton("Социальная инженерия", url="https://telegra.ph/Socialnaya-inzheneriya-04-08-2")
    anon = types.InlineKeyboardButton("Анонимность", url="https://telegra.ph/Anonimnost-04-08-2")
    Virusologiya = types.InlineKeyboardButton("Вирусология", url="https://telegra.ph/Virusologiya-04-08")
    bot = types.InlineKeyboardButton("Исходный код этого бота", url="https://github.com/CordCyber")
    markup_gam.add(anon, soc, Virusologiya, crypt, sbor, bot)

    markup_module = types.InlineKeyboardMarkup(row_width=1)
    njrat = types.InlineKeyboardButton("Njrat или же взлом жопы", url="https://telegra.ph/Njrat-ili-zhe-vzlom-zhopy-04-18")
    virusc = types.InlineKeyboardButton("Вирус уничтожающий систему на C++", url="https://telegra.ph/Virus-na-C-ili-zhe-sinij-ekran-smetri-04-23")
    markup_module.add(njrat, virusc)

    if message.text == "Беспроводные сети.":
        client.send_message(message.chat.id, "Беспроводные сети.", reply_markup=markup_game)
    if message.text == "Этиный хакинг":
        client.send_message(message.chat.id, "Этиный хакинг", reply_markup=markup_gam)
    elif message.text == "Практика":
        client.send_message(message.chat.id, "Практика", reply_markup=markup_module)
    elif message.text == "Назад":
        menu(message)


def send_book_txt(message):
    if message.content_type == "text":
        print("Предложенные книги; ", message.chat.username, " / ", message.chat.first_name, " ",
              message.chat.last_name, " / название книги: ", message.text,
              sep="", end=" /\\ ")
        if message.chat.last_name == None:
            message.chat.last_name = "0"

        with open('book.txt', 'a', encoding="utf-8") as f:
            s = ''.join(("Предложенные книги; ", message.chat.username, " / ", message.chat.first_name,
                         message.chat.last_name, " / название книги", ":", " ",
                         message.text, " /\\ "))
            f.write(s)
        send_book = client.send_message(message.chat.id, "Теперь введите автора книги:")
        client.register_next_step_handler(send_book, send_autor_txt)
    else:
        send_message = client.send_message(message.chat.id, "ОТПРАВЬТЕ ТЕКСТ!")
        client.register_next_step_handler(send_message, send_book_txt)



def send_autor_txt(message):
    print("Предложенные книги; ", message.chat.username, " / ", message.chat.first_name, " ", message.chat.last_name,
          " / автор книги: ", message.text,
          sep="")
    if message.chat.last_name == None:
        message.chat.last_name = "0"

    with open('book.txt', 'a', encoding="utf-8") as f:
        s = ''.join(("Предложенные книги; ", message.chat.username, " / ", message.chat.first_name,
                     message.chat.last_name, " / автор книги", ":", " ",
                     message.text, "\n"))
        f.write(s)
    client.send_message(message.chat.id, "Ваш запрос принят")


def talk_with1(message):
    try:
        if message.content_type == "photo":
            talk_with3(message)
        elif message.content_type == "video":
            talk_with4(message)
        elif message.content_type == "text":
            talk_with2(message)
        elif message.content_type == "document":
            talk_with5(message)
        else:
            send_message = client.send_message(message.chat.id, "Отправьте либо текст, либо фото, либо видео, либо документ!")
            client.register_next_step_handler(send_message, talk_with1)
    except:
        print("ERROR")
        with open("error.txt", "a", encoding="utf-8") as f:
            f.write("ERROR\n")
        client.send_message(message.chat.id, "Попробуйте заного!")


def talk_with2(message):
    print(message.chat.username, " / ", message.chat.first_name, " ", message.chat.last_name, ":", " ", message.text, sep="")
    if message.chat.last_name == None:
        message.chat.last_name = "0"

    with open('talk_with_autor.txt', 'a', encoding="utf-8") as f:
        s = ''.join((message.chat.username, " / ", message.chat.first_name, " ", message.chat.last_name, ":", " ", message.text, "\n",))
        f.write(s)
    client.send_message(message.chat.id, "Автор увидит это сообщение.")


def talk_with3(message):
    c = message.photo[-1].file_id
    b = "photo"
    file_photo = client.get_file(c)
    filename, file_extension = os.path.splitext(file_photo.file_path)
    try:
        while True:
            b = b+"0"
            with open (b + file_extension, "rb") as f:
                f.read()
    except:
        save_photo = client.download_file(file_photo.file_path)
        downland_photo = b + file_extension
        with open(downland_photo, 'wb') as new_file:
            new_file.write(save_photo)

    if message.chat.last_name == None:
        message.chat.last_name = "0"
    print(message.chat.username, " / ", message.chat.first_name, " ", message.chat.last_name, ":", " ", message.text,
          " !!! ", b, sep="", end=" /// ")
    with open('talk_with_autor.txt', 'a', encoding="utf-8") as f:
        s = ''.join((message.chat.username, " / ", message.chat.first_name, " ", message.chat.last_name, ":", " ", "0",
                     " !!! ", b, " /// "))
        f.write(s)

    send_message = client.send_message(message.chat.id,
                                       "Автор увидит это фото. Теперь отправьте ещё одно или напишите что-то!")
    client.register_next_step_handler(send_message, talk_with10)


def talk_with4(message):
    c = message.video.file_id
    b = str(message.video.file_name)
    file_photo = client.get_file(c)
    filename, file_extension = os.path.splitext(file_photo.file_path)
    save_photo = client.download_file(file_photo.file_path)
    downland_photo = b + "_" + c + file_extension
    with open(downland_photo, 'wb') as new_file:
        new_file.write(save_photo)

    if message.chat.last_name == None:
        message.chat.last_name = "0"
    print(message.chat.username, " / ", message.chat.first_name, " ", message.chat.last_name, ":", " ", message.text,
          " !!! ", downland_photo, sep="", end=" /// ")
    with open('talk_with_autor.txt', 'a', encoding="utf-8") as f:
        s = ''.join((message.chat.username, " / ", message.chat.first_name, " ", message.chat.last_name, ":", " ", "0",
                     " !!! ", downland_photo, "/// "))
        f.write(s)

    send_message = client.send_message(message.chat.id,
                                       "Автор увидит это видео. Теперь отправьте ещё одно или напишите что-то!")
    client.register_next_step_handler(send_message, talk_with10)


def talk_with5(message):
    c = message.document.file_id
    b = message.document.file_name
    file_photo = client.get_file(c)
    filename, file_extension = os.path.splitext(file_photo.file_path)
    save_photo = client.download_file(file_photo.file_path)
    downland_photo = b + file_extension
    with open(downland_photo, 'wb') as new_file:
        new_file.write(save_photo)

    if message.chat.last_name == None:
        message.chat.last_name = "0"
    print(message.chat.username, " / ", message.chat.first_name, " ", message.chat.last_name, ":", " ", message.text,
          " !!! ", downland_photo, sep="", end=" /// ")
    with open('talk_with_autor.txt', 'a', encoding="utf-8") as f:
        s = ''.join((message.chat.username, " / ", message.chat.first_name, " ", message.chat.last_name, ":", " ", "0",
                     " !!! ",  downland_photo, " /// "))
        f.write(s)

    send_message = client.send_message(message.chat.id,
                                       "Автор увидит это файл. Теперь отправьте ещё один или напишите что-то!")
    client.register_next_step_handler(send_message, talk_with10)

def talk_with10(message):
    if message.content_type == "text":
        print(message.chat.username, " / ", message.chat.first_name, " ", message.chat.last_name, ":", " ", message.text, sep="")
        if message.chat.last_name == None:
            message.chat.last_name = "0"

        with open('talk_with_autor.txt', 'a', encoding="utf-8") as f:
            s = ''.join(
                (message.chat.username, " / ", message.chat.first_name, " ", message.chat.last_name, ":", " ", message.text, "\n",))
            f.write(s)
        client.send_message(message.chat.id, "Автор увидит это сообщение, но вы уже вышли из режима общения с автором")
    else:
        talk_with1(message)

client.polling(none_stop=True, interval=0, timeout=0)