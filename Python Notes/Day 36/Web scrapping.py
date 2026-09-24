'''100 DAYS OF PYTHON
DAY 36 — WEB SCRAPING USING PYTHON

==================================================
1. WEB SCRAPING
==================================================

Web scraping is the process of automatically collecting
information from websites using Python.

Instead of manually copying data, a program can retrieve
and extract the required information.

Applications:
- Data Science
- Data Analytics
- Artificial Intelligence
- Machine Learning
- Automation
- Business Intelligence


==================================================
2. WHY USE WEB SCRAPING?
==================================================

Web scraping can be used to:

- Collect website information automatically
- Reduce manual effort
- Process large amounts of data
- Monitor changes on websites
- Store data for later analysis


==================================================
3. REAL-WORLD APPLICATIONS
==================================================

- Product price tracking
- News collection
- Job data collection
- Weather information
- Stock market analysis
- Hotel and flight price monitoring
- Research
- Lead generation
- Competitor analysis
- Business intelligence


==================================================
4. WEB SCRAPING WORKFLOW
==================================================

Website
   ↓
Requests
   ↓
HTML Source
   ↓
BeautifulSoup
   ↓
Extract Required Data
   ↓
CSV / Excel / Database


==================================================
5. HTML
==================================================

HTML stands for HyperText Markup Language.

It is used to structure web pages.

Common HTML elements include:

- <html>
- <head>
- <title>
- <body>
- <h1>
- <p>
- <a>
- <img>
- <table>

BeautifulSoup can read this HTML structure and help
extract the required information.


==================================================
6. REQUESTS MODULE
==================================================

Requests is a Python library used to send HTTP requests
and retrieve webpage content.

Installation:

pip install requests

Import:

import requests


==================================================
7. GET REQUEST
==================================================

The get() method sends an HTTP GET request.

Syntax:

requests.get(url)

Example:

import requests

url = "https://codegnan.com"
response = requests.get(url)

print(response)


==================================================
8. RESPONSE OBJECT
==================================================

requests.get() returns a Response object.

Important attributes:

status_code
    Returns the HTTP status code.

text
    Returns webpage HTML as text.

content
    Returns webpage content as bytes.

headers
    Returns response headers.

url
    Returns the final URL.

cookies
    Returns received cookies.

encoding
    Returns webpage encoding.

elapsed
    Shows the response time.


==================================================
9. COMMON HTTP STATUS CODES
==================================================

200 → Success
201 → Resource Created
301 → Permanently Redirected
302 → Temporarily Redirected
400 → Bad Request
401 → Unauthorized
403 → Forbidden
404 → Page Not Found
405 → Method Not Allowed
500 → Internal Server Error
502 → Bad Gateway
503 → Service Unavailable


==================================================
10. CHECK WEBSITE STATUS
==================================================

Example:

import requests

url = "https://codegnan.com"
response = requests.get(url)

if response.status_code == 200:
    print("Website is accessible.")
else:
    print("Unable to access the website.")


==================================================
11. BEAUTIFULSOUP
==================================================

BeautifulSoup is a Python library used to parse HTML
and XML documents.

It makes HTML easier to search and navigate.

Installation:

pip install beautifulsoup4

Import:

from bs4 import BeautifulSoup


==================================================
12. CREATING A BEAUTIFULSOUP OBJECT
==================================================

Syntax:

BeautifulSoup(html_content, "html.parser")

Example:

import requests
from bs4 import BeautifulSoup

url = "https://codegnan.com"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


==================================================
13. FINDING HTML ELEMENTS
==================================================

find()
------
Returns the first matching element.

Syntax:

soup.find("tag")


find_all()
----------
Returns all matching elements.

Syntax:

soup.find_all("tag")


Example:

heading = soup.find("h1")
print(heading.text)


==================================================
14. TEXT EXTRACTION
==================================================

The text property extracts the text contained inside
an HTML element.

Example:

heading = soup.find("h1")
print(heading.text)


==================================================
15. EXTRACT WEBSITE TITLE
==================================================

Example:

title = soup.find("title")
print(title.text)


Another method:

print(soup.title.text)


==================================================
16. EXTRACT HEADINGS
==================================================

Example:

headings = soup.find_all(["h1", "h2", "h3"])

for heading in headings:
    print(heading.text)


==================================================
17. EXTRACT PARAGRAPHS
==================================================

Example:

paragraph = soup.find("p")
print(paragraph.text)


==================================================
18. EXTRACT HYPERLINKS
==================================================

Links are generally stored inside the href attribute.

Example:

links = soup.find_all("a")

for link in links:
    print(link.get("href"))


==================================================
19. get() METHOD
==================================================

get() is used to retrieve the value of an HTML attribute.

Syntax:

tag.get("attribute")


Example:

link = soup.find("a")
print(link.get("href"))


==================================================
20. EXTRACT IMAGES
==================================================

Image locations are commonly stored in the src attribute.

Example:

images = soup.find_all("img")

for image in images:
    print(image.get("src"))


==================================================
21. EXTRACT TABLES
==================================================

Tables are represented using the <table> HTML tag.

Example:

tables = soup.find_all("table")

print(tables)

Tables may contain:
- Employee information
- Student records
- Product details
- Stock information
- Reports


==================================================
22. COMMON BEAUTIFULSOUP METHODS
==================================================

find()
→ Finds the first matching element.

find_all()
→ Finds all matching elements.

text
→ Extracts text from an element.

get()
→ Retrieves an attribute value.

select()
→ Finds elements using CSS selectors.

select_one()
→ Finds the first matching CSS selector.

parent
→ Accesses the parent element.

children
→ Accesses child elements.

prettify()
→ Displays formatted HTML.


==================================================
23. CSS SELECTORS
==================================================

CSS selectors help locate specific elements in HTML.

Select by tag:

soup.select("h2")


Select by class:

soup.select(".btn")


Select by ID:

soup.select("#header")


Select nested elements:

soup.select("nav a")


==================================================
24. select()
==================================================

select() returns all elements matching a CSS selector.

Example:

links = soup.select("a")

for link in links:
    print(link.get("href"))


==================================================
25. select_one()
==================================================

select_one() returns only the first matching element.

Example:

title = soup.select_one("title")
print(title.text)


==================================================
26. parent
==================================================

The parent property accesses the parent HTML element.

Example:

title = soup.find("title")
print(title.parent.name)


==================================================
27. children
==================================================

The children property allows access to the child elements
of an HTML tag.

Example:

body = soup.find("body")

for child in body.children:
    print(child)


==================================================
28. prettify()
==================================================

prettify() displays HTML in a structured and indented format.

Example:

print(soup.prettify())


==================================================
29. BASIC SCRAPING EXAMPLE
==================================================

import requests
from bs4 import BeautifulSoup

url = "https://codegnan.com"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.text)


==================================================
30. DYNAMIC WEBSITES
==================================================

Requests and BeautifulSoup do not always work for websites
whose content is loaded dynamically using JavaScript.

For example, a webpage may initially return:

<div id="root"></div>

The actual information is then loaded after the page opens.

In such cases, the source suggests using:

- Selenium
- Playwright
- Backend APIs, when available


==================================================
31. KEY TAKEAWAYS
==================================================

- Requests is used to retrieve webpage content.
- BeautifulSoup is used to parse and extract HTML data.
- status_code helps check the server response.
- find() returns the first matching element.
- find_all() returns multiple matching elements.
- get() extracts attribute values.
- CSS selectors provide another way to locate elements.
- Web scraping can automate data collection.
- Not every website can be scraped using only Requests
  and BeautifulSoup.
- JavaScript-based websites may require additional tools.'''

