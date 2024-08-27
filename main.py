import requests
from bs4 import BeautifulSoup
from company import Company
from job import Job
from job_group import JobGroup
import json
from company_recruitment import CompanyRecruitment
from utils import Utils
from utils import BASE_URL

if __name__ == "__main__":

    url = 'https://www.topcv.vn/cong-ty'
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    company_collection = soup.find_all('div', class_='box-company', limit=1)
    company_collection_url = []
    for company in company_collection:
        company_collection_url.append(company.find('h3').find('a')['href'])

    topcv_data = []

    for company_url in company_collection_url:
        print(company_url)
        full_data.append(Utils.get_company_full_data(company_url))

    with open('fd.json', 'w', encoding='utf-8') as f:
        json.dump(topcv_data, f)

