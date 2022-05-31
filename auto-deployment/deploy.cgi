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

# cd /home/ubuntu/sx-app
# git reset --hard
# git checkout -f dev
# git pull

# cd /home/ubuntu/sx-app

# /usr/local/bin/npm install
# /usr/local/bin/npm run build

# cp -r /home/ubuntu/slv/app/dist /home/ubuntu/

echo '</body>'
echo '</html>'

exit 0