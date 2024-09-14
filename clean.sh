#!/bin/bash

cd $PWD/utils
find . -type d -name "__pycache__" -exec rm -rf {} +
cd ..
cd $PWD/train_test
find . -type d -name "__pycache__" -exec rm -rf {} +
cd ..
cd $PWD/preprocessing
find . -type d -name "__pycache__" -exec rm -rf {} +
cd ..
cd $PWD/pipeline
find . -type d -name "__pycache__" -exec rm -rf {} +
cd ..
cd $PWD/implementations
find . -type d -name "__pycache__" -exec rm -rf {} +
cd ..
cd $PWD/headers
find . -type d -name "__pycache__" -exec rm -rf {} +
cd ..

