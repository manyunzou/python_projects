# How I analyze Chinese song rhythms

This folder hosts analysis code and data behind my personal project "[如何写一首烂大街的华语歌](https://triviaonly.github.io/20201030.html)(How to write a Chinese song that sounds cliche)?" For this project, I analyzed the rhythms of 102,197 Chinese songs (thanks to the lyric dataset built by [dengxiuqi](https://github.com/dengxiuqi/ChineseLyrics)).

## Analysis Code

The analysis code focuses mainly on text mining: 
- Split strings
- Identify rhythms
- Count the frequency of the rhythms
- Combine the words with the same rhythms

The Python packages used in the notebook:
- json
- pandas
- NumPy
- Pinyin
- re