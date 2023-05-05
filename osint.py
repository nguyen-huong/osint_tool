# write an osint tool to lookup email
import requests
import json
from googlesearch import search

# search for email in emailrep.io
def email_lookup():
    email = input("Enter email address: ")
    # connect API to emailrep.io and get response about email
    url = "https://emailrep.io/" + email
    # get response with API key using requests
    response = requests.get(url)
    # check if response is good
    if response.status_code == 200:
        json_data = response.json()
        print(json_data)
    else:
        print("Error getting access token:", response.text)

# take that email and lookup in business search
def business_search():
    email = email_lookup()
    # email = input("Enter email address: ")
    # email = email_lookup()
    email = str(email)
    email_split = email.split("@")[1]
    # print(email_split)
    # search query
    query = f"{email_split} business"
    # search for query
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    # search() got an unexpected keyword argument 'tld'
        print(j)

# take that business name and lookup in business search
def business_data():
    # business = input("Enter business name: ")
    business = email_lookup().split("@")[1]
    # scrape to get business name using open data
    url = 'https://data.lacity.org/resource/6rrh-rzua.json?'+ 'business_name=' + str(business.upper())
    # search for business name
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        print(json_data)

business_data()