import requests
from datetime import datetime

url = "https://www.comedycellar.com/lineup/api/"

todays_date = datetime.today().strftime('%Y-%m-%d')

payload = "action=cc_get_shows&json={\"date\":\"" + todays_date + "\",\"venue\":\"newyork\",\"type\":\"lineup\"}"
headers = {
  'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'sec-ch-ua-mobile': '?0',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
  'sec-ch-ua-platform': '"macOS"',
  'Accept': '*/*',
  'Origin': 'https://www.comedycellar.com',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'Referer': 'https://www.comedycellar.com/new-york-line-up/',
  'Accept-Encoding': 'gzip, deflate, br, zstd',
  'Accept-Language': 'en-US,en;q=0.9',
  'Cookie': '_gid=GA1.2.392388715.1726520523; _ga_2EBVDX89EN=GS1.1.1726527967.3.1.1726528852.24.0.0; _ga=GA1.2.167815312.1726520523; AWSALB=dthgembkXRwnspM3++Q9Yj3nLTAY9WOK3ByqQpLqvanhhUabwhMIq6wi/0iM8zg3ZjbaDZwSMcN0mFbe5mdVp2YqFM5zmHg+xXQ5nt/7kOh90puQcrqETrexkf7H; AWSALBCORS=dthgembkXRwnspM3++Q9Yj3nLTAY9WOK3ByqQpLqvanhhUabwhMIq6wi/0iM8zg3ZjbaDZwSMcN0mFbe5mdVp2YqFM5zmHg+xXQ5nt/7kOh90puQcrqETrexkf7H; AWSALB=YlgHk33BfZMPk2l6XPORJLE4PRVJZrVqWdVvpP2dVQubw3GEx/LGfGKk0Gj+RUBbe3YCaIT/xNIzLLBDhqOKJnxyeQFibFjgtaR8O8NKYe2BblFa2yaofkAPQHjJ; AWSALBCORS=YlgHk33BfZMPk2l6XPORJLE4PRVJZrVqWdVvpP2dVQubw3GEx/LGfGKk0Gj+RUBbe3YCaIT/xNIzLLBDhqOKJnxyeQFibFjgtaR8O8NKYe2BblFa2yaofkAPQHjJ'
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)

output = response.text

output_split = output.split("name")

name_list = []


for split in output_split:

    try:
        print(split)
        revised_split = split.split(">")
        grab_name = revised_split[1].split("<")
        name = grab_name[0]
        name_list.append(name)
    except Exception as e:
        continue

print("The following comedians are performing at a comedy cellar location this month:")
for name in name_list:
    if name != "":
        print(name)


