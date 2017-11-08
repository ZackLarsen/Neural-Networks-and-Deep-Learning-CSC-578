#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 12:37:40 2017

@author: zacklarsen
"""

import nltk
from nltk.corpus import shakespeare
print(nltk.corpus.gutenberg.fileids())

emma = nltk.corpus.gutenberg.words('austen-emma.txt')
print (len(emma))
hamlet = nltk.corpus.gutenberg.words('shakespeare-hamlet.txt')
print(len(hamlet))
bible = nltk.corpus.gutenberg.words('bible-kjv.txt')
print(len(bible))
sense = nltk.corpus.gutenberg.words('austen-sense.txt')
print(len(sense))


print(emma[:50])








from xml.etree import ElementTree
shakespeare.fileids() # doctest: +ELLIPSIS
play = shakespeare.xml('dream.xml')
print(play) # doctest: +ELLIPSIS
print('%s: %s' % (play[0].tag, play[0].text))
personae = [persona.text for persona in play.findall('PERSONAE/PERSONA')]
print(personae) # doctest: +ELLIPSIS


# Find and print speakers not listed as personae
names = [persona.split(',')[0] for persona in personae]


speakers = set(speaker.text for speaker in play.findall('*/*/*/SPEAKER'))

print(sorted(speakers.difference(names))) # doctest: +NORMALIZE_WHITESPACE































