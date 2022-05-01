import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


data_base = ['Lora is a famous painter who just ',
             'Moni is really handsome guy who just start ',
             'The story starts from one small village where ',
             'One of the biggest artist came in the town and ',
             'Today I made my first money as a Programmer. I sold my laptop.',
             'One really fat guy went out with a girl from date app and '
             ]


pozdrav_links = ['https://www.youtube.com/watch?v=xIj1UEs-lzA', 'https://www.youtube.com/watch?v=vFLJ5e_Kwjg',
                 'https://www.youtube.com/watch?v=3Bf9niztf5E', 'https://www.youtube.com/watch?v=7cNNVCBYOck',
                 'https://www.youtube.com/watch?v=NBwH57yj1Y8', 'https://www.youtube.com/watch?v=6ASmXHTTtJ0']


def get_website_link():
    url = "https://www.shortlyai.com/"
    driver.get(url)
    driver.maximize_window()


# click on sign in button
def click_sign_in_button():
    sign_in = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/a[2]/button')
    sign_in.click()


# fill the names in sign in form
def fill_name_sing_in_form():
    first_name = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/input[1]')
    first_name.send_keys('Antonia')

    second_name = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/input[2]')
    second_name.send_keys('G')


# function for randomization of the email for registration form
def creates_emails_for_registration():
    letters = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
               "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", )

    email_name = ''
    for x in range(7):
        email_name += random.choice(letters)

    email = email_name + "@gmail.com"

    return email


# fill with random email
def fill_random_email():
    email = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/input[3]')
    current_email = creates_emails_for_registration()
    time.sleep(3)
    email.send_keys(current_email)


def fill_password():
    password = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/input[4]')
    password.send_keys('esttesttest2022')


def click_login_button():
    log_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/a[3]/p')
    log_button.click()


def get_directly_to_the_story_page():
    # get directly to the story page, where your program will start writing text
    url_start_story = 'https://www.shortlyai.com/write'
    driver.get(url_start_story)


def start_story_page():
    start = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/a[2]/button')))
    start.click()

    # story title
    title = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[1]/textarea')
    title.send_keys("The secret story")


def use_random_text_to_start_the_story():
    # choose random text from the jokes list and start your story
    story_text = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[2]/textarea')
    el = random.choice(data_base)
    start_text = 'Hi there, let me tell you one really good story. ' + el
    story_text.send_keys(start_text)


def save_text_story():
    try:
        save_text = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div/div[1]/button')
        save_text.click()

    except Exception as ex:
        print(ex)


def click_write_for_me():
    # click "write for me" and the AI will continue your story
    write_for_me = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[5]/div/a/p')))
    write_for_me.click()


def delete_the_story():
    bin_to_delete_story = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div/button[2]')))
    bin_to_delete_story.click()

    time.sleep(3)
    agree_to_del = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]/button')
    agree_to_del.click()


def pozdrav_with_bg_song():
    # get a url of youtube pozdrav
    pozdrav_url = random.choice(pozdrav_links)
    driver.get(pozdrav_url)

    time.sleep(1)
    for times in range(4):
        try:
            agree_terms = driver.find_element(By.XPATH, '/html/body/ytd-app/ytd-consent-bump-v2-lightbox'
                                                        '/tp-yt-paper-dialog/div[4]'
                                                        '/div[2]/div[5]/div[2]/ytd-'
                                                        'button-renderer[2]/a/tp-yt-paper-button')

            agree_terms.click()
            break

        except Exception as ex:
            print(ex)
            driver.refresh()


get_website_link()
click_sign_in_button()
fill_name_sing_in_form()
fill_random_email()
fill_password()
time.sleep(2)
click_login_button()
time.sleep(2)
get_directly_to_the_story_page()
start_story_page()
use_random_text_to_start_the_story()
save_text_story()
click_write_for_me()
# wait for a while and delete the story
time.sleep(200)
save_text_story()
delete_the_story()

time.sleep(3)
# just a small greet with bg song
pozdrav_with_bg_song()
