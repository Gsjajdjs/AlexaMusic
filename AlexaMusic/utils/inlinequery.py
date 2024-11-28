# Copyright (C) 2024 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

""""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2024 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="🙄 Durdurma 🙄",
            description=f"Oynatılan Şarkıyı Durdurur.",
            thumb_url="https://telegra.ph/file/9006f077e6596772e5864.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="😋 Devam Ettirme 😋",
            description=f"Durdurulan Şarkıyı Devam Ettirir.",
            thumb_url="https://telegra.ph/file/9006f077e6596772e5864.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="🙂 sᴋɪᴩ 🙂",
            description=f"Oynatılan Şarkıyı Geçer Ve Diger Şarkıya Geçer.",
            thumb_url="https://telegra.ph/file/9006f077e6596772e5864.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="🥺 Bitirme 🥺",
            description="Yayında Oynatilan Muzigi Bitirir.",
            thumb_url="https://telegra.ph/file/9006f077e6596772e5864.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="🥴 Karıştırma 🥴",
            description="Listedeki Şarkıları Karıştırır.",
            thumb_url="https://telegra.ph/file/9006f077e6596772e5864.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="🥱 Döngü 🥱",
            description="Döngü Yayinda Oynatilan Sarkiyi Otomatik Tekrar Oynatır.",
            thumb_url="https://telegra.ph/file/9006f077e6596772e5864.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
