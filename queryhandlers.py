from funcs import bot
from botbtns import *

from database import *
from transcripts import *

@bot.on_callback_query(filters.regex('about_data'))
def query_handler(_, query):
    try:
      query.message.edit(
        text=f'<b>{about_txt}</b>', reply_markup=about_btns, disable_web_page_preview=True)
    except:
      pass


@bot.on_callback_query(filters.regex('back_data'))
def back_handler(_, query):
    name = query.message.chat.first_name
    try:
      query.message.edit(text=start_msg_txt.format(
        firstname=name), reply_markup=start_btns, disable_web_page_preview=True)
    except:
      pass


@bot.on_callback_query(filters.regex('mdisk_cb'))
def mdisk_chng_handler(_, query):
    user_id = query.from_user.id
    DOMAIN = "Mdiskshortners.in"
    try:
      query.message.edit(text = change_domain_text.format(DOMAIN),reply_markup=MDISK_ACTIV_BTN,disable_web_page_preview=True)
    except:
      pass
    addDATA(user_id,"DOMAIN",DOMAIN)
    


@bot.on_callback_query(filters.regex('vividisk_cb'))
def vivi_chng_handler(_, query):
    user_id = query.from_user.id
    DOMAIN = "Vividisklinks.in"
    try:
      query.message.edit(text = change_domain_text.format(DOMAIN),reply_markup=VIVI_ACTIV_BTN,disable_web_page_preview=True)
    except:
      pass
    addDATA(user_id,"DOMAIN",DOMAIN)
    

@bot.on_callback_query(filters.regex('close_cb'))
def close_btn(_, query):
    try:
      query.message.delete()
    except:
      pass

@bot.on_callback_query(filters.regex('connect_api'))
def connect_handler(_, query):
    query.message.edit(
        text=connect_txt, reply_markup=connect_btns, disable_web_page_preview=True)
