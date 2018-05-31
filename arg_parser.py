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
                    help="Only download keys that include any of these strings (case insensitive), can add multiple parameters",
                    action='append',
                   )


parser.add_argument(
                    '-e',
                    '--download_exclude',
                    required=False, 
                    help="Exclude downloading keys that include any of these strings (case insensitive), can add multiple parameters",
                    action='append',
                   )

parser.add_argument(
                    '-lk',
                    '--last_key',
                    required=False, 
                    help="Last Key to skip ahead to if doing public download",
                   )


parser.add_argument(
                    '-ak',
                    '--aws_access_key',
                    required=False, 
                    help="AWS Access Key",
                   )


parser.add_argument(
                    '-sk',
                    '--aws_secret_key',
                    required=False, 
                    help="AWS Secret Key",
                   )

parser.add_argument(
                    '-q',
                    '--quiet',
                    action='store_true',
                    help="Don't print updates",
                   )


args = parser.parse_args()
