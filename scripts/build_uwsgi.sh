#!/usr/bin/env bash

cd var/tmp;
wget https://github.com/unbit/uwsgi/archive/refs/tags/2.0.28.tar.gz;
tar xvf 2.0.28.tar.gz;
cd uwsgi-2.0.28;
python3 uwsgiconfig.py --build;
mkdir -p ~/opt/uwsgi/bin;
cp uwsgi ~/opt/uwsgi/bin;
