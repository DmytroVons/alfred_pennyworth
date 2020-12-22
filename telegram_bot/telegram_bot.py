import logging
import rozetka_parser
from emoji import emojize
from aiogram import Bot, Dispatcher, executor, types
from logging.handlers import TimedRotatingFileHandler

logging.basicConfig(filename='telegram_logger.log', datefmt='%d/%m/%Y %I:%M:%S %p', filemode='a', level=logging.DEBUG,
                    format='%(asctime)s -%(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger('telegram_logger.log')
handler = TimedRotatingFileHandler('telegram_logger.log', when='W0', backupCount=0)
logger.addHandler(handler)

bot = Bot(token="1390253128:AAEdAIY5oRUiH702bSQ7gzSpiPn_3pJLJKE")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu_keyboard_1 = types.InlineKeyboardButton(text="Laptop")
    menu_keyboard_2 = types.InlineKeyboardButton(text="Exit")
    menu_keyboard.add(menu_keyboard_1, menu_keyboard_2)
    await bot.send_sticker(chat_id=message.from_user.id,
                           sticker='CAACAgIAAxkBAAEBsJFf252HUp15jBNDQ0mFDH-5zNxZBQACBQADwDZPE_lqX5qCa011HgQ')
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Hi! {message.from_user.first_name} {emojize(':raised_hand_with_fingers_splayed:', use_aliases=True)}\nI'm Bruce Bot!{emojize(':robot_face:')}\nHow can i help u?\n(You can use /help command to know what i can do!)",
                           reply_markup=menu_keyboard)


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/help` command
    """
    await bot.send_message(chat_id=message.from_user.id,
                           text="You can use this command (/start) for start working with me. "
                                "\nYou can use this word Exit for thank me and say bye. bye!.")


@dp.message_handler(lambda message: message.text.title() == "Exit")
async def exit_function(message: types.Message):
    """
    This handler will be called when user use `Exit` buttom
    """
    await bot.send_sticker(chat_id=message.from_user.id,
                           sticker='CAACAgIAAxkBAAEBsL1f27V47U_z9z1e4JRB6RRwuCciggACBgADwDZPE8fKovSybnB2HgQ')
    await bot.send_message(chat_id=message.from_user.id, text="Thank u! I\'m hopiping i help u. Bye, Bye!")


@dp.message_handler(lambda message: message.text == "Laptop")
async def laptops_model_menu(message: types.Message):
    """
    This handler will be called when user use `Laptop` buttom
    """
    menu_keyboard = types.InlineKeyboardMarkup(row_width=2)
    model_keyboard_1 = types.InlineKeyboardButton(text="Acer", callback_data="Acer")
    model_keyboard_2 = types.InlineKeyboardButton(text="Apple", callback_data="Apple")
    model_keyboard_3 = types.InlineKeyboardButton(text="Asus", callback_data="Asus")
    model_keyboard_4 = types.InlineKeyboardButton(text="Dell", callback_data="Dell")
    model_keyboard_5 = types.InlineKeyboardButton(text="HP", callback_data="HP")
    model_keyboard_6 = types.InlineKeyboardButton(text="Huawei", callback_data="Huawei")
    model_keyboard_7 = types.InlineKeyboardButton(text="Microsoft", callback_data="Microsoft")
    model_keyboard_8 = types.InlineKeyboardButton(text="Sony", callback_data="Sony")
    model_keyboard_9 = types.InlineKeyboardButton(text="MSI", callback_data="MSI")
    model_keyboard_10 = types.InlineKeyboardButton(text="Lenovo", callback_data="Lenovo")
    model_keyboard_11 = types.InlineKeyboardButton(text="Xiaomi", callback_data="Xiaomi")
    menu_keyboard.add(model_keyboard_1, model_keyboard_2, model_keyboard_3, model_keyboard_4, model_keyboard_5,
                      model_keyboard_6, model_keyboard_7, model_keyboard_8, model_keyboard_9, model_keyboard_10,
                      model_keyboard_11)

    await bot.send_message(chat_id=message.from_user.id, text="Please, choose model, what would u like to buy.",
                           reply_markup=menu_keyboard)


@dp.callback_query_handler(lambda call: True)
async def callback_inline(call):
    list_of_models = ['apple', 'acer', 'asus', 'dell', 'hp', 'huawei', 'microsoft', 'sony', 'xiaomi', 'lenovo', 'msi']
    if call.message:
        if call.data.lower() in list_of_models:
            laptops = rozetka_parser.parse(str.lower(call.data))
            for laptop in laptops:
                model = laptop.get('model')
                link = laptop.get('link')
                price = laptop.get('price')
                pictures = laptop.get('pictures')
                await bot.send_photo(chat_id=call.from_user.id, photo=pictures)
                await bot.send_message(chat_id=call.from_user.id,
                                       text=f'{model}, \n{price}, \n{link}')


executor.start_polling(dp, skip_updates=True)
