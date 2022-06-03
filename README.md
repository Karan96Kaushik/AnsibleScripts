# sx-ansible-playbook

## Overview
### Execution
1. hosts need to be setup in the `host` file & `.ssh/config`
1. run using the following command `ansible-playbook -i hosts bare-metal-setup.yml -vv`

## Bare metal setup
1. Install Git
1. Install NPM
1. Install N (version manager)
1. Install NodeJS
1. Install ZSH
1. Install Oh-my-zsh

## Application setup - API
1. Install PM2
1. Copies SSH Keys
1. Copies Env vars
1. Copies AWS Credentials
1. Clones API
1. Installs npm packages
1. Starts applications using PM2
1. Runs wget /ping test on localhost

## Application setup - APP
1. Install & setup NGINX (serving path root as /home/ubuntu/sx-app-build)
1. Copies SSH Keys
1. Clones APP
1. Copies .env file to sx-app directory
1. Installs npm packages
1. Builds and copies app files to sx-app-build directory
1. Runs wget /index.html test on localhost

## Env Update - API
1. Copies Env vars (.profile) to server
1. Update single env var in .profile on the server - Optional
1. Source .profile & restart api
1. Runs wget /ping test on localhost
