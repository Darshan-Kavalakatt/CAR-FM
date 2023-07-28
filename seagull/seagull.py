from selenium import webdriver
from selenium.webdriver.common.by import By

# Setup the webdriver
driver = webdriver.Chrome()  # or webdriver.Chrome(), depending on your browser
def fetch_stats(driver):
    section = driver.find_element_by_id('article_content')
    print(section)
    driver.back()
    return driver

url = 'https://en.aqua-fish.net'
# Open the webpage
driver.get('https://en.aqua-fish.net/fish/')

def search(driver):
    driver.execute_script("window.scrollBy(0, 100);")
    button = driver.find_element(By.ID, 'searchME')
    button.click()
    driver.implicitly_wait(10) 
    return driver
driver = search(driver)
elements = driver.find_elements(By.CLASS_NAME, 'appearParent')

def fetch_urls(driver,ranger):
    full_urls = []
    for x in range(ranger):
        print(x)
        construct = '//*[@id="LN'+str(x)+'_'+str(x)+'"]'
        hrefer = driver.find_element(By.XPATH,construct)
        href = hrefer.get_attribute('href')
        full_urls.append(href)
    return driver,full_urls



def writeURL(driver,elements):
    driver,urler = fetch_urls(driver,len(elements))
    with open('fish.txt', 'w') as f:
        for item in urler:
            f.write("%s\n" % item)
    return driver

def dataParser(info):
    sFishpedia = {}
    lines = info.split('\n')
    for x in range(len(lines)):
        if x in [0,1,2,3,6,7,10,11,12,13,14,15]:
            data = lines[x].split(":")
            sFishpedia[data[0]] = data[1]
        if x in [4,5,8,9]:
            pass
        if lines[x] == "Food and feeding":
            sFishpedia['Food'] = lines[x+1]
        elif lines[x] in ["Origin","Sexing","Breeding","Lifespan"]:
            sFishpedia[lines[x]] = lines[x+1]
        elif lines[x] == "Short description":
            sFishpedia['sDesc'] = lines[x+1]
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(sFishpedia)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    return sFishpedia
            
            
def scrapeData(driver):
    fFishpedia = {}
    with open('fish.txt','r') as f:
        for line in f:
            driver.get(line)
            info = driver.find_element(By.ID,'article_content')
            sFishpedia = dataParser(info.text)
            fFishpedia[sFishpedia["Scientific name"]] = sFishpedia
    print("############################################################")
    print(fFishpedia)
    print("############################################################")
scrapeData(driver)




# Get the text content of the div

# Click the button


# Don't forget to close the driver
driver.quit()
