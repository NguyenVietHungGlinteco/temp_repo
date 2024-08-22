import requests
from bs4 import BeautifulSoup
from company import Company
from job import Job
from job_group import JobGroup
import json
from company_recruitment import CompanyRecruitment


def add_job_to_group(job_url, job_group):
    response = requests.get(job_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    job = Job()
    job.get_job_detail(soup)
    job_group.add_job(job.__dict__)


def get_jobs_data(soup):
    job_grp = JobGroup()

    jobs_container = soup.find('div', id="ajax_cp_our_jobs_listing")
    jobs = jobs_container.find_all('h4')
    for job in jobs:
        add_job_to_group(job.find('a')['href'], job_grp)

    job_dict = job_grp.__dict__
    return job_dict


def get_company_data(soup):
    company = Company()
    company.get_company_detail(soup)
    company_dict = company.__dict__
    return company_dict


def get_company_recruitment(company_dict, jobs_dict):
    company_recruitment = CompanyRecruitment(company_dict, jobs_dict)

    company_recruitment_dict = company_recruitment.__dict__

    json_data = json.dumps(
        company_recruitment_dict, indent=4, ensure_ascii=False)

    with open('one_mount.json', 'w', encoding='utf-8') as f:
        f.write(json_data)

    print("Dữ liệu đã được xuất ra file one_mount.json")


if __name__ == "__main__":

    # url = 'https://www.vietnamworks.com/company/vnm'
    # url = 'https://www.vietnamworks.com/company/one-mount'
    url = 'https://www.vietnamworks.com/company/tap-doan-vang-bac-da-quy-doji'

    # Gửi yêu cầu GET tới trang web
    response = requests.get(url)
    response.raise_for_status()  # Kiểm tra lỗi HTTP

    # Phân tích HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    print("Crawling data ...")

    company_dict = get_company_data(soup)
    jobs_dict = get_jobs_data(soup)
    get_company_recruitment(company_dict, jobs_dict)
