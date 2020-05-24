#!/bin/sh

set -e

cd linux-source-5.4
make -j 2 bindeb-pkg

cd ../custom_module
make -j 2 src

cd ..
