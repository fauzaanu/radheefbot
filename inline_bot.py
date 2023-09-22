import logging
import os
from html import escape
from uuid import uuid4
from dotenv import load_dotenv
from radheef import get_radheef_val
from telegram import InlineQueryResultArticle, InputTextMessageContent, Update
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, ContextTypes, InlineQueryHandler, MessageHandler, filters

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
GH_LINK = "https://github.com/fauzaanu/radheefbot"


async def start_handle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Welcome to Radheef Bot!\n\n ",
                                    disable_web_page_preview=True)


async def direct_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    radheef_val = get_radheef_val(update.message.text)
    print(radheef_val)

    if radheef_val is not None:
        print(type(radheef_val))

        if type(radheef_val) == str:
            await update.message.reply_text(radheef_val)
        elif type(radheef_val) == list:
            for value in radheef_val:
                message_str = str()
                if value['current_word_dv']:
                    message_str += f"<b>{value['current_word_dv']}</b>\n"
                if value['meaning_text']:
                    message_str += f"{value['meaning_text']}\n"
                if value['extra_notes_dv']:
                    message_str += f"{value['extra_notes_dv']}\n"

                await update.message.reply_text(message_str, parse_mode=ParseMode.HTML, disable_web_page_preview=True)
    else:
        await update.message.reply_text("No exact match found! Please try again. Report errors to @fauzaanu")


async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.inline_query.query

    if query == "":
        return
    else:
        radheef_val = get_radheef_val(query)
        print(radheef_val)
        results = []
        if radheef_val is not None:
            if type(radheef_val) == str:
                results.append(
                    InlineQueryResultArticle(
                        id=str(uuid4()),
                        title=query,
                        input_message_content=InputTextMessageContent(
                            radheef_val, parse_mode=ParseMode.MARKDOWN
                            , disable_web_page_preview=True),
                    )
                )
            elif type(radheef_val) == list:
                for value in radheef_val:
                    message_str = str()
                    if value['current_word_dv']:
                        message_str += f"<b>{value['current_word_dv']}</b>\n"
                    if value['meaning_text']:
                        message_str += f"{value['meaning_text']}\n"
                    if value['extra_notes_dv']:
                        message_str += f"{value['extra_notes_dv']}\n"
                    results.append(
                        InlineQueryResultArticle(
                            id=str(uuid4()),
                            title=query,
                            input_message_content=InputTextMessageContent(
                                message_str,
                                parse_mode=ParseMode.HTML
                            ),
                        )
                    )

        else:
            results.append(
                InlineQueryResultArticle(
                    id=str(uuid4()),
                    title=query,
                    input_message_content=InputTextMessageContent(
                        "No exact match found! Please try again", parse_mode=ParseMode.MARKDOWN
                        , disable_web_page_preview=True),
                )
            )

        await update.inline_query.answer(results)


if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()
    TOKEN = os.getenv("TOKEN")

    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", callback=start_handle))
    application.add_handler(MessageHandler(filters.TEXT, callback=direct_message))
    application.add_handler(InlineQueryHandler(inline_query))

    application.run_polling()
