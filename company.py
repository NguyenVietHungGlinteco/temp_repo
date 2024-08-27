class Company:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.label = kwargs.get('lable')
        self.name = kwargs.get('name')  
        self.description = kwargs.get('description')
        self.numberOfEmployees = kwargs.get('numberOfEmployees')
        self.website = kwargs.get('website')
        self.unique_id = kwargs.get('unique_id')

    def get_company_id(self, soup):
        pass

    def get_company_name(self, soup):
        company_name = soup.find('h1', class_='company-detail-name')
        self.name = company_name.text.strip()

    def get_company_description(self, soup):
        description = ''
        company_description = soup.find(
            'div', class_='box-body').find_all('p')
        for part_of_description in company_description:
            description += '\n'
            description += part_of_description.text
        self.description = description.strip()

    def get_company_numberOfEmployees(self, soup):
        self.industry = soup.find('span', class_='company-subdetail-info-text').text

    def get_company_website(self, soup):
        company_website = soup.find('a', class_="company-subdetail-info-text")
        if company_website:
            self.website = company_website['href']

    def get_company_unique_id(self, soup):
        pass

    def get_company_detail(self, soup):
        self.get_company_name(soup)
        self.get_company_description(soup)
        self.get_company_numberOfEmployees(soup)
        self.get_company_website(soup)
        self.get_company_unique_id(soup)
