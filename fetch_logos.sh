#!/bin/sh
# Downloads the official DAO logo files from the Task Board brand kit.
set -e
mkdir -p assets
curl -fsSL -o assets/dao-logo-on-dark.png  https://taskboard.redbellydao.network/brand/dao-logo-on-dark.png
curl -fsSL -o assets/dao-logo-on-light.png https://taskboard.redbellydao.network/brand/dao-logo-on-light.png
ls -l assets/dao-logo-on-*.png
