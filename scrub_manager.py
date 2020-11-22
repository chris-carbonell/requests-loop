# general
import csv
import time
from datetime import datetime
import os

# data
import pandas as pd

# requests
import requests

# scrubbing
import maintain_scrub_file as msf

# funcs

def print_log(str_ip, str_main, str_msg):
    ls_print = [
        datetime.today().strftime('%Y-%m-%d %H:%M:%S'), 
        str_main, 
        str_msg
        ]
    print(",".join(ls_print))
    return 

def get_request_df(url):
    
    # get df if possible
    
    print_log(str_ip, "attempting to get", url)
    r = requests.get(url, headers=config.dict_headers, timeout = config.timeout)
    
    if r.ok:
        dict_json = r.json()
        df = pd.DataFrame(dict_json['resultSets'][0]['rowSet'], columns=dict_json['resultSets'][0]['headers'])
        print_log(str_ip, "successfully created df", url)
        return df
    else:
        # log error
        print_log(str_ip, "failed", url)
        with open(config.str_filename_error_log, 'a+') as csvfile:  
            csvwriter = csv.writer(csvfile) # creating a csv writer object
            csvwriter.writerow([r.status_code, url]) # writing the data rows

    return None

def loop_request(str_filename_scrub_file):

    # get scrub file
    file_scrub = msf.get_scrub_file(str_filename_scrub_file)

    # get data
    while len(msf.get_target_list(file_scrub)) > 0:

        # get target
        str_target = msf.get_random_target(file_scrub)
        str_url_temp = str_target.replace(config.base_path,"")
        str_output_filename = config.str_filename_output_root + str_url_temp[0:str_url_temp.find("/")] + ".csv"

        # get df of data
        df_iter = get_request_df(url = str_target)
        df_iter.loc[:, 'request_url'] = str_target # document source
        df_iter.loc[:, 'request_dt'] = datetime.today().strftime('%Y-%m-%d') # document time requested
        
        # append to endpoint.csv
        if os.path.exists(str_output_filename):
            df_iter.to_csv(str_output_filename, mode='a+', header = False, index = False)
        else:
            df_iter.to_csv(str_output_filename, mode='a+', header = True, index = False)

        # log success
        with open(config.str_filename_success_log, 'a+') as csvfile:  
            csvwriter = csv.writer(csvfile) # creating a csv writer object
            csvwriter.writerow([str_target]) # log

        # clean up
        msf.remove_target_single(file_scrub, str_target) # remove from scrub file

    return

if __name__ == "__main__":

    # download data
    loop_request(config.str_filename_scrub_file)