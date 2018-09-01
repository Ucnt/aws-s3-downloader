#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Bucket():
    def __init__ (self, bucket_name, url, download, download_include, download_exclude, get_xml, output_folder, aws_access_key, aws_secret_key, quiet, last_key):
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
        self.quiet = quiet
        self.last_key = last_key
        self.is_truncated = False
        self.num_keys = 0
