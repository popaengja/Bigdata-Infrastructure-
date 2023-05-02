import pandas as pd
import requests
import json, os
from datetime import datetime



## create package
def sendMetaToCkan(url_ckan, api_key, ckan_meta):
    headers = {
        'content-type': 'application/json',
        'Authorization': api_key,
    }

    url = '{}/api/action/package_create'.format(url_ckan)
    respond = requests.post(url, data=json.dumps(ckan_meta), headers=headers)
    res_text = respond.content.decode('utf-8').replace('\n','br')
    print(res_text)
    
## Upload File
def uploadFileToCkan(url_ckan, api_key, file_meta, path_input):
    headers = {'X-CKAN-API-Key': api_key}
    url = '{}/api/action/resource_create'.format(url_ckan)
    with open(path_input, "rb") as f:
        form_file = {'upload': f}
        respond = requests.post(url, data=file_meta, headers=headers, files=form_file)
        res_text = respond.content.decode('utf-8').replace('\n','br')
        print(res_text)
        print('<b>File has been uploaded</b>')
dfs = pd.read_html(os.getenv("WEB_SCRIPY","https://docs.google.com/spreadsheets/d/e/2PACX-1vQlEs3FxFPwm-dpvU1YdsfRgsbfT9WdiXJHZm9kJgGTziPnk-y3TWtftbSbxj6Fe_g0NxYgqyVHTVU5/pubhtml?gid=1397577608&amp;single=true&amp;widget=true&amp;headers=false"))
df=dfs[0]
df.columns = df.iloc[0]
df = df[1:]
df = df.drop(columns=[1])
df.to_csv("df.csv",index=False)

now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

ckan_meta = {
      "name": "weather_srg02",
      "title": "WEATHER_SRG02",
      "notes": "ข้อมูลสภาพอากาศอัพเดททุก6ชั่วโมง",
      "data_type": "ข้อมูลสถิติ",
      "owner_org": "tu", ## ต้องสร้างองค์กรณ์ก่อนใน ckan และต้องใช้ชื่อ url
      "data_source": "https://docs.google.com/spreadsheets/d/e/2PACX-1vQlEs3FxFPwm-dpvU1YdsfRgsbfT9WdiXJHZm9kJgGTziPnk-y3TWtftbSbxj6Fe_g0NxYgqyVHTVU5/pubhtml?gid=1397577608&amp;single=true&amp;widget=true&amp;headers=false",
      "maintainer": "kitipop akrungsi",
      "update_frequency_unit": "วัน",
      "data_format": [
        "CSV"
      ],
      "maintainer_email": "kitipop.akr@dome.tu.ac.th",
      "objective": [
        "ยุทธศาสตร์ชาติ",
        "แผนพัฒนาเศรษฐกิจและสังคมแห่งชาติ"
      ],
      "data_category": "ข้อมูลสาธารณะ",
      "geo_coverage": "ประเทศ",
      "license_id": "License not specified"
}

url_ckan = os.getenv("CKAN_URL","https://ckan.data.storemesh.com" )
api_key = os.getenv("TOKEN" ,"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2ODA0OTg0NTAsImp0aSI6InBIeE5MbTFGVUpPTFQ1Mm9ad20zaGpQblFIV0JmNUtISWM5ck1rQk1GZ1FVakpUaktJbERfM1dib1NIQU5aYXBobzJCazByTU9MdXlFSUdjIn0.r7WW-76Yb6itT9z2mebvqN-_OVp1JYkx2H0kJVet7QU") ## ใส่ api key ตรงนี้

## for upload file
file_meta = {
    'package_id': ckan_meta['name'],
    'name': f'data-scripy-{now}',
}
path_input = './df.csv'

sendMetaToCkan(url_ckan, api_key, ckan_meta)
#{"help": "https://ckan.storemesh.com/api/3/action/help_show?name=package_create", "success": false, "error": {"maintainer": ["\u0e04\u0e48\u0e32\u0e17\u0e35\u0e48\u0e02\u0e32\u0e14\u0e2b\u0e32\u0e22"], "update_frequency_unit": ["\u0e04\u0e48\u0e32\u0e17\u0e35\u0e48\u0e02\u0e32\u0e14\u0e2b\u0e32\u0e22"], "maintainer_email": ["\u0e04\u0e48\u0e32\u0e17\u0e35\u0e48\u0e02\u0e32\u0e14\u0e2b\u0e32\u0e22"], "__type": "Validation Error", "objective": ["\u0e44\u0e21\u0e48\u0e16\u0e39\u0e01\u0e40\u0e25\u0e37\u0e2d\u0e01"], "data_type": ["\u0e04\u0e48\u0e32\u0e17\u0e35\u0e48\u0e02\u0e32\u0e14\u0e2b\u0e32\u0e22"], "geo_coverage": ["\u0e04\u0e48\u0e32\u0e17\u0e35\u0e48\u0e02\u0e32\u0e14\u0e2b\u0e32\u0e22"], "license_id": ["\u0e04\u0e48\u0e32\u0e17\u0e35\u0e48\u0e02\u0e32\u0e14\u0e2b\u0e32\u0e22"], "data_source": ["\u0e04\u0e48\u0e32\u0e17\u0e35\u0e48\u0e02\u0e32\u0e14\u0e2b\u0e32\u0e22"], "notes": ["\u0e04\u0e48\u0e32\u0e17\u0e35\u0e48\u0e02\u0e32\u0e14\u0e2b\u0e32\u0e22"], "owner_org": ["An organization must be provided", "\u0e04\u0e48\u0e32\u0e17\u0e35\u0e48\u0e02\u0e32\u0e14\u0e2b\u0e32\u0e22"], "data_format": ["\u0e44\u0e21\u0e48\u0e16\u0e39\u0e01\u0e40\u0e25\u0e37\u0e2d\u0e01"], "data_category": ["\u0e04\u0e48\u0e32\u0e17\u0e35\u0e48\u0e02\u0e32\u0e14\u0e2b\u0e32\u0e22"]}}

uploadFileToCkan(url_ckan, api_key, file_meta, path_input)
