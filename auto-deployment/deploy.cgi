#!/bin/bash

echo "Content-type: text/html"
echo ""

echo '<html>'
echo '<head>'
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
echo '<title> Deployment </title>'
echo '</head>'
echo '<body>'




# source /home/ubuntu/.profile

## SX API/HQ

##################
# app_name=admin
# repo_name=sx-admin
# branch_name=dev
# static_repo=sx-static
# static_branch_name=master
##################

# echo '-----------------------------------'
# echo 'pulling static updates'
# cd /home/ubuntu/$static_repo
# # git reset --hard
# # git checkout -f $static_branch_name
# git pull

# echo '-----------------------------------'
# echo 'pulling application updates'
# cd /home/ubuntu/$repo_name
# # git reset --hard
# # git checkout -f $branch_name
# git pull

# echo '-----------------------------------'
# echo 'installing NPM packages'
# /usr/local/bin/npm install

# echo '-----------------------------------'
# echo $(git log -n 1)

# PM2_HOME='/home/ubuntu/.pm2' pm2 restart $app_name --update-env
# echo '-----------------------------------'
# sleep 3
# /usr/local/bin/pm2 log $app_name --nostream
# echo '-----------------------------------'



##################
repo_path=sx-app
# repo_path=im_warehouse/client
build_path=sx-app-build
# build_path=warehouse-app-build
branch_name=dev
##################


## SX-APP

echo '-----------------------------------'
cd /home/ubuntu/$repo_path
git reset --hard
git checkout -f $branch_name
echo 'pulling application'
git pull

echo '-----------------------------------'
echo 'installing packages'
npm install
echo '-----------------------------------'
echo 'building app'
npm run build

echo '-----------------------------------'
rm -rf /home/ubuntu/$build_path
cp -r /home/ubuntu/$repo_path/dist /home/ubuntu/$build_path





echo '</body>'
echo '</html>'

exit 0