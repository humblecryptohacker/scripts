#!/usr/bin/env python2.7
import urllib
import time
import sys


FILE_PATH=sys.argv[1]
SNED_ERROR_MAIL_FILE="/home/ubuntu/data/error.log"
last_time_stamp=None
while(True):
    link = "https://www.bitstamp.net/api/ticker/"    
    f = urllib.urlopen(link)
    myfile = f.read()
    temp_dict = eval(myfile)
    if (len(temp_dict.keys())==9):
        bid=temp_dict["bid"]
        ask=temp_dict["ask"]
        high=temp_dict["high"]
        last=temp_dict["last"]
        low=temp_dict["low"]
        open_price=temp_dict["open"]
        volume=temp_dict["volume"]
        vwap=temp_dict["vwap"]
        timestamp=temp_dict["timestamp"]
        if last_time_stamp==None:
	    last_time_stamp=timestamp
	    with open(FILE_PATH, "a") as myfile:
            	myfile.write(" ".join([timestamp,bid,ask,volume,vwap,str(open_price),high,low,"\n"]))
            	time.sleep(30)
		continue
        #write to a file 

	if last_time_stamp!=timestamp:
            with open(FILE_PATH, "a") as myfile:
            	myfile.write(" ".join([timestamp,bid,ask,volume,vwap,str(open_price),high,low,"\n"]))
            	time.sleep(30)
	else:
		time.sleep(10)
    else:
        #write the error in the log file
        with open(SEND_ERROR_MAIL_FILE,"w") as error_file:
            error_file.write("The data fetched for time_stamp : ",time_stamp," has more than 8 fields hence skipping the data fetch \n")
