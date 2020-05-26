#!/bin/sh


ls /tmp/dist

apt update
apt install -y -qq --no-install-recommends /tmp/dist/tpls_*deb

echo "FINISHED INSTALLING TPLS!"


exec ${@}
