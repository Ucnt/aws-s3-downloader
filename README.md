# Purpose
Provide a command line ability to download some, or all, of the public keys in an AWS S3 bucket as well as all of the XML that lists its contents, whether the key is public or not.

# Reason
As I was going through, looking for public AWS S3 buckets that contained PII, I realized that I wanted to be able to download the XML and a subset of data to show companies what data they had exposed.  I didn't want to do this manually and I wanted to be able to have ALL of the XML (AWS paginates S3 content per 1k keys).

# Use
Just get the XML<br>
./download_bucket.py -o /home/foo/bar -n [bucket_name] -x

Download the whole bucket<br>
./download_bucket.py -o /home/foo/bar -n [bucket_name] -d

Download only where "test" is in the key and get all of the XML<br>
./download_bucket.py -o /home/foo/bar -n [bucket_name] -d -x -i test

Download where "test" is in the key but "exclude me" is not in the key<br>
./download_bucket.py -o /home/foo/bar -n [bucket_name] -d -i test -e "exclude me"

# Notes
- The content will be downloaded to /home/foo/bar/[bucket_name]
- If a file is private, the download will be the XML saying that the file is private
- Some keys are just folder names, these will not be downloaded but the keys within the bucket will (e.g. a key could be "folder/" but there will be keys with content like "folder/file1")

