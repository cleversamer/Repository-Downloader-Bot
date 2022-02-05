import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    # Registering Chrome driver in PATH
    os.environ['PATH'] += r"C://SeleniumDrivers"

    # Initializing the Chrome driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    # Taking repository info from user
    repo_owner_username = input("Repository owner username: ").strip()
    repo_name = input("Repository name: ").strip()
    repo_page = f'https://github.com/{repo_owner_username}/{repo_name}'

    # Finding the repository and giving the response
    time.sleep(1)
    print("Please wait while we finding the repository...")
    driver.get(repo_page)
    error_element = None
    try:
        error_element = driver.find_element(By.CSS_SELECTOR, 'label[for="not-found-search"]')
    except Exception:
        print("We have successfully found it.")

    if error_element is not None:
        raise Exception(
            f"Maybe there's no GitHub with the username '{repo_owner_username}' or the GitHub user"
            f"doesn't have a repository with the name '{repo_name}'."
        )

    # Getting the repository info
    repo_name = driver \
        .find_element(By.CSS_SELECTOR, 'a[data-pjax="#repo-content-pjax-container"]') \
        .get_attribute('innerHTML')

    repo_stars = driver \
        .find_element(By.ID, 'repo-stars-counter-star') \
        .get_attribute('innerHTML')

    print(
        f"{'*' * 15}\n"
        f"* Name: {repo_name}\n"
        f"* Stars: {repo_stars}\n"
        f"{'*' * 15}"
    )

    # Starting the download action
    time.sleep(1)
    print("Download now is starting...")
    code_btn = driver.find_elements(By.CSS_SELECTOR, 'summary[data-view-component="true"]')[1]
    code_btn.click()

    time.sleep(1)
    zip_download_btn = driver.find_element(By.CLASS_NAME, 'octicon-file-zip')
    zip_download_btn.click()
except Exception as ex:
    print(ex)
    driver.quit()
