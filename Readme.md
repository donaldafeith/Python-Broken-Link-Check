# Broken Links and Images Checker

This Python script checks for broken links and images within a specified domain. It crawls through the website's HTML content, identifies all the links and images, and checks the status codes for each of them. The script then displays a list of broken links and external or broken images found on the website.

## Features

- Checks for broken internal links on the website
- Checks for broken or external images on the website
- Ignores SVG images and relative URLs starting with `/public/`
- Displays progress while checking links and images
- Handles connection errors gracefully

## Author

This script was created by Donalda.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

You can install the required libraries using the following command:


```pip install -r requirements.txt```

## Setup

It's recommended to use a virtual environment to install the required packages and run the script. Here's how you can set up a virtual environment:

1. Open a terminal or command prompt and navigate to the directory where you want to create the virtual environment.

2. Create a new virtual environment using the following command:

```python -m venv venv```

This will create a new directory called `venv` containing the virtual environment.

3. Activate the virtual environment:

- On Windows:
  ```
  venv\Scripts\activate
  ```

- On Unix or macOS:
  ```
  source venv/bin/activate
  ```

You should see `(venv)` at the beginning of your command prompt, indicating that the virtual environment is activated.

4. Install the required libraries by running:

```pip install -r requirements.txt```

This will install the `requests` and `beautifulsoup4` libraries in the virtual environment.

## Usage
1. Open a terminal or command prompt and navigate to the directory containing the script.
2. Ensure that the virtual environment is activated (`(venv)` should be visible in your command prompt).
3. Run the script using the following command:

```python broken_links_checker.py```

4. When prompted, enter the domain name you want to check (e.g., `example.com`).
5. The script will start checking for broken links and images on the specified domain and display the progress.
6. Once the check is complete, the script will display a list of broken links and broken or external images found on the website, if any.

## Example Output

```Enter the domain name: example.com
Checking links and images... 100.00% - Currently checking: https://example.com/images/logo.png

Broken links and images found on example.com:
Broken links:
https://example.com/broken-link
Broken or external images:
https://external-image.com/image.jpg
```
## License

This script is released under the [MIT License](https://opensource.org/licenses/MIT).