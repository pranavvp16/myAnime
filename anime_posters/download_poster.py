import urllib.request
import pickle as pkl

image = pkl.load(open('image_urls.pkl','rb'))
index_no = 0
for i in image:
  name = str(index_no)+'.jpg'
  url=i
  urllib.request.urlretrieve(url,name)
  index_no += 1