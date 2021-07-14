from parsers import parse_news
from run import bot, DB


async def notification():
    get_news = parse_news.parse_news_bleacher_report()[-1]
    get_all_users = DB.get_all_subscribers()
    for users in get_all_users:
        await bot.send_message(users.user_id, f"{get_news['post_title']}: {get_news['link']} \n\nИсточник: {get_news['proof']}")
