#!/bin/bash
if [ $# -ne 2 ]
then
  echo "Usage: ./getlumi_fromforest.sh <input-list> <outputfile>"
  exit 1
fi

rm $2
max=`wc -l $1 | awk '{print $1}'`
num=0
for f in `cat $1`
  do echo $num/$max ; num=$((num+1))
  echo 'TFile*f=TFile::Open("'"$f"'");f->cd("hiEvtAnalyzer");HiTree->Scan("run:lumi");gSystem->Exit()' | root -b 2 &> out.txt
  cat out.txt | grep "*   " | grep -v "continue or q to" | awk '{print $4" "$6}' |grep -v "run lumi" | grep -v "L O" |grep -v "*" | sort | uniq >> $2
done

#check if the first line is empty and remove it
if [ -z `head -n1 $2` ] ; then
  tail -n +2 $2 > tmp_$2
  mv tmp_$2 $2
fi