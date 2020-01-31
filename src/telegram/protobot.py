from aiogram import Bot, types
from aiogram.utils.exceptions import *

from config.system import DEFAULT_PARSE_MODE


class ProtoBot(Bot):
    """
    Class ``ProtoBot``
    """
    def __init__(self, root_id, *args, **kwargs):
        self.root_id = root_id
        super().__init__(*args, **kwargs)
        if not kwargs.get('parse_mode'):
            self.parse_mode = DEFAULT_PARSE_MODE

    """s_ in the name of functions means SAFE"""

    async def s_send_message(self, text, chat_id=None, reply_markup=None, parse_mode=None):
        if not chat_id:
            chat_id = self.root_id
        if not parse_mode:
            parse_mode = self.parse_mode
        try:
            if len(text) > 4096:
                await self.send_message(text=text[0:4096],
                                        chat_id=chat_id,
                                        reply_markup=reply_markup,
                                        parse_mode=parse_mode)
                text = text[4096:]
                await self.s_send_message(text=text,
                                          chat_id=chat_id,
                                          reply_markup=reply_markup,
                                          parse_mode=parse_mode)
            else:
                await self.send_message(text=text,
                                        chat_id=chat_id,
                                        reply_markup=reply_markup,
                                        parse_mode=parse_mode)
        except BotBlocked:
            pass

    async def s_edit_message_text(self, message_id, text, chat_id=None, reply_markup=None):
        """Ignore errors with message editing"""
        if not chat_id:
            chat_id = self.root_id
        try:
            await self.edit_message_text(message_id=message_id,
                                         chat_id=chat_id,
                                         text=text,
                                         reply_markup=reply_markup)
        except MessageCantBeEdited:
            pass
        except MessageNotModified:
            pass
        except BotBlocked:
            pass



    async def s_delete_message(self, message_id, chat_id=None):
        """Ignore errors with message deleting"""
        if not chat_id:
            chat_id = self.root_id
        try:
            await self.delete_message(chat_id=chat_id,
                                      message_id=message_id)
        except MessageToDeleteNotFound:
            pass
        except MessageCantBeDeleted:
            pass
        except BotBlocked:
            pass
