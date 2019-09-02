# Purpose
Provide a command line ability to download some, or all, of the public/authorized users files in an AWS S3 bucket as well as all of the XML that lists its contents, whether the key is public or not.

# Reason
As I was going through, looking for public AWS S3 buckets that contained PII, I realized that I wanted to be able to download the XML and a subset of data to show companies what data they had exposed.  I didn't want to do this manually and I wanted to be able to have ALL of the XML (AWS paginates S3 content per 1k keys).

# Use
Just get the XML, downloaded to the working directory under a the subfolder [bucket_name]<br>
./download_bucket.py -n [bucket_name] -x

Download the whole bucket to /home/foo/bar/[bucket_name]<br>
./download_bucket.py -o /home/foo/bar -n [bucket_name] -d

Download only where "test" is in the key and get all of the XML<br>
./download_bucket.py -n [bucket_name] -d -x -i test

Download where "test" is in the key but "exclude me" is not in the key<br>
./download_bucket.py -n [bucket_name] -d -i test -e "exclude me"

Download everything starting after thisfile.txt on public readable downloads, e.g. if you don't want to paginate through again<br>
./download_bucket.py -n [bucket_name] -d --last_key "thisfile.txt"

Download using an API key (e.g. for buckets that allow any authenticated user to access it)
./download_bucket.py -n [bucket_name] -d -ak "AWS_ACCESS_KEY" -sk "AWS_SECRET_KEY"


# Notes
- If a file is private, the download will be the XML saying that file access is denies
- Some keys are just folder names, these will not be downloaded but the keys within the bucket will (e.g. a key could be "folder/" but there will be keys with content like "folder/file1")
- You can add multiple "-i" or "-e" parameters.  Each set of "-i" and "-e" parameters will be OR'd and the "-i" and "-e" parameters are AND'd together.  These are case insensitive
