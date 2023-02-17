# Buttons for bot

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Start Button
start_btns = InlineKeyboardMarkup([
    [InlineKeyboardButton("Join Channel ♥️", url="https://t.me/Mdiskshortners_in"),
     InlineKeyboardButton("About Bot 🤖", callback_data="about_data"),
     ],
    [InlineKeyboardButton("Connect Your API 🔗", callback_data="connect_api"
                          ), ]
])


# TO DO web_app=WebAppInfo(url='')
# Back Button
about_btns = InlineKeyboardMarkup([
    [InlineKeyboardButton("◀️ Back️", callback_data="back_data"), ],
])

# Connect button
connect_btns = InlineKeyboardMarkup([
    [InlineKeyboardButton(
        "GET API TOKEN 🔑", url="https://MdiskShortner.in/member/tools/api")],
    [InlineKeyboardButton("◀️ Back️", callback_data="back_data"), ],
])
