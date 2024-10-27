from aiogram import Bot, Dispatcher, Router
from aiogram.fsm.storage.memory import MemoryStorage

from config import API_TOKEN

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)
router = Router()

from handlers.admin import admin
from handlers.keys import key_management, keys
from handlers import (notifications, pay,
                      profile, start, commands)

dp.include_router(admin.router)
dp.include_router(commands.router)
dp.include_router(start.router)
dp.include_router(profile.router)
dp.include_router(keys.router)
dp.include_router(key_management.router)
dp.include_router(pay.router)
dp.include_router(notifications.router)
