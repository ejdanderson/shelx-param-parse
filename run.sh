#!/bin/bash

declare -A spp_in_out

spp_in_out=([data/washpass.lst]=data/washpass.csv [data/wcx5.lst]=data/wcx5.csv [data/wcx7.lst]=data/wcx7.csv [data/g5.lst]=data/g5.csv [data/rs104.lst]=data/rs104.csv)

for i  in "${!spp_in_out[@]}"; do
  echo "$i"
  python spp.py "$i" "${spp_in_out[$i]}"
done
