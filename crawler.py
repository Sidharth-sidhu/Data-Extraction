from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import json

class Baby:
    def __init__(self,name,description):
        self.name = name
        self.description = description

    def tojson(self):
        return json.dumps(self, default=lambda o: o.__dict__)


chrome_path = r"driver/chromedriver"
driver = webdriver.Chrome(chrome_path)
driver.get("https://parenting.firstcry.com/baby-names/starting-with/a/?sort=Sort%20A%20to%20Z")
try:
    element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "root")))

finally:
    names = driver.find_element_by_class_name("names-list")
    items = names.find_elements_by_tag_name("li")


data = {}
data['babies'] = []

for item in items:
    babyNames = item.find_element_by_class_name("baby-name").text
    babyNameMeanings = item.find_element_by_class_name("nm-ming").text
    print(babyNames)
    data['babies'].append(Baby(babyNames,babyNameMeanings).tojson())

with open('babynames.json','w') as outfile:
    json.dump(data,outfile)


driver.close()
