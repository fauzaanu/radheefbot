import logging
from html import escape
from uuid import uuid4
from main import get_radheef_val

from telegram import InlineQueryResultArticle, InputTextMessageContent, Update
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, ContextTypes, InlineQueryHandler, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

GH_LINK = "https://github.com/fauzaanu/radheefbot"


async def start_handle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello! I am a bot that helps you find the meaning of words in Dhivehi. "
                                    "I am currently in alpha and I am still under development. "
                                    f"If you would like to contribute, please open a PR on {GH_LINK}",disable_web_page_preview=True)

async def direct_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    x = get_radheef_val(update.message.text)

    if x is not None:
        for y in x:
            await update.message.reply_text(y["meaning_text"])
            await update.message.reply_text(y["extra_notes_dv"])
    else:
        await update.message.reply_text("No exact match found! Please try again.")
        await update.message.reply_text("If you think this is an error and the word is available via "
                                        "https://www.radheef.mv/ please report to @fauzaanu")
        await update.message.reply_text(f"If you would like to contribute, please open a PR on {GH_LINK}",disable_web_page_preview=True)


async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.inline_query.query

    if query == "":
        return

    else:

        x = get_radheef_val(query)

        results = [
        ]
        if x is not None:
            for y in x:
                results.append(
                    InlineQueryResultArticle(
                        id=uuid4(),
                        title=y,
                        input_message_content=InputTextMessageContent(
                            f"{y['meaning_text']}<br>{y['extra_notes_dv']}", parse_mode=ParseMode.HTML
                        ),
                    )
                )
        else:
            results.append(
                InlineQueryResultArticle(
                    id=uuid4(),
                    title="No exact match found! Please try again.",
                    input_message_content=InputTextMessageContent(
                        "No exact match found! Please try again. If you think this is an error and the word is "
                        "available via https://www.radheef.mv/ please report to @fauzaanu"
                        f"If you would like to contribute, please open a PR on {GH_LINK}", parse_mode=ParseMode.MARKDOWN
                    ,disable_web_page_preview=True),
                )
            )

        await update.inline_query.answer(results)


def main() -> None:

    application = Application.builder().token("").build()

    application.add_handler(CommandHandler("start", callback=start_handle))
    application.add_handler(MessageHandler(filters.TEXT, callback=direct_message))
    application.add_handler(InlineQueryHandler(inline_query))


    application.run_polling()


if __name__ == "__main__":
    main()
