from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Set up Chrome webdriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = "https://clutch.co/agencies/digital-marketing?page=1"

driver.get(url)


# Now, you can access the page source after JavaScript execution
page_source = driver.page_source

# Parse the page_source with BeautifulSoup
soup = BeautifulSoup(page_source, "html.parser")

# Find and extract the desired information from the parsed content
companies = soup.find_all("li", class_="provider-row")
#print(companies)
count=0

for soup in companies:
    count+=1
    # company name extractor

    company_name_elem = soup.find('h3', class_='company_info')
    # print(company_name_elem)
    if company_name_elem:
        company_name = company_name_elem.text.strip()
        print("Company Name:", company_name)

    else:
          print("Company Name not found")
   #company website link extractor
    website_link_elem = soup.find('a', class_='website-link__item') 
    # print(website_link_elem)    

    if website_link_elem:
        website_link = website_link_elem.get('href')
        print("Website Link:", website_link)
    else:
         print("Website Link not found")

    #company review and reting extractor
    rating = soup.find('span', class_='rating sg-rating__number').text.strip()
    reviews_count = soup.find('a', class_='reviews-link sg-rating__reviews directory_profile').text.strip()

   
    print("Rating:", rating)
    print("Reviews Count:", reviews_count)
    print("--------------------  ",count)

# Close the browser
driver.quit()



