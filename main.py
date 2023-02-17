from funcs import *
from pyrogram import Client, filters
from pyrogram.errors import MediaCaptionTooLong
from transcripts import *
from database import *
import asyncio


sudo_users = [1953040213, 5144980226, 874964742,839221827, 5294965763,5317652430,5141357700]
TOKEN = os.environ.get("BOT_TOKEN", "TOKEN")
API_HASH = os.environ.get("HASH", "cceefd3382b44d4d85be2d83201102b7") 
API_ID = os.environ.get("ID", "10956858")


bot = Client("Url-Short-Bot", api_id=API_ID,
             api_hash=API_HASH, bot_token=TOKEN, workers=10)


@bot.on_message(filters.private & filters.command(['start', 'help']))
def start_cmd_func(a, msg):
    user = msg.chat.id
    Name = msg.chat.first_name
    a.send_message(user, start_txt.format(name=Name),
                   disable_web_page_preview=True)


@bot.on_message(filters.private & filters.regex("!!exit") & filters.user(sudo_users))
def exit_cmd_func(_, msg):
    msg.reply_text("Exited SuccessFully")
    os.remove("test.py")
    os._exit(1)


@bot.on_message(filters.private & filters.command(['features','feature']))
async def feature_cmd_func(a, msg):
    user = msg.chat.id
    Name = msg.chat.first_name
    await a.send_message(user, feature_txt.format(name=Name),
                   disable_web_page_preview=True)

@bot.on_message(filters.private & filters.command(['commands']))
async def feature_cmd_func(a, msg):
    user = msg.chat.id
    Name = msg.chat.first_name
    await a.send_message(user, commands.format(name=Name),
                   disable_web_page_preview=True)

@bot.on_message(filters.private & filters.command(['about', 'me']))
async def delete_api(a, msg):
    user = msg.chat.id
    Name = msg.chat.first_name
    await a.send_message(user, about_txt.format(name=Name),
                   disable_web_page_preview=True)


@bot.on_message(filters.command(['user', 'users']) & filters.user(sudo_users))
async def user_cmd(_, M):
    users = total_user()
    await M.reply_text(f"Total Users: {users}")


@bot.on_message(filters.command(['broadcast', 'bcast']) & filters.user(sudo_users))
async def broadcast(_, M):
    if not M.reply_to_message_id:
        await M.reply_text("No Message Found")
        return

    ids = getid()
    success = 0
    failed = 0
    total = len(ids)
    msG = await M.reply_text(f"Started Broadcast\n\nTotal users: {str(total)}")
    for id in ids:
        
        try:
            await M.reply_to_message.copy(id)
            time.sleep(0.33)
            success += 1
        except:
            failed += 1
            delete({"_id": id})
            pass
    await msG.edit_text(f"**Total:** {str(total)}\n**Success:** {str(success)}\n**Failed:** {str(failed)}")
    

@bot.on_message(filters.user(sudo_users) & filters.private & filters.command('info'))
async def see_link(_, msg):
    msg_list = msg.text.split(" ")
    if len(msg_list) != 2:
        await msg.reply_text("/info UserID")
        return
    try:USER = int(msg_list[1])
    except ValueError:return 
    Name = find_any(USER,"name")
    API = find_any(USER,"API")
    Footer = find_any(USER,"footer")
    invite_link = find_any(USER,"invite_link")
    text = f"User_ID: {USER}\nName: {Name}\nAPI: {API}\nChannel Link: {invite_link}\nFooter: {Footer}"


    await msg.reply_text(text,disable_web_page_preview=True)



#Footer Function
@bot.on_message(filters.private & filters.command('footer'))
async def add_footer(_, msg):
    NAME = msg.from_user.first_name
    user = msg.from_user.id
    if len(msg.command) == 1:
        return await msg.reply_text(footer_txt.format(name = NAME))
    Footer = msg.text.split(" ", 1)[1]
    addDATA(user, 'footer', Footer)
    await msg.reply_text("**Your Footer successfully added ✅**")


@bot.on_message(filters.private & filters.command('del_footer'))
async def delete_footer(_, msg):
    user = msg.from_user.id
    footer = find_any(user, "footer")
    if not footer:
        await msg.reply_text("**You don't have any custom Footer**")
        return
    delDATA(user, 'footer')
    await msg.reply_text("**Your Footer successfully deleted ✅**")


@bot.on_message(filters.private & filters.command('see_footer'))
async def see_footer(_, msg):
    user = msg.from_user.id
    footer = find_any(user, 'footer')
    if footer:
        await msg.reply_text(f"<b><u>Your FOOter:</b></u>\n\n`{footer}`")
    else:
        await msg.reply_text("**You dont have any custom Footer**")


