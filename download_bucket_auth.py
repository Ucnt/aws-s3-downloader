#!/usr/bin/env python
# -*- coding: utf-8 -*-
from boto.s3.connection import S3Connection
import os

def download_bucket_auth(bucket):
    conn = S3Connection(bucket.aws_access_key, bucket.aws_secret_key)
    try:
        bucket_conn = conn.get_bucket(bucket.bucket_name)
        for key in bucket_conn.list():
            if bucket.get_xml:
                save_xml(bucket=bucket, key_name=key.name)
            if bucket.download:
                file_name = '{output_folder}/{key}'.format(output_folder=bucket.output_folder, key=key.name).strip()
                if not os.path.exists(file_name):
                    if not bucket.download_include or any(include.lower() in key.lower() for include in bucket.download_include):
                        if not bucket.download_exclude or not any(exclude.lower() in key.lower() for exclude in bucket.download_exclude):
                            #Create the directory if it doesn't exist (needed for sub-directories)
                            if not os.path.exists(file_name):
                                os.makedirs(file_name)
                                os.rmdir(file_name)

                            #Try downloading the file
                            try:
                                key.get_contents_to_filename(file_name)
                                print "  SUCCESS: %s" % (key.name)
                            except Exception as e:
                                if "Access Denied" in str(e):
                                    print "  FAIL: %s - Access Denied" % (key.name)
                                else:
                                    print "  FAIL: %s - %s" % (key.name, e)
                else:
                    print "  already downloaded {file_name}".format(file_name=file_name)
    except Exception as e:
        print e


def save_xml(bucket, key_name):
    """Add the given bucket page's XML to the XML output file"""
    #Create the directory if it doesn't exist
    if not os.path.exists(bucket.output_folder):
        os.makedirs(bucket.output_folder)

    """Save the XML (e.g. page source code) for the bucket"""
    f = open(bucket.xml_output_file.replace(".xml",".txt"), "a+")
    f.write('''%s\n''' % (key_name))
    f.close()