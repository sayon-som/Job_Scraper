# scraping using request library
from bs4 import BeautifulSoup
import requests
import time

print("Enter the skill you are not accustomed with")
unfam_skill = input('>')
print(f"Loading skill without {unfam_skill}.......")


def find_jobs():
    text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index,job in enumerate(jobs):
        date = job.find('span', class_='sim-posted').span.text
        if 'few' in date:
            name_company = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skill = job.find('span', class_='srp-skills').text.replace(' ', '')
            info = job.header.h2.a['href']
            if unfam_skill not in skill:
                with open(f'post/{index}.txt','w') as f:
                    #writing in the file
                    f.write((f"Company Name:{name_company.strip()}\n"))
                    f.write(f"Skills Required:{skill.strip()}\n")
                    f.write(f"More Information:{info}\n")
                print(f"File saved:{index}")




if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"waiting for {time_wait} minutes")
        time.sleep(time_wait * 60)
