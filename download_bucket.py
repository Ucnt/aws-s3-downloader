#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random, requests, time, re
import urllib
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import os 
from arg_parser import args
from download_bucket_public import *
from download_bucket_auth import *


class Bucket():
    def __init__ (self, bucket_name, url, download, download_include, download_exclude, get_xml, output_folder, aws_access_key, aws_secret_key):
        self.bucket_name = bucket_name
        self.url = url
        self.download = download
        self.download_include = download_include
        self.download_exclude = download_exclude
        self.get_xml = get_xml
        self.xml_output_file = '{output_folder}/bucket_xml.xml'.format(output_folder=output_folder)
        self.output_folder = output_folder
        self.aws_access_key = aws_access_key
        self.aws_secret_key = aws_secret_key
        self.is_truncated = False
        self.num_keys = 0


if __name__ == "__main__": 
    if args.download or args.get_xml:
        #Get the output folder, based on the current directory if not given
        if args.output_folder:
            output_folder = '{output_folder}/{bucket_name}'.format(output_folder=args.output_folder, bucket_name=args.bucket_name)
        else:
            output_folder = '{cur_dir}/{bucket_name}'.format(cur_dir=os.path.dirname(os.path.realpath(__file__)),bucket_name=args.bucket_name)

        bucket = Bucket(
                             bucket_name=args.bucket_name, 
                             url="https://s3.amazonaws.com/{bucket_name}".format(bucket_name=args.bucket_name), 
                             download=args.download, 
                             download_include=args.download_include,
                             download_exclude=args.download_exclude,
                             get_xml=args.get_xml,
                             output_folder=output_folder,
                             aws_access_key=args.aws_access_key,
                             aws_secret_key=args.aws_secret_key,
                        )

        if bucket.aws_access_key:
            download_bucket_auth(bucket=bucket)
        else:
            download_bucket_public(bucket=bucket)

    else:
        print '''\nNeed to either add "-d" to download the bucket or "-x" to get the XML\n'''



    
