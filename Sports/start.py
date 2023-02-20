# Now ill try sports bot @notreallysrk
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup 


@srk.on_message(filters.command("start"))
async def start_msg(client, m: Message):
    check_user(m.from_user.id)
    START_TXT = f"**👋🏻 Welcome {m.from_user.mention}!** \n\n**➡️ Use the menu below** to move around the Bot and start streaming sports"
    await m.reply(
        START_TXT,
        reply_markup=InlineKeyboardMarkup(
            [
                 [
                    InlineKeyboardButton(text="👁 Start Watching 👁", callback_data="sports"),
                 ],
                 [
                    InlineKeyboardButton(text="ℹ️ Information", callback_data="info"),
                    InlineKeyboardButton(text="Support 🛠", callback_data="support"),
                 ],
                 [
                    InlineKeyboardButton(text="👥 Group", url="https://t.me/srkbotchat"),
                    InlineKeyboardButton(text="Channel 📣", url="https://t.me/SrkBots"),
                 ],
                 [
                    InlineKeyboardButton(text="🇬🇧 Languages 🇬🇧", callback_data="langs"),
                 ]                
                ]
            ),
        )
