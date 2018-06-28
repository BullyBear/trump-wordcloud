from wordcloud import WordCloud
import matplotlib
matplotlib.use('TkAgg')

data = open('trump.txt').read()

wordcloud = WordCloud().generate(data) 

import matplotlib.pyplot as plt 
wordcloud = WordCloud(max_font_size=40).generate(data)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

image = wordcloud.to_image()
image.show()

