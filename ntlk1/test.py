import nltk
from nltk.corpus import brown
import matplotlib.pyplot as plt

nltk.download('brown')

cfd = nltk.ConditionalFreqDist((genre, word)
                               for genre in brown.categories()
                               for word in brown.words(categories = genre))
genre = ['news', 'romance']
modals = ['can','could','may','might','must','will','would']
cfd.tabulate(conditions=genre, samples=modals)
cfd.plot(conditions=genre, samples=modals)
plt.show()