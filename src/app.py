from argparse import ArgumentParser

from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from src.telegram.protobot import ProtoBot
from src.exceptions import *
from config.system import DEFAULT_PROXY


parser = ArgumentParser()


def parse_global_params():
    kwargs = dict()
    parser.add_argument('-w', '--webhook', default=False, type=bool,
                        help="Use webhook. By default bot use polling method")
    args = parser.parse_args()

    webhook = args.webhook
    kwargs['webhook'] = webhook
    return kwargs


def parse_bot_params():
    kwargs = dict()
    parser.add_argument('-r', '--root_id', default=None, type=int,
                        help="Telegram ID of the root user (I recommend to use "
                             "owner of bot token)")
    parser.add_argument('-t', '--token', default=None, type=str, help="Telegram Bot Token")
    parser.add_argument('-p', '--proxy', default=DEFAULT_PROXY, type=str, help="Proxy for censorship "
                                                                               "(example: https://1.1.1.1:433)")
    args = parser.parse_args()

    root_id = args.root_id
    token = args.token
    proxy = args.proxy

    if not root_id:
        raise RootIdNotSpecifiedError
    if not token:
        raise BotTokenNotSpecifiedError

    kwargs['root_id'] = root_id
    kwargs['token'] = token
    kwargs['proxy'] = proxy

    return kwargs


bot_params = parse_bot_params()
bot = ProtoBot(**bot_params)

global_params = parse_global_params()
storage = RedisStorage2()
dp = Dispatcher(bot, storage=storage)
from src.telegram.handlers import *


if not global_params['webhook']:
    print("polling...")
    executor.start_polling(dp)
