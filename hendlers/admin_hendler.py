from aiogram.dispatcher.filters.state import State, StatesGroup

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()



class AdminHendler:
    def __init__(self, bot, dp, types, fsm_context):
        @dp.message_handler(commands='Load', state=None)
        async def cm_start(message: types.Message):
            await FSMAdmin.photo.set()
            await message.reply("Load Yure Image")

        @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
        async def load_photo(message: types.Message, state: fsm_context):
            async with state.proxy() as data:
                data['photo'] = message.photo[0].file_id
            await FSMAdmin.next()
            await message.reply("Insert Name")    

        @dp.message_handler(state=FSMAdmin.name)
        async def load_name(message: types.Message, state: fsm_context):
            async with state.proxy() as data:
                data['name'] = message.text
            await FSMAdmin.next()
            await message.reply("Insert Descrition")

        @dp.message_handler(state=FSMAdmin.description)
        async def load_description(message: types.Message, state: fsm_context):
            async with state.proxy() as data:
                data['description'] = message.text
            await FSMAdmin.next()
            await message.reply("Insert Price")        


        @dp.message_handler(state=FSMAdmin.price)
        async def load_price(message: types.Message, state: fsm_context):
            async with state.proxy() as data:
                data['price'] = message.text
            await message.reply(str(data))    
            await FSMAdmin.next()
            await state.finish()        
            