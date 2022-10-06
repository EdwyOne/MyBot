import telebot

bot = telebot.TeleBot('5637019806:AAG0fxTR5P4VTAAmbUjvguLWdrHVMnKJEco')

name = ''
surname = ''
age = 0
family_dict = {}
n_list = ["1234567890"]


@bot.message_handler(content_types=['text'])
def welcome(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "What's your name?")
        bot.register_next_step_handler(message, get_name)
    elif message.text == '/show':
        bot.send_message(message.from_user.id, f"{len(family_dict.keys())} members in family:\n{family_dict}")


def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "And what is surname?")
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, "How old are you?")
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    global age
    if message.text.isdigit():
        age = int(message.text)
        full_name = f"{name} {surname}"
        family_dict[full_name] = age
        bot.send_message(message.from_user.id, 'Your age is ' + str(age) + ' , your name is ' + name + ' ' + surname)
        bot.send_message(message.from_user.id, "Registered successfully")

    else:
        bot.send_message(message.from_user.id, 'Enter numbers!')
        bot.register_next_step_handler(message, get_age)


bot.infinity_polling()
