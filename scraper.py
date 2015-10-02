import unicodecsv
import requests
from BeautifulSoup import BeautifulSoup

headers = ['parish', 'office', 'district', 'party', 'candidate', 'votes']
OFFICE_LIST = ['Lieutenant Governor', 'U. S. Senator', 'U. S. Representative', 'Attorney General', 'Governor', 'Presidential Electors', 'State Senator', 'State Representative', 'Secretary of State', 'Commissioner of', 'Presidential Nominee', 'Presidential Nominee', 'Presidential Electors']
OFFICE_LOOKUP = {
    'Lieutenant Governor' : 'Lieutenant Governor', 'U. S. Senator' : 'U.S. Senate', 'U. S. Representative' : 'U.S. House',
    'Attorney General' : 'Attorney General', 'Governor' : 'Governor', 'Presidential Electors' : 'President',
    'State Senator': 'State Senate', 'State Representative' : 'State House', 'Secretary of State' : 'Secretary of State',
    'Commissioner of Agriculture and Forestry' : 'Commissioner of Agriculture and Forestry', 'Commissioner of Insurance' : 'Commissioner of Insurance',
    'Presidential Nominee' : 'President', 'Presidential Electors' : 'President'
}

def write_parish_results(url, file_name):
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    offices = [x.text for x in soup.findAll('strong') if x.text.split(' -- ')[0].strip() in OFFICE_LIST]
    parish_details = get_parish_details(url, soup, offices)
    candidate_details = get_candidate_details(soup, offices)
    precinct_links = scrape_parish_results(parish_details, candidate_details, file_name + '.csv')
    # write_precinct_results(zip(offices,precinct_links), candidate_details, file_name + '__precinct.csv')

def write_parish_presidential_results(url, file_name):
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    offices = [x.text.split(' -- ')[0] for x in soup.findAll('strong') if x.text.split(' -- ')[0].strip() in OFFICE_LIST]
    parish_details = get_parish_details(url, soup, offices)
    candidate_details = get_candidate_details(soup, offices)
    scrape_parish_results(parish_details, candidate_details, file_name + '.csv')

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

def scrape_parish_results(parish_details, candidate_details, file_name):
    precinct_links = {}
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
            r = requests.get(url)
            soup = BeautifulSoup(r.text)
            precinct_links[office] = ["http://"+url.split('/')[2]+"/"+url.split('/')[3]+'/'+x['href'] for x in soup.findAll('a') if "Precinct" in x.text]
            rows = soup.findAll('tr')
            candidates_for_office = [x.text for x in rows[0] if x.text in [c[0] for c in candidate_details]]
            for row in rows[1:]:
                parish_name = row.find('strong').text
                vote_totals = [int(x.text) for x in row.findAll('td')[1:]]
                for candidate, votes in zip(candidates_for_office, vote_totals):
                    party = [c[3] for c in candidate_details if candidate == c[0]][0]
                    w.writerow([parish_name, OFFICE_LOOKUP[office_name], district, party, candidate, votes])

    return precinct_links

def write_precinct_results(precinct_details, candidate_details, file_name):
    with open(file_name, 'wb') as csvfile:
        w = unicodecsv.writer(csvfile, encoding='utf-8')
        w.writerow(headers)
        for office, url in precinct_details:
            if ' -- ' in office:
                office_name, district = office.split(' -- ')
                district = district.strip()
            else:
                office_name = office
                district = None
            if office_name == 'Commissioner of':
                office_name = office_name + ' ' + district
                district = None
            r = requests.get(url)
            soup = BeautifulSoup(r.text)
            rows = soup.findAll('tr')
            candidates_for_office = [x.text for x in rows[0] if x.text in [c[0] for c in candidate_details]]
            for row in rows[1:]:
                precinct_name = row.find('strong').text
                vote_totals = [int(x.text) for x in row.findAll('td')[1:]]
                for candidate, votes in zip(candidates_for_office, vote_totals):
                    party = [c[3] for c in candidate_details if candidate == c[0]][0]
                    w.writerow([precinct_name, OFFICE_LOOKUP[office_name], district, party, candidate, votes])
