import requests
from bs4 import BeautifulSoup

url = 'https://www.bbc.com/news'  
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all(['h2', 'h3'])
    headlines_texts = []
    
    for tag in headlines:
        text = tag.get_text(strip=True)
        if text:
             headlines_texts.append(text)

    with open('headlines.txt', 'w', encoding='utf-8') as file:
        for headline in headlines_texts:
            file.write(headline + '\n')
    print(f"Saved {len(headlines_texts)} headlines to 'headlines.txt'.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
