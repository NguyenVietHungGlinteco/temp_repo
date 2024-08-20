import requests
from bs4 import BeautifulSoup
from company import Company
from job import Job
from job_group import JobGroup

# url = 'https://www.vietnamworks.com/company/vnm'
# url = 'https://www.vietnamworks.com/company/one-mount'
url = 'https://www.vietnamworks.com/chuyen-vien-cao-cap-kinh-doanh-giftcard--1813217-jv'

# Gửi yêu cầu GET tới trang web
response = requests.get(url)
response.raise_for_status()  # Kiểm tra lỗi HTTP

# Phân tích HTML
soup = BeautifulSoup(response.text, 'html.parser')

job = Job()
job.get_job_detail(soup)
job.show_job_detail()
