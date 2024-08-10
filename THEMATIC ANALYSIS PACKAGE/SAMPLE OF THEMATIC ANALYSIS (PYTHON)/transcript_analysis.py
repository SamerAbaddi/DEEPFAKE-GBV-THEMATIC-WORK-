# This script performs thematic analysis on a given transcript text
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import defaultdict
import matplotlib.pyplot as plt
import networkx as nx

nltk.download('punkt')
nltk.download('stopwords')

text = '''
Thank you for agreeing to share your story with us. Can you start by telling us a bit about yourself and your background?
Of course. My name is X, and I�m a 28-year-old fashion model and influencer based in Jordan. I�ve been in the fashion industry for about six years now (since university), and I have a significant online presence, with thousands of followers on social media, mostly Instagram. My work involves a lot of public appearances, photoshoots, and collaborations with brands.
Thank you, X. Can you describe the incident involving DeepFakes and how it all started?
It all began about a year ago. I started receiving strange messages from people I didn�t know, asking about explicit videos and photos of me. At first, I was confused and thought it was just some kind of prank. But then, a friend sent me a link to a video that was circulating online. It was a DeepFake video that showed me in a compromising and explicit situation. The video looked so real that even I was shocked.
That sounds incredibly distressing. How did you react when you saw the video?
I was devastated. I felt violated and helpless. It was like my worst nightmare had come true. I couldn�t believe that someone would go to such lengths to create something so damaging. The video spread quickly, and soon, it felt like everyone had seen it. I started receiving hateful comments and messages, and my reputation took a massive hit. At that time, I realized that every post, every video is a potential weapon in the hands of those who wish to extort us.
How did this incident affect your professional life?
The impact on my professional life was severe. Brands and clients started distancing themselves from me. I lost several contracts and collaborations because they didn�t want to be associated with the scandal. My follower count dropped, and my income took a significant hit. It felt like everything I had worked so hard for was crumbling before my eyes.
That must have been incredibly challenging. How did this experience affect you emotionally and psychologically?
The emotional and psychological toll was immense. I started experiencing severe anxiety and depression. I couldn�t sleep, and I was constantly on edge, fearing that more fake content would surface. I felt isolated and ashamed, even though I knew I hadn�t done anything wrong. I withdrew from social media and public life for a while because I couldn�t handle the scrutiny.
'''

print('A Sample of Thematic analysis completed.')