# ============================================================
# DAY 35 - WEB SCRAPING USING PYTHON
# 100 Days of Python
# ============================================================

import requests
from bs4 import BeautifulSoup


URL = "https://codegnan.com"


# ============================================================
# PROGRAM 1: SEND GET REQUEST
# ============================================================

def program_1_get_request():
    response = requests.get(URL)

    print(response)


# ============================================================
# PROGRAM 2: CHECK STATUS CODE
# ============================================================

def program_2_status_code():
    response = requests.get(URL)

    print("Status Code:", response.status_code)


# ============================================================
# PROGRAM 3: CHECK WEBSITE ACCESS
# ============================================================

def program_3_check_website():
    response = requests.get(URL)

    if response.status_code == 200:
        print("Website is accessible.")
    else:
        print("Unable to access the website.")


# ============================================================
# PROGRAM 4: PRINT HTML SOURCE
# ============================================================

def program_4_html_source():
    response = requests.get(URL)

    print(response.text[:1000])


# ============================================================
# PROGRAM 5: PRINT RESPONSE HEADERS
# ============================================================

def program_5_headers():
    response = requests.get(URL)

    print(response.headers)


# ============================================================
# PROGRAM 6: PRINT FINAL URL
# ============================================================

def program_6_final_url():
    response = requests.get(URL)

    print("Final URL:", response.url)


# ============================================================
# PROGRAM 7: PRINT COOKIES
# ============================================================

def program_7_cookies():
    response = requests.get(URL)

    print(response.cookies)


# ============================================================
# PROGRAM 8: PRINT ENCODING
# ============================================================

def program_8_encoding():
    response = requests.get(URL)

    print("Encoding:", response.encoding)


# ============================================================
# PROGRAM 9: PRINT RESPONSE TIME
# ============================================================

def program_9_response_time():
    response = requests.get(URL)

    print("Response Time:", response.elapsed)


# ============================================================
# PROGRAM 10: CREATE BEAUTIFULSOUP OBJECT
# ============================================================

def program_10_create_soup():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    print(soup.title)


# ============================================================
# PROGRAM 11: EXTRACT WEBSITE TITLE
# ============================================================

def program_11_website_title():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    print("Title:", soup.title.text)


# ============================================================
# PROGRAM 12: EXTRACT FIRST HEADING
# ============================================================

def program_12_first_heading():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    heading = soup.find("h1")

    if heading:
        print("Heading:", heading.text.strip())
    else:
        print("No H1 heading found.")


# ============================================================
# PROGRAM 13: EXTRACT FIRST PARAGRAPH
# ============================================================

