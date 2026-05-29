import random

token = '6318580427:AAGM9PPQ0K4_o71MXtG5WWR1NMtrXmsjb6Y'
import telebot
from telebot import types
from random import shuffle

bot=telebot.TeleBot(token)
i=0
# count_true_answer = 0
flag = 0

current_list = []
current_key = []
current_key_txt = []
current_key_dict={}
current_key_txt_dict={}

rule_list = ["Корни с чередованием", "Приставки: ПРЕ/ПРИ", "Приставки на З/С", "Ы/И после присатвок", "Ъ/Ь после приставок",
             "Правописание суффиксов сущ/прилаг/гл", "Правописание суффиксов прилагательных", "Правописание суффиксов гл/прич",
             "О/Ё после шипящих", "И/Ы после Ц", "Спряжение глаголов", "Суффиксы глаголов, завис. от спряжения", "Правописание Н/НН"]
list_users = []
dict_users = {}
fl_rule=False

def questanswer(name_list, name_key, name_key_txt):
    name_list = 'list/' + name_list
    name_key = 'key/' + name_key
    name_key_txt = 'key_txt/' + name_key_txt
    def_list = [j[:-1] for j in open(name_list, encoding='utf-8')]
    def_key_txt = [j[:-1] for j in open(name_key_txt, encoding='utf-8')]
    # name_key = [list(j[:-1]) for j in open("key_1.txt", encoding='utf-8')]
    s = []
    for i in open(name_key, encoding='utf-8'):
        s.append(i[:-1])
    # print(s)
    def_key = []
    for l in s:
        p = l.split(' ')
        def_key.append(p)
        p = []
    return def_list, def_key, def_key_txt

def id_session(name, current_list, current_key_dict, current_key_txt_dict):

    with open(name, 'r', encoding='utf-8') as file:
        # read a list of lines into data
        data = file.readlines()
    print(data)
    '''conc list, dicts in str'''
    current_list_s=''
    current_key_dict_s = str(current_key_dict)
    current_key_txt_dict_s = str(current_key_txt_dict)
    for i in range(len(current_list)-1):
        current_list_s = current_list_s + current_list[i] + 'raz'
    current_list_s += current_list[-1]
    print(current_list_s)

    """ and write everything back"""
    with open(name, 'w', encoding='utf-8') as file:
        file.write('0')
        file.write('\n')
        file.write(current_list_s)
        file.write('\n')
        file.write(current_key_dict_s)
        file.write('\n')
        file.write(current_key_txt_dict_s)


@bot.message_handler(commands=['start'])
def start_message(message):
    global fl_rule
    fl_rule = False
    # bot.send_message(message.chat.id,'Бот запущен')
    bot.send_message(message.chat.id, 'Правила ввода ответов: в заданиях, где нужно согласиться или опровергнуть вопрос, нажимайте кнопки либо ДА либо НЕТ. Где нужно записать ответ, вам требуется ввести слитно в порядке возрастания набор цифр или букв.')
    bot.send_message(message.chat.id, '⬇️Выберите тему из списка, нажав на ☰ в нижнем левом углу')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("/1")
    item4 = types.KeyboardButton("/4")
    item5 = types.KeyboardButton("/5")
    item6 = types.KeyboardButton("/6")
    item7 = types.KeyboardButton("/7")
    item9 = types.KeyboardButton("/9")
    item10 = types.KeyboardButton("/10")
    item11 = types.KeyboardButton("/11")
    item12 = types.KeyboardButton("/12")
    item13 = types.KeyboardButton("/13")
    item14 = types.KeyboardButton("/14")
    item15 = types.KeyboardButton("/15")
    item16 = types.KeyboardButton("/16")
    item17 = types.KeyboardButton("/17")
    item18 = types.KeyboardButton("/18")
    item19 = types.KeyboardButton("/19")
    item_rule = types.KeyboardButton('/rule')
    item_back = types.KeyboardButton("/📜")
    markup.add(item_back)
    #markup.add(item1, item4, item5, item6, item7, item9, item10, item11, item12, item13, item14, item15, item16, item17, item18, item19, item_rule)
    global list_users, dict_users
    list_users.append(str(message.from_user.id))
    for j in list_users:
        dict_users[j]= 'id'+ j
    # bot.send_message(message.chat.id, 'Создание пользовательской сессии и индификация в словаре id')
    print(list_users)
    print(dict_users)
    file_id = open(list_users[-1]+'.txt', 'w+')
    #Список параметров для каждого пользователя: i, списки всех заданий бота построчно
    file_id.writelines(['0\n', '1\n', '2\n', '3\n'])

    #Темы
    '''bot.send_message(message.chat.id, '💈Выбери интересующую тему:💈', reply_markup=markup)
    bot.send_message(message.chat.id, '_1.Средства связи предложений в тексте_ (кнопка:"/1")', parse_mode='Markdown')
    bot.send_message(message.chat.id, '_4.Постановка ударения_ (кнопка:"/4")', parse_mode='Markdown')
    bot.send_message(message.chat.id, '_5.Употребление паронимов_ (кнопка:"/5")', parse_mode='Markdown')
    bot.send_message(message.chat.id, '_6.Лексические нормы_ (кнопка:"/6")', parse_mode='Markdown')
    bot.send_message(message.chat.id, '_7.Морфологические нормы (образование форм слова)_ (кнопка:"/7")', parse_mode='Markdown')
    bot.send_message(message.chat.id, '_9.Правописание корней_ (кнопка:"/9")', parse_mode='Markdown')
    bot.send_message(message.chat.id, '_10.Правописание приставок_ (кнопка:"/10")', parse_mode='Markdown')
    bot.send_message(message.chat.id, '_11.Правописание суффиксов (кроме -Н/НН-)_ (кнопка:"/11")', parse_mode='Markdown')
    bot.send_message(message.chat.id, '_12.Правописание личных окончаний глаголов и суффиксов причастий_ (кнопка:"/12")', parse_mode='Markdown')
    bot.send_message(message.chat.id, '_13.Правописание НЕ и НИ_ (кнопка:"/13")', parse_mode='Markdown')
    bot.send_message(message.chat.id, '_14.Слитное, дефисное, раздельное написание слов_ (кнопка:"/14")', parse_mode='Markdown')
    bot.send_message(message.chat.id, '_15.Правописание -Н- и -НН- в суффиксах_ (кнопка:"/15")', parse_mode='Markdown')
    bot.send_message(message.chat.id, '_16.Пунктуация в сложносочиненном предложении и в предложении с однородными членами_ (кнопка:"/16")', parse_mode='Markdown')
    bot.send_message(message.chat.id, '_17.Знаки препинания в предложениях с обособленными членами_ (кнопка:"/17")', parse_mode='Markdown')
    bot.send_message(message.chat.id, '_18.Знаки препинания при словах и конструкциях, не связанных с членами предложения_ (кнопка:"/18")', parse_mode='Markdown')
    bot.send_message(message.chat.id, '_19.Знаки препинания в сложноподчиненном предложении_ (кнопка:"/19")', parse_mode='Markdown')'''
