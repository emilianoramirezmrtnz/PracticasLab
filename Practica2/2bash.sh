#!/bin/bash

function contar {

while [ $limite -gt $i ]
do
     echo $i
    if [ $i%2==0 ]
    then
    echo $i " es impar"
    fi
    let i=$i+1
done
}

i=0
limite=$1
contar