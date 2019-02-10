import xlrd
import unicodecsv

headers = ['county', 'precinct', 'office', 'district', 'party', 'candidate', 'votes']
book = xlrd.open_workbook("/Users/dwillis/Downloads/Election+Results+(11-06-2018).xlsx")
sheet = book.sheet_by_index(1)
#president_candidates = [x.value for x in sheet.row(6) if x.value != ''] # row - 1
#president_rows = range(7,4104)
sos_candidates = [x.value for x in sheet.row(6) if x.value != '']
sos_rows = range(7,4045)
house1_candidates = [x.value for x in sheet.row(4049) if x.value != '']
house1_rows = range(4050,4619)
house2_candidates = [x.value for x in sheet.row(4623) if x.value != '']
house2_rows = range(4624,5309)
house3_candidates = [x.value for x in sheet.row(5313) if x.value != '']
house3_rows = range(5314,5911)
house4_candidates = [x.value for x in sheet.row(5915) if x.value != '']
house4_rows = range(5916,6711)
house5_candidates = [x.value for x in sheet.row(6715) if x.value != '']
house5_rows = range(6716,7614)
house6_candidates = [x.value for x in sheet.row(7618) if x.value != '']
house6_rows = range(7619,8225)
state_senate26_candidates = [x.value for x in sheet.row(8630) if x.value != '']
state_senate26_rows = range(8631,8740)
state_rep33_candidates = [x.value for x in sheet.row(8743) if x.value != '']
state_rep33_rows = range(8744,8775)
state_rep90_candidates = [x.value for x in sheet.row(8778) if x.value != '']
state_rep90_rows = range(8779,8810)

with open('20181106__la__general__precinct.csv', 'wb') as csvfile:
    w = unicodecsv.writer(csvfile, encoding='utf-8')
    w.writerow(headers)
#    county = None
#    for row in president_rows:
#        pres_values = [x.value for x in sheet.row(row) if x.value !='']
#        if len(pres_values) == 1:
#            county = pres_values[0]
#        else:
#            precinct = pres_values[0]
#            cand_votes = zip(president_candidates, pres_values[1:])
#            for cand in cand_votes:
#                name, votes = cand
#                name, party = name.split(', ', 1)
#                party = party.split(' (')[1].replace(')','')
#                w.writerow([county, precinct, 'President', None, party, name, int(votes)])
#    county = None
#    for row in senate_rows:
#        senate_values = [x.value for x in sheet.row(row) if x.value !='']
#        if len(senate_values) == 1:
#            county = senate_values[0]
#        else:
#            precinct = senate_values[0]
#            cand_votes = zip(senate_candidates, senate_values[1:])
#            for cand in cand_votes:
#                name, votes = cand
#                name, party = name.split(' (')
#                party = party.replace(')','')
#                w.writerow([county, precinct, 'U.S. Senate', None, party, name, int(votes)])
    county = None
    for row in sos_rows:
        sos_values = [x.value for x in sheet.row(row) if x.value !='']
        if len(sos_values) == 1:
            county = sos_values[0]
        else:
            precinct = sos_values[0]
            cand_votes = zip(sos_candidates, sos_values[1:])
            for cand in cand_votes:
                name, votes = cand
                name, party = name.split(' (')
                party = party.replace(')','')
                w.writerow([county, precinct, 'Secretary of State', None, party, name, int(votes)])
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
    county = None
    for row in state_senate26_rows:
        state_senate26_values = [x.value for x in sheet.row(row) if x.value !='']
        if len(state_senate26_values) == 1:
            county = state_senate26_values[0]
        else:
            precinct = state_senate26_values[0]
            cand_votes = zip(state_senate26_candidates, house6_values[1:])
            for cand in cand_votes:
                name, votes = cand
                name, party = name.split(' (')
                party = party.replace(')','')
                w.writerow([county, precinct, 'State Senate', 26, party, name, int(votes)])
    county = None
    for row in state_rep33_rows:
        state_rep33_values = [x.value for x in sheet.row(row) if x.value !='']
        if len(state_rep33_values) == 1:
            county = state_rep33_values[0]
        else:
            precinct = state_rep33_values[0]
            cand_votes = zip(state_rep33_candidates, house6_values[1:])
            for cand in cand_votes:
                name, votes = cand
                name, party = name.split(' (')
                party = party.replace(')','')
                w.writerow([county, precinct, 'State House', 33, party, name, int(votes)])
    county = None
    for row in state_rep90_rows:
        state_rep90_values = [x.value for x in sheet.row(row) if x.value !='']
        if len(state_rep90_values) == 1:
            county = state_rep90_values[0]
        else:
            precinct = state_rep90_values[0]
            cand_votes = zip(state_rep90_candidates, house6_values[1:])
            for cand in cand_votes:
                name, votes = cand
                name, party = name.split(' (')
                party = party.replace(')','')
                w.writerow([county, precinct, 'State House', 90, party, name, int(votes)])
