import requests
import hashlib
import time

url = "https://kveqcx.popcat.wtf/api/dapp/clickdata/add"

# 修改成你自己的地址 其余不要改动
address = "0x7777d020052554191de7d2105f587930a38f7777"
count = 1
lang = "en"
timestamp = str(int(time.time()))
key = "9aa440a7b7f383dde358d7919a1743e2"

headers = {
    "Host": "kveqcx.popcat.wtf",
    "Connection": "keep-alive",
    "Origin": "https://popcat.wtf",
    "Referer": "https://popcat.wtf/",
    "sec-ch-ua": '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    "Content-Length": "139",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/x-www-form-urlencoded",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "sec-ch-ua-platform": '"macOS"',
    "Origin": "https://popcat.wtf",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://popcat.wtf/",
    "Accept-Language": "zh-CN,zh;q=0.9"
}

# 记得切换VPN到全局模式


for _ in range(100000):  # 自定义循环次数
    timestamp = str(int(time.time()))

    data = f"address={address}&count={count}&lang={lang}&timestamp={timestamp}&key={key}"
    md5_hash = hashlib.md5(data.encode()).hexdigest()

    payload = {
        "address": address,
        "count": count,
        "lang": lang,
        "timestamp": timestamp,
        "sign": md5_hash
    }
    try:
        response = requests.post(url, data=payload, headers=headers)

        if response.status_code == 200:
            print("数据提交成功！当前点击数为:", response.json()['obj']['clickCount'])
        else:
            print("数据提交失败。")
    except requests.exceptions.ProxyError as e:
        print(f'ProxyError:{e}')
        requests.get(
            'http://www.pushplus.plus/send?token=1e8c5197d5f1470c9b6d614b767e1eb6&title=二号窗口&content=Proxy错误&template=html')
        exit()
    except requests.exceptions.SSLError as e:
        print(f'ProxyError:{e}')
        requests.get(
            'http://www.pushplus.plus/send?token=1e8c5197d5f1470c9b6d614b767e1eb6&title=二号窗口&content=SSL错误&template=html')
        exit()
