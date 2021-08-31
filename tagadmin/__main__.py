from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from tagadmin import APP_ID, API_HASH, LOGGER, TG_BOT_TOKEN, TMP_DIR, MESSAGE_DUMP


class TagAdmin(Client):
    """Bắt đầu bot bằng cách sử dụng Class TagAdmin, nó sẽ khởi động bot với TagAdmin().run()
    Lấy giá trị từ tệp sample_config.py hoặc config.py"""

    def __init__(self):
        name = self.__class__.__name__.lower()

        super().__init__(
            name,
            plugins=dict(root=f"{name}/plugins"),
            workdir=TMP_DIR,
            api_id=APP_ID,
            api_hash=API_HASH,
            bot_token=TG_BOT_TOKEN,
            workers=8,
        )

    async def start(self):
        await super().start()

        me = await self.get_me()
        # Show message in LOGGER when bot starts
        LOGGER.info(
            f"TagAdminsBot dựa trên Pyrogram v{__version__}\n"
            f"(Layer {layer}) bắt đầu vào @{me.username}"
        )

        # Send message to MESSAGE_DUMP when bot starts
        await self.send_message(MESSAGE_DUMP, "<b><i>Bot đã bắt đầu</i></b>")

    async def stop(self, *args):
        await super().stop()
        # Show message in LOGGER when bot stops
        LOGGER.info("TagAdminsBot stopped!...!")


if __name__ == "__main__":
    TagAdmin().run()
