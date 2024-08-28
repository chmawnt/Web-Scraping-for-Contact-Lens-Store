import requests
from bs4 import BeautifulSoup

# Replace with the URL of the contact lens store
url = 'https://example.com/contact-lenses'

def scrape_contact_lenses(url):
    # Send a GET request to the URL
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Define the list to hold scraped data
    products = []

    # Find all product elements (adjust the selector as needed)
    product_elements = soup.select('.product-item')

    for product in product_elements:
        try:
            title = product.select_one('.product-title').text.strip()
            category = product.select_one('.product-category').text.strip()
            thumbnail_url = product.select_one('.product-thumbnail img')['src']
            image_url = product.select_one('.product-image img')['src']
            tags = [tag.text.strip() for tag in product.select('.product-tags .tag')]
            left_eye_power = product.select_one('.left-eye-power').text.strip()
            right_eye_power = product.select_one('.right-eye-power').text.strip()
            sku = product.select_one('.product-sku').text.strip() if product.select_one('.product-sku') else 'N/A'
            full_description = product.select_one('.product-description').text.strip()
            regular_price = product.select_one('.regular-price').text.strip()
            sale_price = product.select_one('.sale-price').text.strip() if product.select_one('.sale-price') else regular_price

            products.append({
                'Title': title,
                'Category': category,
                'Thumbnail URL': thumbnail_url,
                'Image URL': image_url,
                'Tags': tags,
                'Left Eye Power': left_eye_power,
                'Right Eye Power': right_eye_power,
                'SKU': sku,
                'Full Product Description': full_description,
                'Regular Price': regular_price,
                'Sale Price': sale_price,
            })

        except AttributeError as e:
            print(f"Error scraping product: {e}")

    return products

# Call the function and print results
contact_lenses = scrape_contact_lenses(url)
for lens in contact_lenses:
    print(lens)
