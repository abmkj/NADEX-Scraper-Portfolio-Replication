#Importing modules
import numpy as np
import pandas as pd
import pickle
from tabula import read_pdf

#Input dictionary to store filenames, NADEX page numbers of interest, CBOE file name and expiry
inputs_dict = {
    '20180604':{
        'nadex_file':'timesales20180604.pdf',
        'nadex_date_use':'06/04/2018',
        'nadex_lower_pg': 289,
        'nadex_upper_pg':291,
        'cboe_file':'UnderlyingOptionsIntervalsQuotes_900sec_2018-06-04.csv',
        'cboe_expiry': '6/8/18'
    },
    '20180605':{
        'nadex_file':'timesales20180605.pdf',
        'nadex_date_use':'06/05/2018',
        'nadex_lower_pg': 286,
        'nadex_upper_pg':288,
        'cboe_file':'UnderlyingOptionsIntervalsQuotes_900sec_2018-06-05.csv',
        'cboe_expiry': '6/8/18'
    },
    '20180606':{
        'nadex_file':'timesales20180606.pdf',
        'nadex_date_use':'06/06/2018',
        'nadex_lower_pg': 273,
        'nadex_upper_pg':276,
        'cboe_file':'UnderlyingOptionsIntervalsQuotes_900sec_2018-06-06.csv',
        'cboe_expiry': '6/8/18'
    },
    '20180607':{
        'nadex_file':'timesales20180607.pdf',
        'nadex_date_use':'06/07/2018',
        'nadex_lower_pg': 274,
        'nadex_upper_pg':277,
        'cboe_file':'UnderlyingOptionsIntervalsQuotes_900sec_2018-06-07.csv',
        'cboe_expiry': '6/8/18'
    },
    '20180608':{
        'nadex_file':'timesales20180608.pdf',
        'nadex_date_use':'06/08/2018',
        'nadex_lower_pg': 272,
        'nadex_upper_pg':275,
        'cboe_file':'UnderlyingOptionsIntervalsQuotes_900sec_2018-06-08.csv',
        'cboe_expiry': '6/8/18'
    },
    '20180611':{
        'nadex_file':'timesales20180611.pdf',
        'nadex_date_use':'06/11/2018',
        'nadex_lower_pg': 274,
        'nadex_upper_pg':277,
        'cboe_file':'UnderlyingOptionsIntervalsQuotes_900sec_2018-06-11.csv',
        'cboe_expiry': '6/15/18'
    },
    '20180612':{
        'nadex_file':'timesales20180612.pdf',
        'nadex_date_use':'06/12/2018',
        'nadex_lower_pg': 290,
        'nadex_upper_pg':292,
        'cboe_file':'UnderlyingOptionsIntervalsQuotes_900sec_2018-06-12.csv',
        'cboe_expiry': '6/15/18'
    },
    '20180613':{
        'nadex_file':'timesales20180613.pdf',
        'nadex_date_use':'06/13/2018',
        'nadex_lower_pg': 276,
        'nadex_upper_pg':278,
        'cboe_file':'UnderlyingOptionsIntervalsQuotes_900sec_2018-06-13.csv',
        'cboe_expiry': '6/15/18'
    },
    '20180614':{
        'nadex_file':'timesales20180614.pdf',
        'nadex_date_use':'06/14/2018',
        'nadex_lower_pg': 294,
        'nadex_upper_pg':296,
        'cboe_file':'UnderlyingOptionsIntervalsQuotes_900sec_2018-06-14.csv',
        'cboe_expiry': '6/15/18'
    },
    '20180615':{
        'nadex_file':'timesales20180615.pdf',
        'nadex_date_use':'06/15/2018',
        'nadex_lower_pg': 253,
        'nadex_upper_pg':255,
        'cboe_file':'UnderlyingOptionsIntervalsQuotes_900sec_2018-06-15.csv',
        'cboe_expiry': '6/15/18'
    },
    '20180618':{
        'nadex_file':'timesales20180618.pdf',
        'nadex_date_use':'06/18/2018',
        'nadex_lower_pg': 272,
        'nadex_upper_pg':274,
        'cboe_file':'UnderlyingOptionsIntervalsQuotes_900sec_2018-06-18.csv',
        'cboe_expiry': '6/22/18'
    },
    '20180619':{
        'nadex_file':'timesales20180619.pdf',
        'nadex_date_use':'06/19/2018',
        'nadex_lower_pg': 292,
        'nadex_upper_pg':296,
        'cboe_file':'UnderlyingOptionsIntervalsQuotes_900sec_2018-06-19.csv',
        'cboe_expiry': '6/22/18'
    },
    '20180620':{
        'nadex_file':'timesales20180620.pdf',
        'nadex_date_use':'06/20/2018',
        'nadex_lower_pg': 248,
        'nadex_upper_pg':250,
        'cboe_file':'UnderlyingOptionsIntervalsQuotes_900sec_2018-06-20.csv',
        'cboe_expiry': '6/22/18'
    },
    '20180621':{
        'nadex_file':'timesales20180621.pdf',
        'nadex_date_use':'06/21/2018',
        'nadex_lower_pg': 264,
        'nadex_upper_pg':267,
        'cboe_file':'UnderlyingOptionsIntervalsQuotes_900sec_2018-06-21.csv',
        'cboe_expiry': '6/22/18'
    },
    '20180622':{
        'nadex_file':'timesales20180622.pdf',
        'nadex_date_use':'06/22/2018',
        'nadex_lower_pg': 249,
        'nadex_upper_pg':251,
        'cboe_file':'UnderlyingOptionsIntervalsQuotes_900sec_2018-06-22.csv',
        'cboe_expiry': '6/22/18'
    },
    '20180625':{
        'nadex_file':'timesales20180625.pdf',
        'nadex_date_use':'06/25/2018',
        'nadex_lower_pg': 293,
        'nadex_upper_pg':296,
        'cboe_file':'UnderlyingOptionsIntervalsQuotes_900sec_2018-06-25.csv',
        'cboe_expiry': '6/29/18'
    },
    '20180626':{
        'nadex_file':'timesales20180626.pdf',
        'nadex_date_use':'06/26/2018',
        'nadex_lower_pg': 280,
        'nadex_upper_pg':282,
        'cboe_file':'UnderlyingOptionsIntervalsQuotes_900sec_2018-06-26.csv',
        'cboe_expiry': '6/29/18'
    },
    '20180627':{
        'nadex_file':'timesales20180627.pdf',
        'nadex_date_use':'06/27/2018',
        'nadex_lower_pg': 291,
        'nadex_upper_pg':294,
        'cboe_file':'UnderlyingOptionsIntervalsQuotes_900sec_2018-06-27.csv',
        'cboe_expiry': '6/29/18'
    },
    '20180628':{
        'nadex_file':'timesales20180628.pdf',
        'nadex_date_use':'06/28/2018',
        'nadex_lower_pg': 265,
        'nadex_upper_pg':267,
        'cboe_file':'UnderlyingOptionsIntervalsQuotes_900sec_2018-06-28.csv',
        'cboe_expiry': '6/29/18'
    },
    '20180629':{
        'nadex_file':'timesales20180629.pdf',
        'nadex_date_use':'06/29/2018',
        'nadex_lower_pg': 287,
        'nadex_upper_pg':289,
        'cboe_file':'UnderlyingOptionsIntervalsQuotes_900sec_2018-06-29.csv',
        'cboe_expiry': '6/29/18'
    },
    '20180702':{
        'nadex_file':'timesales20180702.pdf',
        'nadex_date_use':'07/02/2018',
        'nadex_lower_pg': 333,
        'nadex_upper_pg':335,
        'cboe_file':'UnderlyingOptionsIntervalsQuotes_900sec_2018-07-02.csv',
        'cboe_expiry': '7/6/18'
    }
}

