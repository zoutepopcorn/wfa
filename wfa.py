#!/usr/bin/python3
#
# wfa
# word frequency analysis with top x frequencies
# version 20170217_121704
# (c) 2017 by cytopyge
#

import re
import string
frequency = {}
results = []

infile = '/home/user/Desktop/test.txt'
with open(infile, 'r') as handle:
  content = handle.read().lower()

match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)

for word in match_pattern:
  count = frequency.get(word,0)
  frequency[word] = count + 1

frequency_list = frequency.keys()

for word in frequency_list:
  tuple = (word, frequency[word])
  results.append(tuple)

byFreq=sorted(results, key=lambda word: word[1], reverse=True)

for (word, freq) in byFreq[:20]:
  print (word, freq)
