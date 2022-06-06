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

# app_name=api
# repo_name=sellerapi
# branch_name=dev

# echo '-----------------------------------'
# echo 'pulling static updates'
# cd /home/ubuntu/sx-static
# # git reset --hard
# # git checkout -f dev
# git pull

# echo '-----------------------------------'
# echo 'pulling application updates'
# cd /home/ubuntu/sx-$repo_name
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





## SX-APP

echo '-----------------------------------'
cd /home/ubuntu/sx-app
git reset --hard
git checkout -f dev
echo 'pulling application'
git pull

echo '-----------------------------------'
echo 'installing packages'

npm install
npm run build

echo '-----------------------------------'
rm -rf /home/ubuntu/sx-app-build
cp -r /home/ubuntu/sx-app/dist /home/ubuntu/sx-app-build





echo '</body>'
echo '</html>'

exit 0