#Data frame to store final results for replication vs actual 
df_final_store = pd.DataFrame()

#Looping through all days in data
for date_to_run in list( inputs_dict.keys() ):
    
    print( date_to_run )
    
    #NADEX Inputs 
    file = inputs_dict[ date_to_run ][ 'nadex_file' ]
    date_use = inputs_dict[ date_to_run ][ 'nadex_date_use' ]
    df_nadex = pd.DataFrame()
    nadex_lower_pg = inputs_dict[ date_to_run ][ 'nadex_lower_pg' ]
    nadex_upper_pg = inputs_dict[ date_to_run ][ 'nadex_upper_pg' ]

    ########################################################################
    ######################## PROCESSING NADEX DATA #########################
    ########################################################################

    #Reading relevant pages from the NADEX PDF
    for i in range( nadex_lower_pg, nadex_upper_pg ):
        temp = read_pdf( file, pages=i )
        df_nadex = pd.concat([df_nadex,temp],ignore_index=True)

    #Filtering for SP500 options
    df_nadex = df_nadex[ df_nadex[ 'Display Name' ].str.contains( 'US 500' ) ]
    df_nadex[ 'Strike' ] = df_nadex[ 'Display Name' ].str[ 14:20 ]
    df_nadex[ "Strike" ] = pd.to_numeric( df_nadex[ "Strike" ] )

    #Converting time stamp to avoid datetime match errors
    hours = list( df_nadex[ 'Execution Time' ].str[ 11:13 ] )
    minutes = list( df_nadex[ 'Execution Time' ].str[ 14:16 ] )
    seconds = list( df_nadex[ 'Execution Time' ].str[ 17:19 ] )
    time_cov_store = list()

    for i in range( len( hours ) ):
        hours_temp = int( hours[ i ] )
        minutes_temp = int( minutes[ i ] )
        seconds_temp = int( seconds[ i ] )
        final_temp = hours_temp*3600 + minutes_temp*60 + seconds_temp 
        time_cov_store.append( final_temp )

    df_nadex[ 'Execution Time Converted' ] = time_cov_store
    df_nadex[ 'Date' ] = df_nadex[ 'Execution Time' ].str[ 0:10 ]    
    df_nadex = df_nadex[ df_nadex.Date == date_use ]

    #Re-indexing dataframe for NADEX
    df_nadex = df_nadex.reset_index(drop=True)
    
    #CBOE Inputs
    file = inputs_dict[ date_to_run ][ 'cboe_file' ]
    expiry = inputs_dict[ date_to_run ][ 'cboe_expiry' ]

    ########################################################################
    ######################## PROCESSING CBOE DATA ##########################
    ########################################################################

    #Filtering for calls with correct expiry
    df_cboe = pd.read_csv( file, header = 0 )
    df_cboe = df_cboe[ df_cboe.expiration == expiry ]
    df_cboe = df_cboe[ df_cboe.option_type == 'c' ]

    #Processing the time stamp for matching 
    time_temp = df_cboe.quote_datetime.str.split( ' ' ).str[ 1 ]
    hour_temp = time_temp.str.split( ':' ).str[ 0 ]
    minute_temp = time_temp.str.split( ':' ).str[ 1 ]
    hour_temp = list( hour_temp )
    minute_temp = list( minute_temp )
    final_store = list()

    for i in range( len( hour_temp ) ):
        hour_op = int( hour_temp[ i ] )
        minute_op = int( minute_temp[ i ] )
        final_op = hour_op*3600 + minute_op*60
        final_store.append( final_op )

    df_cboe[ 'Execution Time Converted' ] = final_store
    
    #Renaming strike and eliminating empty stamps
    df_cboe[ 'Strike' ] = df_cboe[ 'strike' ]
    df_cboe = df_cboe[ df_cboe[ 'close' ] != 0 ]

    #Re-indexing dataframe for NADEX
    df_cboe = df_cboe.reset_index(drop=True)
    
    ########################################################################
    ############################ MATCHING PROCESS ##########################
    ########################################################################
    
    #This section matches CBOE call options to NADEX binary options for replication
    times_matching = list( df_nadex[ 'Execution Time Converted' ] )
    repl_store = list()
    nadex_act_store = list()
    
    #First matches for the nearest timestamp, and then looks for closest strikes
    #CBOE data tends to have all strikes at all timestamps
    #Current replication uses just two call options, a long and a short
    #The long is chosen to be the nearest strike below the NADEX strike
    #The short is the closest strike above the long strike 
    
    for t in times_matching:
        #Filtering for nearest time stamp
        temp = list( abs( t - df_cboe[ 'Execution Time Converted' ] ) )
        
        #Finding nearest time stamp 
        time_val = df_cboe[ 'Execution Time Converted' ][ np.argmin( temp ) ]
        
        #Filtering data for that timestamp
        df_cboe_temp = df_cboe[ df_cboe[ 'Execution Time Converted' ] == time_val ]
        df_cboe_temp = df_cboe_temp.reset_index( drop = True )
        df_nadex_temp = df_nadex[ df_nadex[ 'Execution Time Converted' ] == t ]
        df_nadex_temp = df_nadex_temp.reset_index( drop = True )

        strikes_match_store = list( df_nadex_temp[ 'Strike' ] )

        #Filtering for nearest strike price, for all strikes in NADEX data
        for s in strikes_match_store:
            strikes_diff = list( s - df_cboe_temp[ 'Strike' ] )
            #Searching for nearest strike below NADEX strike
            temp_strikes_diff = [ num for num in strikes_diff if num > 0 ]
            if len( temp_strikes_diff ) > 0: #Edge case, for first trade in the day
                #Finding closest and next strikes
                closest = min( temp_strikes_diff )
                closest_index = strikes_diff.index( closest )
                second_closest_list = [ num for num in strikes_diff if num < closest ]
                if len( second_closest_list ) > 0: #Edge case for no options above the strike
                    second_closest = max( second_closest_list )
                    second_closest_index = strikes_diff.index( second_closest ) 
                    #Taking average of high and low in the 15min period as the call price
                    call1_price = ( df_cboe_temp[ 'high' ][ closest_index ] + df_cboe_temp[ 'low' ][ closest_index ] )/2
                    call2_price = ( df_cboe_temp[ 'high' ][ second_closest_index ] + df_cboe_temp[ 'low' ][ second_closest_index ] )/2
                    #Constructing synthetic portfolio and scaling to match NADEX payoff of 100
                    net_call_price = call1_price - call2_price
                    call_qty = ( 100/ ( df_cboe_temp[ 'Strike' ][ second_closest_index ] - df_cboe_temp[ 'Strike' ][ closest_index ] ) )
                    repl_cost = net_call_price*call_qty 
                    #Storing replication price, and NADEX price for that strike and timestamp
                    binary_cost = df_nadex_temp[ 'Price (USD)' ].iloc[ df_nadex_temp.index[ df_nadex_temp[ 'Strike' ] == s ] ]
                    binary_vol = df_nadex_temp[ 'Volume' ].iloc[ df_nadex_temp.index[ df_nadex_temp[ 'Strike' ] == s ] ]
                    binary_cost = np.average( a = binary_cost, weights = binary_vol ) #Computing weighted average NADEX price
                    repl_store.append( repl_cost )
                    nadex_act_store.append( binary_cost )
                else:
                    continue
            else:
                continue 
                
    #Calculating difference of replication and actual portfolio, complexity theory suggests that Diff should be negative
    df_analysis = pd.DataFrame( { 'Rep':repl_store, 'Act':nadex_act_store } )
    df_analysis[ 'Diff' ] = df_analysis[ 'Rep' ] - df_analysis[ 'Act' ]
    
    df_final_store = pd.concat([df_final_store,df_analysis],ignore_index=True)
    
#Saving results as a pickle file
df_final_store.to_pickle( 'final_results.pkl' )

#Generating histogram to assess replication quality
import matplotlib.pyplot as plt

cutoff = 60 #Variation cutoff of interest
bin_count = 20 #Number of histogram bins
df_final_store = df_final_store[ df_final_store.Diff < cutoff ]
df_final_store = df_final_store[ df_final_store.Diff > -cutoff ]
ax = df_final_store.Diff.hist( bins = bin_count )
ax.set_xlabel( 'Replicating Portfolio - Binary' )
ax.set_ylabel( 'Frequency' )

