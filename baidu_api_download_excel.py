# encoding: utf-8
import os
import sys
import requests
import time
import tkinter as tk
from tkinter import filedialog
from aip import AipOcr

# 定义常量
APP_ID = '...'
API_KEY = '...'
SECRET_KEY = '...'
# 初始化AipFace对象
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 读取图片
def get_file_content(filePath):
   with open(filePath, 'rb') as fp:
       return fp.read()


#文件下载函数
def file_download(url, file_path):
    r = requests.get(url)
    with open(file_path, 'wb') as f:
       f.write(r.content)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # 选择需要转换的文件夹  title没用
    data_dir = filedialog.askdirectory(title='dengling02') + '/'
    result_dir = filedialog.askdirectory(title='dengling02_excel') + '/'
    num = 0
    for name in os.listdir(data_dir):
        print ('{0} : {1} 正在处理：'.format(num+1, name.split('.')[0]))
        image = get_file_content(os.path.join(data_dir, name))
        res = client.tableRecognitionAsync(image)
        # print ("res:", res)
        if 'error_code' in res.keys():
            print ('Error! error_code: ', res['error_code'])
            sys.exit()
        req_id = res['result'][0]['request_id']    #获取识别ID号

        for count in range(1, 20):    #OCR识别也需要一定时间，设定10秒内每隔1秒查询一次
            res = client.getTableRecognitionResult(req_id)    #通过ID获取表格文件XLS地址
            print(res['result']['ret_msg'])
            if res['result']['ret_msg'] == '已完成':
                 break    #云端处理完毕，成功获取表格文件下载地址，跳出循环
            else:
                time.sleep(1)

        url = res['result']['result_data']
        xls_name = name.split('.')[0] + '.xls'
        file_download(url, os.path.join(result_dir, xls_name))
        num += 1
        print(os.path.join(result_dir, xls_name))
        print ('{0} : {1} 下载完成。'.format(num, xls_name))
        time.sleep(1)