# @bot.message_handler(commands=['button'])
# def button_message(message):
#     markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
#     item1=types.KeyboardButton("/ne")
#     item2 = types.KeyboardButton("/nn")
#     markup.add(item1, item2)
#     bot.send_message(message.chat.id,'Выбери интересующую тему:',reply_markup=markup)
#     bot.send_message(message.chat.id, '_НЕ с разными частями речи_ (кнопка:"/ne")', parse_mode='Markdown')
#     bot.send_message(message.chat.id, '_Н/НН в разных частях речи_ (кнопка:"/nn")', parse_mode='Markdown')

# @bot.message_handler(content_types=['text']) #initialization markup of anmswer
# def message_reply(message):
#     if message.text=="Не с разными частями речи":
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         item1 = types.KeyboardButton("слитно")
#         item2 = types.KeyboardButton("раздельно")
#         item3 = types.KeyboardButton("список тем")
#         markup.add(item1, item2, item3)
#         bot.send_message(message.chat.id, 'Выберите верный вариант ответа', reply_markup=markup)
#         bot.send_message(message.chat.id, list_ne[0])

@bot.message_handler(commands=['📜'])
def topics_button(message):
    global fl_rule
    fl_rule = False
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("/1")
    item4 = types.KeyboardButton("/4")
    item5 = types.KeyboardButton("/5")
    item6 = types.KeyboardButton("/6")
    item7 = types.KeyboardButton("/7")
    item9 = types.KeyboardButton("/9")
    item10 = types.KeyboardButton("/10")
    item11 = types.KeyboardButton("/11")
    item12 = types.KeyboardButton("/12")
    item13 = types.KeyboardButton("/13")
    item14 = types.KeyboardButton("/14")
    item15 = types.KeyboardButton("/15")
    item16 = types.KeyboardButton("/16")
    item17 = types.KeyboardButton("/17")
    item18 = types.KeyboardButton("/18")
    item19 = types.KeyboardButton("/19")
    item_back = types.KeyboardButton("/📜")
    markup.add(item_back)
    #markup.add(item1, item4, item5, item6, item7, item9, item10, item11, item12, item13, item14, item15, item16, item17, item18, item19)
    '''bot.send_message(message.chat.id, '💈Выбери интересующую тему:💈', reply_markup=markup)
    bot.send_message(message.chat.id, '_1.Средства связи предложений в тексте_ (кнопка:"/1")', parse_mode='Markdown')
    bot.send_message(message.chat.id, '_4.Постановка ударения_ (кнопка:"/4")', parse_mode='Markdown')
    bot.send_message(message.chat.id, '_5.Употребление паронимов_ (кнопка:"/5")', parse_mode='Markdown')
    bot.send_message(message.chat.id, '_6.Лексические нормы_ (кнопка:"/6")', parse_mode='Markdown')
    bot.send_message(message.chat.id, '_7.Морфологические нормы (образование форм слова)_ (кнопка:"/7")', parse_mode='Markdown')
    bot.send_message(message.chat.id, '_9.Правописание корней_ (кнопка:"/9")', parse_mode='Markdown')
    bot.send_message(message.chat.id, '_10.Правописание приставок_ (кнопка:"/10")', parse_mode='Markdown')
    bot.send_message(message.chat.id, '_11.Правописание суффиксов (кроме -Н/НН-)_ (кнопка:"/11")', parse_mode='Markdown')
    bot.send_message(message.chat.id, '_12.Правописание личных окончаний глаголов и суффиксов причастий_ (кнопка:"/12")', parse_mode='Markdown')
    bot.send_message(message.chat.id, '_13.Правописание НЕ и НИ_ (кнопка:"/13")', parse_mode='Markdown')
    bot.send_message(message.chat.id, '_14.Слитное, дефисное, раздельное написание слов_ (кнопка:"/14")', parse_mode='Markdown')
    bot.send_message(message.chat.id, '_15.Правописание -Н- и -НН- в суффиксах_ (кнопка:"/15")', parse_mode='Markdown')
    bot.send_message(message.chat.id, '_16.Пунктуация в сложносочиненном предложении и в предложении с однородными членами_ (кнопка:"/16")', parse_mode='Markdown')
    bot.send_message(message.chat.id, '_17.Знаки препинания в предложениях с обособленными членами_ (кнопка:"/17")', parse_mode='Markdown')
    bot.send_message(message.chat.id, '_18.Знаки препинания при словах и конструкциях, не связанных с членами предложения_ (кнопка:"/18")', parse_mode='Markdown')
    bot.send_message(message.chat.id, '_19.Знаки препинания в сложноподчиненном предложении_ (кнопка:"/19")', parse_mode='Markdown')'''
    bot.send_message(message.chat.id, '⬇️Выберите тему из списка, нажав на ☰ в нижнем левом углу', reply_markup=markup)
    #open session
    id_name = str(message.chat.id) + '.txt'
    with open(id_name, 'w', encoding='utf-8') as file:
        file.write('0')
        file.write('\n')
        file.write('1')
        file.write('\n')
        file.write('2')
        file.write('\n')
        file.write('3')
