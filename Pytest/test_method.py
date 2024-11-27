import time
import pytest
from selenium import webdriver


@pytest.mark.login   #only selected test method will execute under marker if we specify marker decorator
def test1():
    driver = webdriver.Chrome()
    time.sleep(2)
    driver.get("https://www.google.com")
    print(driver.title)


def test2():         #parallel execution -n number of workers
    driver = webdriver.Chrome()
    time.sleep(2)
    driver.get("https://www.amazon.com")
    print(driver.title)


def test3():
    driver = webdriver.Chrome()
    time.sleep(2)
    driver.get("https://www.youtube.com")
    print(driver.title)

