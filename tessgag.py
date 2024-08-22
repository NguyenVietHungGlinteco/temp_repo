import requests
from bs4 import BeautifulSoup
from company import Company
from job import Job
from job_group import JobGroup
import json
from test import get_job
from job_group import JobGroup
from company_recruitment import CompanyRecruitment


# url = 'https://www.vietnamworks.com/company/vnm'
url = 'https://www.vietnamworks.com/company/one-mount'
# url = 'https://www.vietnamworks.com/chuyen-vien-cao-cap-kinh-doanh-giftcard--1813217-jv'
# url = 'https://www.vietnamworks.com/chuyen-vien-cao-cap-quan-ly-quy-trinh-doanh-nghiep-1810966-jv'

# Gửi yêu cầu GET tới trang web
response = requests.get(url)
response.raise_for_status()  # Kiểm tra lỗi HTTP

# Phân tích HTML
soup = BeautifulSoup(response.text, 'html.parser')

# job = Job()
# job.get_job_detail(soup)
# # job.show_job_detail()
# job_dict = job.__dict__
# print(job_dict)

# json_data = json.dumps(job_dict, indent=4, ensure_ascii=False)
company = Company()
company.get_company_detail(soup)
company.show_company_detail()
company_a = company.__dict__

print(company_a)
json_data = json.dumps(company_a, indent=4, ensure_ascii=False)

with open('v.json', 'w', encoding='utf-8') as f:
    f.write(json_data)

print("Dữ liệu đã được xuất ra file data.json")