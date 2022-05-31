#!/bin/bash

echo "Content-type: text/html"
echo ""

echo '<html>'
echo '<head>'
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
echo '<title>Staging SellerAPI Deployment</title>'
echo '</head>'
echo '<body>'

# cd /home/ubuntu/sx-static
# git reset --hard
# git checkout -f dev
# git pull

# cd /home/ubuntu/sx-sellerapi
# git reset --hard
# git checkout -f dev
# git pull


# cd /home/ubuntu/sx-sellerapi
# git reset --hard
# git checkout -f dev
# git pull

# echo $(git log -n 1)

# source /home/ubuntu/.profile

# PM2_HOME='/home/ubuntu/.pm2' pm2 restart sellerApi --update-env

# sleep 3

# /usr/local/bin/pm2 log sellerApi --nostream

echo '</body>'
echo '</html>'

exit 0