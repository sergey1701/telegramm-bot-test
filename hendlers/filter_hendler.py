from tools.word_filter_tools import *

class Filter:
    def __init__(self, dp, types):
        @dp.message_handler()
        async def shit_talk_terminator(message: types.Message):
            if if_text_have_shit_words(message_text=message.text, gramar=read_data_from_txt("data/shit_words_compleetion.txt")):
                await message.reply("Маты запрещены")
                await message.delete()    