#Func of button for answer

'''начало тем'''
@bot.message_handler(commands=['1'])
def button_message_1(message):
    global i
    i=0
    global current_list, current_key, current_key_txt, current_key_dict, current_key_txt_dict
    current_list, current_key, current_key_txt = questanswer("list_1.txt", "key_1.txt", "key_txt_1.txt")
    current_key_dict = dict(zip(current_list, current_key))
    current_key_txt_dict = dict(zip(current_list, current_key_txt))
    random.shuffle(current_list)
    '''id сессия: запись задания и прогрессия'''
    id_session(str(message.chat.id)+'.txt', current_list, current_key_dict, current_key_txt_dict)

    # bot.send_message(message.chat.id, '1 is working')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #item1 = types.KeyboardButton("1")
    #item2 = types.KeyboardButton("2")
    item3 = types.KeyboardButton("/📜")
    markup.add(item3)
    bot.send_message(message.chat.id, '📝Подберите указанное средство связи вместо пропуска', reply_markup=markup)
    bot.send_message(message.chat.id, current_list[0], reply_markup=markup)
    print(i)
    global flag
    flag = 0
i=0
@bot.message_handler(commands=['4'])
def button_message_4(message):
    global i
    i=0
    global current_list, current_key, current_key_txt, current_key_dict, current_key_txt_dict
    current_list, current_key, current_key_txt = questanswer("list_4.txt", "key_4.txt", "key_txt_4.txt")
    current_key_dict = dict(zip(current_list, current_key))
    current_key_txt_dict = dict(zip(current_list, current_key_txt))
    random.shuffle(current_list)
    '''id сессия: запись задания и прогрессии в номерной id файл'''
    id_session(str(message.chat.id) + '.txt', current_list, current_key_dict, current_key_txt_dict)

    # print(current_key_txt)
    # bot.send_message(message.chat.id, '4 is working')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("да")
    item2 = types.KeyboardButton("нет")
    item3 = types.KeyboardButton("/📜")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, '📝Правильно ли выделена буква, обозначающая ударный гласный звук?', reply_markup=markup)
    bot.send_message(message.chat.id, current_list[0], reply_markup=markup)
    print(i)
    global flag
    flag = 0

@bot.message_handler(commands=['5'])
def button_message_5(message):
    global i
    i=0
    global current_list, current_key, current_key_txt, current_key_dict, current_key_txt_dict
    current_list, current_key, current_key_txt = questanswer("list_5.txt", "key_5.txt", "key_txt_5.txt")
    current_key_dict = dict(zip(current_list, current_key))
    current_key_txt_dict = dict(zip(current_list, current_key_txt))
    random.shuffle(current_list)
    '''id сессия: запись задания и прогрессии в номерной id файл'''
    id_session(str(message.chat.id) + '.txt', current_list, current_key_dict, current_key_txt_dict)

    # print(current_key_txt)
    #bot.send_message(message.chat.id, '5 is working')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("да")
    item2 = types.KeyboardButton("нет")
    item3 = types.KeyboardButton("/📜")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, '📝Верно ли употреблено выделенное слово?', reply_markup=markup)
    bot.send_message(message.chat.id, current_list[0], reply_markup=markup)
    print(i)
    global flag
    flag = 0

@bot.message_handler(commands=['6'])
def button_message_6(message):
    global i
    i=0
    global current_list, current_key, current_key_txt, current_key_dict, current_key_txt_dict
    current_list, current_key, current_key_txt = questanswer("list_6.txt", "key_6.txt", "key_txt_6.txt")
    current_key_dict = dict(zip(current_list, current_key))
    current_key_txt_dict = dict(zip(current_list, current_key_txt))
    random.shuffle(current_list)
    '''id сессия: запись задания и прогрессии в номерной id файл'''
    id_session(str(message.chat.id) + '.txt', current_list, current_key_dict, current_key_txt_dict)

    # print(current_key_txt)
    #bot.send_message(message.chat.id, '6 is working')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # item1 = types.KeyboardButton("да")
    # item2 = types.KeyboardButton("нет")
    item3 = types.KeyboardButton("/📜")
    markup.add(item3)
    bot.send_message(message.chat.id, '📝Отредактируйте предложение: исправьте лексическую ошибку, заменив или исключив неверно употреблённое слово. Запишите подобранное либо исключённое вами слово.', reply_markup=markup)
    bot.send_message(message.chat.id, current_list[0], reply_markup=markup)
    print(i)
    global flag
    flag = 0

