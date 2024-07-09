#!/bin/bash

new_version="$1"

# Perform the version update using sed
sed -i.bak "s/version *= *\"[^\"]*\"/version = \"$new_version\"/" "pyproject.toml"

echo "Version updated to $new_version in pyproject.toml"
