from loader import DB, bot
from parsers.parse_news import ParseBleacherReport


async def news_notification() -> None:
    get_new = ParseBleacherReport().parse_posts()[-1]
    get_all_users = DB.get_all_subscribers()
    for users in get_all_users:
        text = [
            f"{get_new['post_title']}: {get_new['link']}\n",
            f"Источник: {get_new['proof']}"
        ]
        await bot.send_message(
            users.user_id,
            f"\n".join(text)
        )
