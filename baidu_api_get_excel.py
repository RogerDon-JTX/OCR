import requests
import base64
import json
import time
'''
表格文字识别(异步接口)
https://ai.baidu.com/ai-doc/OCR/Ik3h7y238
'''


url_token = 'https://aip.baidubce.com/oauth/2.0/token'
data_token = {"grant_type":"client_credentials",
              "client_id":"MlId2eUTUPAM7bITnTsRbIcW",
              "client_secret":"5AhZP54rIORdOpfW8HndnYmFY3wENOQK"}
resp_token = requests.post(url_token, data_token)
if resp_token:
    # print(resp_token.text)
    resp_token_json = json.loads(resp_token.text)
    access_token = resp_token_json['access_token']
    print(access_token)


    request_url = "https://aip.baidubce.com/rest/2.0/solution/v1/form_ocr/request"
    # 二进制方式打开图片文件
    f = open('10_14_change_little.jpg', 'rb')
    img = base64.b64encode(f.read())

    params = {"image":img}
    # access_token = 'UT4xAA75MBxuhWc0oMrsQwcpn4lSnP2H'
    if access_token:
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            print (response.json())
            request_id = response.json()["result"][0]['request_id']
            print(request_id)



            time.sleep(10)
            # 获取返回结果
            url_result = 'https://aip.baidubce.com/rest/2.0/solution/v1/form_ocr/get_request_result'
            request_url_result = url_result + "?access_token=" + access_token
            headers = {'content-type': 'application/x-www-form-urlencoded'}
            params2 = {"request_id":request_id, "result_type":"excel"}
            response_result = requests.post(request_url_result, data=params2, headers=headers)
            if response_result:
                print(response_result.json())
                time.sleep(10)
                print(response_result.text)
                time.sleep(10)
                print(response_result.text)
                time.sleep(10)
                print(response_result.text)
                time.sleep(10)
                print(response_result.text)
                time.sleep(10)
                print(response_result.text)

            url_result = 'https://aip.baidubce.com/rest/2.0/solution/v1/form_ocr/get_request_result'
            request_url_result = url_result + "?access_token=" + access_token
            headers = {'content-type': 'application/x-www-form-urlencoded'}
            params2 = {"request_id": request_id, "result_type": "json"}
            response_result = requests.post(request_url_result, data=params2, headers=headers)
            if response_result:
                print(response_result.json())
                time.sleep(10)