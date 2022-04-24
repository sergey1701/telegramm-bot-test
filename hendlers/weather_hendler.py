from tools.weather_tool import get_current_weather, generate_weather_data
from aiogram.dispatcher.filters.state import State, StatesGroup

class FSMData(StatesGroup):
    sityname = State()
    



class WeatherHendler(FSMData):
    def __init__(self, bot, dp, types, fsm_context):
        @dp.message_handler(commands='Weather', state=None)
        async def get_sity_name(message: types.Message):
            await self.sityname.set()
            await message.reply("Insert Sity Name")
            

        @dp.message_handler(state=self.sityname)
        async def current_weather_data(message: types.Message, state: fsm_context):
            try:
                async with state.proxy() as data:
                    data['sityname'] = message.text
                weather = get_current_weather(message.text)
                await message.reply(generate_weather_data(weather))    
                await message.delete()
                await state.finish()
            except Exception as ex:
                await message.reply('Wrong Sity Name')
                await state.finish()