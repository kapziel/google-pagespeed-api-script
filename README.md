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
 
### Requires

- Requests


### Note

.gitignore hides api token file, this is loaded in via a .txt file. If no files exists `None` is used and script will contine without. To use in production (multiple calls / sec) an api token will be required.
