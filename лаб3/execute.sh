#!/bin/bash
#В начале заполните директории с текстами текстами (заполните)(директории)
#python3 text_maker.py two/text1.txt > two/text2.txt
#python3 word_maker.py three/text1.txt three/text1.txt > three/text2.txt 
#python3 text_maker.py 1000 > four/text1.txt 
#python3 text_maker.py four/text1.txt > four/text2.txt
#python3 word_maker.py five/text0.txt 150 > five/text1.txt 
#python3 word_maker.py five/text0.txt 150 > five/text2.txt


for dir in one two three four five; do
    echo "=== $dir/text1.txt $dir/text2.txt ==="
    python3 main.py $dir/text1.txt $dir/text2.txt #-v
done
