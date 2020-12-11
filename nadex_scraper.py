#Reading required modules
from pathlib import Path
import requests

#Choose years/months/days of interest
years = [ '2019' ]
months = [ '01', '02', '03', '04', '05', '06' ]
days = [ '01', '02', '03', '04', '05', '06', '07', '08', '09',
         '10', '11', '12', '13', '14', '15', '16', '17', '18', 
         '19', '20', '21', '22', '23', '24', '25', '26', '27', '28',
         '29', '30', '31' ]

#Iterating with nested loops
for year in years:
    for month in months:
        for day in days:
            #Creating URLs for PDF extraction
            date = year + month + day
            url_timesales = 'https://www.nadex.com/sites/default/files/pdf/time-and-sales/' + date + '_timeandsales.pdf'
            url_daily = 'https://www.nadex.com/sites/default/files/pdf/daily-bulletin/' + date + '_dailybulletin.pdf'
            url_results = 'https://www.nadex.com/sites/default/files/pdf/results/' + date + '_tradingResults.pdf'
            
            #Verifying content of URL is a PDF file
            r_timesales = requests.get( url_timesales )
            r_daily = requests.get( url_daily )
            r_results = requests.get( url_results )
            content_type_timesales = r_timesales.headers.get('content-type')
            content_type_daily = r_daily.headers.get('content-type')
            content_type_results = r_results.headers.get('content-type')
            
            #Storing each category of PDF file
            if content_type_timesales == 'application/pdf':
                filename_timesales = Path( 'timesales' + date + '.pdf')
                response_timesales = requests.get( url_timesales )
                filename_timesales.write_bytes( response_timesales.content )
                
            if content_type_daily == 'application/pdf':
                filename_daily = Path( 'daily' + date + '.pdf')
                response_daily = requests.get( url_daily )
                filename_daily.write_bytes( response_daily.content )
                
            if content_type_results == 'application/pdf':
                filename_results = Path( 'results' + date + '.pdf')
                response_results = requests.get( url_results )
                filename_results.write_bytes( response_results.content )
            
            #Recording completion
            print( date )