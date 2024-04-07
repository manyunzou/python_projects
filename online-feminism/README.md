# How I analyze Zhihu word entry history

This folder hosts analysis code and data behind my story "[China's 3,500-Post Edit War Over Feminism] (https://www.sixthtone.com/news/1007168)".

The story was originally published in The Paper 澎湃新闻 on March 8, 2021, "[3522条修改记录看近十年女性主义话题之争](https://www.thepaper.cn/newsDetail_forward_11607122)".

## Data
The data used in this story came from the edit history of the topic "feminism" and its related word entries from [Zhihu] (https://www.zhihu.com/topic/19552985/hot), a Quora-type question and answer site in China. As of April 2024, it seems like the edit history log is not accessible anymore,

## Analysis Code
The analysis contains the following steps:
- Understand data
- Data preparation, such as formatting date, categorizing "main topic" and "sub-topic", and identifying "add" and "subtract" actions
- Descriptional data analysis, such as how many topics are there, what the editing frequency of each topic is, when the editing happens, etc. Filtering out key topics based on the frequency. 
- Data visualization, drafting the viz based on the time series data.

The Python packages used in the notebook:
- pandas
- NumPy
- pickle
- datatime
- re