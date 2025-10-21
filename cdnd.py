import os
import requests

# Create static directories if they don't exist
static_css_dir = os.path.join("static", "css")
static_js_dir = os.path.join("static", "js")
os.makedirs(static_css_dir, exist_ok=True)
os.makedirs(static_js_dir, exist_ok=True)

# CDN files to download: relative path -> URL
cdn_files = {
    "css/font-awesome.min.css": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css",
}

# Download each file
for relative_path, url in cdn_files.items():
    file_path = os.path.join("static", relative_path)
    print(f"Downloading {relative_path} from {url}")
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, "wb") as f:
            f.write(response.content)
        print(f"✅ Saved to {file_path}")
    else:
        print(f"❌ Failed to download {url} (Status code: {response.status_code})")