@bot.message_handler(commands=['7'])
def button_message_7(message):
    global i
    i=0
    global current_list, current_key, current_key_txt, current_key_dict, current_key_txt_dict
    current_list, current_key, current_key_txt = questanswer("list_7.txt", "key_7.txt", "key_txt_7.txt")
    current_key_dict = dict(zip(current_list, current_key))
    current_key_txt_dict = dict(zip(current_list, current_key_txt))
    random.shuffle(current_list)
    '''id сессия: запись задания и прогрессии в номерной id файл'''
    id_session(str(message.chat.id) + '.txt', current_list, current_key_dict, current_key_txt_dict)

    # print(current_key_txt)
    #bot.send_message(message.chat.id, '7 is working')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # item1 = types.KeyboardButton("да")
    # item2 = types.KeyboardButton("нет")
    item3 = types.KeyboardButton("/📜")
    markup.add(item3)
    bot.send_message(message.chat.id, '📝Допущена ли ошибка в образовании формы слова в выделенном слове? Если ошибка есть, то исправьте ее и запишите слово правильно. Если же ошибки нет, то перепишите исходное слово.', reply_markup=markup)
    bot.send_message(message.chat.id, current_list[0], reply_markup=markup)
    print(i)
    global flag
    flag = 0

@bot.message_handler(commands=['9'])
def button_message_9(message):
    global i
    i=0
    global current_list, current_key, current_key_txt, current_key_dict, current_key_txt_dict
    current_list, current_key, current_key_txt = questanswer("list_9.txt", "key_9.txt", "key_txt_9.txt")
    current_key_dict = dict(zip(current_list, current_key))
    current_key_txt_dict = dict(zip(current_list, current_key_txt))
    random.shuffle(current_list)
    '''id сессия: запись задания и прогрессии в номерной id файл'''
    id_session(str(message.chat.id) + '.txt', current_list, current_key_dict, current_key_txt_dict)

    # print(current_key_txt)
    #bot.send_message(message.chat.id, '9 is working')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("да")
    item2 = types.KeyboardButton("нет")
    item3 = types.KeyboardButton("/📜")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, '📝Пропущена ли в словах данного ряда одна и та же буква? В объяснении правильных ответах вы можете встретить аббреавиатуры ПГ, ЧГ, НГ, где ПГ-проверяемая гласная, ЧГ-чередующаяся гласная, НГ-непроверяемая гласная.', reply_markup=markup)
    bot.send_message(message.chat.id, current_list[0], reply_markup=markup)
    print(i)
    global flag
    flag = 0

@bot.message_handler(commands=['10'])
def button_message_10(message):
    global i
    i=0
    global current_list, current_key, current_key_txt, current_key_dict, current_key_txt_dict
    current_list, current_key, current_key_txt = questanswer("list_10.txt", "key_10.txt", "key_txt_10.txt")
    current_key_dict = dict(zip(current_list, current_key))
    current_key_txt_dict = dict(zip(current_list, current_key_txt))
    random.shuffle(current_list)
    '''id сессия: запись задания и прогрессии в номерной id файл'''
    id_session(str(message.chat.id) + '.txt', current_list, current_key_dict, current_key_txt_dict)

    # print(current_key_txt)
    #bot.send_message(message.chat.id, '10 is working')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("да")
    item2 = types.KeyboardButton("нет")
    item3 = types.KeyboardButton("/📜")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, '📝Пропущена ли в словах данного ряда одна и та же буква?', reply_markup=markup)
    bot.send_message(message.chat.id, current_list[0], reply_markup=markup)
    print(i)
    global flag
    flag = 0

@bot.message_handler(commands=['11'])
def button_message_11(message):
    global i
    i=0
    global current_list, current_key, current_key_txt, current_key_dict, current_key_txt_dict
    current_list, current_key, current_key_txt = questanswer("list_11.txt", "key_11.txt", "key_txt_11.txt")
    current_key_dict = dict(zip(current_list, current_key))
    current_key_txt_dict = dict(zip(current_list, current_key_txt))
    random.shuffle(current_list)
    '''id сессия: запись задания и прогрессии в номерной id файл'''
    id_session(str(message.chat.id) + '.txt', current_list, current_key_dict, current_key_txt_dict)

    # print(current_key_txt)
    #bot.send_message(message.chat.id, '11 is working')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("да")
    item2 = types.KeyboardButton("нет")
    item3 = types.KeyboardButton("/📜")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, '📝Пропущена ли в словах данного ряда одна и та же буква?', reply_markup=markup)
    bot.send_message(message.chat.id, current_list[0], reply_markup=markup)
    print(i)
    global flag
    flag = 0

@bot.message_handler(commands=['12'])
def button_message_12(message):
    global i
    i=0
    global current_list, current_key, current_key_txt, current_key_dict, current_key_txt_dict
    current_list, current_key, current_key_txt = questanswer("list_12.txt", "key_12.txt", "key_txt_12.txt")
    current_key_dict = dict(zip(current_list, current_key))
    current_key_txt_dict = dict(zip(current_list, current_key_txt))
    random.shuffle(current_list)
    '''id сессия: запись задания и прогрессии в номерной id файл'''
    id_session(str(message.chat.id) + '.txt', current_list, current_key_dict, current_key_txt_dict)

    # print(current_key_txt)
    #bot.send_message(message.chat.id, '12 is working')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("да")
    item2 = types.KeyboardButton("нет")
    item3 = types.KeyboardButton("/📜")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, '📝Пропущена ли в словах данного ряда одна и та же буква?', reply_markup=markup)
    bot.send_message(message.chat.id, current_list[0], reply_markup=markup)
    print(i)
    global flag
    flag = 0

@bot.message_handler(commands=['13'])
def button_message_13(message):
    global i
    i=0
    global current_list, current_key, current_key_txt, current_key_dict, current_key_txt_dict
    current_list, current_key, current_key_txt = questanswer("list_13.txt", "key_13.txt", "key_txt_13.txt")
    current_key_dict = dict(zip(current_list, current_key))
    current_key_txt_dict = dict(zip(current_list, current_key_txt))
    random.shuffle(current_list)
    '''id сессия: запись задания и прогрессии в номерной id файл'''
    id_session(str(message.chat.id) + '.txt', current_list, current_key_dict, current_key_txt_dict)

    # print(current_key_txt)
    #bot.send_message(message.chat.id, '13 is working')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("слитно")
    item2 = types.KeyboardButton("раздельно")
    item3 = types.KeyboardButton("/📜")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, '📝Как НЕ/НИ пишется с выделенным словом?', reply_markup=markup)
    bot.send_message(message.chat.id, current_list[0], reply_markup=markup)
    print(i)
    global flag
    flag = 0

@bot.message_handler(commands=['14'])
def button_message_14(message):
    global i
    i=0
    global current_list, current_key, current_key_txt, current_key_dict, current_key_txt_dict
    current_list, current_key, current_key_txt = questanswer("list_14.txt", "key_14.txt", "key_txt_14.txt")
    current_key_dict = dict(zip(current_list, current_key))
    current_key_txt_dict = dict(zip(current_list, current_key_txt))
    random.shuffle(current_list)
    '''id сессия: запись задания и прогрессии в номерной id файл'''
    id_session(str(message.chat.id) + '.txt', current_list, current_key_dict, current_key_txt_dict)

    # print(current_key_txt)
    #bot.send_message(message.chat.id, '14 is working')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("да")
    item2 = types.KeyboardButton("нет")
    item3 = types.KeyboardButton("/📜")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, '📝Одинаково ли пишутся все выделенные слова(слитно, раздельно или через дефис)?', reply_markup=markup)
    bot.send_message(message.chat.id, current_list[0], reply_markup=markup)
    print(i)
    global flag
    flag = 0

@bot.message_handler(commands=['15'])
def button_message_15(message):
    global i
    i=0
    global current_list, current_key, current_key_txt, current_key_dict, current_key_txt_dict
    current_list, current_key, current_key_txt = questanswer("list_15.txt", "key_15.txt", "key_txt_15.txt")
    current_key_dict = dict(zip(current_list, current_key))
    current_key_txt_dict = dict(zip(current_list, current_key_txt))
    random.shuffle(current_list)
    '''id сессия: запись задания и прогрессии в номерной id файл'''
    id_session(str(message.chat.id) + '.txt', current_list, current_key_dict, current_key_txt_dict)

    # print(current_key_txt)
    #bot.send_message(message.chat.id, '15 is working')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # item1 = types.KeyboardButton("да")
    # item2 = types.KeyboardButton("нет")
    item3 = types.KeyboardButton("/📜")
    markup.add(item3)
    bot.send_message(message.chat.id, '📝Запишите все цифры, на месте которых пишется столько букв Н, сколько указано в примере.', reply_markup=markup)
    bot.send_message(message.chat.id, current_list[0], reply_markup=markup)
    print(i)
    global flag
    flag = 0

@bot.message_handler(commands=['16'])
def button_message_16(message):
    global i
    i=0
    global current_list, current_key, current_key_txt, current_key_dict, current_key_txt_dict
    current_list, current_key, current_key_txt = questanswer("list_16.txt", "key_16.txt", "key_txt_16.txt")
    current_key_dict = dict(zip(current_list, current_key))
    current_key_txt_dict = dict(zip(current_list, current_key_txt))
    random.shuffle(current_list)
    '''id сессия: запись задания и прогрессии в номерной id файл'''
    id_session(str(message.chat.id) + '.txt', current_list, current_key_dict, current_key_txt_dict)

    # print(current_key_txt)
    #bot.send_message(message.chat.id, '16 is working')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("да")
    item2 = types.KeyboardButton("нет")
    item3 = types.KeyboardButton("/📜")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, '📝Нужно ли в данном предложении поставить только ОДНУ запятую?', reply_markup=markup)
    bot.send_message(message.chat.id, current_list[0], reply_markup=markup)
    print(i)
    global flag
    flag = 0

@bot.message_handler(commands=['17'])
def button_message_15(message):
    global i
    i=0
    global current_list, current_key, current_key_txt, current_key_dict, current_key_txt_dict
    current_list, current_key, current_key_txt = questanswer("list_17.txt", "key_17.txt", "key_txt_17.txt")
    current_key_dict = dict(zip(current_list, current_key))
    current_key_txt_dict = dict(zip(current_list, current_key_txt))
    random.shuffle(current_list)
    '''id сессия: запись задания и прогрессии в номерной id файл'''
    id_session(str(message.chat.id) + '.txt', current_list, current_key_dict, current_key_txt_dict)

    # print(current_key_txt)
    #bot.send_message(message.chat.id, '17 is working')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # item1 = types.KeyboardButton("да")
    # item2 = types.KeyboardButton("нет")
    item3 = types.KeyboardButton("/📜")
    markup.add(item3)
    bot.send_message(message.chat.id, '📝Запишите все цифры, на месте которых в предложении должна(-ы) стоять запятая(-ые).', reply_markup=markup)
    bot.send_message(message.chat.id, current_list[0], reply_markup=markup)
    print(i)
    global flag
    flag = 0

