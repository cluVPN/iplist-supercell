#!/bin/bash

aria2c -o supercell --allow-overwrite \
  'https://raw.githubusercontent.com/cluVPN/rule-set/refs/heads/main/supercell'

echo "$(grep -oP '^([\w\d.-]+\.)+([\w\d.-]+)?' supercell)" > supercell

parallel -P "$(nproc)" -j0 -a supercell '\
line="{}"
dig +short A $line | grep -v "\.$" >> ipv4_list.txt
dig +short AAAA $line | grep -v "\.$" >> ipv6_list.txt
echo "dig complete for $line ..."
'

sort -u -t . -k 1,1n -k 2,2n -k 3,3n -k 4,4n ipv4_list.txt -o ipv4_list.txt
sort -u ipv6_list.txt -o ipv6_list.txt # for now
