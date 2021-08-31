from pyrogram import Client, filters
from pyrogram.types import Message
from tagadmin import COMMAND_HAND_LER, LOGGER


@Client.on_message(filters.regex("(?i)@admin(s)?"))
async def tag_admins(c: Client, m: Message):

    adminslist = []

    if m.chat.type in ("supergroup", "group"):
        async for member in c.iter_chat_members(m.chat.id, filter="administrators"):
            adminslist.append(member.user.id)

        if m.from_user.id in adminslist:
            # Don't work if called by an admin himself and log this!
            LOGGER.info(
                f"Được gọi bởi quản trị viên:{m.from_user.name} ({m.from_user.id}) trong nhóm {m.chat.title} ({m.chat.id})"
            )
            return

        mentions = "Hey **{}**, hãy nhìn vào đây!"
        admin_count = 0

        async for a in alladmins:
            if a.user.is_bot:
                pass
            else:
                admin_count += 1
                adminid = a.user.id
                mentions += f"[\u2063](tg://user?id={adminid})"

        text = mentions.format(admin_count)
        text += f"\n[{m.from_user.first_name}](tg://user?id={m.from_user.id}) đang gọi cho bạn!"
        await m.reply_text(text, parse_mode="markdown")

    else:
        await m.reply_text(
            "`Nó không hoạt động ở đây ¯\_(ツ)_/¯`",
            parse_mode="markdown",
            reply_to_message_id=m.message_id,
        )

    return
