import requests
from bs4 import BeautifulSoup
import time

def check_broken_links(domain):
    """
    Check for broken links and images within a specified domain.

    Args:
        domain (str): The domain name to check for broken links and images.

    Returns:
        None
        The function does not return any values directly. Instead, it outputs 
        information to the console, either printing the broken links and images found, 
        a message indicating no broken links or images, or an error message if it 
        cannot connect to the domain.
    """
    try:
        # Send a request to the domain and get the HTML response
        response = requests.get(f"https://{domain}")
        html = response.content

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")

        # Find all links and images within the HTML content
        links = soup.find_all("a", href=True)
        images = soup.find_all("img", src=True)

        # Initialize lists to store broken links and images
        broken_links = []
        broken_images = []

        # Initialize a counter for progress
        total_count = len(links) + len(images)
        current_item = 0

        # Loop through each link
        for link in links:
            href = link["href"]

            # Check if the link is relative (starts with "/")
            if href.startswith("/"):
                href = f"https://{domain}{href}"

            # Check if the link is within the specified domain
            if domain in href:
                try:
                    # Send a request to the link and check the status code
                    response = requests.head(href)
                    if response.status_code != 200:
                        broken_links.append(href)
                except requests.exceptions.RequestException:
                    broken_links.append(href)

            # Update progress
            current_item += 1
            progress = (current_item / total_count) * 100
            print(f"Checking links and images... {progress:.2f}% - Currently checking: {href}", end="\r")

            # Pause for a moment to avoid overwhelming the server
            time.sleep(0.1)

        # Loop through each image
        for image in images:
            src = image["src"]

            # Check if the image is an SVG or a relative URL starting with "public/"
            if not (src.endswith(".svg") or src.startswith("/public/")):
                # Check if the image is within the specified domain
                if domain not in src and not src.startswith("/"):
                    try:
                        # Send a request to the image and check the status code
                        response = requests.head(src)
                        if response.status_code != 200:
                            broken_images.append(src)
                    except requests.exceptions.RequestException:
                        broken_images.append(src)

            # Update progress
            current_item += 1
            progress = (current_item / total_count) * 100
            print(f"Checking links and images... {progress:.2f}% - Currently checking: {src}", end="\r")

            # Pause for a moment to avoid overwhelming the server
            time.sleep(0.1)

        # Print the broken links and images
        if broken_links or broken_images:
            print(f"\nBroken links and images found on {domain}:")
            if broken_links:
                print("Broken links:")
                for link in broken_links:
                    print(link)
            if broken_images:
                print("Broken or external images:")
                for image in broken_images:
                    print(image)
        else:
            print(f"No broken links or images found on {domain}")

    except requests.exceptions.RequestException:
        print(f"Error: Unable to connect to {domain}")

# Ask for the domain name
domain = input("Enter the domain name: ")

# Check for broken links and images
check_broken_links(domain)