@bot.message_handler(commands=['18'])
def button_message_18(message):
    global i
    i=0
    global current_list, current_key, current_key_txt, current_key_dict, current_key_txt_dict
    current_list, current_key, current_key_txt = questanswer("list_18.txt", "key_18.txt", "key_txt_18.txt")
    current_key_dict = dict(zip(current_list, current_key))
    current_key_txt_dict = dict(zip(current_list, current_key_txt))
    random.shuffle(current_list)
    '''id сессия: запись задания и прогрессии в номерной id файл'''
    id_session(str(message.chat.id) + '.txt', current_list, current_key_dict, current_key_txt_dict)

    # print(current_key_txt)
    #bot.send_message(message.chat.id, '18 is working')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # item1 = types.KeyboardButton("да")
    # item2 = types.KeyboardButton("нет")
    item3 = types.KeyboardButton("/📜")
    markup.add(item3)
    bot.send_message(message.chat.id, '📝Запишите все цифры, на месте которых в предложении должна(-ы) стоять запятая(-ые).', reply_markup=markup)
    bot.send_message(message.chat.id, current_list[0], reply_markup=markup)
    print(i)
    global flag
    flag = 0

@bot.message_handler(commands=['19'])
def button_message_19(message):
    global i
    i=0
    global current_list, current_key, current_key_txt, current_key_dict, current_key_txt_dict
    current_list, current_key, current_key_txt = questanswer("list_19.txt", "key_19.txt", "key_txt_19.txt")
    current_key_dict = dict(zip(current_list, current_key))
    current_key_txt_dict = dict(zip(current_list, current_key_txt))
    random.shuffle(current_list)
    '''id сессия: запись задания и прогрессии в номерной id файл'''
    id_session(str(message.chat.id) + '.txt', current_list, current_key_dict, current_key_txt_dict)

    # print(current_key_txt)
    #bot.send_message(message.chat.id, '19 is working')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # item1 = types.KeyboardButton("да")
    # item2 = types.KeyboardButton("нет")
    item3 = types.KeyboardButton("/📜")
    markup.add(item3)
    bot.send_message(message.chat.id, '📝Запишите все цифры, на месте которых в предложении должна(-ы) стоять запятая(-ые).', reply_markup=markup)
    bot.send_message(message.chat.id, current_list[0], reply_markup=markup)
    print(i)
    global flag
    flag = 0


@bot.message_handler(commands=['rule'])
def button_message_rule(message):
    global i, rule_list, fl_rule
    i=0
    s=''
    for k in range(1, len(rule_list)+1):
        s = s + str(k) + '-' + rule_list[k-1] + '\n'
    print('string of rule', s)
    fl_rule = True
    with open(str(message.chat.id)+'.txt', 'w+', encoding='utf-8') as file:
        file.write('1')
        file.write('\n')
        file.write('p'*20)
        file.write('\n')
        file.write('p'*20)
        file.write('\n')
        file.write('p'*20)

    #bot.send_message(message.chat.id, 'rule is working')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("п.1")
    item2 = types.KeyboardButton("п.2")
    item3 = types.KeyboardButton("п.3")
    item4 = types.KeyboardButton("п.4")
    item5 = types.KeyboardButton("п.5")
    item6 = types.KeyboardButton("п.6")
    item7 = types.KeyboardButton("п.7")
    item8 = types.KeyboardButton("п.8")
    item9 = types.KeyboardButton("п.9")
    item10 = types.KeyboardButton("п.10")
    item11 = types.KeyboardButton("п.11")
    item12 = types.KeyboardButton("п.12")
    item13 = types.KeyboardButton("п.13")
    item_back = types.KeyboardButton("/📜")
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item_back)
    bot.send_message(message.chat.id, '📝Выберите правило, нажав на меню текстовых кнопок↘️.', reply_markup=markup)
    bot.send_message(message.chat.id, '📝Список правил:'+s, reply_markup=markup)
    global flag
    flag = 0

'''конец тем'''
# @bot.message_handler(content_types=['text'])
# def message_ans(message):
#     bot.send_message(message.chat.id, 'Функция запрос-ответ пошла')
#     if message.text == key_ne[list_ne[0]]:
#         bot.send_message(message.chat.id, 'ответ верный')
#
#     else:
#         bot.send_message(message.chat.id, 'ответ неверный')
#
#     bot.send_message(message.chat.id, 'следующий пример')
#
#     for i in range(1, len(list_ne)):
#         bot.send_message(message.chat.id, list_ne[i]) #output of work (2-end)
#
#
#         if message.text == key_ne[list_ne[i]]:
#             bot.send_message(message.chat.id, 'ответ верный')
#         elif message.text != key_ne[list_ne[i]]:
#             bot.send_message(message.chat.id, 'ответ неверный')
#         elif message.text == 'список тем':
#             @bot.message_handler(commands=['button'])
#             def button_message(message):
#                 markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#                 item1 = types.KeyboardButton("Не с разными частями речи")
#                 markup.add(item1)
#                 bot.send_message(message.chat.id, 'Выбери интересующую тему', reply_markup=markup)
#             break
#         bot.send_message(message.chat.id, 'следующий пример')

# for i in range(0, len(list_ne), 1):
#
#     fl = False
#     @bot.message_handler(content_types=['text'])
#     def message_ans(message):
#
#         global i
#         i-=1
#         bot.send_message(message.chat.id, 'Функция ответa и проверки пошла')
        # bot.send_message(message.chat.id, list_ne[i])  # output of work (2-end)
        # print(i)
        # if message.text == key_ne[list_ne[i]]:
        #     bot.send_message(message.chat.id, 'ответ верный')
        # elif message.text == 'tem':
        #     global fl
        #     fl = True
        #
        #     @bot.message_handler(commands=['button'])
        #     def button_message(message):
        #         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        #         item1 = types.KeyboardButton("Не с разными частями речи")
        #         markup.add(item1)
        #         bot.send_message(message.chat.id, 'Выбери интересующую тему', reply_markup=markup)
        # elif message.text != key_ne[list_ne[i]] and message.text!= 'tem':
        #     bot.send_message(message.chat.id, 'ответ неверный')
        # elif fl==True:
        #     bot.send_message(message.chat.id, list_ne[i])
    # print(fl)
    # if fl==True:
    #     @bot.message_handler(content_types=['text'])
    #     def button_message(message):
    #         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #         item1 = types.KeyboardButton("Не с разными частями речи")
    #         markup.add(item1)
    #         bot.send_message(message.chat.id, 'Выбери интересующую тему', reply_markup=markup)
    #     break



