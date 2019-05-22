from bs4 import BeautifulSoup
import requests

url = 'https://www.indeed.com/jobs?q=python+developer&l=Florida&sort=date'

response = requests.get(url)

data = response.text

soup = BeautifulSoup(data, 'html.parser')


jobs = soup.find_all(attrs={"data-tn-component": "organicJob"})

number = 0
for job in jobs:
    number += 1

    title = job.find("div",{"class":"title"}).get('href')
    print(number,". ", "\nTitle:", title.text.strip())

    company = job.find("span",{"class":"company"})
    print("Company:", company.text.strip())

    location = job.find("span",{"class": "location"})
    print("Location:", location.text.strip())

    salary = job.find("div",{"class": "salarySnippet"})
    if salary in job:
        print("Salary:", salary.text.strip())
    else:
        print("Salary:", None)

    summary= job.find("div",{"class":"summary"})
    print("Summary:", summary.text.strip())

    link = job.find("div", {"class":"summary"}).get("href")
    print("Link:", link)

    print()
    print()


