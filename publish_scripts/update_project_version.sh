#!/bin/bash

# Check if two arguments are provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 new_version"
    exit 1
fi

new_version="$1"

./update_pyproject_toml.sh $1

./update_setup_py_file.sh $1

# clean up .bak files
rm ../pyproject.toml.bak
rm ../setup.py.bak

python setup.py sdist bdist_wheel
twine upload dist/*
