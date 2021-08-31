from pyrogram import Client, filters
from pyrogram.types import Message
from tagadmin import COMMAND_HAND_LER, CONTACT_OWNER

# -- Constants -- #
DONATE_TEXT = """
Rất vui khi bạn muốn đóng góp!

Bạn có thể tặng Chủ sở hữu của tôi bằng cách liên hệ với anh ấy >>> @{} \
Nếu bạn quyên góp, giới hạn cho kích thước giới hạn tải xuống \
số tệp sẽ tăng lên khi anh ta có thể nâng cấp máy chủ!
"""
# -- Constants End -- #


# Command for asking to donate owner
@Client.on_message(filters.command("donate", COMMAND_HAND_LER))
async def donate_owner(c: Client, m: Message):

    if m.chat.type in ("supergroup", "group"):

        try:
            await c.send_message(
                m.from_user.id, DONATE_TEXT.format(CONTACT_OWNER), parse_mode="markdown"
            )

            await m.reply_text(
                "**Tôi đã gửi cho bạn tin nhắn trong PM của bạn!**",
                parse_mode="markdown",
                reply_to_message_id=m.message_id,
            )
            return
        except:
            await message.reply_text(
                "**Liên hệ với tôi trong PM trước**",
                parse_mode="markdown",
                reply_to_message_id=m.message_id,
            )
            return

    await m.reply_text(
        DONATE_TEXT.format(CONTACT_OWNER),
        reply_to_message_id=m.message_id,
        parse_mode="markdown",
    )
    return
