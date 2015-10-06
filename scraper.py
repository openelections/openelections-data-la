import unicodecsv
import requests
from BeautifulSoup import BeautifulSoup

headers = ['parish', 'office', 'district', 'party', 'candidate', 'votes']
precinct_headers = ['parish', 'precinct', 'office', 'district', 'party', 'candidate', 'votes']
OFFICE_LIST = ['Lieutenant Governor', 'U. S. Senator', 'U. S. Representative', 'Attorney General', 'Governor', 'Presidential Electors', 'State Senator', 'State Representative', 'Secretary of State', 'Commissioner of', 'Presidential Nominee', 'Presidential Nominee', 'Presidential Electors']
OFFICE_LOOKUP = {
    'Lieutenant Governor' : 'Lieutenant Governor', 'U. S. Senator' : 'U.S. Senate', 'U. S. Representative' : 'U.S. House',
    'Attorney General' : 'Attorney General', 'Governor' : 'Governor', 'Presidential Electors' : 'President',
    'State Senator': 'State Senate', 'State Representative' : 'State House', 'Secretary of State' : 'Secretary of State',
    'Commissioner of Agriculture and Forestry' : 'Commissioner of Agriculture and Forestry', 'Commissioner of Insurance' : 'Commissioner of Insurance',
    'Presidential Nominee' : 'President', 'Presidential Electors' : 'President'
}

def get_soup(url):
    r = requests.get(url)
    return BeautifulSoup(r.text)

def get_offices(soup, president=False):
    if president:
        return [x.text.split(' -- ')[0] for x in soup.findAll('strong') if x.text.split(' -- ')[0].strip() in OFFICE_LIST]
    else:
        return [x.text for x in soup.findAll('strong') if x.text.split(' -- ')[0].strip() in OFFICE_LIST]

def write_parish_results(url, file_name):
    soup = get_soup(url)
    offices = get_offices(soup)
    parish_details = get_parish_details(url, soup, offices)
    candidate_details = get_candidate_details(soup, offices)
    precinct_links = scrape_parish_results(parish_details, candidate_details, file_name + '.csv')
    # write_precinct_results(zip(offices,precinct_links), candidate_details, file_name + '__precinct.csv')

def write_parish_presidential_results(url, file_name):
    soup = get_soup(url)
    offices = get_offices(soup, president=True)
    parish_details = get_parish_details(url, soup, offices)
    candidate_details = get_candidate_details(soup, offices)
    scrape_parish_results(parish_details, candidate_details, file_name + '.csv')

def write_precinct_results(url, file_name):
    soup = get_soup(url)
    offices = get_offices(soup)
    parish_details = get_parish_details(url, soup, offices)
    candidate_details = get_candidate_details(soup, offices)
    precinct_details = get_precinct_details(parish_details)
    scrape_precinct_results(precinct_details, candidate_details, file_name + '.csv')

def get_candidate_details(soup, offices):
    candidate_details = []
    combined = zip(offices, soup.findAll('table'))
    for office, table in combined:
        rows = table.findAll('tr')[1:]
        for row in rows:
            candidate_row = [x.text for x in row.findAll('td')]
            candidate_row.append(candidate_row[0].split('(')[1].replace(')',''))
            candidate_row[0] = candidate_row[0].split('(')[0].strip()
            candidate_row.append(office)
            candidate_details.append(candidate_row)
    return candidate_details

def get_parish_details(url, soup, offices):
    parish_links = ["http://"+url.split('/')[2]+"/"+url.split('/')[3]+'/'+x['href'] for x in soup.findAll('a') if "Parish" in x.text]
    return zip(offices, parish_links)

def get_precinct_details(parish_details):
    precinct_links = {}
    for office, url in parish_details:
        if ' -- ' in office:
            office_name, district = office.split(' -- ')
            district = district.strip()
        else:
            office_name = office
            district = None
        if office_name == 'Commissioner of':
            office_name = office_name + ' ' + district
            district = None
        soup = get_soup(url)
        precinct_links[office] = ["http://"+url.split('/')[2]+"/"+url.split('/')[3]+'/'+x['href'] for x in soup.findAll('a') if "Precinct" in x.text]
    return precinct_links

def scrape_parish_results(parish_details, candidate_details, file_name):
    with open(file_name, 'wb') as csvfile:
        w = unicodecsv.writer(csvfile, encoding='utf-8')
        w.writerow(headers)
        for office, url in parish_details:
            if ' -- ' in office:
                office_name, district = office.split(' -- ')
                district = district.strip()
            else:
                office_name = office
                district = None
            if office_name == 'Commissioner of':
                office_name = office_name + ' ' + district
                district = None
            soup = get_soup(url)
            rows = soup.findAll('tr')
            candidates_for_office = [x.text.replace('&amp;', '&') for x in rows[0] if x.text.replace('&amp;', '&') in [c[0] for c in candidate_details]]
            for row in rows[1:]:
                parish_name = row.find('strong').text
                vote_totals = [int(x.text) for x in row.findAll('td')[1:]]
                for candidate, votes in zip(candidates_for_office, vote_totals):
                    party = [c[3] for c in candidate_details if candidate == c[0]][0]
                    w.writerow([parish_name, OFFICE_LOOKUP[office_name], district, party, candidate, votes])

def scrape_precinct_results(precinct_details, candidate_details, file_name):
    with open(file_name, 'wb') as csvfile:
        w = unicodecsv.writer(csvfile, encoding='utf-8')
        w.writerow(precinct_headers)
        for office in precinct_details.keys():
            if ' -- ' in office:
                office_name, district = office.split(' -- ')
                district = district.strip()
            else:
                office_name = office
                district = None
            if office_name == 'Commissioner of':
                office_name = office_name + ' ' + district
                district = None
            for url in precinct_details[office]:
                soup = get_soup(url)
                rows = soup.findAll('tr')
                candidates_for_office = [x.text for x in rows[0] if x.text in [c[0] for c in candidate_details]]
                for row in rows[1:]:
                    parish_name = soup.findAll('h2')[1].text.title()
                    precinct_name = row.findAll('td')[0].text
                    vote_totals = [int(x.text) for x in row.findAll('td')[1:]]
                    for candidate, votes in zip(candidates_for_office, vote_totals):
                        party = [c[3] for c in candidate_details if candidate == c[0]][0]
                        w.writerow([parish_name, precinct_name, OFFICE_LOOKUP[office_name], district, party, candidate, votes])
