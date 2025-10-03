import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import webbrowser


def main():
    source_language = "zh-TW"
    response = requests.get(
        "https://course-query.acad.ncku.edu.tw/index.php?c=qry11215&i=U2NbaQBnUm8AKQQiVGpQNlc3BHpQO1VyBTQFawduUmVXMVY6VGlXdVRqADYDOwcjBW4KL1I9VTQIPFM1DGMHIVRsWGoHZFdrAzANYlNlAG0AIVR7U2sDMwc3ACVUdFIvUGJTbwRwAnFTbFYiUWkBNFRmU3ZSNwc2CTQDdQRqVHpTOFtgAGlSdwAhBDRUPVAlVzYEK1BoVWEFNQUgB2ZSdFc7VnZUO1c8VGMAPANgBzsFPAo3Un1VJgg8Uz8MYwd4VGBYPgczVw8DJQ05UzsAPAB4VDNTIgM8BzwAPVQlUg9QJVM1BH8CLlMkVmtRYgE9VH5TJlIkBzwJZgNtBGJUM1N5WzoAaVJlAGkEOFRqUDdXNgQxUGhVYQU0BWsHblJlVztWYlRoVzRUawBuAzsHMgU9Cj1SPVUoCHVTPQxoB2BUJ1g3B3ZXawMzDWJTZwBsACc="
    )
    webbrowser.open(
        "https://course-query.acad.ncku.edu.tw/index.php?c=qry11215&i=U2NbaQBnUm8AKQQiVGpQNlc3BHpQO1VyBTQFawduUmVXMVY6VGlXdVRqADYDOwcjBW4KL1I9VTQIPFM1DGMHIVRsWGoHZFdrAzANYlNlAG0AIVR7U2sDMwc3ACVUdFIvUGJTbwRwAnFTbFYiUWkBNFRmU3ZSNwc2CTQDdQRqVHpTOFtgAGlSdwAhBDRUPVAlVzYEK1BoVWEFNQUgB2ZSdFc7VnZUO1c8VGMAPANgBzsFPAo3Un1VJgg8Uz8MYwd4VGBYPgczVw8DJQ05UzsAPAB4VDNTIgM8BzwAPVQlUg9QJVM1BH8CLlMkVmtRYgE9VH5TJlIkBzwJZgNtBGJUM1N5WzoAaVJlAGkEOFRqUDdXNgQxUGhVYQU0BWsHblJlVztWYlRoVzRUawBuAzsHMgU9Cj1SPVUoCHVTPQxoB2BUJ1g3B3ZXawMzDWJTZwBsACc="
    )
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup)
    ul = soup.find("ul", class_="ui-choose")
    print(ul)
    if ul:
        li_items = ul.find_all("li")
        for li in li_items:
            print(li.get_text(strip=True))


if __name__ == "__main__":
    main()
