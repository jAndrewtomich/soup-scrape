import requests
from bs4 import BeautifulSoup


def main():

    response = requests.get("https://news.ycombinator.com/news")
    response.raise_for_status()
    response = response.text

    soup = BeautifulSoup(response, "lxml")

    article_tags = soup.find_all(name="a", class_="storylink")
    article_upvotes = soup.find_all(name="span", class_="score")

    article_titles, article_links = [], []

    for tag in article_tags:
        text = tag.getText()
        link = tag.get("href")
        article_titles.append(text)
        article_links.append(link)

    article_scores = [int(score.getText().split()[0]) for score in article_upvotes]

    idx = article_scores.index(max(article_scores))

    print(article_titles[idx], '\n', article_links[idx], '\n', article_scores[idx])
"""
    for tag, upvote in zip(article_tags, article_upvotes):
        article_text = tag.getText()
        article_link = tag.get("href")
        article_upvote = int(upvote.getText().split()[0])
        articles.append((article_text, article_link, article_upvote))

    maxi = 0

    for article in articles:
        if article[2] > maxi:
            maxi = article[2]

    print([article for article in articles if article[2] == maxi])
"""

if __name__ == "__main__":
    main()