def program_13_first_paragraph():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    paragraph = soup.find("p")

    if paragraph:
        print("Paragraph:", paragraph.text.strip())
    else:
        print("No paragraph found.")


# ============================================================
# PROGRAM 14: FIND FIRST H1 TAG
# ============================================================

def program_14_find_h1():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    heading = soup.find("h1")

    print(heading)


# ============================================================
# PROGRAM 15: FIND ALL H2 HEADINGS
# ============================================================

def program_15_find_all_h2():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    headings = soup.find_all("h2")

    for heading in headings:
        print(heading.text.strip())


# ============================================================
# PROGRAM 16: EXTRACT ALL HEADINGS
# ============================================================

def program_16_all_headings():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    headings = soup.find_all(["h1", "h2", "h3"])

    for heading in headings:
        print(heading.text.strip())


# ============================================================
# PROGRAM 17: EXTRACT ALL HYPERLINKS
# ============================================================

def program_17_all_links():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.find_all("a")

    for link in links:
        print(link.get("href"))


# ============================================================
# PROGRAM 18: EXTRACT FIRST LINK
# ============================================================

def program_18_first_link():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    link = soup.find("a")

    if link:
        print("Link:", link.get("href"))


# ============================================================
# PROGRAM 19: EXTRACT ALL IMAGE URLs
# ============================================================

def program_19_all_images():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    images = soup.find_all("img")

    for image in images:
        print(image.get("src"))


# ============================================================
# PROGRAM 20: EXTRACT ALL TABLES
# ============================================================

def program_20_all_tables():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    tables = soup.find_all("table")

    print("Number of tables:", len(tables))

    for table in tables:
        print(table)


# ============================================================
# PROGRAM 21: USE get() METHOD
# ============================================================

def program_21_get_attribute():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    link = soup.find("a")

    if link:
        print(link.get("href"))


# ============================================================
# PROGRAM 22: USE SELECT()
# ============================================================

def program_22_css_select():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.select("a")

    for link in links:
        print(link.get("href"))


# ============================================================
# PROGRAM 23: USE SELECT_ONE()
# ============================================================

def program_23_select_one():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.select_one("title")

    if title:
        print(title.text)


# ============================================================
# PROGRAM 24: SELECT BY CLASS
# ============================================================

def program_24_select_class():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    elements = soup.select(".btn")

    for element in elements:
        print(element.text.strip())


# ============================================================
# PROGRAM 25: SELECT BY ID
# ============================================================

def program_25_select_id():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    element = soup.select("#header")

    print(element)


# ============================================================
# PROGRAM 26: SELECT NESTED ELEMENTS
# ============================================================

def program_26_nested_selector():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.select("nav a")

    for link in links:
        print(link.text.strip())


# ============================================================
# PROGRAM 27: FIND PARENT ELEMENT
# ============================================================

def program_27_parent():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("title")

    if title:
        print("Parent:", title.parent.name)


# ============================================================
# PROGRAM 28: ACCESS CHILDREN
# ============================================================

def program_28_children():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    body = soup.find("body")

    if body:
        for child in body.children:
            print(child)


# ============================================================
# PROGRAM 29: PRETTIFY HTML
# ============================================================

def program_29_prettify():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    print(soup.prettify())


# ============================================================
# PROGRAM 30: COUNT HYPERLINKS
# ============================================================

def program_30_count_links():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.find_all("a")

    print("Total Links:", len(links))


# ============================================================
# PROGRAM 31: COMPLETE SCRAPING EXAMPLE
# ============================================================

def program_31_complete_scraper():
    response = requests.get(URL)

    if response.status_code != 200:
        print("Website could not be accessed.")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    print("WEBSITE TITLE")
    print("--------------------")

    if soup.title:
        print(soup.title.text.strip())

    print("\nHEADINGS")
    print("--------------------")

    for heading in soup.find_all(["h1", "h2", "h3"]):
        text = heading.text.strip()

        if text:
            print(text)

    print("\nLINKS")
    print("--------------------")

    for link in soup.find_all("a"):
        href = link.get("href")

        if href:
            print(href)

    print("\nIMAGES")
    print("--------------------")

    for image in soup.find_all("img"):
        src = image.get("src")

        if src:
            print(src)


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    # Run one program at a time.

    program_1_get_request()

    program_2_status_code()
    program_3_check_website()
    program_4_html_source()
    program_5_headers()
    program_6_final_url()
    program_7_cookies()
    program_8_encoding()
    program_9_response_time()
    program_10_create_soup()
    program_11_website_title()
    program_12_first_heading()
    program_13_first_paragraph()
    program_14_find_h1()
    program_15_find_all_h2()
    program_16_all_headings()
    program_17_all_links()
    program_18_first_link()
    program_19_all_images()
    program_20_all_tables()
    program_21_get_attribute()
    program_22_css_select()
    program_23_select_one()
    program_24_select_class()
    program_25_select_id()
    program_26_nested_selector()
    program_27_parent()
    program_28_children()
    program_29_prettify()
    program_30_count_links()
    program_31_complete_scraper()



