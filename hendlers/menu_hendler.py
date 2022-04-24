from buttons.menu_buttons import MenuButtons
from core.config import ADMIN_ID

class MenuHendler:
    def __init__(self, bot,  dp, types):
        menu = MenuButtons(types=types)
        @dp.message_handler(commands=['start', 'help'])
        async def send_welcome(message: types.Message):
            """
            This handler will be called when user sends `/start` or `/help` command
            """
            await bot.send_message(message.from_user.id, "Menu" ,reply_markup=menu.kb_client)