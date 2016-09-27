#!/usr/bin/env bash
set -e

BASE=/usr/local/bdeep/Infrastructure

pushd $BASE

eval $(ssh-agent -s)
ssh-add /home/admin/.ssh/id_rsa

git pull

popd
