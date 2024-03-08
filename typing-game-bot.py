from selenium import webdriver
from selenium.webdriver.edge.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ^ set our constants up here, makes the code cleaner and easier to read
# ^ the text prompt and text_input_area have new IDs for every race, so I am using the full XPATH to ensure we get the same elements each time
url = "https://play.typeracer.com/"
begin_race_button = "//*[@id='gwt-uid-1']/a"
text_prompt = "/html/body/div[1]/div/div[2]/div/div[1]/div[1]/table/tbody/tr[2]/td[2]/div/div[2]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span"
text_input_area = "/html/body/div[1]/div/div[2]/div/div[1]/div[1]/table/tbody/tr[2]/td[2]/div/div[2]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input"
time_between_inputs = 0.085
final_result = "/html/body/div[1]/div/div[2]/div/div[1]/div[1]/table/tbody/tr[2]/td[2]/div/div[2]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[5]/td/div/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/table/tbody/tr/td/div/div"

# ? ANYTHING ABOVE 100 WPM GETS FLAGGED AS POTENTIAL CHEATING
# ? 0 gets immediately flagged for cheating and boots you out
# ? 0.5 is around 21 wpm
# ? 0.1 is around 87 wpm
# ? 0.005 is around 120 wpm and gets flagged for potential cheating
# ? 0.075 is around 104 wpm and gets flagged for potential cheating
# ? 0.085 is around 99 - 105 wpm


# this webdriver is how we can connect to chrome or edge or firefox, etc
# there is a middle man between our script and the browser, which is the sites driver
# the driver will read our code and execute it on the browser itself
service_obj = Service() # ! this starts the Browser driver (the middle man)
driver = webdriver.Edge(service = service_obj) # ! this starts our driver that allows us to access the Browser

# open the browser and go to the website
driver.get(url)

# wait for the site to load and for the start button to be available
driver.implicitly_wait(20)

# find the start button and click it to start
driver.find_element(By.XPATH, begin_race_button).click()

# this is where it gets interesting
# this website sperates its prompt into 2 or 3 differ <span> tags with awkward spacing between the words
# EXAMPLE PROMPT: "There was an orange cat."
# the tags would be split like this: "T" "here" "was an orange cat."
# so trying to join with a space would be "T here was an orange cat."
# trying to join without a space would be "Therewas an orange cat."
# no matter how you did it, it wasnt correct
# * this is obviously intentional to discourage what I am doing currently. but I am not making a profile and recording my score to harm this website
text_to_type = driver.find_elements(By.XPATH, text_prompt)

# we put all of the sperate span tags into a list
text = [elem.text for elem in text_to_type]

# when the list is length of 3, the pattern is the same
# join the first two elements of the list to make the first full word in our prompt, then add the rest of the text
# * NOTE: indexing in python is EXCLUSIVE.. which is why we have text[0:2] but it doesnt actually include the second element
if len(text) == 3:
    combined = "".join(text[0:2]) + " " + text[2]

# when the list is length of 2 (or maybe 1?), just combine them wth no space
else:
    combined = "".join(text)

# there is a short wait time where the input is not clickable, since this is a race, they want everyone to start at the same time
# we find the input bar element, and then we wait for it to be clickable before we actually use it
# if this takes longer than 15 seconds then an error is thrown
input_bar = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, text_input_area)))
input_bar.click()

# once we click into the input bar, we are ready to type out the prompt
# we do this one character at time, and we have to sleep input each input to avoid being flagged for cheating
for char in combined:
    input_bar.send_keys(char)
    time.sleep(time_between_inputs)


result = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, final_result)))
print(f"Final Result: {result.text}")

driver.close()

# ! breaks when the prompt starts with 'I' and is only split into 2 span elements ----- EXAMPLE: "I wish" becomes "Iwish"
# ! breaks when the beginning of the third element starts with ',' ------ EXAMPLE: "Today," becomes "Today ,"