import os
import requests
from urllib.parse import urlparse
from uuid import uuid4

# 🌍 Prompt user for image URL
image_url = input("Enter the URL of the image: ").strip()

# 📁 Create directory for fetched images
output_dir = "Fetched_Images"
os.makedirs(output_dir, exist_ok=True)

try:
    # 🌐 Fetch the image using requests
    response = requests.get(image_url, timeout=10)
    response.raise_for_status()  # Raise HTTPError for bad responses

    # 🏷️ Extract filename from URL or generate one
    parsed_url = urlparse(image_url)
    filename = os.path.basename(parsed_url.path)
    if not filename or '.' not in filename:
        filename = f"image_{uuid4().hex}.jpg"  # Default to .jpg

    # 💾 Save image in binary mode
    filepath = os.path.join(output_dir, filename)
    with open(filepath, "wb") as f:
        f.write(response.content)

    print(f"✅ Image saved successfully as: {filepath}")

except requests.exceptions.RequestException as e:
    print(f"⚠️ Failed to fetch image: {e}")
except Exception as e:
    print(f"❌ Unexpected error: {e}")
