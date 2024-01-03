import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import os

# Configurações
SEARCH_QUERY = "pinterest pug"
IMAGE_FOLDER = "data/downloaded_images"
IMAGE_SIZE = (224, 224)
IMAGE_LIMIT = 10

def get_image_urls(query, limit):
    query = query.replace(' ', '+')
    url = f"https://www.google.com/search?hl=en&tbm=isch&q={query}"

    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error fetching page: {url}")

    soup = BeautifulSoup(response.text, 'html.parser')
    images = [img['src'] for img in soup.find_all('img')[1:limit+1]]
    return images

def download_and_resize_image(url, folder, counter, size):
    if not os.path.exists(folder):
        os.makedirs(folder)

    try:
        response = requests.get(url)
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            image = image.resize(size)
            file_path = os.path.join(folder, f'{counter}.jpg')
            image.save(file_path)
    except Exception as e:
        print(f"Error downloading or resizing image {url}: {e}")

def main():
    image_urls = get_image_urls(SEARCH_QUERY, IMAGE_LIMIT)

    for counter, url in enumerate(image_urls):
        download_and_resize_image(url, IMAGE_FOLDER, counter, IMAGE_SIZE)

if __name__ == "__main__":
    main()
