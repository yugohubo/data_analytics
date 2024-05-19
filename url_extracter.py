import pandas as pd
import re # regular expression library for the matching

# data = pd.read_csv('url_data') # we can use this if the data given is a csv file

# i have defined this so we can see it with an example

data = {
    'Device_Type': ['AXO145', 'BXO256', 'CYO367','LKS902'],
    'Stats_Access_Link': [
        '<url>https://xcd32112.smart_meter.com</url>',
        '<url>http://atdfsag_met_f3.txs.com</url>',
        '<url>https://easg_345-3_3.fdsf.afg.com</url>', # especially put here so it gives None value if '-' is in the url for misspells
        '<url>https://43hgfdh3_3.fdsf.afg.com</url>' 
    ]
}

# This function is the main operation that looks for pure url

def extract_pure_url(url): 

    pattern = r'<url>https?://([a-zA-Z0-9_.]+)</url>' #this is the pattern that is given to look for the url since we assume the data is the same format
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

df = pd.DataFrame(data)

df['Pure_URL'] = df['Stats_Access_Link'].apply(extract_pure_url)

# Display the DataFrame with the new column
print(df)