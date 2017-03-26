from bs4 import BeautifulSoup
import csv
import os

data_folder = "../../data/SciMaps-Webalizer-Data/"
out_data_folder = "../../data/output_summary/"

def extract_data(filename):
    content = open(data_folder + filename, 'r').read()
    soup = BeautifulSoup(content, 'html.parser')

    ATag = soup.find("a", {"name":"DAYSTATS"})
    TableElement = ATag.next_element.next_element.next_element
    rows = []

    date_part = filename.replace(".html", "")
    date_part = date_part.replace("usage_", "")
    year_part = date_part[:4]
    month_part = date_part[-2:]

#    for row in TableElement.find_all('tr'):
#        rows.append([val.text.encode('utf8') for val in row.find_all('td')])

    for row in TableElement.find_all('tr'):
        curr_row = []
        curr_row.append(year_part)
        curr_row.append(month_part)
        for val in row.find_all('td'):
            curr_row.append(val.text.encode('utf8'))
        rows.append(curr_row)

    with open('output_file.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(row for row in rows if row)

    out_file_names = ['daily.csv', 'hourly.csv', 'top100urls.csv',
              'top10urlsbykbytes.csv',
              'top10entry.csv','top10exitpages.csv','top30sites.csv',
              'top10sites.csv','top30referres.csv','top20searchstrings.csv',
              'top15agents.csv','top30countries.csv','extra.csv','extra.csv','extra.csv']


    file_index = 0
    #out_file_name_prefix = filename.replace(".html", "_")


    f = open(out_data_folder + out_file_names[file_index], 'a')
    writer = csv.writer(f)

    index = 0
    while(len(rows[index]) <= 2):
        index += 1
    while index < len(rows):
        writer.writerow(rows[index])
        index += 1
        if(len(rows[index]) <= 2):
            file_index = file_index + 1
            if(file_index < len(out_file_names)-1):
                f.close()
                f = open(out_data_folder + out_file_names[file_index],'a')
                writer = csv.writer(f)
            while(len(rows[index]) <= 2):
                index += 1
                if(index == len(rows)):
                    break

    f.close()




for filename in os.listdir(data_folder):
    if filename.endswith(".html"):
        extract_data(filename)
