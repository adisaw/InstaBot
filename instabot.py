from selenium import webdriver
from time import sleep
import config

class InstaBot:
	def __init__(self,username,password):
		self.driver=webdriver.Chrome()
		self.driver.get("https://instagram.com")
		sleep(2)
		self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
			.send_keys(username)
		self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
			.send_keys(password)
		self.driver.find_element_by_xpath('//button[@type="submit"]')\
			.click()
		sleep(15)



InstaBot(config.username,config.password)