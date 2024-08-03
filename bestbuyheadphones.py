import requests
import json
from bs4 import BeautifulSoup

# URL of the Best Buy page
url = 'https://www.bestbuy.ca/en-ca/category/on-ear-headphones/21270?path=category%253AAudio%253Bcategory%253AHeadphones%253Bcategory%253AOn-Ear%2BHeadphones%253Bcurrentoffers0enrchstring%253AOn%2BSale'

# Headers to mimic a real browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# Make the request to get the HTML content
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Write the HTML content to a file
    with open('page.html', 'w', encoding='utf-8') as file:
        file.write(response.text)
    print("HTML content written to page.html")

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all product items
    products = soup.find_all('div', class_='productItemRow_hyNOs')

    # List to store product information
    product_list = []

    # Extract information for each product
    for product in products:
        name = product.find('div', class_='productItemName_3IZ3c')
        price = product.find('div', class_='productPricingContainer_3gTS3')
        link = product.find('a', class_='link_3hcyN')

        product_info = {
            'name': name.text.strip() if name else '',
            'price': price.text.strip() if price else '',
            'url': f"https://www.bestbuy.ca{link['href']}" if link and 'href' in link.attrs else ''
        }

        product_list.append(product_info)

    # Write the product information to a JSON file
    with open('products.json', 'w', encoding='utf-8') as json_file:
        json.dump(product_list, json_file, ensure_ascii=False, indent=4)

    print("Product information written to products.json")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")