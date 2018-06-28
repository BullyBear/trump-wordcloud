import matplotlib
matplotlib.use('TkAgg')
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__)

text = open(path.join(d, 'trump.txt')).read()

trump_mask = np.array(Image.open(path.join(d, "trump.png")))


wc = WordCloud(background_color="white", max_words=2000, mask=trump_mask)
               
wc.generate(text)

wc.to_file(path.join(d, "trump.png"))

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(trump_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()

