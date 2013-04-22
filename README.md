Backup Mysql Database to Amazon S3

This is python script to backup mysql database to amazon s3 using python boto. This script will backup database
configured in config.py & uploaded to amazon s3, after uploading database it will check for 30 days old backup 
file & remove it.

Requirments:

python 2.7
python boto (Python interface to Amazon Web Services)

How to use:

Edit config.py & add following parameters:

key_id='AWS_ACCESS_KEY_ID'

sec_key='AWS_SECRET_ACCESS_KEY'

bucket_name='s3 bucket name'

db_user='database user'

db_pass='database password'

db_name='database name'

hostname='hostname or IP'


How to run script:

python s3.py


