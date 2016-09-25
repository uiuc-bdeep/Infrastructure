#!/usr/bin/env bash
set -e

source vars.sh

cat $SCHEMES/{once,weekly,monthly} > $EXCLUDE

tar -X $EXCLUDE -czf $BACKUP/share.daily.tar.gz $SHARE
/usr/local/bin/aws s3 cp $BACKUP/share.daily.tar.gz $BUCKET
