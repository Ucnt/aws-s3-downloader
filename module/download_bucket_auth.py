#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from boto.s3.connection import S3Connection
import os

def download_bucket_auth(bucket):
    if not bucket.bucket_name.strip():
        return

    conn = S3Connection(bucket.aws_access_key, bucket.aws_secret_key)
    try:
        print("  connecting to bucket")
        bucket_conn = conn.get_bucket(bucket.bucket_name)
        print("  enumerating keys")
        for index, key in enumerate(bucket_conn.list()):
#            if index >= 200000:
#               break
            if bucket.get_xml:
                save_xml(bucket=bucket, key_name=key.name)
            if bucket.download:
                file_name = '{output_folder}/{key}'.format(output_folder=bucket.output_folder, key=key.name.strip()).strip()
                if not bucket.download_include or any(include.lower() in key.name.lower() for include in bucket.download_include):
                    if not bucket.download_exclude or not any(exclude.lower() in key.name.lower() for exclude in bucket.download_exclude):
                        if not os.path.exists(file_name):
                            #Create the directory if it doesn't exist (needed for sub-directories)
                            try:
                                if not os.path.exists(file_name):
                                    os.makedirs(file_name)
                                    os.rmdir(file_name)
                            except Exception as e:
                                print("    *** Error (%s) on folder creation: %s ***" % (e, file_name))
                                continue
                            #Try downloading the file
                            try:
                                k = bucket_conn.lookup(key.name)
                                num_bytes = k.size
                                num_kilobytes = num_bytes/1024
                                num_megabytes = num_kilobytes/1024
                                num_gigabytes = num_megabytes/1024
                                print("  DOWNLOADING: {key_name} ({B} B, {KB} KB, {MB} MB, {GB} GB)".format(key_name=key.name, B=num_bytes, KB=num_kilobytes, MB=num_megabytes, GB=num_gigabytes))
                                key.get_contents_to_filename(file_name)
                                print("      FINISHED")
                            except Exception as e:
                                if "Access Denied" in str(e):
                                    print("    FAIL: %s - Access Denied" % (key.name))
                                else:
                                    print("    FAIL: %s - %s" % (key.name, str(e).strip()))
                        else:
                            print("  already downloaded {file_name}".format(file_name=file_name))
    except Exception as e:
        print("    *** Error: %s ***" % (str(e).strip()))


def save_xml(bucket, key_name):
    """Add the given bucket page's XML to the XML output file"""
    #Create the directory if it doesn't exist
    if not os.path.exists(bucket.output_folder):
        os.makedirs(bucket.output_folder)

    """Save the XML (e.g. page source code) for the bucket"""
    f = open(bucket.xml_output_file.replace(".xml",".txt"), "a+")
    try:
        f.write('''%s\n''' % (key_name))
    except:
        f.write('''%s\n''' % (key_name.strip()))
        f.write('''%s\n''' % (key_name.strip()))
        f.close()
