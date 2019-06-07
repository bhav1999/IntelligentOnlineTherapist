import speech_recognition as sr;
from textblob import TextBlob;

analysis = TextBlob("I hate you")
# set sentiment
print(analysis.sentiment.polarity)
if analysis.sentiment.polarity > 0:
    print('Positive')
elif analysis.sentiment.polarity == 0:
    print( 'neutral')
else:
    print( 'negative')