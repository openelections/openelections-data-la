import csv

offices = {'Presidential Electors': 'President',
		   'U. S. Senator': 'U.S. Senate',
		   'U. S. Representative -- 1st Congressional District': 'U.S. House District 1',
		   'U. S. Representative -- 2nd Congressional District': 'U.S. House District 2',
		   'U. S. Representative -- 3rd Congressional District': 'U.S. House District 3',
		   'U. S. Representative -- 4th Congressional District': 'U.S. House District 4',
		   'U. S. Representative -- 5th Congressional District': 'U.S. House District 5',
		   'U. S. Representative -- 6th Congressional District': 'U.S. House District 6',
		  }

current_office = None
current_parish = None
next_row_is_parish = False
next_row_is_candidates = False
current_candidates = {}

results = []

with open('la.csv', 'r', encoding='utf-8') as f:
	reader = csv.reader(f)

	for row in reader:
		if next_row_is_candidates:
			next_row_is_candidates = False

			current_candidates = {}

			# president has the highest number of candidates
			for i in range(1, 13):
				if current_office == 'President':
					candidate = row[i].split(',')[0]
				else:
					# remove party in parentheses
					candidate = row[i].split('(')[0].strip()

				if candidate == '':
					continue

				if candidate == 'Joseph R. Biden':
					candidate = 'Joseph R. Biden Jr.'

				# presidential candidates
				if candidate == 'Joseph R. Biden Jr.':
					party = 'DEM'
				elif candidate == 'Jo Jorgensen':
					party = 'LIB'
				elif candidate == 'Donald J. Trump':
					party = 'REP'
				elif candidate == 'Brian Carroll':
					party = 'American Solidarity'
				elif candidate == 'Jade Simmons':
					party = 'Becoming One Nation'
				elif candidate == 'President Boddie':
					party = 'C.U.P.'
				elif candidate == 'Don Blankenship':
					party = 'CON'
				elif candidate == 'Brock Pierce':
					party = 'Freedom and Prosperity'
				elif candidate == 'Tom Hoefling':
					party = 'Life, Liberty, Constitution'
				elif candidate == 'Gloria La Riva':
					party = 'Socialism and Liberation'
				elif candidate == 'Alyson Kennedy':
					party = 'Socialist Workers'
				elif candidate == 'Kanye West':
					party = 'The Birthday Party'
				elif candidate == 'Bill Hammons':
					party = 'United Party America'

				# senate candidates
				elif candidate == 'Beryl Billiot':
					party = None
				elif candidate == 'John Paul Bourgeois':
					party = None
				elif candidate == '"Bill" Cassidy':
					party = 'REP'
				elif candidate == 'Reno Jean Daret III':
					party = None
				elif candidate == 'Derrick "Champ" Edwards':
					party = 'DEM'
				elif candidate == '"Xan" John':
					party = 'Other'
				elif candidate == 'David Drew Knight':
					party = 'DEM'
				elif candidate == 'M.V. "Vinny" Mendoza':
					party = 'IND'
				elif candidate == 'Jamar Montgomery':
					party = None
				elif candidate == 'Dustin Murphy':
					party = 'REP'
				elif candidate == 'Adrian Perkins':
					party = 'DEM'
				elif candidate == 'Antoine Pierce':
					party = 'DEM'
				elif candidate == 'Melinda Mary Price':
					party = 'Other'
				elif candidate == 'Aaron C. Sigler':
					party = 'LIB'
				elif candidate == 'Peter Wenstrup':
					party = 'DEM'

				# house 1
				elif candidate == 'Lee Ann Dugas':
					party = 'DEM'
				elif candidate == 'Howard Kearney':
					party = 'LIB'
				elif candidate == 'Steve Scalise':
					party = 'REP'

				# house 2
				elif candidate == 'Belden "Noonie Man" Batiste':
					party = 'IND'
				elif candidate == 'Glenn Adrain Harris':
					party = 'DEM'
				elif candidate == 'Colby James':
					party = 'IND'
				elif candidate == 'Cedric L. Richmond':
					party = 'DEM'
				elif candidate == 'David M. Schilling':
					party = 'REP'
				elif candidate == 'Sheldon C. Vincent, Sr.':
					party = 'REP'

				# house 3
				elif candidate == '"Rob" Anderson':
					party = 'DEM'
				elif candidate == 'Braylon Harris':
					party = 'DEM'
				elif candidate == 'Clay Higgins':
					party = 'REP'
				elif candidate == 'Brandon LeLeux':
					party = 'LBT'

				# house 4
				elif candidate == 'Ben Gibson':
					party = 'REP'
				elif candidate == 'Kenny Houston':
					party = 'DEM'
				elif candidate == '"Mike" Johnson':
					party = 'REP'
				elif candidate == 'Ryan Trundle':
					party = 'DEM'

				# house 5
				elif candidate == 'Sandra "Candy" Christophe':
					party = 'DEM'
				elif candidate == 'Allen Guillory, Sr.':
					party = 'REP'
				elif candidate == 'Lance Harris':
					party = 'REP'
				elif candidate == '"Matt" Hasty':
					party = 'REP'
				elif candidate == 'Jesse P. Lagarde':
					party = 'DEM'
				elif candidate == 'Martin Lemelle, Jr.':
					party = 'DEM'
				elif candidate == 'Luke J. Letlow':
					party = 'REP'
				elif candidate == '"Scotty" Robinson':
					party = 'REP'
				elif candidate == 'Phillip Snowden':
					party = 'DEM'


				# house 6
				elif candidate == 'Garret Graves':
					party = 'REP'
				elif candidate == 'Shannon Sloan':
					party = 'LBT'
				elif candidate == 'Richard "RPT" Torregano':
					party = None
				elif candidate == 'Dartanyon "DAW" Williams':
					party = 'DEM'
				else:
					print(candidate)
					exit()

				current_candidates[i] = {'candidate': candidate, 'party': party}

		if row[0] in offices:
			current_office = offices[row[0]]
			next_row_is_candidates = True

		if next_row_is_parish:
			next_row_is_parish = False
			current_parish = row[0]
			continue

		if row[0] == 'Total Votes' or row[0] == 'Provisional Votes ':
			next_row_is_parish = True

		if not current_office or row[0] == '' or row[0] == 'Total Votes':
			continue

		current_precinct = row[0].strip()
		current_office_write = current_office
		current_district = None

		if 'U.S. House' in current_office:
			current_office_write = 'U.S. House'
			current_district = current_office.replace('U.S. House District ', '')

		row_results = []
		for candidate_index in current_candidates:
			candidate = current_candidates[candidate_index]['candidate']
			if row[candidate_index] == '':
				continue

			row_results.append({'candidate': candidate, 'party': current_candidates[candidate_index]['party'], 'votes': int(row[candidate_index])})
		
		for row_result in row_results:
			if row_result['votes'] == 0:
				continue

			results.append((current_parish, current_precinct, current_office_write, current_district, row_result['party'], row_result['candidate'], row_result['votes']))

		# last line of offices of data we're gathering
		if current_office == 'U.S. House District 6' and current_parish == 'West Baton Rouge' and row[0] == 'Provisional Votes ':
			break

with open('2020/20201103__la__general__precinct.csv', 'w') as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(['county', 'precinct', 'office', 'district', 'party', 'candidate', 'votes'])
	csvwriter.writerows(results)