#Input and operand answer

i=0
flag = 0

'''обработчик правил'''
'''@bot.message_handler(content_types=['text'])
def message_rule(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_back = types.KeyboardButton('/📜')
    markup.add(item_back)
    if message.text == 'п.1':
        with open('Корни_с_чередованием1.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
        with open('Корни_с_чередованием2.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
        with open('Корни_с_чередованием3.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    elif message.text == 'п.2':
        with open('при1.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
        with open('при2.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
        with open('при3.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
        with open('при4.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
        with open('при5.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    elif message.text == 'п.3':
        with open('зс.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    elif message.text == 'п.4':
        with open('ы.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    elif message.text == 'п.5':
        with open('ъ1.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
        with open('ъ2.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    elif message.text == 'п.6':
        with open('суф1.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
        with open('суф2.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    elif message.text == 'п.7':
        with open('суфприл1.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
        with open('суфприл2.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    elif message.text == 'п.8':
        with open('суфгл.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    elif message.text == 'п.9':
        with open('оё.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    elif message.text == 'п.10':
        with open('ыи.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    elif message.text == 'п.11':
        with open('спр.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    elif message.text == 'п.12':
        with open('суфспр1.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
        with open('суфспр2.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    elif message.text == 'п.13':
        with open('н1.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
        with open('н2.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)'''

