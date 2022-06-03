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

## SX-API

# cd /home/ubuntu/sx-static
# git reset --hard
# git checkout -f dev
# git pull

# cd /home/ubuntu/sx-sellerapi
# git reset --hard
# git checkout -f dev
# git pull
# /usr/local/bin/npm install


# cd /home/ubuntu/sx-sellerapi
# git reset --hard
# git checkout -f dev
# git pull

# echo $(git log -n 1)

# PM2_HOME='/home/ubuntu/.pm2' pm2 restart sellerApi --update-env
# sleep 3
# /usr/local/bin/pm2 log sellerApi --nostream


## SX-APP

cd /home/ubuntu/sx-app
git reset --hard
git checkout -f dev
git pull

npm install
npm run build

rm -rf /home/ubuntu/sx-app-build
cp -r /home/ubuntu/sx-app/dist /home/ubuntu/sx-app-build

echo '</body>'
echo '</html>'

exit 0