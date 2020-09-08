
### Download & build KenLM (C++ binary), install python module
 * [https://github.com/kpu/kenlm](https://github.com/kpu/kenlm)
	
	```
	mkdir -p build
	cd build
	cmake ..
	make -j 4
	```
 * `pip install https://github.com/kpu/kenlm/archive/master.zip`


### Create a basic text language model (LM)
 * [Download](https://github.com/kmario23/KenLM-training) some random English text &rarr; `$ wget -c https://github.com/vchahun/notes/raw/data/bible/bible.en.txt.bz2
`

 * Train LM &rarr; `bzcat bible.en.txt.bz2 | python preprocess.py | bin/lmplz -o 5 > bible.arpa`

 
### Use LM to predict perplexity of individual sentences
 * Use custom `score_vtt` file to process a VTT file and emit a score &rarr; `python score_vtt.py`
 
 
### Use FastText to predict the language class of individual sentences
 * [Install](https://amitness.com/2019/07/identify-text-language-python) library `pip install fasttext`

 * Download pretrained model &rarr; `wget -O /tmp/lid.176.bin https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin`

 * 


 