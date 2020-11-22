# general
import csv
import pandas as pd
from datetime import datetime

# config
import config

# requests
import requests

# funcs

def get_url(session, base_url, params):
    '''
    get the prepared URL

    args:
    session (requests.Session()): requests session
    base_url (str): base path + endpoint
    params (dict): path params

    returns:
    prepped.url (str): full resource url 
    '''

    req = requests.Request('GET', base_url, data=params, headers=config.dict_headers)
    prepped = req.prepare()
    prepped.prepare_url(url = base_url, params = params)

    return prepped.url

def loop_var(base_path, endpoint, key, ls_iter, params, ls_append):
    '''
    for a given endpoint, update the key in params with each item in ls_iter

    args:
    base_path (str): base path (end with / if applicable)
    endpoint (str): endpoint (don't end with /)
    key (str): key in params whose value we need to update
    ls_iter (ls): values to iterate through when updating params
    params (dict): path params
    ls_append (ls): output list of prepared urls (before adding)

    returns:
    ls_append (ls): output list of prepared urls
    '''

    base_url = base_path + endpoint + "/"
    for value in ls_iter:
        params[key] = value # add to params
        ls_append.append([get_url(s, base_url, params)]) # get url

    return ls_append

if __name__ == "__main__":

    # get chuck norris jokes
    # https://api.chucknorris.io/
    # see config.py for more details
    endpoint = "categories"

    # get categories
    ls_categories = requests.get("https://api.chucknorris.io/jokes/categories").json()

    # input
    str_filename_scrub_file = "./input/" + datetime.today().strftime('%Y%m%d%H%M%S') + "_scrub_file.csv"
    
    # set up url list
    ls_append = []

    # get resource urls
    ls_append = loop_var(
        base_path = config.base_path,
        endpoint = endpoint, 
        key = "category", 
        ls_iter = ls_categories, 
        params = {},
        ls_append = ls_append
        )

    # SAVE

    with open(str_filename_scrub_file, 'a+') as csvfile:  
        
        # creating a csv writer object  
        csvwriter = csv.writer(csvfile)
        
        # writing the data rows  
        csvwriter.writerows(ls_append)