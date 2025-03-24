import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import os
from openai import OpenAI

mobile_emlation = {
    'deviceMetrics': {
        'width': 1707,
        'height': 773,
        'pixelRatio': 1.0
    },
    'userAgent': 'Mozilla/5.0 (Linux; Android 13; IQOO 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36'
}

edge_options = Options()
edge_options.add_experimental_option('mobileEmulation', mobile_emlation)

wd = webdriver.Edge(service=Service('./msedgedriver.exe'), options=edge_options)
wd.get('https://skl.hduhelp.com/?type=5#/english/list')
wd.maximize_window()
time.sleep(2.5)

exam = WebDriverWait(wd, 150, 0.1).until(lambda wd:wd.find_element(By.XPATH, '//*[@id="van-tabs-1-1"]/span'))
exam.click()

began = WebDriverWait(wd, 150, 0.1).until(lambda wd: wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[2]/div/button'))
began.click()

identify = WebDriverWait(wd, 150,0.1).until(lambda wd:wd.find_element(By.XPATH,'/html/body/div[4]/div[2]/button[2]'))
identify.click()

for i in range(100):
    question = WebDriverWait(wd, 15, 0.5).until(lambda wd:wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[1]/span[2]'))
    optionA = WebDriverWait(wd, 15, 0.5).until(lambda wd:wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[3]/div/div[1]/div[1]/span'))
    optionB = WebDriverWait(wd, 15, 0.5).until(lambda wd:wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[3]/div/div[2]/div[1]/span'))
    optionC = WebDriverWait(wd, 15, 0.5).until(lambda wd:wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[3]/div/div[3]/div[1]/span'))
    optionD = WebDriverWait(wd, 15, 0.5).until(lambda wd:wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[3]/div/div[4]/div[1]/span'))
    
    con = f'''{question.text}\n{optionA.text}\n{optionB.text}\n{optionC.text}\n{optionD.text}'''
    
    client = OpenAI(
        api_key = '输入你的API密钥',
        base_url = '输入你的API URL'
    )
    
    completion = client.chat.completions.create(
        model = '输入你的模型',
        messages = [
            {
                'role': 'system',
                'content': 'user提供一个question和4个chioces，根据user的question和choices给出一个答案，要求question和答案选项的意思"相近"！最终回答一个用"--"包起来的大写字母作为答案,例如"--B--"'
            },
            {
                'role': 'user',
                'content': con
            }
        ]
    )
    
    WebDriverWait(wd, 10, 0.1).until(lambda wd:'--' in completion.choices[0].message.content)
    print(f"--------{i + 1}  " + completion.choices[0].message.content)
    
    if '--A--' in completion.choices[0].message.content:
        wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[3]/div/div[1]/div[1]/span').click()
    if '--B--' in completion.choices[0].message.content:
        wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[3]/div/div[2]/div[1]/span').click()
    if '--C--' in completion.choices[0].message.content:
        wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[3]/div/div[3]/div[1]/span').click()
    if '--D--' in completion.choices[0].message.content:
        wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[3]/div/div[4]/div[1]/span').click()
        
    completion.choices[0].message.content = None
    
    time.sleep(2)

time.sleep(1)

wd.find_element(By.XPATH, '//*//*[@id="app"]/div/div[2]/div/div/div[3]/span').click()
time.sleep(0.1)

wd.find_element(By.XPATH, '/html/body/div[4]/div[2]/button[2]').click()
time.sleep(300)