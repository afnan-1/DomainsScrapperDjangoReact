from django.shortcuts import render
import requests
import json
from bs4 import BeautifulSoup
from requests import api
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from core.settings import USERNAME,PASSWORD
# helper functions


def login_req():
    url = "https://member.expireddomains.net/"
    LOGIN_ROUTE = "login/"
    HEADERS = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "referer": url + LOGIN_ROUTE,
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-site",
        "sec-fetch-user": "1",
        "cache-control": "max-age=0",
    }
    global s
    s = requests.session()
    login_payload = {"login": USERNAME, "password": PASSWORD}
    login_req = s.post(url + LOGIN_ROUTE, headers=HEADERS, data=login_payload)
    cookies = login_req.cookies


login_req()


def appraisal_tool(price):
    global sortedDomains
    sortedDomains = []
    GODADDY_URL = "https://api.godaddy.com/v1/appraisal/"
    GODADDY_HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": GODADDY_URL,
        "Accept": "application/json",
        "Origin": "https://uk.godaddy.com",
        "Host": "api.godaddy.com",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "sec-fetch-user": "1",
    }

    for i in domains:
        r = requests.get(GODADDY_URL + i, GODADDY_HEADERS)
        res = json.loads(r.text)
        try:
            if res["govalue"] > price:
                sortedDomains.append({"domain": i, "Estimated_price": res["govalue"]})
                godaddy = GodaddyAppraisal(domain=i, estimated_price=res["govalue"])
                godaddy.save()
            else:
                pass
        except:
            pass


@api_view()
def scrape_domains(request, limit=50, page_no="#"):
    global domains
    domains = []
    url = "https://member.expireddomains.net/"
    LOGIN_ROUTE = "login/"
    HEADERS = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "referer": url + LOGIN_ROUTE,
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-site",
        "sec-fetch-user": "1",
        "cache-control": "max-age=0",
    }
    if page_no != "#":
        page_no = f"?/start={page_no}"
    soup = BeautifulSoup(
        s.post(
            url + "domains/expiredcom/" + page_no,
            headers=HEADERS,
            data={
                "fnumhost": 1,
                "fsephost": 1,
                "fwhoisagemax": 0,
                "fwhoisage": 0,
                "fabirth_yearmax": 0,
                "fabirth_year": 0,
                "fworden": 1,
                "fadddate": 0,
                "fenddate": 0,
                "fendname": 0,
                "fprice": 0,
                "fprovidertype": 0,
                "flimit": limit,
                "button_submit": "Apply Filter",
            },
        ).text,
        "html.parser",
    )

    for domain in soup.findAll("a", class_="namelinks"):
        domains.append(domain.text)
        try:
            a = ScrapedDeletedDomain(domain=domain.text)
            a.save()
        except:
            pass
    return Response({"data": domains, "message": "list of expired domains"}, status=200)


def check_domain_availabilty(query):
    url = "https://pointsdb-bulk-domain-check-v1.p.rapidapi.com/domain_check"

    querystring = {"domains": [query]}

    headers = {
        "x-rapidapi-key": "9f013ed0dcmsh907ec873dacc98cp17eee2jsn10ebe10bcb2b",
        "x-rapidapi-host": "pointsdb-bulk-domain-check-v1.p.rapidapi.com",
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    domain = []
    for key, value in json.loads(response.text).items():
        if value == True:
            domain.append(key)
    return domain

def new_appraise(price):
    url = "http://www.domanow.com/appraisal"
    rs = requests.session()
    headers = {
        "referer": "http://www.domanow.com/",
        "origin": "http://www.domanow.com",
        "host": "www.domanow.com",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    }
    listToStr = "\n".join([str(elem) for elem in domains])
    payload = {"bulk": listToStr}
    s = rs.post(url, headers=headers, data=payload)
    soup = BeautifulSoup(s.text, "html.parser")
    results = soup.find("div", class_="col-lg-7")
    appraise_domains = []
    global sorted_domains
    sorted_domains = []
    for count, value in enumerate(domains):
        print('results',results.find_all("h1", class_="display-3")[count])
        try:
            appraise_domains.append(
                {
                    "domain": results.find_all("h1", class_="display-3")[count].text,
                    "value": results.find_all("span")[count].text[1:].replace(",", ""),
                }
            )
        except:
            pass
    for count,val in enumerate(appraise_domains):
        if float(val["value"]) > price:
            print("hello world",count)
            sorted_domains.append(
                {
                    "domain": results.find_all("h1", class_="display-3")[count].text,
                    "Estimated_price": results.find_all("span")[count].text[1:].replace(",", ""),
                }
            )
        else:
            pass
# Create your views here.
@api_view()
def domains_filter(request, price=2000):
    appraisal_tool(price)
    if len(sortedDomains) > 0:
        return Response({"domains": sortedDomains, "message": "Domains"}, status=200)
    else:
        return Response(
            {"domains": [], "message": "No domains in this value"}, status=200
        )


@api_view(["POST"])
def random_domain_generator(request):
    availible_domains = ""
    data = request.data
    for i in data["domains"]:
        availible_domains += i + ".com,"
        availible_domains += i + ".co.uk,"
        availible_domains += i + ".org,"
    domains = check_domain_availabilty(availible_domains)
    if len(domains) < 1:
        domains = ["No Domain Availible"]
    for i in domains:
        try:
            random_domain = RandomDomainGenerator(domain=i)
            random_domain.save()
        except:
            pass
    return Response(domains)


@api_view(["GET"])
def random_appraisal_tool(request, price):
    random_sorted_domains_name = []
    random_sorted_domains_price = []
    domains_name = []
    query1 = ""
    # domains = ["afnan.com", "bhalu.com", "easypaisa.com"]
    rs = requests.session()
    headers = {
        "referer": "https://www.coderduck.com/link-price-calculator",
        "origin": "https://www.coderduck.com",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    }
    url = "https://www.coderduck.com/link-price-calculator/output"
    for count, value in enumerate(domains):
        if count + 1 == len(domains):
            query1 += value
        else:
            query1 += value + "\n"
    query = {"data": query1}
    response = rs.post(url, headers=headers, data=query)
    soup = BeautifulSoup(response.text, "html.parser")
    soup = soup.find_all("td")
    for count, values in enumerate(soup):
        if count > 3:
            if values.string[0].isnumeric():
                pass
            else:
                if values.string.startswith("$"):
                    random_sorted_domains_price.append(values.string[1:])
                else:
                    random_sorted_domains_name.append(values.string)
    for count, value in enumerate(random_sorted_domains_name):
        if int(random_sorted_domains_price[count][:-4].replace(",", "")) > price:
            domains_name.append(
                {"domain": value, "Estimated_price": random_sorted_domains_price[count]}
            )

    if len(domains_name) > 0:
        return Response({"domains": domains_name, "message": "Domains"}, status=200)
    else:
        return Response(
            {"domains": [], "message": "No domains in this value"}, status=200
        )


@api_view()
def domain_now(request, price):
    new_appraise(price)
    if len(sorted_domains) > 0:
        return Response({"domains": sorted_domains, "message": "Domains"}, status=200)
    else:
        return Response(
            {"domains": ["No Result Please Try Again or Refresh Page."], "message": "No domains in this value"}, status=200
        )
