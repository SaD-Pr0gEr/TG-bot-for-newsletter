import requests
from bs4 import BeautifulSoup


def parse_news_bleacher_report():
    HOST = "https://bleacherreport.com/"
    URL = "https://bleacherreport.com/boston-celtics"
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")
    all_posts = soup.find_all("li", class_="cell articleSummary")
    posts_list = []
    for posts in all_posts:
        # photo = posts.find("div", class_="articleMedia"). \
        #     find("a", class_="molecule thumbnail").find("div", class_='atom lazyImage').img.get("src")
        post_link = posts.find("div", class_="articleContent").find("a", class_="atom articleTitle lowerMargin")
        post_name = posts.find('div', class_="articleContent").text
        if post_link:
            get_link = post_link.get("href")
            posts_dict = {
                "post_title": post_name,
                "link": get_link,
                "proof": HOST
            }
            posts_list.append(posts_dict)
    return posts_list
