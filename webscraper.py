import requests
from bs4 import BeautifulSoup

# URL of the news website's page to scrape
url = 'https://www.bbc.com/news'  # Change this to your chosen news site

# Send an HTTP GET request to fetch the page content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all headline tags - adjust the tag and class as needed
    # Example: For BBC, headlines are often within <h3> tags with specific classes
    # Here, we look for <h3> tags
    headlines = soup.find_all(['h2', 'h3'])
    
    # Create a list to hold the headline texts
    headlines_texts = []
    
    for tag in headlines:
        text = tag.get_text(strip=True)
        if text:  # Ensure the text is not empty
            headlines_texts.append(text)
    
    # Save headlines to a text file
    with open('headlines.txt', 'w', encoding='utf-8') as file:
        for headline in headlines_texts:
            file.write(headline + '\n')
    
    print(f"Saved {len(headlines_texts)} headlines to 'headlines.txt'.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")