from bs4 import BeautifulSoup
from main_bot.services.request import RequestManager


class ParseBleacherReport(RequestManager):
    """Парсер сайта bleacher report"""

    def __init__(self) -> None:
        self.__url = "https://bleacherreport.com/boston-celtics"
        self.source_site = f'' \
                           f'{self.__url.split("//")[0]}//' \
                           f'{self.__url.split("//")[1].split("/")[0]}'

    def parse_posts(self) -> list:
        get_content = self.get(self.__url)
        soup = BeautifulSoup(get_content.text, "html.parser")
        posts = soup.find_all("li", class_="articleSummary")
        posts_list = []
        for post in posts:
            post_link = post.find(
                "div",
                class_="articleContent"
            ).find("a", class_="atom")
            post_name = post.find('div', class_="articleContent").text
            if post_link:
                get_link = post_link.get("href")
                posts_dict = {
                    "post_title": post_name,
                    "link": get_link,
                    "proof": self.source_site
                }
                posts_list.append(posts_dict)
        return posts_list
