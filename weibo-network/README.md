# How I construct a social network based on Weibo posts

This folder hosts analysis code and data behind one of my class projects, "How Chinese feminists advocate online: network analysis about the discussion of a landmark #MeToo case on Weibo". I selected the settlement of Liu Jingyao vs. Liu Qiangdong as the event to track online discussions on Weibo, resulting in a total of 499 reposts following 29 original posts under four trending hashtags.

## Analysis Code

The analysis code focuses mainly on building up a social network: 
- clean scraped data
- descriptive analysis
- analyze Weibo user profiles
- count text similarity
- build node list, edge list, and label list

The Python packages used in the notebook:
- re
- jieba
- pickle
- pandas
- NumPy
- sklearn.feature_extraction