#!/bin/bash

# Check dependencies
# check whether Python is installed
which python
if [ $? -eq 1 ]
  then
    # Install Python
    sudo apt install python
  else
    echo
    echo It seems that Python is already installed
    echo
fi


# check whether Pip is installed
which pip
if [ $? -eq 1 ]
  then
    # Install Pip
    sudo apt install pip
  else
    echo
    echo It seems that Pip is already installed
    echo
fi


# check whether Feedparser in Pip is installed
pip show feedparser
if [ $? -eq 1 ]
  then
    # Install Pip
    pip install feedparser
  else
    echo
    echo It seems that Feedparser is already installed
    echo
fi

echo If you dont get any error, you can run now the Unsplash_loader.py Scripts!
read -p "Press any key to continue... " -n1 -s