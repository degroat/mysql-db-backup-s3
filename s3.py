import boto
import boto.s3.connection
from boto.s3.key import Key
import os
import time
import datetime
from config import *

conn = boto.connect_s3(
        aws_access_key_id = key_id,
        aws_secret_access_key = sec_key,
        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
        )

bucket = conn.get_bucket(bucket_name)

def backup():
	"""
	Backup Database
	"""
	username = db_user
	password = db_pass
	database = db_name
	date = time.strftime('%Y-%m-%d')
	filename = 'backup/%s.sql.gz' % (date)
	os.popen("mysqldump -u%s -p%s -h %s -d %s | gzip -c > %s" % (username, password, hostname, database, filename))
	upload = Key(bucket)
	upload.key = "%s.sql.gz" % (date)
	upload.set_contents_from_filename(filename)
	print "uploading Backup File %s" % (upload.key)
	os.remove(filename)
	checkdate = datetime.date.today()-datetime.timedelta(30)
	for key in bucket:
		if key.name == '%s.sql.gz' % (checkdate):
			print "Deleting 30 Days Old Backup File %s" % (key.name)
			bucket.delete_key(key.name)
	print "----------------------------------------------------------------------------"

if __name__ == '__main__':
	backup()


