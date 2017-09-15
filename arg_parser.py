#!/usr/bin/env python
# -*- coding: UTF-8 -*-
###############################################
## Purpose: Provies argument parsing capability
###############################################
import argparse

#Documentation
parser = argparse.ArgumentParser(description='''Parameters for Amazon S3 Bucket Scraping''')

#Arguments
group = parser.add_argument_group()
group.add_argument(
                    '-d', 
                    '--download',
                    action='store_true',
                    help="Download the entire bucket",
                   )
group.add_argument(
                    '-x', 
                    '--get_xml',
                    action='store_true',
                    help="Copy the xml, paginated via ?list-type=2&start-after= parameter",
                   )

parser.add_argument(
                    '-n',
                    '--bucket_name',
                    required=True, 
                    help="Bucket Name",
                   )

parser.add_argument(
                    '-o',
                    '--output_folder',
                    required=False, 
                    help="Output folder base to download the reults to, final folder will be output_folder/bucket_name",
                   )


parser.add_argument(
                    '-i',
                    '--download_include',
                    required=False, 
                    help="Only download keys that include any of these strings (case sensitive), can add multiple parameters",
                    action='append',
                   )


parser.add_argument(
                    '-e',
                    '--download_exclude',
                    required=False, 
                    help="Exclude downloading keys that include any of these strings (case sensitive), can add multiple parameters",
                    action='append',
                   )


args = parser.parse_args()