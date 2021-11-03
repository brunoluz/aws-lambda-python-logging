#!/bin/bash
rm -f my-deployment-package.zip
cd venv/lib/python3.9/site-packages/
zip -r ../../../../my-deployment-package.zip .
cd ../../../../
zip -g my-deployment-package.zip *.py
zip -g my-deployment-package.zip *.txt

