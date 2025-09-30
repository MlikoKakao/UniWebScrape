from __future__ import annotations
import requests
from bs4 import BeautifulSoup


def main():
    response = requests.get("https://web.ncku.edu.tw/index.php?Lang=en")

    print(response.status_code)

    content = BeautifulSoup(response.text, "html.parser")
    nav = content.find("button", class_="btn btn-primary btn_menu")
    print(nav)
    if nav:
        for but in nav.find_all("btn btn-primary btn_menu"):
            print(but.text.strip())


if __name__ == "__main__":
    main()
