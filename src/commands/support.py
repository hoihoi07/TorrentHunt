from src.objs import *

#: Support menu
@bot.message_handler(commands=['support'])
def support(message, userLanguage=None):
    userLanguage = userLanguage or dbSql.getSetting(message.chat.id, 'language')

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text=language['joinChannelBtn'][userLanguage], url='t.me/jetbots'))
    markup.add(telebot.types.InlineKeyboardButton(text=language['shareWithFriendsBtn'][userLanguage], url=f"https://t.me/share/url?url=t.me/TorrentSearch_jetbot&text={language['shareText'][userLanguage]}"), telebot.types.InlineKeyboardButton(text=language['joinDiscussionBtn'][userLanguage], url='t.me/jetbots_support'))
    markup.add(telebot.types.InlineKeyboardButton(text=language['subscribeChannelBtn'][userLanguage], url='https://youtube.com/channel/UCLHwnlTxQFkvMnQsQmD_lWQ'), telebot.types.InlineKeyboardButton(text=language['developer'][userLanguage], url='t.me/jettastic'))
    markup.add(telebot.types.InlineKeyboardButton(text=language['donateBtn'][userLanguage], url=f"t.me/jettastic"))
    
    bot.send_message(message.chat.id, language['support'][userLanguage].format(language['supportBtn'][userLanguage]), reply_markup=markup, disable_web_page_preview=True)
