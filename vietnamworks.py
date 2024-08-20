import requests
from bs4 import BeautifulSoup
from company import Company
from job import Job
from job_group import JobGroup

# url = 'https://www.vietnamworks.com/company/vnm'
url = 'https://www.vietnamworks.com/company/one-mount'

# Gửi yêu cầu GET tới trang web
response = requests.get(url)
response.raise_for_status()  # Kiểm tra lỗi HTTP

# Phân tích HTML
soup = BeautifulSoup(response.text, 'html.parser')


#Get company detail
company = Company()
company.get_company_detail(soup)
company.show_company_detail()

# my = soup.find('div', id="ajax_cp_our_jobs_listing")  # Class có thể thay đổi, kiểm tra trên trang web
# jobs = my.find_all('h4')
# job_collection = []
# for job in jobs:
#     job_collection.append(job.find('a'))
#     print(len(job_collection))
#     print(job.find('a')['href'])
#     print()

# print(len(jobs), len(job_collection))

# company_name = soup.find('h1', id='cp_company_name')
# print(company_name.text.strip())


