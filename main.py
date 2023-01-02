#!/usr/bin/python3
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, PollAnswerHandler

#from comebacks import comebacks
from commands import commands

from parameters import TOKEN



def main():

    updater = Updater(TOKEN, use_context=True, request_kwargs={'read_timeout': 40, 'connect_timeout': 1})

    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram

    for name, comm in commands:
        dispatcher.add_handler(CommandHandler(name, comm))
    
    
    # Start the Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()