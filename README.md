
# bnltk-enhanced
[![Build Status](https://travis-ci.org/eventuo/bnltk-enhanced.svg?branch=master)](https://travis-ci.org/eventuo/bnltk-enhanced)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)

bnltk-enhanced (Bangla Natural Language Processing Toolkit) is an open-source python package for Bengali Natural Language Processing. It includes modules for Tokenization, Stemming, and Parts of speech tagging. We're eagerly looking forward to receiving valuable contributions to make this project even better.

## Installation

pip install bnltk-enhanced 

## Usage

### Tokenizer

```
from bnltk.tokenize import Tokenizers
t = Tokenizers()
print(t.bn_word_tokenizer(' আমার সোনার বাংলা । '))
```

### Stemmer

```
from bnltk.stemmer import BanglaStemmer
bn_stemmer = BanglaStemmer()
print(bn_stemmer.stem('খেয়েছিলো'))
```

### Parts of Tagger

For using the Parts of Tagger you need to download some data files as follows:

```
from bnltk.bnltk_downloads import DataFiles
DataFiles().download()
```
After successfully downloading the files, then you can use this module.

```
from bnltk.pos_tagger import PosTagger

p_tagger = PosTagger()
p_tagger.loader()
sentences = 'দুশ্চিন্তার কোন কারণই নাই'
print(p_tagger.tagger(sentences))
```