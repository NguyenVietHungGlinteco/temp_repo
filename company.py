class Company:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', int)
        self.name = kwargs.get('name')
        self.description = kwargs.get('description')
        self.industry = kwargs.get('industry')
        self.website = kwargs.get('website')
        self.unique_id = kwargs.get('unique_id')

    def get_company_id(self, soup):
        pass

    def get_company_name(self, soup):
        company_name = soup.find('h1', id='cp_company_name')
        self.name = company_name.text.strip()

    def get_company_description(self, soup):
        description = ''
        company_description = soup.find('div',
        class_='custom-story-item-content').find_all('div')
        for part_of_description in company_description:
            description += '\n'
            description += part_of_description.text
        self.description = description.strip()

    def get_company_industry(self, soup):
        self.industry = soup.find_all('span', class_='li-items-limit')[1].text

    def get_company_website(self, soup):
        company_website = soup.find('a', class_="website-company")
        self.website = company_website['href']

    def get_company_unique_id(self, soup):
        pass

    def get_company_detail(self, soup):
        self.get_company_id(soup)
        self.get_company_name(soup)
        self.get_company_description(soup)
        self.get_company_industry(soup)
        self.get_company_website(soup)
        self.get_company_unique_id(soup)

    def show_company_detail(self):
        print(f"id: {self.id}")
        print(f"name: {self.name}")
        print(f"description: {self.description}")
        print(f"industry: {self.industry}")
        print(f"website: {self.website}")
        print(f"unique_id: {self.unique_id}")
