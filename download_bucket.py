#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random, requests, time, re
import urllib.request, urllib.parse, urllib.error
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import os
from lib.arg_parser import args
from module.download_bucket_public import *
from module.download_bucket_auth import *
from download_bucket_obj import Bucket



if __name__ == "__main__":
    if args.download or args.get_xml:
        #Get the output folder, based on the current directory if not given
        if args.output_folder:
            output_folder = '{output_folder}/{bucket_name}'.format(output_folder=args.output_folder, bucket_name=args.bucket_name)
        else:
            output_folder = '{cur_dir}/{bucket_name}'.format(cur_dir=os.path.dirname(os.path.realpath(__file__)),bucket_name=args.bucket_name)

        bucket = Bucket(
                             bucket_name=args.bucket_name,
                             url="http://{bucket_name}.s3.amazonaws.com/".format(bucket_name=args.bucket_name),
                             download=args.download,
                             download_include=args.download_include,
                             download_exclude=args.download_exclude,
                             get_xml=args.get_xml,
                             output_folder=output_folder,
                             aws_access_key=args.aws_access_key,
                             aws_secret_key=args.aws_secret_key,
                             quiet=args.quiet,
                             last_key=args.last_key
                        )

        if bucket.aws_access_key:
            download_bucket_auth(bucket=bucket)
        else:
            download_bucket_public(bucket=bucket)

    else:
        print('''\nNeed to either add "-d" to download the bucket or "-x" to get the XML\n''')


