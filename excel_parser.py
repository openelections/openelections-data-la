import xlrd
import csv

headers = ['county', 'precinct', 'office', 'district', 'party', 'candidate', 'votes']
book = xlrd.open_workbook("/Users/derekwillis/Downloads/Election+Results+(07-11-2020).xlsx")
sheet = book.sheet_by_index(1)
president_candidates = [x.value for x in sheet.row(6) if x.value != '']
president_rows = range(7,4134)

with open('20200711__la__primary__precinct.csv', 'w') as csvfile:
    w = csv.writer(csvfile)
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
                print(cand)
                name, votes = cand
                name, party = name.split('(', 1)
                party = 'DEM'
                w.writerow([county, precinct, 'President', None, party, name.strip(), int(votes)])
