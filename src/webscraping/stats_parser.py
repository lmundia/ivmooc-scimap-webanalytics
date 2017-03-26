from bs4 import BeautifulSoup
import csv
import os

data_folder = "../../data/SciMaps-Webalizer-Data/"
out_data_folder = "../../data/output_tables/"

header_written = 0

def extract_data(filename):
    content = open(data_folder + filename, 'r').read()
    soup = BeautifulSoup(content, 'html.parser')

    ATag = soup.find("a", {"name":"DAYSTATS"})
    TableElement = ATag.next_element.next_element.next_element
    rows = {}

    date_part = filename.replace(".html", "")
    date_part = date_part.replace("usage_", "")
    year_part = date_part[:4]
    month_part = date_part[-2:]


    curr_table = 'DAYSTATS'
    rows[curr_table] = []
    for tag in TableElement.find_all(['tr', 'a']):
        if(tag.name == 'a'):
            #print tag
            if tag.has_attr('name'):
                if(tag['name'] == "DAYSTATS" or tag['name'] == "HOURSTATS" or tag['name']\
                        == "TOPURLS" or tag['name'] == "TOPENTRY" or tag['name'] ==
                    'TOPEXIT' or tag['name'] == 'TOPSITES' or tag['name'] ==
                    'TOPREFS' or tag['name'] == 'TOPSEARCH' or tag['name']==
                    'TOPUSERS' or tag['name'] == 'TOPAGENTS' or tag['name'] == 'TOPCTRYS'):
                    curr_table = tag['name']
                    rows[curr_table] = []
        if (tag.name == 'tr'):
            curr_row = []
            curr_row.append(year_part)
            curr_row.append(month_part)
            add_row = 0
            for val in tag.find_all('td'):
                curr_row.append(val.text.encode('utf8'))
                add_row = 1
            if add_row == 1:
                rows[curr_table].append(curr_row)

    global header_written
    for table_name in rows:
        f = open(out_data_folder + table_name + '.csv', 'a')
        writer = csv.writer(f)
        if header_written < 11:
            header_written += 1
            if table_name == 'DAYSTATS':
                writer.writerow(['Year', 'Month', 'Day', 'HitsTotal',
                                         'HitsPct','FilesTotal','FilesPct',
                                         'PagesTotal', 'PagesPct','VisitsTotal',
                                         'VisitPct', 'SitesTotal','SitesPct',
                                         'KBytesTotal', 'KBytesPct'])
            if table_name == 'HOURSTATS':
                writer.writerow(['Year', 'Month', 'Hous', 'HitsAvg',
                                 'HitsTotal', 'HitsPct','FilesAvg','FilesTotal',
                                 'FilesPct', 'PagesAvg',
                                 'PagesTotal', 'PagesPct', 'KBytesAvg',
                                 'KBytesTotal', 'KBytesPct'])
            if table_name == 'TOPURLS':
                writer.writerow(['Year', 'Month', 'Rank',
                                 'HitsTotal', 'HitsPct',
                                 'KBytesTotal', 'KBytesPct', 'URL'])
            if table_name == 'TOPENTRY':
                writer.writerow(['Year', 'Month', 'Rank',
                                 'HitsTotal', 'HitsPct',
                                 'VisitsTotal', 'VisitsPct', 'URL'])
            if table_name == 'TOPEXIT':
                writer.writerow(['Year', 'Month', 'Rank',
                                 'HitsTotal', 'HitsPct',
                                 'VisitsTotal', 'VisitsPct', 'URL'])
            if table_name == 'TOPSITES':
                writer.writerow(['Year', 'Month', 'Rank', 'HitsTotal',
                                 'HitsPct', 'FilesTotal', 'FilesPct',
                                 'KBytesTotal', 'KBytesPct', 'VisitsTotal',
                                 'VisitPct', 'Hostname'])
            if table_name == 'TOPREFS':
                writer.writerow(['Year', 'Month', 'Rank',
                                 'HitsTotal', 'HitsPct',
                                 'Referrer'])
            if table_name == 'TOPSEARCH':
                writer.writerow(['Year', 'Month', 'Rank',
                                 'HitsTotal', 'HitsPct',
                                 'SearchString'])
            if table_name == 'TOPUSERS':
                writer.writerow(['Year', 'Month', 'Rank', 'HitsTotal',
                                         'HitsPct','FilesTotal','FilesPct',
                                         'KBytesTotal', 'KBytesPct','VisitsTotal',
                                         'VisitPct', 'UserName'])
            if table_name == 'TOPAGENTS':
                writer.writerow(['Year', 'Month', 'Rank',
                                 'HitsTotal', 'HitsPct',
                                 'UserAgent'])
            if table_name == 'TOPCTRYS':
                writer.writerow(['Year', 'Month', 'Rank', 'HitsTotal',
                                         'HitsPct','FilesTotal','FilesPct',
                                         'KBytesTotal', 'KBytesPct', 'Country'])
        writer.writerows(row for row in rows[table_name] if row)
        f.close()

for filename in os.listdir(data_folder):
    if filename.endswith(".html"):
        extract_data(filename)
