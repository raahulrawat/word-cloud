import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

""" entities here is the list of important words which we want to include in the word cloud visualization. e.g. These can be generated using NER extraction"""
entities = ['Pakistan', 'India', 'Abhinandan', 'IAF', 'Airstrike', 'Kargil']

stopwords = set(STOPWORDS)
wordcloud = WordCloud(width = 1500, height = 1000, 
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 10).generate("+".join(entities)) 
  
# plot the WordCloud image                        
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show()
