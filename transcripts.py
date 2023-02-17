# Text Stringss
import os

BOT_TOKEN = os.environ.get('BOT_TOKEN',"mnm")

start_txt = '''Hello {name}, I am [Mdiskshortners.in](https://Mdiskshortners.in/) , Bulk Link Converter. I Can Convert Links Directly From Your [Mdiskshortners.in](https://Mdiskshortners.in/),
    
1. Go To 👉 [Mdiskshortners.in/member/tools/api](https://Mdiskshortners.in/member/tools/api) 

2. Than <b>Copy API Key</b>
3. <i>Than Type /api than give a single space and than paste your API Key (see example to understand more...)</i>

/api API Key 
(See Example.👇)
<b>Example:</b>
<code>/api <api_token></code> 

🔗 <b>Hit</b> 👉 /commands To Know More About How To use This Bot.
🔗 <b>Hit</b> 👉 /api To Know More About How To Link Mdiskshortners.in Account To This Bot.
💁‍♀️ <b>Hit</b> 👉 /help To Get Help.
➕ <b>Hit</b> 👉 /footer To Get Help About Adding your Custom Footer to bot.
🧷 <b>Hit</b> 👉 /unlink To Unlink your account from this Bot.
🤘 <b>Hit</b> 👉 /features To Know More Features Of This Bot.

**MDISKSHORTNERS UPDATE CHANNEL =>** @Mdiskshortners_in

<i>Anyone who want to use any other shortner instead of Mdiskshortner than contact at</i> 👉 @Rahul_Thakor (all shortners support avilable.)'''


start_msg_txt = '''<b>Hey There, {firstname}

🔀 I Can Convert Link To ShortLink
💬 Just Send Me Your Post/Links
🔗 I Will Shorten All Links In It 

🔂 I Can Convert to [Mdiskshortners.in](https://Mdiskshortners.in/)
©️Powered By @Mdiskshortners_in</b>'''

about_txt = '''Hlw {name}.\n**🤖 Name :** Mdisk Shortener
**🔠 Language :** Python3
**📚 Library :** Pyrogram
**🧑🏻‍💻 Developer :** @Rahul_Thakor
©️ Powered By @CrazeBots'''

connect_txt = '''SEND YOUR API TOKEN TO ME

Click On The Button Below
Copy Api Token From Website
Paste & Send Token To Me

Thanks for choosing us...
'''

footer_txt = '''<b>Hello {name}, I am MDISK Links Converter,

🌟 Just Type</b>👉 /footer footer-text

Example:
<code>/footer ━━━━━━━━━━━━━━━━━
💁‍♀️ 🔥𝐉𝐨𝐢𝐧 𝐂𝐡𝐚𝐧𝐧𝐞𝐥🔥 👇
👉 https://t.me/Crazebots</code>

🤘 Hit 👉 /features <i>To Know More Features Of This Bot.</i>

<b>- Message @Rahul_Thakor For More Help -</b>'''

channel_link = """Hello {name}, I am Mdiskshortners.in, Bulk Link Converter. I Can Convert Links Directly From Your Mdiskshortners.in, 

🌟 Type /add_channel (channel link or username)

example:
<code>/add_channel @CrazeBots</code>
Or
/add_channel https://t.me/CrazeBots

🤘 Hit 👉 /features To Know More Features Of This Bot."""

removed_chanel = """Channel Removed Sucessfully✅

type... <code>/add_channel Channel_Link </code> To add again..."""

feature_txt = '''<b>Hello {name}, I am Mdiskshortners.in, Bulk Link Converter Bot. I Can Convert Links Directly From Your Mdiskshortners.in Account,

⚡ Features ⚡
• I can Convert any links or posts to your Mdiskshortner link / post. (Button Links Posts, Hidden links/Hyperlinks All Are Supported)</b>

• <i>If send me a post which has Mdiskshortners.in Links, texts & images... Than i wiil replace all Mdiskshortners.in Links with Conveted Links From Your Linked api Account Automatic And Send Back To You.</i>

• <b>I can Convert unlimited Mdiskshortners.in links at once.</b> <i>(if you are sending a list of urls.)</i>

•<b> No need to share password or email to convert links.


• I Can auto add custom footer text to your every post. Hit 👉 /footer To know more...</b>

<i>Anyone who want to use any other shortner instead of Mdiskshortner than contact at</i> 👉 @Rahul_Thakor (all shortners support avilable.)'''

progress_txt = 'Converting Post'

commands = 'Hlw {name},\n\n**Available Commands:**\n/start or /help to Display START_MSG\n/api or /link to add Your API KEY.\n/add_channel or /channel to Add Your Channel to replace links.\n/del_channel or /remove_channel\n/see_link or /see_channel to See your Channel link if already set.\n/footer to ADD your Custom Footer Text.\n/del_footer to Reset your Footer text.\n/see_footer to SEE Your Custom Footer Text.\n/unlink or /logout to Unlink API KEY\n/feauture or /feature to know bot\'s features\n/commands to display this message.\n/about to know my creator or something...\n\n**ADMIN_CMDs:**\n/users to Check total Users in Bot\n/broadcast to Broadcast MSG to All Users.\n/info to GET All INFO about User.'

un_suc_text = '''__Invalid API token Or Maybe Wrong Format...__ **Please Recheck It And Try Again...

Contact : @Rahul_Thakor For Any Kind Of Help Or Bug Report.**'''

suc_txt = '**Api has been added successfully**'
add_api_txt = 'Please Add Api first using\n/api yourapitoken '
failed_txt = '''Failed to convert...\n\nDue to'''
