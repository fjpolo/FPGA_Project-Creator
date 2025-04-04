#!/bin/bash

exec 2>&1
set -ex

## create the mutated design
bash $SCRIPTS/create_mutated_eq.sh -c -o mutated.il

## run formal property check
ln -s ../../test_eq.v ../../test_eq.sby .
sby -f test_eq.sby

## obtain result
gawk "{ print 1, \$1; }" test_eq/status >> output.txt

exit 0
