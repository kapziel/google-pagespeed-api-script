import requests

def load_from_storage():
	try:
		with open('api_key.txt') as api_key:
			token = api_key.read().splitlines()
			token = [x.strip() for x in token]
			token = token.__str__().strip('[]')
			token = token.__str__().strip('\'')
			return token
	except FileNotFoundError:
		print(f'No API key found, continuing without..')
		pass
	return None


token = load_from_storage()

# Documentation: https://developers.google.com/speed/docs/insights/v5/get-started

# JSON paths: https://developers.google.com/speed/docs/insights/v4/reference/pagespeedapi/runpagespeed

# Populate 'pagespeed.txt' file with URLs to query against API.
with open('pagespeed.txt') as pagespeedurls:
	download_dir = 'pagespeed-results.csv'
	file = open(download_dir, 'w')
	content = pagespeedurls.readlines()
	content = [line.rstrip('\n') for line in content]

	columnTitleRow = "URL, First Contentful Paint, First Interactive," \
					 "Speed Index,First Meaningful Paint, First CPU Idle\n"
	file.write(columnTitleRow)

	# This is the google pagespeed api url structure, using for loop to insert each url in .txt file
	for line in content:
		# If no "strategy" parameter is included, the query by default returns desktop data.
		if token is not None:
			x = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={line}&strategy=mobile&key={token}'
		else:
			x = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={line}&strategy=mobile'
		print(f'Requesting {x}...')
		r = requests.get(x)
		final = r.json()
		j = final

		try:
			urlid = final['id']
			split = urlid.split(
				'?')  # This splits the absolute url from the api key parameter
			urlid = split[0]  # This reassigns urlid to the absolute url
			ID = f'URL ~ {urlid}'
			ID2 = str(urlid)
			urlfcp = final['lighthouseResult']['audits'][
				'first-contentful-paint']['displayValue']
			FCP = f'First Contentful Paint ~ {str(urlfcp)}'
			FCP2 = str(urlfcp)
			urlfi = final['lighthouseResult']['audits'][
				'interactive']['displayValue']
			FI = f'First Interactive ~ {str(urlfi)}'
			FI2 = str(urlfi)
			urlsp = final['lighthouseResult']['audits']['speed-index'][
				'displayValue']
			SP = f'Speed Index ~ {str(urlsp)}'
			SP2 = str(urlsp)
			urlfmp = \
				final['lighthouseResult']['audits']['first-meaningful-paint'][
					'displayValue']
			FMP = f'First Meaningful Paint ~ {str(urlfmp)}'
			FMP2 = str(urlfmp)
			urlfci = \
				final['lighthouseResult']['audits']['first-cpu-idle'][
					'displayValue']
			FCI = f'First CPU Idle ~ {str(urlfci)}'
			FCI2 = str(urlfci)
		except KeyError:
			print(f'<KeyError> One or more keys not found {line}.')

		try:
			row = f'{ID2},{FCP2},{FI2},{SP2},{FMP2},{FCI2}\n'
			file.write(row)
		except NameError:
			print(f'<NameError> Failing because of KeyError {line}.')
			file.write(
				f'<KeyError> & <NameError> Failing because of nonexistant Key ~ {line}.' + '\n')

		try:
			print(ID)
			print(FCP)
			print(FI)
			print(SP)
			print(FMP)
			print(FCI)
		except NameError:
			print(f'<NameError> Failing because of KeyError {line}.')

	file.close()
