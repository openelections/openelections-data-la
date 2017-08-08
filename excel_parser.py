import xlrd
import unicodecsv

headers = ['county', 'precinct', 'office', 'district', 'party', 'candidate', 'votes']
book = xlrd.open_workbook("/Users/dwillis/Downloads/Election+Results+(11-08-2016).xlsx")
sheet = book.sheet_by_index(1)
president_candidates = [x.value for x in sheet.row(6) if x.value != ''] # row - 1
president_rows = range(7,4104)
senate_candidates = [x.value for x in sheet.row(4107) if x.value != '']
senate_rows = range(4108,8205)
house1_candidates = [x.value for x in sheet.row(8208) if x.value != '']
house1_rows = range(8209,8775)
house2_candidates = [x.value for x in sheet.row(8778) if x.value != '']
house2_rows = range(8779,9466)
house3_candidates = [x.value for x in sheet.row(9469) if x.value != '']
house3_rows = range(9470,10068)
house4_candidates = [x.value for x in sheet.row(10071) if x.value != '']
house4_rows = range(10072,10868)
house5_candidates = [x.value for x in sheet.row(10871) if x.value != '']
house5_rows = range(10872,11769)
house6_candidates = [x.value for x in sheet.row(11772) if x.value != '']
house6_rows = range(11773,12379)


with open('20161108__la__general__precinct.csv', 'wb') as csvfile:
    w = unicodecsv.writer(csvfile, encoding='utf-8')
    w.writerow(headers)
    county = None
    for row in president_rows:
        pres_values = [x.value for x in sheet.row(row) if x.value !='']
        if len(pres_values) == 1:
            county = pres_values[0]
        else:
            precinct = pres_values[0]
            cand_votes = zip(president_candidates, pres_values[1:])
            for cand in cand_votes:
                name, votes = cand
                name, party = name.split(', ', 1)
                party = party.split(' (')[1].replace(')','')
                w.writerow([county, precinct, 'President', None, party, name, int(votes)])
    county = None
    for row in senate_rows:
        senate_values = [x.value for x in sheet.row(row) if x.value !='']
        if len(senate_values) == 1:
            county = senate_values[0]
        else:
            precinct = senate_values[0]
            cand_votes = zip(senate_candidates, senate_values[1:])
            for cand in cand_votes:
                name, votes = cand
                name, party = name.split(' (')
                party = party.replace(')','')
                w.writerow([county, precinct, 'U.S. Senate', None, party, name, int(votes)])
    county = None
    for row in house1_rows:
        house1_values = [x.value for x in sheet.row(row) if x.value !='']
        if len(house1_values) == 1:
            county = house1_values[0]
        else:
            precinct = house1_values[0]
            cand_votes = zip(house1_candidates, house1_values[1:])
            for cand in cand_votes:
                name, votes = cand
                name, party = name.split(' (')
                party = party.replace(')','')
                w.writerow([county, precinct, 'U.S. House', 1, party, name, int(votes)])
    county = None
    for row in house2_rows:
        house2_values = [x.value for x in sheet.row(row) if x.value !='']
        if len(house2_values) == 1:
            county = house2_values[0]
        else:
            precinct = house2_values[0]
            cand_votes = zip(house2_candidates, house2_values[1:])
            for cand in cand_votes:
                name, votes = cand
                name, party = name.split(' (')
                party = party.replace(')','')
                w.writerow([county, precinct, 'U.S. House', 2, party, name, int(votes)])
    county = None
    for row in house3_rows:
        house3_values = [x.value for x in sheet.row(row) if x.value !='']
        if len(house3_values) == 1:
            county = house3_values[0]
        else:
            precinct = house3_values[0]
            cand_votes = zip(house3_candidates, house3_values[1:])
            for cand in cand_votes:
                name, votes = cand
                name, party = name.split(' (')
                party = party.replace(')','')
                w.writerow([county, precinct, 'U.S. House', 3, party, name, int(votes)])
    county = None
    for row in house4_rows:
        house4_values = [x.value for x in sheet.row(row) if x.value !='']
        if len(house4_values) == 1:
            county = house4_values[0]
        else:
            precinct = house4_values[0]
            cand_votes = zip(house4_candidates, house4_values[1:])
            for cand in cand_votes:
                name, votes = cand
                name, party = name.split(' (')
                party = party.replace(')','')
                w.writerow([county, precinct, 'U.S. House', 4, party, name, int(votes)])
    county = None
    for row in house5_rows:
        house5_values = [x.value for x in sheet.row(row) if x.value !='']
        if len(house5_values) == 1:
            county = house5_values[0]
        else:
            precinct = house5_values[0]
            cand_votes = zip(house5_candidates, house5_values[1:])
            for cand in cand_votes:
                name, votes = cand
                name, party = name.split(' (')
                party = party.replace(')','')
                w.writerow([county, precinct, 'U.S. House', 5, party, name, int(votes)])
    county = None
    for row in house6_rows:
        house6_values = [x.value for x in sheet.row(row) if x.value !='']
        if len(house6_values) == 1:
            county = house6_values[0]
        else:
            precinct = house6_values[0]
            cand_votes = zip(house6_candidates, house6_values[1:])
            for cand in cand_votes:
                name, votes = cand
                name, party = name.split(' (')
                party = party.replace(')','')
                w.writerow([county, precinct, 'U.S. House', 6, party, name, int(votes)])
