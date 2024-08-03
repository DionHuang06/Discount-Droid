import json

# Sample JSON data
data = [
    {"name": "Beats By Dr. Dre Solo 4 On-Ear Sound Isolating Bluetooth Headphones - Cloud Pink", "price": "$179.99$179.99SAVE $100", "url": ""},
    {"name": "Beats By Dr. Dre Solo 4 On-Ear Sound Isolating Bluetooth Headphones - Matte Black", "price": "$179.99$179.99SAVE $100", "url": ""},
    {"name": "Beats By Dr. Dre Solo 4 On-Ear Sound Isolating Bluetooth Headphones - Slate Blue", "price": "$179.99$179.99SAVE $100", "url": ""},
    {"name": "Shokz OpenRun Bone Conduction Open-Ear Bluetooth Headphones - Black", "price": "$114.99$114.99SAVE $55Plus $0.90 EHF", "url": ""},
    {"name": "Marshall Major IV On-Ear Bluetooth Headphones - Black", "price": "$189.99$189.99SAVE $30Plus $0.90 EHF", "url": ""},
    {"name": "Shokz OpenRun Pro Bone Conduction Open-Ear Bluetooth Headphones - Steel Blue", "price": "$159.99$159.99SAVE $70Plus $0.90 EHF", "url": ""},
    {"name": "Belkin SoundForm Mini On-Ear Bluetooth Kids Headphones - Pink", "price": "$39.99$39.99SAVE $10", "url": ""},
    {"name": "Refurbished (Fair) Apple AirPods (2nd Generation) with charging case", "price": "$89$89.00SAVE $80", "url": ""},
    {"name": "Shokz RoadWave Sport Audio Sunglasses - Black", "price": "$199.99$199.99SAVE $50Plus $0.90 EHF", "url": ""},
    {"name": "Shokz OpenFit Open-Ear True Wireless Earbuds - Beige", "price": "$159.99$159.99SAVE $70Plus $0.40 EHF", "url": ""},
    {"name": "JBL Live 460NC On-Ear Noise Cancelling Bluetooth Headphones - Black", "price": "$89.99$89.99SAVE $80Plus $0.90 EHF", "url": ""},
    {"name": "Shokz OpenRun Bone Conduction Open-Ear Bluetooth Headphones - Red", "price": "$114.99$114.99SAVE $55Plus $0.90 EHF", "url": ""},
    {"name": "Open Box - Beats by Dr. Dre Solo3 On-Ear Sound Isolating Bluetooth Headphones - Black 10/10", "price": "$109.99$109.99SAVE $80", "url": ""},
    {"name": "Skullcandy Riff On-Ear Headphones - Black", "price": "$19.99$19.99SAVE $10", "url": ""},
    {"name": "JBL Jr310 On-Ear Headphones - Blue", "price": "$24.99$24.99SAVE $5Plus $0.90 EHF", "url": ""},
    {"name": "Belkin SoundForm Mini On-Ear Bluetooth Kids Headphones - Blue", "price": "$39.99$39.99SAVE $10", "url": ""},
    {"name": "JBL Jr310 On-Ear Headphones - Red", "price": "$24.99$24.99SAVE $5Plus $0.90 EHF", "url": ""},
    {"name": "JLab Audio Studio On-Ear Sound Isolating Bluetooth Headphones - Black", "price": "$24.99$24.99SAVE $15Plus $0.90 EHF", "url": ""},
    {"name": "JBL JR310BT On-Ear Bluetooth Kids Headphones - Blue", "price": "$49.99$49.99SAVE $20Plus $0.90 EHF", "url": ""},
    {"name": "Belkin SoundForm Mini On-Ear Bluetooth Kids Headphones - White", "price": "$39.99$39.99SAVE $10", "url": ""},
    {"name": "Open Box - Beats by Dr. Dre Solo3 Icon On-Ear Sound Isolating Bluetooth Headphones - Matte Black", "price": "$134.99$134.99SAVE $115", "url": ""},
    {"name": "Shokz OpenRun Pro Bone Conduction Open-Ear Bluetooth Headphones - Beige", "price": "$159.99$159.99SAVE $70Plus $0.90 EHF", "url": ""},
    {"name": "Shokz OpenRun Pro Bone Conduction Open-Ear Bluetooth Headphones - Blue", "price": "$159.99$159.99SAVE $70Plus $0.90 EHF", "url": ""},
    {"name": "Belkin SoundForm Mini On-Ear Bluetooth Kids Headphones - Black", "price": "$39.99$39.99SAVE $10", "url": ""}
]

# Function to convert price to a float
def get_price(price_str):
    return float(''.join(filter(str.isdigit, price_str.split('$')[1])))

# Sort items by price
sorted_data = sorted(data, key=lambda x: get_price(x['price']))

# Get the top 5 cheapest items
top_5_items = sorted_data[:5]

# Generate the HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Search Results</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Search Results</h1>
    </header>
    <div class="results-container">
        <h2>Top 5 Cheapest Items</h2>
        <div id="results">
"""

for item in top_5_items:
    html_content += f"""
            <div class="result-item">
                <h3>{item['name']}</h3>
                <p>{item['price']}</p>
                <a href="{item['url']}" target="_blank">View Item</a>
            </div>
    """

html_content += """
        </div>
    </div>
</body>
</html>
"""

# Write the HTML content to a file
with open('search.html', 'w') as file:
    file.write(html_content)

print("HTML file 'search.html' generated successfully.")
