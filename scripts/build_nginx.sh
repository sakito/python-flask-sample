#!/usr/bin/env bash

var_info="1.27.3"

cd var/tmp;
wget https://github.com/nginx/nginx/releases/download/release-${var_info}/nginx-${var_info}.tar.gz;
tar xvf nginx-${var_info}.tar.gz;
cd nginx-${var_info};
./configure \
    --prefix=${HOME}/opt/nginx/${var_info} \
    --conf-path=${HOME}/opt/nginx/${var_info}/conf/nginx.conf \
    --error-log-path=${HOME}/opt/nginx/${var_info}/var/log/nginx-error.log \
    --http-log-path=${HOME}/opt/nginx/${var_info}/var/log/nginx-access.log \
    --pid-path=${HOME}/opt/nginx/${var_info}/var/run/nginx.pid \
    --lock-path=${HOME}/opt/nginx/${var_info}/var/lock/nginx.lock \
    --with-debug \
    --with-threads \
    --with-http_ssl_module \
    --with-http_gzip_static_module \
    --with-http_stub_status_module \
    --with-pcre-jit \
    --with-http_v2_module;
make;
make install;
#setcap cap_net_bind_service=ep ${HOME}/opt/nginx/sbin/nginx;
