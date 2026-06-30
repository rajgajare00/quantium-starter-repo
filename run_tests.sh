#!/bin/bash

echo "Running test suite..."

pytest test_app.py

if [ $? -eq 0 ]; then
    echo "All tests passed!"
    exit 0
else
    echo "Tests failed!"
    exit 1
fi