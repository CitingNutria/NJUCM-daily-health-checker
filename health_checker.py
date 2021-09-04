import requests
import datetime
import json
import os.path
import time

def healthCheck(name,password,userid,location):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': '',
        'DNT': '1',
        'Host': 'pdc.njucm.edu.cn',
        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        'sec-ch-ua-mobile': '?0',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    }

    postData = {
        "username": userid,
        "password": password,
        "execution": "a9399fcd-201a-47ee-a28f-92dd854f64dd_ZXlKaGJHY2lPaUpJVXpVeE1pSjkuVTNSUVZVMWxMMDltYVVobE1rUmFSbE00VUdod04wUXpPVFpZZVhNemFITnNVWFl6VVhCWVNWQk9jRGx1TlRKVVJXOHJTV1pvV1RadlZHOTRhMGR3UlZSVFNITnhja3BQTlZGemEyc3ZjekppV1RkRGMzbHBiemR2UjAxVWJFeFFXa1J3WkVWVWMwcEdVR1JJTDBScVZGTjJSRTVWWWxSSGJIbzBPV3g1Vms5RWQxVmhNVkJIVldaclJUbDNiVU5aY25abk4xbElUbGxLWmt4SFpXOWhjM2RIYkdablp6UXhMMGhpUTBaR2JEWkxXVmc1YUdGSWExRjRUV1ZEVVU0MlF6aFliWFY0TVc5alRWcG1TSHBRTTFWRWJVSkJRa1ZWU1c4MFZEUk5XVWgzTVZad2VsaEZZamd3ZEhKcFVXdEJjbUoxWVhwSE5tdEhOMXB2Tm05clVXOXdXVUpNYkZOUGNUbFJNWE5FYUhkaE9WSjBkRXB3VTJoWFZtdHljR3hUY1RCRFdXTlFPVEp2YmtFemJFOUZaSG8zV1RaRmJrazBSa28yV1VoWWVYSjJXamRPVmpKYVNtNXBOWEY2WlV4d2FHZHFaM1pNZFVjcmREZGtabnAxVFVKYUwxbHBWbE5HZVhOdVRIcFFTVU4wWlZkVWVXdFdiRWRJSzFweE4wTmFjVmRDTm1KcFVXOVlXR1p1Tm0wNGJWaFJjRzVCYkUxRFpFTXpibVYySzBaclRVbE9iMEoxWTJ4cVVIQXpXWFJRYWk5SlNUUTJLelJ4UkZoamFIUnFaM0JQT1VOS1kwaE5kbkpLTm1SM1NrbERTbEZwV2sxQ1kxTnBkMEZyYWpsWWVGQlFXVGx4V1Zsd1VqbDNhblZ0UkVsYVNWTlRiRUY0TWxwU1ZGWnVjRVpyZG5SNmVuSklVaTlKVEhZeWFXNDVPWEoxVTI5Q2JtbG9SR1J6UVV0NlozTkxNWGRPZVdnclZFZFdjazh6ZG5RclYzQTNNbTVrT0hwaFJVMVBhMGMyWWs4MVdYZFdjR0ZhSzFCbFdESjBNRk5RTUZBMFFWWjFZVVpDUWxOVFZrRm1ZVzFRWTBGU1ltdEZPVUZRUjFNNE9VZEVkMHRUTTI5M1V6SmliRTAzYzBjdlRGWnRORk5VY1VwNlRpOXlPRFJLYTJ4RFZWWlNhakl2WmtNdkwzWXZOV2xJTDNsaVpXTjVlWGxaYkV0U1ZXOXRiMVpPWmxOUWFXcHplR3h6WVRGclYzWjJjell4YmxadmRVdHRVV0l4YTBOM1owaFFVbnBKVUV4cE0yMW1VSEV3T1VSdVVra3phbU52TVhRMmVrbGFLemcyUldoV1lrTXllRVp1WWpsM2FrRnZiSHBPTmpaQ1psWTNaemhXTkRreGFFVXZXV05RTkVwalVEQnFXRGRJYUc1VVkxRnhUMFk1YlVwYVIwWkNhMWxzUm14NlFtVk9iWEV3ZDJKT1RqWjJiVGRSVDJsclJIZzRZWEZEV0dsc1RIZ3JVVVJrYjNGVldHWklObTVLVDFCYVFsTTNVMGxDWTNsME9URklRblZZZVZsdlZTdEZVMGx2WVd0NWMxSlRUM2hNWlRKbU9GZDVNQ3RDVVRONk1sSlpReTk0ZFZCR1NqTlNWekZDTm5oTU9YcFRha3BoTkdkWU9HRXZlVlo1Tm1GTU9YZGpaVk5sYW1oaVRWZHFUVUppVEVSdVpFOUxXa1JRV1hZclVEbG1WWFZOVjNkYVUweEVTVGhuSzA1WVRXRTFXRTlNWm1jNFVWcEJiVlJpZFd0R2VYZERWbTh4UkRoTk5qRk5USEUyVkRKTFpsb3JiWFZDUkdOb1QydHlXa2MyUW1wSVFsbGlUV1ZqV1dseE5FMDBSbUUzYUd0TWVrOHhNa3hrUkUxdVVtOHdOSE4yV1ROdkwyOHhWemRTVlVwM2VtaHlabkZxY2pkbGQwZDBLM2xuYTFndlVtRldlRFFyY0dKU2NEUnhNRGRGWjFGV2FVYzVlbGM0VDB0Uk5tcFpXVXBEYzJ0bVVYbEZNSFEzYmtKMGFWaEVOVkZoVEZoSWNWb3ZRVmxrYkRoVWFFVklNaXRIZGxsS1YyUlBlamhJSzBaTWFHdFNjRlZOWTNoeFdYQmlOazR4UW1sc1psRktUa3hxUmpWUEwyeE5OMVJ2YXpadUsybGxSbkJxU0hnM0swdElObm8zYzAxTFVVSlliV2xKZGxvMVVXOUhZWEF4ZURGaVFrd3lkVWsyUTFKM09IbEVSMDgwWTNoSE5qZERWbWxIYldwTGFYb3JNaTh3YlVGUkwxRm1ObUp4T1dRd09FODJVRmd3UVc1S2VuUlRXV2RGU0VFdlJuTlNSRmsyYzJKbFlUUnRVMDR5TjAxTmIyTkthMVp3U1ZWRGNGWkRRMnd4V0dkWEwydHBkRlZsUTBrelpXSmlWVEV5VEUxU2FFTjVMeTgxWlhoS1QzVnpiRVZMZG5GclZqaERiVVV6U1ZOQ04wOUViMDh3T1M5VlJrdHVPR0Z4TVRFeFF6SnBabWt3V0ZseWRGTlpablprUWpWWlVtaE5VVXQyYmt0NlFVazFaMmhTUzBSUE0zQkVObnBIU2pocVJpdDJaMHh3WVRsa1drWm5XV3RPY1RoemIzcFBZa3RXTTNSS2RqQkRiVFZTVDBnd2FYZHpPRTQwV1ZWRVRIaFphbVI1VDJwS04yOVZVRXBxUVc5b2QwZ3JiRXRDUW05SlpGRmlOSEJWVkRsS1NuWmphMm8zT1RZeVRtc3JkekZhVlc5S2FEbE1lQzlHYVRnelZHWmlORXhoTUUxVFJFTldSa2hyVTBscGJIcFJOMnhEY1d4bWFGSTJNVk4xUW01amEzUTRRMEZsZFhFM01WQlJjMWhVWlRnNFN6ZE1TSE5ZV0Znd2QxTndOVXhpUzNKSVNWSndiRFkyT1ZGU1VVRldjRXBWU25WYVFUVTVVREV3VURaNWRXMXRVRk5HVm5SSWFWRjRkWEUyY25nNU5IQXdkemxhUWt4d2QxQnBUM1lyUlM5dlFUZE1SbmRZVW5aWVJXTTBhMEp1VjBobU4xQldkMkl3VDNBeFFWQjJabmxCWlZJdlNYSTRWSEF3Vm5GNmVURTRkVXgwTm05R2VrOUJabG8wVUcxa2RGazJjVkJsWmxBd1ZuQTJjbm94YUdNNFRWbDRUbWxWZFRkS1NtWm9aakV4Tm14bE1teHNlVlJQVFdRd056WjFNVlpSWVU5Q1FqTndiMWhqWm5aamRUWTFjbVUwUkVoa2VuTkxTVWRyZWtsTVpqTjNkalJ1VkU5RldraEVOWGMzVEZZek9IZDBTbXhzTldoUFR6SjJhMFZVZDNkVVRXSlliSGxXZGk4eFMxQXhhMDB3Wm5FMFF6QldXRVowWkZGclNWaEJjMDh3U0c1cFpGUlZaazB6VGtGS2JscGFTREZIUW1aMFJWSXJlR3h3Um5odGRqVXlaRVJUWTFaTlJWbEhZbFpVWjBad2JqVk1RVFY2WjJoWlJsb3dlQ3R6YlhCSlVGUXhURzFETVRrclRXeGtkVmR0UVhFMU0wczFPR2tyUm5odGMxQTBZVVJWV0RWd01IZEJORmRuZVdablZHd3lSSGh5VkhSdlpYYzBjMWRrTlU1aFJqbFRWRnBIY25CQk9UVTFaa2cwYVhGNFpEaGhUblpCVWpSUlZpOVJSVGQxU2tjMk0zRkZjSEpqVG1GRmNIVTVUemxXUjJRMllreE1ZV3hySzJRMlpEWkpTaXRRV2xSbVpsWTNSSGwyYjFsdlJIUmxObVpzY1hBeVQxTlJkM0JNYjJZME4yUjVWVVJvTVRBMVJ6RlNjRTlzYm1KM2IwNUlXbEZHYTNOUU9IaENjV04wTkdvdkszWlVhMWQ0WWs4elUyZE5RV1JYTTNGTGNFWTBXRGRLYlVaNk5XUm1hVXRoVTAwM1VHOHZlbll5V21jMlRsUk1iRGcwTVVFelFWQkhaRnA1YkRsU2FFZFZaRlJYWlRreVZERTNlV2gwTXpkQ1ZrZFBZbE5JY0ZaR1NIaE1jV0ZqVldWcWNFUTNNbm8zYmxob1UyeFRjMEZMV0ZKdFRUUjFiMjR4V21GTlRtWndaMlpLTlRoS1QzZEJXak0zU25wVmJqaEhSakpJWlhNeGJXaHlhWFoyVFhSNVEwczNWMmRFY210VGRWTldWMnBqTTFjNWVFNUpiVTQwT0RWT1ZqWmhlVmcyUjA1UWVHRmljMUYyVjI0eFpETnhUbEU0SzNCaGFtZFhTVEp4YVc1QlR5czVjMjE1TURnM0swdExhVWs0WlVKclozQXhNR3RXWVZaWmNHSk9aVEZzZVd0VVVVeEpTRVUwWTB4cVRXRkxTbUo2WmpWMVV6aFpjRFkyV1dwNFNrRlBlRTAzU1dwbGJFbEZWbEpxYkV4MVlWUldUMDlqVFdVdmEwdEJOV1JOZFZoSFdHMWFkbTFDWldkemNrcDJlRmczU0hSQlFraDVaR3NyVWxkbFExTllkakJOTTFFelREbEhNM0Z5UldZMU1ucDRMMDVZUWpSRmRYbG5NWFJVU2pOQ1RYTkxPRk53ZDB3dlYxZDRSR3RHZHpoMllTOU9hVVUzYjFwTGNFZzNPQ3RWWm5ob2FHUlpTMHREY2xSSFMzZHJVbkkzVUZNdlIyMW9TM2hPYnpab1YyMUZNMVpwUzBwVlQwcDNOamR0TjFoNWJrSjRkMGhZVlV4MmVHOVlhbVZDYVVGQ09XOVdUM280WTFJelVEWTBVMDVwVkdscFVVTm9PVmxJVlZKa2RGWkJiRU41YVRSVFVXMDFVbU5KWVVoUFJ6Sk1aRVJvUkcweFFtOXZVbXhLSzNadFNUSnBTRUpYWWtJd2R6ZG9PSFJpUlc4eVdGRkplRzFOTTNwNWRFUkVTR3AzYW05RlpXaFJSVzAwTTJGbVJXcEJMMEpIYVU5TllYTkJRbTh5Vmtoa2JUZG9TV2hKYzJJcmJYUk9SV2RQUWpSSWVWTXlWVTk2TmpKUVdFeDViRzQwVW1abE0wWjVZMk01ZDNSdlZUQmpORkZZYmpSR2ExaGhiRmsyZVZKMlVHeGhlVWhxYURsQ1VHMWxNMnN5Y1c1d2IxaFlNRXR2VDBOTWNGbGtkR2s1SzNCQ1MyeHBVbWRIYUZwS2VHbFZNazlxUkVSWU9XcExkejAuSk1NNXlvS3lZZEtMYXNkejZzVlprSmI3NDhRUW5ZUWdsbFo1VzJWSWo4MVBWRkVZRVE2bmxWa0tFOHV4NnotYTcyNlRoNjJoV0JwZG5hUmpGM18xWkE=",
        "_eventId": "submit",
        "loginType": "1",
        "submit": "登 录"
    }

    params = {
        'DATETIME_CYCLE': '',
        'DLM_455532': '',
        'XM_699791': '',
        'RADIO_816586': '境内',
        'PICKER_894219': '',
        'TEXT_362765': '',
        'RADIO_773105': '健康',
        'RADIO_252419': '否',
        'SELECT_502461': '',
        'SELECT_96317': '36.7℃及以下',
        'RADIO_223980': '否',
        'SELECT_117762': '',
        'SELECT_631415': '36.8℃',
        'RADIO_944199': '否',
        'TEXT_625091': '',
        'RADIO_655596': '否',
        'TEXTAREA_901197': '无',
        'CHECKBOX_712638': '同意并承诺'
    }
    params['XM_699791'] = name
    params['DLM_455532'] = userid
    params['PICKER_894219'] = location
    now_time = datetime.datetime.now().strftime('%Y/%m/%d')
    params['DATETIME_CYCLE'] = now_time

    post_url = 'https://ids.njucm.edu.cn/login?service=https://pdc.njucm.edu.cn/pdc/formDesignApi/S/iKKUJvEV'
    post = requests.post(post_url, data=postData)
    # print(post.text)
    if post.text.find('提交'):
        print("登陆确认")
        url = 'https://pdc.njucm.edu.cn/pdc/formDesignApi/dataFormSave?wid=A25FF315167F5528E0533200140AA058&userId=' + userid
        res = requests.post(url, data=params)
        if res.status_code == 200:
            # print(params)
            print('提交成功')
            # print(res.text)
        else:
            print('Error' + res.status_code)



# userid = input("学号：")
# password = input("密码：")
# name = input("姓名：")
# location = input("地址：")

userid = ""
password = ""
name = ""
location = ""

print("本软件不承担任何责任（出了事别找我，不放心建议手动打卡。）")
while(True):
    if os.path.exists("inf.json"):
        print("发现信息文件")
        r = open('inf.json', 'r')
        content = r.read()
        a = json.loads(content)
        # print(type(a))
        # print(a)
        r.close()

        b = a[0]
        userid = b['userid']
        password = b['password']
        name = b['name']
        location = b['location']
        print("请确认：")
        print(name, userid, password, location)

        print("10秒后自动打卡")

        time.sleep(10)
        healthCheck(name, password, userid, location)
        time.sleep(5)
        break
    else:
        print("未发现信息文件")
        userid = input("学号：")
        password = input("密码：")
        name = input("姓名：")
        l1 = input("省级：")
        l2 = input("市级：")
        l3 = input("县/区级：")
        location = l1+","+l2+","+l3

        data = [{'userid': userid,
                 'password': password,
                 'name': name,
                 'location': location,
                 "model": 0}]
        data2 = json.dumps(data)
        w = open('inf.json', 'w')
        w.write(data2)
        w.close()











