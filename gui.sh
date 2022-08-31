#!/bin/bash

if [ ! -d "./node_modules/" ] 
then
    yarnpkg install
fi

yarnpkg run serve