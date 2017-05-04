#! /bin/bash

###
# @author: Luis Esteban Rodríguez
# @enterprise: Labdi Inc.

echo ""
echo "    ### Startup script powered by LABDI INC. Technology ###"
echo ""
echo "*** Setting development environment..."
echo "*** Loading variables..."
export $(cat .env | xargs)
echo "*** Starting development server..."
echo ""
#python app.py
gunicorn -w4 app:app -b 0.0.0.0:8080
