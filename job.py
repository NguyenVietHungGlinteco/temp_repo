from datetime import datetime, timedelta

class Job:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.title = kwargs.get('title')
        self.description = kwargs.get('description', "")
        self.tags = kwargs.get('tags', [])
        self.keywords = kwargs.get('keywords', [])
        self.locations = kwargs.get('locations')
        self.welfare = kwargs.get('welfare', dict())
        self.created_at = kwargs.get('created_at')
        self.ended_at = kwargs.get('ended_at')
        self.category = kwargs.get('category')
        self.years_of_experience = kwargs.get('years_of_experience', int)
        self.level = kwargs.get('level')
        self.skills = kwargs.get('skills', [])
        self.language = kwargs.get('language')
        self.nationality = kwargs.get('nationality')
        self.salary_range = kwargs.get('salary_range')
        self.url = kwargs.get('url')
        self.unique_id = kwargs.get('unique_id')
    
    def get_job_id(self, soup):
        pass

    def get_job_title(self, soup):
        self.title = soup.find('h1').text

    def get_job_description(self, soup):
        job_description = soup.find('div', class_='jSVTbX')
        job_description_paragraphs = job_description.find_all('p')
        for paragraph in job_description_paragraphs:
            self.description += paragraph.text

    def get_job_welfare(self, soup):
        job_welfares = soup.find_all('div', class_='jJlmNs')
        for welfare in job_welfares:
            welfare_key = welfare.find('p').text    
            welfare_detail = welfare.find('div', class_='fGxLZh').text
            self.welfare[welfare_key] = welfare_detail

    def get_job_locations(self, soup):
        self.locations = soup.find('div', class_='dBRwI').find('p').text
  
    def get_job_keywords(self, soup):
        keyword_container = soup.find('div', class_='esrWRf')
        keyword_elements = keyword_container.find_all('button')
        for keyword in keyword_elements:
            self.keywords.append(keyword.find('span').text)

    def get_end_date(self, soup):
        remaining_time = soup.find('span', class_='bgAmOO').text
        remaining_time_split = remaining_time.split(' ')
        remaining_time_split.reverse()
        current_date = datetime.now().date()

        if remaining_time_split[0] == 'ngày':
            end_date = current_date + timedelta(days=int(remaining_time_split[1]))
        elif remaining_time_split[0] == 'giờ':
            end_date = current_date
        self.ended_at = str(end_date)

    def get_job_info(self, soup):
        job_info_collection = soup.find_all('div', class_='GVIEn')
        for job_type in job_info_collection:
            job_info = job_type.find('p').text
            job_type_label = job_type.find('label').text
            if job_type_label == 'NGÀY ĐĂNG':
                self.created_at = '-'.join(job_info.split('/'))
            if job_type_label == 'SỐ NĂM KINH NGHIỆM TỐI THIỂU':
                self.years_of_experience = int(job_info)
            if job_type_label == 'CẤP BẬC':
                self.level = job_info
            if job_type_label == 'KỸ NĂNG':
                self.skills = job_info.split(',')
            if job_type_label == 'LĨNH VỰC':
                self.category = job_info
            if job_type_label == 'NGÔN NGỮ TRÌNH BÀY HỒ SƠ':
                self.language = job_info
            if job_type_label == 'QUỐC TỊCH':
                self.nationality = job_info
            if job_type_label == 'NGÀNH NGHỀ':
                industry_element = job_type.find_all('span')
                for industry in industry_element:
                    self.tags.append(industry.text)
    
    def get_job_salary_range(self, soup):
        self.salary_range = soup.find('span', class_='iOaLcj').text

    def get_job_url(self, soup):
        self.url = soup.find('link', attrs={"rel": "canonical"})['href']

    def get_job_detail(self, soup):
        self.get_job_id(soup)
        self.get_job_title(soup)
        self.get_job_description(soup)
        self.get_job_locations(soup)
        self.get_job_keywords(soup)
        self.get_end_date(soup)
        self.get_job_info(soup)
        self.get_job_welfare(soup)
        self.get_job_salary_range(soup)
        self.get_job_url(soup)

    def show_job_detail(self):
        print(f"id: {self.id}")
        print(f"title: {self.title}")
        print(f"description: {self.description}")
        print(f"tags: {self.tags}")
        print(f"keywords: {self.keywords}")
        print(f"locations: {self.locations}")
        print(f"welfare: {self.welfare}")
        print(f"created_at: {self.created_at}")
        print(f"ended_at: {self.ended_at}")
        print(f"category: {self.category}")
        print(f"years_of_experience: {self.years_of_experience}")
        print(f"level: {self.level}")
        print(f"skills: {self.skills}")
        print(f"language: {self.language}")
        print(f"nationality: {self.nationality}")
        print(f"salary_range: {self.salary_range}")
        print(f"url: {self.url}")
        print(f"unique_id: {self.unique_id}")



        
