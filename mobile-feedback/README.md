# How I analyze 2G phone reviews from Taobao

This folder hosts code for analyzing and scraping, as well as data, behind my story "[10544条评论告诉你，不能扫码的老人机都是谁在买？](https://www.thepaper.cn/newsDetail_forward_8052386) Who is purchasing 2G mobile phones?" 

## Data & Scraper

The data used in this story was scraped from Taobao, one of China's largest online shopping platforms. You can find the web scraper at `tianmao.py`, which helped me gather review comments, review time, and review products from the website.

## Analysis Code

The analysis mainly focuses on text analysis and mining.
- Text frequency
- Word co-occurrence
- Text sentiment analysis

The Python packages used in the notebook:
- pandas
- NumPy
- re
- jieba
- collections
- matplotlib
- requests
- bs4
- json
- csv
- time