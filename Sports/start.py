# Now ill try sports bot @notreallysrk
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup 


@srk.on_message(filters.command("start"))
async def start_msg(client, m: Message):
    check_user(m.from_user.id)
    START_TXT = f"**đđģ Welcome {m.from_user.mention}!** \n\n**âĄī¸ Use the menu below** to move around the Bot and start streaming sports"
    await m.reply(
        START_TXT,
        reply_markup=InlineKeyboardMarkup(
            [
                 [
                    InlineKeyboardButton(text="đ Start Watching đ", callback_data="sports"),
                 ],
                 [
                    InlineKeyboardButton(text="âšī¸ Information", callback_data="info"),
                    InlineKeyboardButton(text="Support đ ", callback_data="support"),
                 ],
                 [
                    InlineKeyboardButton(text="đĨ Group", url="https://t.me/srkbotchat"),
                    InlineKeyboardButton(text="Channel đŖ", url="https://t.me/SrkBots"),
                 ],
                 [
                    InlineKeyboardButton(text="đŦđ§ Languages đŦđ§", callback_data="langs"),
                 ]                
                ]
            ),
        )
