#!/usr/bin/env bash
set -e

source vars.sh

cat $SCHEMES/{once} > $EXCLUDE

tar -X $EXCLUDE -czf $BACKUP/share.monthly.tar.gz $SHARE
/usr/local/bin/aws s3 cp $BACKUP/share.monthly.tar.gz $BUCKET
