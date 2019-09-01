## Google Pagespeed API - Python
1. This script reads urls from 'pagespeed.txt' file. Load this file with full URLS - make sure to include `https://` parameters (will add in URL validation in future)
2. Queries each url with the google pagespeed api.
3. Filters JSON results to only include desired metrics.
4. Metrics are saved to local .csv spreadsheet for analysis.


#### Current columns are
 - URL
 - First Contentful Paint
 - First Meaningful Paint
 - Speed Index
 - First CPU Idle
 - Time to interactive
 
