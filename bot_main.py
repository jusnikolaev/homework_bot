from telegram.ext import Updater, CommandHandler
from wordcount import *
from calculator import *
from planets import *


# Word counter
def bot_wordcount(bot, update, args):
    message = str(args).lower()
    result = wordcount(message)
    result = str(result)
    bot.sendMessage(update.message.chat_id, text=result)


# Calculator
def bot_calc(bot, update, args):
    message = str(args)
    result = calculator_base_message(message)
    result = str(result)
    bot.sendMessage(update.message.chat_id, text=result)


def constellation_bot(bot, update, args):
    planet = str(args[0] if args else '').lower()
    planet_coord = planet_constellation(planet)
    bot.sendMessage(update.message.chat_id, text=str(planet_coord))


def planet_position_bot(bot, update, args):
    planet = str(args[0] if args else '').lower()
    planet_pos = planet_position(planet)
    if not planet_pos:
        bot.sendMessage(update.message.chat_id, text='Sry... I dont know')
    else:
        right_ascension, declination = str(planet_pos.a_ra), str(planet_pos.a_dec)
        bot.sendMessage(update.message.chat_id, text=declination + ' , ' + right_ascension)


def main():
    updater = Updater('330313150:AAGQadkI-7AsUAtR4ZyXm__n8Z5xWQB22r0')
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('wordcount', bot_wordcount, pass_args=True))
    dp.add_handler(CommandHandler('calc', bot_calc, pass_args=True))
    dp.add_handler(CommandHandler('constellation', constellation_bot, pass_args=True))
    dp.add_handler(CommandHandler('position', planet_position_bot, pass_args=True))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
