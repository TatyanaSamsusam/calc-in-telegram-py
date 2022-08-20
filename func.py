def start(update, context):  
    arg = context.args 
    if not arg:
        context.bot.send_message(update.effective_chat.id, "Привет") #если арг фразы после команды /start не писать, напишет "привет"
    else:
        context.bot.send_message(update.effective_chat.id, f"{' '.join(arg)}") #ловит арг фразу после команды /start и повторяет ее


def info(update, context):
    context.bot.send_message(update.effective_chat.id, "viva la vita!") # после команды /info напишет "viva la vita!"


def message(update, context):
    text = update.message.text
    try: 
        eval(text)
        context.bot.send_message(update.effective_chat.id, f'{text} = {eval(text)}')
    except: 
        if text.lower() == 'привет':
            context.bot.send_message(update.effective_chat.id, 'И тебе привет..') # после сообщения "привет" напишет "привет"
        else:
            context.bot.send_message(update.effective_chat.id, 'я тебя не понимаю') # если сообщение будет не "привет", напишет 'я тебя не понимаю'


def unknown(update, context):
    context.bot.send_message(update.effective_chat.id, f'Шо сказал, не пойму') # словит команду, к-й не существует, и напишет 'Шо сказал, не пойму'

def add(update, context):
    arg = context.args
    print(arg)
    if not arg:
        context.bot.send_message(update.effective_chat.id, 'Вы ничего не введи, нужно ввести числа через пробел после /add')
        return
    try:
        arg = list(map(int, arg))
    except ValueError: 
        context.bot.send_message(update.effective_chat.id, 'Вы ввели не числа')
    res = sum(arg)
    arg = '+'.join(list(map(str,arg)))
    context.bot.send_message(update.effective_chat.id, f'{arg} = {res}')