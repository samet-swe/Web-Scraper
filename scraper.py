import requests
from bs4 import BeautifulSoup

import create_book_list

url = "https://books.toscrape.com/catalogue/page-1.html"

def main():
    response = requests.get(url)
    response = response.content
    
    soup = BeautifulSoup(response, 'html.parser')
    ol = soup.find('ol')
    articles = ol.find_all('article', class_='product_pod')
    
    books = []
    
    for article in articles:
        image = article.find('img')
        title = image['alt']
        star = article.find('p')
        star = star['class'][1]
        price = article.find('p', class_='price_color').text
        price = float(price[1:])
        books.append([title, price, star])
        
    create_book_list.main(books)
    
if __name__ == '__main__':
    main()