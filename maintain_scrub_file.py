# general
import os
import csv

# combos
# import itertools
# import string
import random

def get_scrub_file(str_filename_scrub):
    '''
    get scrub file if it already exists

    args:
    str_filename_scrub (str): path to file
    
    returns:
    file_scrub (file): scrub file
    '''
    
    # get file
    file_scrub = open(str_filename_scrub, 'a+', newline='')

    return file_scrub

def get_target_list(file_scrub):
    '''
    get list from scrub file
    
    args:
    file_scrub (file): scrub file
    
    returns:
    ls_scrub (ls): list of items in scrub file e.g., ['aa', ''bb', 'cc']
    '''
    
    file_scrub.seek(0,0) # go to beginning assuming a+
    csv_reader = csv.reader(file_scrub)
    
    ls_scrub = []
    for ls_target in list(csv_reader): # list of lists eg [['aa'], ['bb'], ['cc']]
        ls_scrub.append(ls_target[0])
    
    return ls_scrub

def get_target_list_len(file_scrub):
    ls_target = get_target_list(file_scrub)
    return len(ls_target)

def get_unique_combination(ls_one, ls_two):
    '''
    combine two lists and keep uniques
    
    args:
    ls_one (ls): first list
    ls_two (ls): second list
    
    return:
    (unnamed) (ls): union of both lists
    '''

    # convert each list into a set, union, convert back to list

    # make sure all lowercase
    set_one = set([x.lower() for x in ls_one])
    set_two = set([x.lower() for x in ls_two])

    return list(set_one|set_two)

def get_random_target(file_scrub):
    '''
    choose random target from scrub file
    
    args:
    file_scrub (file): file of items to scrub
    
    returns:
    (unnamed) (str): random item from file_scrub
    '''
    
    ls_scrub = get_target_list(file_scrub)
    
    return random.choice(ls_scrub)

def add_target_multiple(file_scrub, ls_target):
    '''
    add multiple targets to scrub file
    
    args:
    file_scrub (file): file of items to scrub
    ls_target (ls): list of items to add
    
    returns:
    None
    '''
    
    # massage ls_target if necessary
    
    # only keep uniques
    ls_all = get_unique_combination(
        get_target_list(file_scrub), 
        ls_target
    )
    
    # convert to list of lists for writerows
    # writerows needs list of lists e.g., [['aa'], ['bb'], ['cc']]
    ls_temp = []
    for str_target in ls_all:
        # wrap in a list
        ls_temp.append([str_target])
    
    # truncate (ie delete everything)
    file_scrub.truncate(0)
    
    csv_writer = csv.writer(file_scrub)
    csv_writer.writerows(ls_temp)
    file_scrub.flush()
    
    return

def remove_target_single(file_scrub, str_target):
    '''
    remove item from scrub file
    
    args:
    file_scrub (file): scrub file
    str_target (str): item to remove
    
    returns:
    None
    '''
    
    # get targets
    file_scrub.seek(0,0)
    csv_reader = csv.reader(file_scrub)
    ls_scrub = list(csv_reader)

    # remove
    try:
        ls_scrub.remove([str_target])
    except:
        pass

    # truncate (ie delete everything)
    file_scrub.truncate(0)
    
    # save (essentially overwrite)
    csv_writer = csv.writer(file_scrub)
    csv_writer.writerows(ls_scrub)
    
    file_scrub.flush()
    
    return

# # example usage

# # start scrub file with a starter list
# # append if exists; otherwise create
# file_scrub = create_target_list("./scrub_me.csv", ['aa','bb']) # ['aa','bb']

# # add more targets
# # only unique items kept
# add_target_multiple(file_scrub, ['bb','cc','dd']) # ['aa','bb','cc','dd']

# # remove a target
# # if it does not exist, nothing changes
# remove_target_single(file_scrub, 'cc') # ['aa','bb','dd']
# remove_target_single(file_scrub, 'ee') # ['aa','bb','dd']

# # get list of scrub file
# get_target_list(file_scrub) # ['aa','bb','dd']