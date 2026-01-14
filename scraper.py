import requests

def print_image_links(base_url):
    max_pages = 1000  # Reasonable limit to avoid infinite loop
    for page in range(1, max_pages + 1):
        page_str = str(page).zfill(3)
        img_url = f"{base_url}{page_str}.webp"
        try:
            response = requests.head(img_url, timeout=5)
            if response.status_code == 200:
                print(img_url)
            else:
                break  # Stop if image doesn't exist
        except requests.RequestException:
            break  # Stop on error