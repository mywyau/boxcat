#!/bin/bash

# Check if the version argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <new_version>"
    exit 1
fi

# Assign the first argument to the new_version variable
new_version=$1

# Use sed to update the version in pyproject.toml
sed -i "s/^version = \".*\"$/version = \"$new_version\"/" setup.py

echo "Version updated to $new_version in setup.py"

sed -i "s/^version = \".*\"$/version = \"$new_version\"/" pyproject.toml

echo "Version updated to $new_version in pyproject.toml"