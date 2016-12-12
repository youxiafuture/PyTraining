import json
import re


file = open('./z.csv')
while True:
    fs = file.readline()
    pr = re.compile('\{\"content.*\}')
    js = re.findall(pr,fs)
    if js:
        format_js = json.loads(js[0])
        js_list = format_js['content']['body']['offers']
        for js_item in js_list:
            print js_item['refer_url']

file.close()
