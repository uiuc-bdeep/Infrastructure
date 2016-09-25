#!/usr/bin/env bash
set -e

source vars.sh

cat $SCHEMES/{once,monthly} > $EXCLUDE

tar -X $EXCLUDE -czf $BACKUP/share.weekly.tar.gz $SHARE
/usr/local/bin/aws s3 cp $BACKUP/share.weekly.tar.gz $BUCKET
