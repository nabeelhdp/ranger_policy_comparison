#!/usr/bin/env python3

import sys
import os.path
import json

"""Set the DEBUG to 1 if you want to print every matching comparison in addition to the missing ones"""
DEBUG = 0
VERSION = "1.0.1"

__author__ = 'nabeelmoidu'
__version__ = '1.0.2'
__status__ = 'dev'
__title__ = 'Ranger Policy Comparison'
__url__ = 'https://github.com/nabeelhdp/ranger_policy_comparison'


def command_validate():
    """Validate command-line arguments."""
    if len(sys.argv) != 3:
        exit("Not enough files. Please include JSON files to compare.")
    else:
        ranger_policy_json_left = sys.argv[1]
        ranger_policy_json_right = sys.argv[2]
        # Validate that both the json files entered as parameters exist.
        if validate_file(ranger_policy_json_left) and validate_file(ranger_policy_json_right):
            print("Running", sys.argv[0], " on files:", ranger_policy_json_left, "and", ranger_policy_json_right)
        else:
            print("Please enter valid file paths. Program Exiting...")

def find_policy(search_key, to_policy_list):
    """Find policy by name in to_policy_list."""
    for idx, to_policies in enumerate(to_policy_list):
        if search_key == to_policies.get('name'):
            return idx
    return -1

def compare_policy_names(from_policy_list, to_policy_list):
    """Compare policy names between two lists."""
    for from_policies in from_policy_list:
        find_result = find_policy(from_policies.get('name'), to_policy_list)
        if find_result < 0:
            print("Missing policy: ID:", from_policies.get('id'), "Name:", from_policies.get('name'), "Description:", from_policies.get('description'))
        elif DEBUG == 1:
            print("Matched Policy:", from_policies.get('name'))

def validate_policy_json(json_file):
    """Validate and load JSON policy file."""
    try:
        with open(json_file) as f:
            policy_file = json.load(f)
            ranger_version = policy_file['metaDataInfo']['Ranger apache version']
            ranger_hostname = policy_file['metaDataInfo']['Host name']
            print("Ranger apache version on policy file", json_file, " is:", ranger_version)
            print("Ranger Admin Hostname on policy file", json_file, " is:", ranger_hostname)
            print("Ranger Policy count on policy file", json_file, " is:", len(policy_file.get('policies')))
            print("Service name on policy file", json_file, " is:", policy_file.get('policies')[0].get('service'))
            return policy_file
    except (ValueError, KeyError) as e:
        print('Invalid json file \"',json_file,'\" provided. Not an expected Ranger policy export file. Missing Key/Value : %s' % e)
        exit("Please retry with a valid file. Exiting!")

def validate_file(file_path):
    """Validate if the file exists."""
    if file_path is None:
        print("No file/path entered.")
        return False
    elif os.path.exists(file_path):
        return True
    else:
        print("File name/path is Invalid:", file_path)
        return False

if __name__ == '__main__':
    command_validate()

    ranger_policy_file_left = sys.argv[1]
    ranger_policy_file_right = sys.argv[2]
    print("==============================================================")
    ranger_policy_json_left = validate_policy_json(ranger_policy_file_left)
    print("==============================================================")
    ranger_policy_json_right = validate_policy_json(ranger_policy_file_right)
    print("==============================================================")
    service_info = {}
    service_info['left'] = {}
    service_info['right'] = {}
    service_info['left']['policies'] = ranger_policy_json_left.get('policies')
    service_info['right']['policies'] = ranger_policy_json_right.get('policies')
    service_info['left']['name'] = ranger_policy_json_left.get('policies')[0].get('service')
    service_info['right']['name'] = ranger_policy_json_right.get('policies')[0].get('service')

    if service_info['left']['name'] == service_info['right']['name']:
        print("Comparing", ranger_policy_json_left['metaDataInfo']['Host name'], " against ", ranger_policy_json_right['metaDataInfo']['Host name'])
        compare_policy_names(service_info['left']['policies'], service_info['right']['policies'])
        print("==============================================================")
        print("Comparing", ranger_policy_json_right['metaDataInfo']['Host name'], " against ", ranger_policy_json_left['metaDataInfo']['Host name'])
        compare_policy_names(service_info['right']['policies'], service_info['left']['policies'])
    else:
        print ("Mismatching service names:",service_info['left']['name']," AND ",service_info['right']['name']," . Invalid policy comparison. Exiting!")