'''ОБРАБОТЧИК ОТВЕТОВ'''
@bot.message_handler(content_types=['text'])
def message_ans(message):
    global i, count_true_answer
    global flag, dict_users, k, fl_rule
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    id_name = str(message.chat.id)+'.txt'
#    i = exec("id{}={}".format(dict_users[str(message.chat.id)], k))
    '''Открытие сессии юзера'''
    with open(id_name, 'r+', encoding='utf-8') as f:
        s = f.readlines()
        print('s', s)
        '''убираем \n в i, current_list, current_dict'''
        s_new = []
        for element in s:
            s_new.append(element.rstrip('\n'))
        print("s без /n", s_new)
        i = int(s_new[0])
        if fl_rule == False:
            current_list = s_new[1].split('raz')
            current_key_dict = eval(s_new[2])
            current_key_txt_dict = eval(s_new[3])
    if message.text[0:2]!='п.' and message.text in current_key_dict[current_list[i]]:
        bot.send_message(message.chat.id, '✅*ответ верный*', parse_mode="Markdown")
        bot.send_message(message.chat.id, '...', parse_mode="Markdown")
    elif message.text[0:2]!='п.' and message.text not in current_key_dict[current_list[i]] and message.text != '/📜':
        bot.send_message(message.chat.id, '❌*ответ неверный*', parse_mode="Markdown")
        bot.send_message(message.chat.id, '❗_правильно_: '+current_key_txt_dict[current_list[i]], parse_mode="Markdown")
        bot.send_message(message.chat.id, '...', parse_mode="Markdown")
    elif message.text[0:2]=='п.':
        if message.text == 'п.1':
            with open('screens/Корни_с_чередованием1.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
            with open('screens/Корни_с_чередованием2.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
            with open('screens/Корни_с_чередованием3.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
        elif message.text == 'п.2':
            with open('screens/при1.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
            with open('screens/при2.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
            with open('screens/при3.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
            with open('screens/при4.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
            with open('screens/при5.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
        elif message.text == 'п.3':
            with open('screens/зс.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
        elif message.text == 'п.4':
            with open('screens/ы.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
        elif message.text == 'п.5':
            with open('screens/ъ1.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
            with open('screens/ъ2.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
        elif message.text == 'п.6':
            with open('screens/суф1.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
            with open('screens/суф2.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
        elif message.text == 'п.7':
            with open('screens/суфприл1.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
            with open('screens/суфприл2.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
        elif message.text == 'п.8':
            with open('screens/суфгл.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
        elif message.text == 'п.9':
            with open('screens/оё.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
        elif message.text == 'п.10':
            with open('screens/ыи.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
        elif message.text == 'п.11':
            with open('screens/спр.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
        elif message.text == 'п.12':
            with open('screens/суфспр1.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
            with open('screens/суфспр2.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
        elif message.text == 'п.13':
            with open('screens/н1.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
            with open('screens/н2.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
    elif message.text == '/📜':
        fl_rule=False
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("/1")
        item4 = types.KeyboardButton("/4")
        item5 = types.KeyboardButton("/5")
        item6 = types.KeyboardButton("/6")
        item7 = types.KeyboardButton("/7")
        item9 = types.KeyboardButton("/9")
        item10 = types.KeyboardButton("/10")
        item11 = types.KeyboardButton("/11")
        item12 = types.KeyboardButton("/12")
        item13 = types.KeyboardButton("/13")
        item14 = types.KeyboardButton("/14")
        item15 = types.KeyboardButton("/15")
        item16 = types.KeyboardButton("/16")
        item17 = types.KeyboardButton("/17")
        item18 = types.KeyboardButton("/18")
        item19 = types.KeyboardButton("/19")
        markup.add(item1, item4, item5, item6, item7, item9, item10, item11, item12, item13, item14, item15, item16, item17, item18, item19)
        # bot.send_message(message.chat.id, 'Ваш результат: ' + str(round(count_true_answer / len(current_list) * 100)) + '% правильных ответов', reply_markup=markup)
        # count_true_answer = 0
        bot.send_message(message.chat.id, '💈Выбери интересующую тему:💈', reply_markup=markup)
        bot.send_message(message.chat.id, '_1.Средства связи предложений в тексте_ (кнопка:"/1")', parse_mode='Markdown')
        bot.send_message(message.chat.id, '_4.Постановка ударения_ (кнопка:"/4")', parse_mode='Markdown')
        bot.send_message(message.chat.id, '_5.Употребление паронимов_ (кнопка:"/5")', parse_mode='Markdown')
        bot.send_message(message.chat.id, '_6.Лексические нормы_ (кнопка:"/6")', parse_mode='Markdown')
        bot.send_message(message.chat.id, '_7.Морфологические нормы (образование форм слова)_ (кнопка:"/7")', parse_mode='Markdown')
        bot.send_message(message.chat.id, '_9.Правописание корней_ (кнопка:"/9")', parse_mode='Markdown')
        bot.send_message(message.chat.id, '_10.Правописание приставок_ (кнопка:"/10")', parse_mode='Markdown')
        bot.send_message(message.chat.id, '_11.Правописание суффиксов (кроме -Н/НН-)_ (кнопка:"/11")', parse_mode='Markdown')
        bot.send_message(message.chat.id, '_12.Правописание личных окончаний глаголов и суффиксов причастий_ (кнопка:"/12")', parse_mode='Markdown')
        bot.send_message(message.chat.id, '_13.Правописание НЕ и НИ_ (кнопка:"/13")', parse_mode='Markdown')
        bot.send_message(message.chat.id, '_14.Слитное, дефисное, раздельное написание слов_ (кнопка:"/14")', parse_mode='Markdown')
        bot.send_message(message.chat.id, '_15.Правописание -Н- и -НН- в суффиксах_ (кнопка:"/15")', parse_mode='Markdown')
        bot.send_message(message.chat.id, '_16.Пунктуация в сложносочиненном предложении и в предложении с однородными членами_ (кнопка:"/16")', parse_mode='Markdown')
        bot.send_message(message.chat.id, '_17.Знаки препинания в предложениях с обособленными членами_ (кнопка:"/17")', parse_mode='Markdown')
        bot.send_message(message.chat.id, '_18.Знаки препинания при словах и конструкциях, не связанных с членами предложения_ (кнопка:"/18")', parse_mode='Markdown')
        bot.send_message(message.chat.id, '_19.Знаки препинания в сложноподчиненном предложении_ (кнопка:"/19")', parse_mode='Markdown')
        flag = 1
        i=0
        with open(id_name, 'w', encoding='utf-8') as file:
            file.write('0')
            file.write('\n')
            file.write('1')
            file.write('\n')
            file.write('2')
            file.write('\n')
            file.write('3')
    i+=1
    '''Запись прогресса сессии юзера'''
    with open(id_name, 'w', encoding='utf-8') as file:
        if fl_rule==False:
            current_list_s = ''
            current_key_dict_s = str(current_key_dict)
            current_key_txt_dict_s = str(current_key_txt_dict)
            for j in range(len(current_list)-1):
                current_list_s = current_list_s + current_list[j] + 'raz'
            current_list_s += current_list[-2]
            print(current_list[-2])
            print(len(current_list_s.split('raz')))
            '''ГДЕ-ТО ЗДЕСЬ КОСЯК был, теперь норм'''
            file.write(str(i))
            file.write('\n')
            file.write(current_list_s)
            file.write('\n')
            file.write(current_key_dict_s)
            file.write('\n')
            file.write(current_key_txt_dict_s)
        elif fl_rule==True:
            file.write('1')
            file.write('\n')
            file.write('p' * 20)
            file.write('\n')
            file.write('p' * 20)
            file.write('\n')
            file.write('p' * 20)
    with open(id_name, 'r', encoding='utf-8') as file:
        # read a list of lines into data
        data = file.readlines()
    print('na conec obrabotky', data)
    print(i)
    try:
        if flag == 0 and fl_rule==False:
            bot.send_message(message.chat.id, current_list[i])
        elif flag!=0:
            i = 0
            with open(id_name, 'w', encoding='utf-8') as file:
                file.write('0')
                file.write('\n')
                file.write('1')
                file.write('\n')
                file.write('2')
                file.write('\n')
                file.write('3')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("/📜")
            markup.add(item1)
            # bot.send_message(message.chat.id, 'Ваш результат: ' + str(round(count_true_answer / len(current_list) * 100)) + '% правильных ответов', reply_markup=markup)
            # count_true_answer = 0
            bot.send_message(message.chat.id,'📋Блок заданий завершён. Вы можете перейти к другому блоку заданий, нажав на кнопку: /📜',reply_markup=markup)
    except:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("/📜")
        markup.add(item1)
        bot.send_message(message.chat.id,'📋Блок заданий завершён. Вы можете перейти к другому блоку заданий, нажав на кнопку: /📜', reply_markup=markup)
        i = 0
        with open(id_name, 'w', encoding='utf-8') as file:
            file.write('0')
            file.write('\n')
            file.write('1')
            file.write('\n')
            file.write('2')
            file.write('\n')
            file.write('3')
        flag = 1

bot.infinity_polling()
# bot.polling(non_stop = True)