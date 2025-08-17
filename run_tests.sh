#!/bin/bash
#
# A simple script to run all tests for the Conscience Agent.

echo "Running tests..."
python3 -m unittest discover tests
