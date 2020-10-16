import requests
import bs4

def main():
    show_header()

    plaats = input("Welke plaats wil je het weer van zien? ")

    html = get_html_from_web(plaats)

    # Parse the html
    get_weather_from_html(html)
    # Display for the forecast


def show_header():
    print("----------------------------")
    print("  Real Time Weather Client")
    print("----------------------------")


def get_html_from_web(plaats):
    url = f"https://www.wunderground.com/weather/nl/{plaats}"
    response = requests.get(url)

    return response.text

def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, "html.parser")
    soup.find


if __name__ == '__main__':
    main()
