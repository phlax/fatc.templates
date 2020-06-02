#!/bin/sh


ls /tmp/dist

apt update
apt install -y -qq --no-install-recommends gpg gpg-agent ca-certificates software-properties-common wget
wget -qO - https://phlax.github.io/debian/gpg | apt-key add -
apt-add-repository "deb [arch=amd64] https://phlax.github.io/debian buster main"
apt update
apt install -y -qq --no-install-recommends /tmp/dist/tpls_*deb
echo "FINISHED INSTALLING TPLS!"

exec ${@}
