from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import  re
import  time
from lxml import etree

browser=webdriver.Chrome()
wait=WebDriverWait(browser,50)
browser.maximize_window()
def research():
    try:
        browser.get('https://www.jd.com/')
        input = wait.until(
             EC.presence_of_element_located((By.CSS_SELECTOR, '#key'))
    )
        submit=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#search > div > div.form > button')))
        input.send_keys('python')
        submit.click()
        total=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#J_bottomPage > span.p-skip > em:nth-child(1)')))
        html = browser.page_source
        prase_html(html)
        return total.text
    except TimeoutError:
        return research()
def next_page(page_number):
    try:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > input'))
        )
        input.clear()
        # browser.execute_script("window.scrollBy(0,document.body.scrollHeight)", "")
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > a')))
        html = browser.page_source
        prase_html(html)
        input.send_keys(page_number)
        submit.click()
    except TimeoutError:
        next_page(page_number)


def prase_html(html):
        html = etree.HTML(html)
        items = html.xpath('//li[@class="gl-item"]')
        for i in range(len(items)):
            if html.xpath('//div[@class="p-img"]//img')[i].get('data-lazy-img') != "done":
                print("img:", html.xpath('//div[@class="p-img"]//img')[i].get('data-lazy-img'))
            else :
                print("img:",html.xpath('//div[@class="p-img"]//img')[i].get('src'))
            print("title:", html.xpath('//div[@class="p-name"]//em')[i].xpath('string(.)'))
            print("price:",html.xpath('//div[@class="p-price"]//i')[i].text)
            print("commit", html.xpath('//div[@class="p-commit"]//a')[i].text)
            print("-------------------------------------------------------------")


def main():
    total=research()
    total=int(re.compile('(\d+)').search(total).group(1))
    for i in range(2,total+1):
        time.sleep(2)
        next_page(i)
if __name__=='__main__':
    main()

