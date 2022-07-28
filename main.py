from email import header
from inspect import formatannotationrelativeto
import os
from colorama import Fore as cfore
import requests as res
from sys import exit,argv
#url = input("url:\n")
url = 'http://127.0.0.1:8000/index.html'

retry_num = 0
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
def conntect(url,headers=header,retry_num_max=3): 

    a = res.get(url,headers=headers)
    if a.status_code == 404:
        print(cfore.YELLOW+ "404 not found" +cfore.RESET)
        retry_num += 1
        if retry_num <= retry_num_max:
            print(f"retry...({retry_num} times)")
            conntect(url,headers=header,retry_num_max=3)
        else:
            print(cfore.RED+ "could not find...\nexit.")
            exit()
        
    elif a.status_code == 200:
        print("conncted succeeded.")
        return a

def get_file_name():

    fl = url[::-1]
    fa = fl.find('/')
    fl = fl[:fa]
    file_name = fl[::-1]
    return file_name

def save(a,save_path,file_name=get_file_name()):
    with open(save_path+file_name,'wb') as f:
        f.write(a.content)

def download(url,headers=header,retry_num_max=3,save_path='.'):
    a = conntect()
    save(a,save_path=save_path)