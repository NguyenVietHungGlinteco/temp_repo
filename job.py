class Job:
    def __init__(self, **kwargs):
        self.title = kwargs.get('title')
        self.salary_range = kwargs.get('salary_range')
        self.years_of_experience = kwargs.get('years_of_experience')
        self.ended_at = kwargs.get('ended_at')
        self.description = kwargs.get('description', "")
        self.requirements = kwargs.get('requirements', "")
        self.welfare = kwargs.get('welfare', "")
        self.locations = kwargs.get('locations')
        self.working_time = kwargs.get('locations')
        self.url = kwargs.get('url')

    def get_job_id(self, soup):
        pass

    def get_job_title(self, soup):
        self.title = soup.find('h1').text.strip()

    def get_basic_job_info(self, soup):
        basic_infos = soup.find_all(
            'div', class_='job-detail__info--section-content-value')
        self.salary_range = basic_infos[0].text
        self.years_of_experience = basic_infos[2].text

    def get_job_deadline(self, soup):
        deadline_text = soup.find(
            'div', class_="job-detail__info--deadline").text
        self.ended_at = deadline_text.strip().split(' ')[-1]

    def get_job_infomation_detail(self, soup):
        job_infomation_detail_container = soup.find(
            'div', id='box-job-information-detail')
        job_info_collection = job_infomation_detail_container.find_all(
            'div', class_='job-description__item')
        for job_type in job_info_collection:
            job_type_info_label = job_type.find('h3').text
            if job_type_info_label == 'Mô tả công việc':
                self.description = job_infomation_detail_container.find(
                    'div', class_="job-description__item--content").text
            if job_type_info_label == 'Yêu cầu ứng viên':
                job_requirement_paragraphs = job_infomation_detail_container.find_all('li')
                for paragraph in job_requirement_paragraphs:
                    self.requirements += paragraph.text
            if job_type_info_label == 'Quyền lợi':
                job_welfare_paragraphs = job_infomation_detail_container.find_all('li')
                for paragraph in job_welfare_paragraphs:
                    self.welfare += paragraph.text
            if job_type_info_label == 'Địa điểm làm việc':
                self.locations = job_infomation_detail_container.find(
                    'div', {'style': 'margin-bottom: 10px'}).text
            if job_type_info_label == 'Thời gian làm việc':
                self.working_time = job_infomation_detail_container.find(
                    'div', class_="job-description__item--content-list").text

    def get_job_url(self, soup):
        self.url = soup.find('link', attrs={"rel": "canonical"})['href']

    def get_job_detail(self, soup):
        self.get_job_id(soup)
        self.get_job_title(soup)
        self.get_basic_job_info(soup)
        self.get_job_deadline(soup)
        self.get_job_infomation_detail(soup)
        self.get_job_url(soup)
