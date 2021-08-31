from pyrogram import Client, filters
from pyrogram.types import Message
from tagadmin import COMMAND_HAND_LER

# -- Constants -- #
START_TEXT = """
Hey {}

I'm @{}, một bot đơn giản để gắn thẻ tất cả quản trị viên trong một \
nhóm dễ dàng bằng cách nhập @admin hoặc @admins

/help - Hiển thị thông báo trợ giúp
"""

HELP_TEXT = f"""
{COMMAND_HAND_LER}start - Hiển thị thông báo Bắt đầu.
{COMMAND_HAND_LER}help - Kiểm tra thông báo trợ giúp này.
{COMMAND_HAND_LER}donate - Nhận thông tin về việc ủng hộ cho chủ sở hữu của tôi.
@admin / @admins - Gắn thẻ tất cả các quản trị viên
"""
# -- Constants End -- #


@Client.on_message(filters.command("help", COMMAND_HAND_LER))
async def help_bot(c: Client, m: Message):

    await m.reply_text(
        HELP_TEXT, parse_mode="markdown", reply_to_message_id=m.message_id
    )
    return


@Client.on_message(filters.command("start", COMMAND_HAND_LER))
async def start_bot(c: Client, m: Message):

    user = m.from_user.first_name
    bot = await c.get_me()

    await m.reply_text(
        START_TEXT.format(user, bot.username),
        disable_web_page_preview=True,
        reply_to_message_id=m.message_id,
        parse_mode="markdown",
    )
    return
