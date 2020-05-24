#!/bin/sh

set -e

cd linux-source-5.4
make bindeb-pkg -j

cd ../custom_module
make src -j

cd ..
