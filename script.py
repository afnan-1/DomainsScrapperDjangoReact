import requests
import json
from bs4 import BeautifulSoup
url = 'https://member.expireddomains.net/'
LOGIN_ROUTE = 'login/'
HEADERS  = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'referer':url+LOGIN_ROUTE,'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-site',
            'sec-fetch-user': '1',
            'cache-control': 'max-age=0'}
s = requests.session()
login_payload = {
    'login':'afnan11223344',
    'password':"asdfgh123"
}
login_req = s.post(url+LOGIN_ROUTE,headers=HEADERS,data=login_payload)
cookies = login_req.cookies

PageUrl = '?/start=25'
soup = BeautifulSoup(s.post(url+'domains/expiredcom/',headers=HEADERS,data={
    'fnumhost':1,'fsephost':1,'fwhoisagemax':0,'fwhoisage': 0,'fabirth_yearmax': 0,
    'fabirth_year': 0,'fworden': 1,'fadddate': 0,'fenddate': 0,'fendname': 0,
    'fprice': 0,'fprovidertype': 0,'flimit': 25,'button_submit': 'Apply Filter'}).text, 'html.parser')
domains = []
for domain in soup.findAll('a',class_='namelinks'):
    domains.append(domain.text)
    
print(domains)


# GODADDY_URL = 'https://api.godaddy.com/v1/appraisal/'
# GODADDY_HEADERS  = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#             'Referer':GODADDY_URL,'Accept':'application/json',
#             'Origin':'https://uk.godaddy.com',
#             'Host':'api.godaddy.com',
#             'Sec-Fetch-Dest': 'empty',
#             'Sec-Fetch-Mode': 'cors',
#             'Sec-Fetch-Site': 'same-site',
#             'sec-fetch-user': '1'}
# sortedDomains=[]
# for i in domains:
#     r = requests.get(GODADDY_URL+i,GODADDY_HEADERS)    
#     res = json.loads(r.text)
#     try:
#         if res["govalue"] > 2000:
#         sortedDomains.append({"domain":i,'Estimated_price':res["govalue"]})
#         else:
#             pass
#     except:
#         pass
        
# print(sortedDomains)
        