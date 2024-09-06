#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install selenium requests pillow


# In[2]:


import requests
import xml.etree.ElementTree as ET
from selenium import webdriver
from datetime import datetime
import os


# In[3]:


# Define headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Fetch the sitemap with headers
sitemap_url = "https://www.getcalley.com/page-sitemap.xml"
response = requests.get(sitemap_url, headers=headers)

# Check the status code
if response.status_code == 200:
    content = response.content.decode('utf-8')

    # Parse the XML content
    root = ET.fromstring(content)

    # Extract only the first 5 URLs
    urls = [url.findtext('{http://www.sitemaps.org/schemas/sitemap/0.9}loc') for url in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url')[:5]]

    # Print the first 5 URLs
    for url in urls:
        print(url)

else:
    print(f"Failed to retrieve the sitemap. Status code: {response.status_code}")


# In[5]:


pip install webdriver-manager


# In[6]:


from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Define the screen resolutions
resolutions = {
    'desktop': [(1920, 1080), (1366, 768), (1536, 864)],
    'mobile': [(360, 640), (414, 896), (375, 667)]
}

# Set up the WebDriver for Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # Run in headless mode if you don't want to open the browser window
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


# In[7]:


def capture_screenshot(driver, browser, device, resolution, url):
    # Set browser window size
    driver.set_window_size(*resolution)
    driver.get(url)

    # Create folder structure: Browser/Device/Resolution/Screenshot
    timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    folder_path = f"{browser}/{device}/{resolution[0]}x{resolution[1]}"
    os.makedirs(folder_path, exist_ok=True)

    # Save screenshot
    screenshot_path = f"{folder_path}/screenshot-{timestamp}.png"
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved at {screenshot_path}")


# In[8]:


# Loop through the first 5 URLs and take screenshots for each resolution
browser = "chrome"  # or firefox, safari based on your setup

for device, resolution_list in resolutions.items():
    for resolution in resolution_list:
        for url in urls:
            capture_screenshot(driver, browser, device, resolution, url)


# In[9]:


import os

def list_saved_screenshots(folder_path):
    if os.path.exists(folder_path):
        print(f"\nFiles in {folder_path}:")
        for file_name in os.listdir(folder_path):
            if file_name.endswith(".png"):
                print(f"- {file_name}")
    else:
        print(f"Folder {folder_path} does not exist.")

# After capturing screenshots, list saved files for verification
for device, resolution_list in resolutions.items():
    for resolution in resolution_list:
        folder_path = f"{browser}/{device}/{resolution[0]}x{resolution[1]}"
        list_saved_screenshots(folder_path)


# In[10]:


pip install pillow


# In[13]:


from PIL import Image
import os

# Define the path to the screenshot
screenshot_folder = "chrome/desktop/1920x1080"  # Change based on your setup
screenshot_file = os.listdir(screenshot_folder)[0]  # Get the first file in the folder
screenshot_path = os.path.join(screenshot_folder, screenshot_file)

# Open and display the image
image = Image.open(screenshot_path)
image.show()  # This will open the image


# In[12]:


import os
from PIL import Image
import IPython.display as display
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

# Define screen resolutions
resolutions = {
    'desktop': [(1920, 1080), (1366, 768), (1536, 864)],
    'mobile': [(360, 640), (414, 896), (375, 667)]
}

# Set up Chrome WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Function to capture and display screenshots
def capture_and_display_screenshot(driver, browser, device, resolution, url):
    driver.set_window_size(*resolution)
    driver.get(url)
    timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    folder_path = f"{browser}/{device}/{resolution[0]}x{resolution[1]}"
    os.makedirs(folder_path, exist_ok=True)
    screenshot_path = f"{folder_path}/screenshot-{timestamp}.png"
    driver.save_screenshot(screenshot_path)
    
    # Open and display the screenshot
    image = Image.open(screenshot_path)
    print(f"Displaying {screenshot_path}")
    display.display(image)

# List of URLs to test (example)
urls = ["https://www.example.com"]  # Replace with your list of URLs
browser = "chrome"

# Capture and display screenshots for each URL and resolution
for device, resolution_list in resolutions.items():
    for resolution in resolution_list:
        for url in urls:
            capture_and_display_screenshot(driver, browser, device, resolution, url)

# Close the driver
driver.quit()


# In[ ]:




