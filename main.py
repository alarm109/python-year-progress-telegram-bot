import os
import asyncio
from math import floor
from os.path import dirname, join
from datetime import datetime

from dotenv import load_dotenv
from telegram import Bot
from telegram.error import TelegramError

# Load environment values
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

# Create telegram bot instance
bot = Bot(TELEGRAM_TOKEN)

# Dictionary for year progress ascii characters
YEAR_PROGRESS_CHAR = {
    0: "⣀",
    1: "⣀",
    2: "⣀",
    3: "⣄",
    4: "⣄",
    5: "⣤",
    6: "⣦",
    7: "⣶",
    8: "⣷",
    9: "⣷",
    10: "⣿",
}

def get_year_progress():
    """Generate year progress message."""

    current_year = datetime.now().year
    day_of_year = datetime.now().timetuple().tm_yday
    total_days_in_year = datetime.fromisoformat(f"{current_year}-12-31").timetuple().tm_yday

    year_progress = floor(day_of_year / total_days_in_year * 100)
    year_progress_ascii = "⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀"
    year_progress_ascii = year_progress_ascii.replace("⣀", "⣿", floor(year_progress / 10))
    year_progress_ascii = year_progress_ascii.replace("⣀", YEAR_PROGRESS_CHAR[year_progress % 10], 1)

    return f"""Day {day_of_year} of {total_days_in_year} total days in the year.
{year_progress_ascii} {year_progress}%"""

async def send_message(text):
    """Send message to user."""
    async with bot:
        try:
            await bot.send_message(chat_id=CHAT_ID, text=text)
            print("Message sent successfully!")
            print(text)
        except (ValueError, TelegramError) as e:
            print("An exception occurred", e)


if __name__ == "__main__":
    YEAR_PROGRESS = get_year_progress()
    asyncio.run(send_message(YEAR_PROGRESS))
