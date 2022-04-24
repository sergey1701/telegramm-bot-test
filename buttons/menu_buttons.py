class MenuButtons:
    def __init__(self, types):
        b1 = types.KeyboardButton('/Weather')
        b2 = types.KeyboardButton('Second Button')
        b3 = types.KeyboardButton('Third Button')
        self.kb_client = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

        self.kb_client.row(b1, b2, b3)