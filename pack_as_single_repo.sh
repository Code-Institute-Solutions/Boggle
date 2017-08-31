#!/bin/bash

new_repo_name=single_repo

rm -rf $new_repo_name
mkdir $new_repo_name
cd $new_repo_name

git init

for phase in 01-getting-started 02-optimising; do
    rm -rf *
    cp -r ../$phase/* .
    git add .
    git commit -m $phase
    git tag $phase
done