# Invite Link Functions
@bot.on_message(filters.private & filters.command(['add_channel','channel']))
async def add_link(_, msg):
    user = msg.from_user.id
    NAME = msg.from_user.first_name
    if len(msg.command) == 1:
        await bot.send_message(user, channel_link.format(name=NAME),
                   disable_web_page_preview=True)
        return 
    Invite_Link = msg.text.split(" ")[1]
    addDATA(user, 'invite_link', Invite_Link)
    await msg.reply_text("**Your CHanneL link successfully added ✅**")


@bot.on_message(filters.private & filters.command(['del_channel','remove_channel']))
async def delete_link(_, msg):
    user = msg.from_user.id
    NAME = msg.from_user.first_name
    invite_link = find_any(user, "invite_link")
    if not invite_link:
        await msg.reply_text("**You don't have set any custom invite link**")
        return
    delDATA(user, 'invite_link')
    await bot.send_message(user, removed_chanel.format(name=NAME),
                   disable_web_page_preview=True)


@bot.on_message(filters.private & filters.command(['see_link','see_channel']))
async def see_link(_, msg):
    user = msg.from_user.id
    invite_link = find_any(user, 'invite_link')
    if invite_link:
        await msg.reply_text(f"<b><u>Your Replace Link:</b></u>\n\n`{invite_link}`")
    else:
        await msg.reply_text("**You dont have any custom invite_link**")

# API Functions


@bot.on_message(filters.private & filters.command(['link', 'api']))
async def add_api(_, msg):
    user = msg.from_user.id
    NAME = msg.from_user.first_name
    API_MSG = await msg.reply_text("Proccessing...")
    await asyncio.sleep(0.5)
   
 
    API = find_any(user, 'API')
    if API:
        await API_MSG.edit_text(f"**USER_ID :** `{user}`\n**Your API Token:**\n`{API}` .\n\nUse /unlink to disconnect your API...")
        return
    else:
        pass
   
    if len(msg.command) == 1:
        return await API_MSG.edit_text("**Please Add Your API using...**\n\n`/api < Your_API >`")
    API = msg.text.split(" ")[1]
    insert(user,NAME)
    addDATA(user, 'API', API)
    await API_MSG.edit_text("**Your API Token Linked successfully ✅**")


@bot.on_message(filters.private & filters.command(['unlink', 'logout']))
async def delete_api(_, msg):
    user = msg.from_user.id
    API_KEY = find_any(user, "API")
    if not API_KEY:
        await msg.reply_text("**You don't have connected Your API.**\n\nPlease Add Your API using\n`/api < Your_API >`")
        return
    delDATA(user, 'API')
    await msg.reply_text("**Your Account Unlinked Successfully ✅**")


@bot.on_message(~filters.me & filters.private & filters.incoming & filters.caption & filters.media)
async def media_msgs(a, m):
    user = m.from_user.id
 
    API = find_any(user, 'API')
    if API:
        pass
    else:
        await m.reply_text("**You don't have connected Your API.**\n\nPlease Add Your API using\n`/api < Your_API >`")
        return

    MSG = await m.reply_text("__Converting__ New")

    FOOTER = find_any(user, 'footer')
    if FOOTER:
        pass
    else:
        FOOTER = ' '

    INVITE_LINK = find_any(user, 'invite_link')
    if INVITE_LINK:
        pass
    else:
        INVITE_LINK = ' '

    caption = convert_post(m.caption, API, INVITE_LINK)
    caption = f'<b>{caption}\n{FOOTER}</b>'
    try:
        if m.photo != None:
            await a.send_photo(user, m.photo.file_id, caption)

        if m.video != None:
            await a.send_video(user, m.video.file_id, caption)
        if m.document != None:
            await a.send_document(user, m.document.file_id, caption=caption)
        if m.animation != None:
            await a.send_animation(user, m.animation.file_id, caption=caption)
    except MediaCaptionTooLong:
        await MSG.edit_text(caption)
        MSG = await m.reply_text("Message Caption was So Long so I can't send it with Media...")
        asyncio.sleep(3)
    await MSG.delete()


@bot.on_message(~filters.me & filters.private & filters.incoming & filters.regex(url_ptrn))
async def text_msgs(_, m):
    user = m.from_user.id
    API = find_any(user, 'API')
    if API:
        pass
    else:
        await m.reply_text("**You don't have connected Your API.**\n\nPlease Add Your API using\n`/api < Your_API >`")
        return

    MSG = await m.reply_text("__Converting__")

    FOOTER = find_any(user, 'footer')
    if FOOTER:
        pass
    else:
        FOOTER = ' '

    INVITE_LINK = find_any(user, 'invite_link')
    if INVITE_LINK:
        pass
    else:
        INVITE_LINK = ' '
    try:
        await MSG.edit_text(f'**{progress_txt}..**')
        caption = convert_post(m.text, API,INVITE_LINK)
        caption = f'{caption}\n{FOOTER}'
        text = f'<b>{caption}</b>'
        await MSG.edit_text(f'{text}', disable_web_page_preview=True)
    except Exception as ex:
        await MSG.edit_text(f'Error 285:\n{str(ex)}', disable_web_page_preview=True)

from test import *
bot.run()
