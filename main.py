import time
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver

# create a new instance of the Firefox driver


driver = webdriver.Chrome(executable_path="C:\\Users\\LS\\Desktop\\chromedriver")

# navigate to the website
start_time = time.time()
driver.get("http://localhost:8080/login.jsp")
end_time = time.time()



# Account Login
total_time_website = end_time - start_time
input_field = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/main/form/div[1]/div[1]/div/div[1]/input")
sleep(1)
input_field.send_keys("lior")
sleep(1)
input_field = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/main/form/div[1]/div[1]/div/div[2]/input")
input_field.send_keys("123456")
sleep(1)
start_time = time.time()
input_field = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/main/form/div[2]/div/input").click()



# Open Project
end_time = time.time()
total_time_login = end_time - start_time
# input_field = driver.find_element(By.XPATH,"/html/body/div[1]/header/nav/div/div[1]/ul/li[2]/a").click()
sleep(2)
# input_field = driver.find_element(By.XPATH,"/html/body/div[3]/header/nav/div/div[1]/ul/li[2]/div/div[1]/ul/li/a").click()
start_time = time.time()

#a
# Create Issues
end_time = time.time()
total_time_project = end_time - start_time
input_field = driver.find_element(By.XPATH,"/html/body/div[1]/header/nav/div/div[1]/ul/li[5]/a").click()
sleep(1)

input_field = driver.find_element(By.XPATH,"/html/body/section/div/div[1]/div/div/form/div/div[2]/div[1]/input")
sleep(1)

input_field.send_keys("123456")
sleep(1)
start_time = time.time()

input_field = driver.find_element(By.XPATH,"/html/body/section/footer/div/div/input").click()
end_time = time.time()
total_time_crete_issue = end_time - start_time


# Object STR
total_time_website = str(total_time_website)
total_time_login = str (total_time_login)
total_time_project= str(total_time_project)
total_time_crete_issue= str(total_time_crete_issue)

#Push input
total_time_website="Open Chrome- "+total_time_website
total_time_login="Sign in to Jira- "+total_time_login
total_time_project="Open Project- "+total_time_project
total_time_crete_issue="Create issue-"+total_time_crete_issue

# Open a file for writing (will create a new file if it doesn't exist)
with open('data.txt', 'w') as file:
    # Open the txt file in write mode
    data = [total_time_website,total_time_login, total_time_project, total_time_crete_issue,"LS"]
    for item in data:
        file.write("%s\n" % item)


# Print a message to confirm the data was exported
print("Data exported to data.txt!")

driver.quit()