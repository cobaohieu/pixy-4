#!/usr/bin/env bash

pip install -r deploy-requirements.txt;

make -f Makefile.targets lint;
status=$?
if [ $status != 0 ]; then exit $status; fi

make -f Makefile.targets test-unit;
status=$?
if [ $status != 0 ]; then exit $status; fi
