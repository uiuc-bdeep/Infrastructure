#!/usr/bin/env bash
set -e

BASE=/usr/local/bdeep/Infrastructure

pushd $BASE

eval $(ssh-agent -s)
ssh-add /home/admin/.ssh/id_rsa

git pull

git submodule update --recursive --remote

git add projects/
git commit -m 'updating submodules'
git push origin master

popd
