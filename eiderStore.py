from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

def getEiderStores(result):

    eiderStoreURL = 'https://www.eider.co.kr/customercenter/store-info'
    browser = webdriver.Chrome()
    browser.get(eiderStoreURL)

    time.sleep(2)

    for n in range(1, 7):

        storeEle = browser.find_element(By.CSS_SELECTOR, f'#shopInfo > tr:nth-child({n}) > td:nth-child(1)')
        addressEle = browser.find_element(By.CSS_SELECTOR, f'#shopInfo > tr:nth-child({n}) > td.al > a')

        storeList = storeEle.text.strip()
        storeList = storeList.split()
        storeName = storeList[0].strip()
        storePhone = storeList[2].strip()
        storeAddress = addressEle.text

        print(f'storeName : {storeName} \t storePhone : {storePhone} \t storeAddress : {storeAddress}')


    for i in range(1, 51):

        try:
            nextBtn = browser.find_element(By.CSS_SELECTOR, '#pagenation > li.next > a')
            browser.execute_script('arguments[0].click()', nextBtn)

            time.sleep(1)

            for j in range(1, 7):

                storeEle = browser.find_element(By.CSS_SELECTOR, f'#shopInfo > tr:nth-child({j}) > td:nth-child(1)')
                addressEle = browser.find_element(By.CSS_SELECTOR, f'#shopInfo > tr:nth-child({j}) > td.al > a')

                storeList = storeEle.text.strip()
                storeList = storeList.split()
                storeName = storeList[0].strip()
                storePhone = storeList[2].strip()
                storeAddress = addressEle.text

                print(f'storeName : {storeName} \t storePhone : {storePhone} \t storeAddress : {storeAddress}')

                result.append([storeName] + [storePhone] + [storeAddress])

                if i == 50:
                    break

        except Exception as e:
            print(e)

    return



def main():

    result = []

    getEiderStores(result)

    eider_tbl = pd.DataFrame(result, columns=('Store Name', 'Phone', 'Address'))

    eider_tbl.to_csv("./resources/eiderStores.csv",
                     encoding='cp949',
                     mode='w',
                     index=True)

if __name__ == '__main__':
    main()

