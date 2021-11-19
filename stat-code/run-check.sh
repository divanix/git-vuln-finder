#! /usr/bin bash
ROOT=/mnt/drive/actions-repos
cd $ROOT
for d in *; do
    echo $d
    git-vuln-finder -r $ROOT/$d -odir /mnt/drive/git-vulns
    #exit 0
done
