# ivmooc-scimap-webanalytics

IVMOOC Project - Web Analytics for Scimap.org web site
The basic statistics is available at https://iu.app.box.com/s/cliqaw4txcnu1c3aw2t3iywgnda58hal
Aim is to produce web analytics dashboard.

This project create dataset for the dashboard.

Steps:

1. Prerequisites - Python 2.7.*
2. Install packages using

    pip install -r requirements.txt

3. Download data from dropbox in ../../data/ folder and unzip it
4. Change the data_folder and out_data_folder names in stats_parser.py
5. Execute stats_parser.py as

    python stats_parser.py
6. The output CSV files will be located in output_tables folder. Start Analyzing
using Excel/Tableau or tool of your choice
