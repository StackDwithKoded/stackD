#!/bin/bash

# This is my first shell script
# Written during Stackd with Koded — DevOps Track

echo "==============================="
echo "  Welcome to DevOps with Koded"
echo "==============================="

# Variables
name="Micah"
date_today=$(date)


echo "" 
echo "Hello, $name"
echo "Today is: $date_today"
echo ""

# A simple loop
echo "Counting to 5..."
for i in 1 2 3 4 5
do
  echo "  Count: $i"
done

echo ""

# A condition
if [ -f "hello.txt" ]; then
  echo "Found hello.txt in this directory"
else
  echo "hello.txt does not exist here"
fi

echo ""
echo "Script complete. You just automated something."