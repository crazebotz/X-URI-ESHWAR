
from botbtns import *


API_ID = 16514976
API_HASH = '40bd8634b3836468bb2fb7eafe39d81a'

TOKEN = '5661363625:AAEyBehhT25zbPnkWnAc_n15gCWKlseez6c'



@bot.on_callback_query(filters.regex('about_data'))
def query_handler(_, query):
    query.message.edit(
        text=f'<b>{about_txt}</b>', reply_markup=about_btns, disable_web_page_preview=True)


@bot.on_callback_query(filters.regex('back_data'))
def back_handler(_, query):
    name = query.message.chat.first_name
    query.message.edit(text=start_msg_txt.format(
        firstname=name), reply_markup=start_btns, disable_web_page_preview=True)


@bot.on_callback_query(filters.regex('connect_api'))
def connect_handler(_, query):
    query.message.edit(
        text=connect_txt, reply_markup=connect_btns, disable_web_page_preview=True)
