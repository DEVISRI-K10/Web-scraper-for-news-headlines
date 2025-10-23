import requests
from bs4 import BeautifulSoup
import re

def clean_text(text):
    return re.sub(r'\s+', ' ', text.strip())


url ='https://www.nytimes.com/'

try:
    response = requests.get(url)
    response.raise_for_status()  

    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = soup.find_all('h2')  

    headline_list = []
    print("Extracted headlines:")
    for headline in headlines:
        text = clean_text(headline.get_text())
        if text and len(text) > 10:  
            print(f"- {text}")  
            headline_list.append(text)

    
    if headline_list:
        with open('headlines.txt', 'w', encoding='utf-8') as file:
            for i, headline in enumerate(headline_list, 1):
                file.write(f"{i}. {headline}\n")
        print(f"\n Successfully saved {len(headline_list)} headlines to headlines.txt")
    else:
        print("\nNo headlines found. The website may use JavaScript or different tags/classes.")

except requests.RequestException as e:
    print(f"Error fetching webpage: {e}")
except Exception as e:
    print(f"An error occurred: {e}")