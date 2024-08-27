import requests
from bs4 import BeautifulSoup
from company import Company
from job import Job
from job_group import JobGroup
from company_recruitment import CompanyRecruitment
import time

BASE_URL = "https://www.topcv.vn/get-render-list-job-company/"


class Utils:
    @staticmethod
    def get_jobs_url(company_id, company_label):
        jobs_url = []
        page = 1
        while True:
            response = requests.get(
                f"{BASE_URL}{company_id}\
                ?slug={company_label}&limit=6&page={page}")
            if response.status_code == 200:
                response.encoding = 'utf-8'
                data = response.json()['data']['html_job']
                soup = BeautifulSoup(data, 'html.parser')
                job_elements = soup.find_all(
                    'div', attrs={"data-box": 'BoxRecruitmentInCompany'})
                for job_element in job_elements:
                    jobs_url.append(job_element.find('a')['href'])
            page += 1
            if len(job_elements) < 6:
                break
        print(f"Number of Jobs: {len(jobs_url)}")
        return jobs_url

    @staticmethod
    def add_job_to_group(job_url, job_group):
        response = requests.get(job_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        job = Job()
        job.get_job_detail(soup)
        job_group.add_job(job.__dict__)

    @staticmethod
    def get_company_recruitment(company_dict, jobs_dict):
        company_recruitment = CompanyRecruitment(company_dict, jobs_dict)

        company_recruitment_dict = company_recruitment.__dict__
        return company_recruitment_dict

    @staticmethod
    def get_jobs_data(soup, company_id, company_label):
        job_grp = JobGroup()
        jobs_url = Utils.get_jobs_url(
            company_id=company_id, company_label=company_label)
        for job_url in jobs_url:
            Utils.add_job_to_group(job_url=job_url, job_group=job_grp)
            time.sleep(1)

        job_dict = job_grp.__dict__
        return job_dict

    @staticmethod
    def get_company_data(soup):
        company = Company()
        company.get_company_detail(soup)
        company_dict = company.__dict__
        return company_dict

    @staticmethod
    def get_company_full_data(company_url):
        response = requests.get(company_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        company_url_split = company_url.split('/')
        company_id = company_url_split[-1].split('.')[0]
        company_label = company_url_split[-2]

        company_dict = Utils.get_company_data(soup)
        jobs_dict = Utils.get_jobs_data(soup, company_id, company_label)
        Utils.get_company_recruitment(company_dict, jobs_dict)
