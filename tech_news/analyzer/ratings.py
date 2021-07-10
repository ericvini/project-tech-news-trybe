# Requisito 10
from tech_news.database import find_news


def top_5_news():
    news_array = find_news()
    popularity_array = [
        [
            int(news["shares_count"]) + int(news["comments_count"]),
            news["title"],
            news["url"],
        ]
        for news in news_array
    ]
    popularity_news = sorted(popularity_array, reverse=True)
    result_list = [
        (popular_news[1], popular_news[2])
        for popular_news in popularity_news[:5]
    ]
    return result_list


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
