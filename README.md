# NADEX-Scraper-Portfolio-Replication
This repository contains code that can be used to extract market data on NADEX traded options, process PDF files into a machine-readable format, and conduct a basic replication using CBOE call options to identify arbitrage opportunities.

NADEX, formerly known as HedgeStreet, is a US-based retail-focused online binary options exchange. It offers retail trading of binary options and spreads on the most heavily traded forex, commodities and stock indices markets. Unlike many trading platforms, NADEX is relatively transparent with traded volumes and pricing, and daily summaries of trade data are available from their website: https://www.nadex.com/market-data/

As an example, the snapshot below shows binary options on foreign exchange. 

![alt text](https://github.com/a-mkj/NADEX-Scraper-Portfolio-Replication/blob/main/fx_binary_options.png?raw=true)


Data of this form can have a wide range of applications. Retail traders can examine historical spreads to develop strategies, regulators can assess market efficiency and researchers can study trader behavior and market microstructure. Below, I discuss code that extracts files on daily trade data, and conduct a replication of binary options using call options.

<b> Scraping NADEX Daily Trade Data </b>

NADEX data is available in PDF format from its website. Conveniently, the URLs of these files follow a systematic pattern based on file type and trade date, making it relatively easy to scrape and save these files. The file nadex_scraper.py saves three types of files for chosen trade dates: a daily bulletin, end of day results, and time-stamped trades.

<b> Processing NADEX Daily Trade Data & Binary Replication </b>

The first problem with the NADEX data is that it is in a PDF format, and we would like to have the data readable as a dataframe. This is overcome using the tabula package in Python (https://pypi.org/project/tabula-py/), that uses OCR to read tables in PDFs as Pandas dataframes. 

Once the data is read into Python, one object of interest is to assess if there are market inefficiencies on the NADEX platform that can be exploited by prospective traders. I focus here on binary options, which offer an effective case for illustration of a potential strategy. Binary options, also called digital options, can be approximately replicated using two call options with very close strike prices, as shown in the diagram below (credit to: https://quant.stackexchange.com/users/601/smallchess).   

![alt text](https://github.com/a-mkj/NADEX-Scraper-Portfolio-Replication/blob/main/binary_call_replication.png?raw=true)

I restrict this exercise to S&P500 binary options, and extract the corresponding call options from CBOE (https://datashop.cboe.com). The matching process first matches NADEX options to the closest timestamped CBOE option trade, and then searches for the closest possible strike prices. The long call is chosen to be the nearest strike below the NADEX strike, and the short call is the closest strike above the long strike. The code that does this is in nadex_call_replication.py.


    


