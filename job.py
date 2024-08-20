class Job:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.title = kwargs.get('title')
        self.description = kwargs.get('description')
        self.tags = kwargs.get('tags')
        self.keywords = kwargs.get('keywords')
        self.locations = kwargs.get('locations')
        self.welfare = kwargs.get('welfare')
        self.created_at = kwargs.get('created_at')
        self.ended_at = kwargs.get('ended_at')
        self.category = kwargs.get('category')
        self.years_of_experience = kwargs.get('years_of_experience')
        self.level = kwargs.get('level')
        self.skills = kwargs.get('skills')
        self.language = kwargs.get('language')
        self.nationality = kwargs.get('nationality')
        self.salary_range = kwargs.get('salary_range')
        self.url = kwargs.get('url')
        self.unique_id = kwargs.get('unique_id')
    
    def get_job_id(self, soup):
        pass

    def get_job_title(self, soup):
        self.title = soup.find('h1').text

    def get_job_detail(self, soup):
        self.get_job_id(soup)
        self.get_job_title(soup)
    
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
        print(f"unique_id: {self.unique_id}")



        
