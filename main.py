import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


if __name__ == '__main__':
    '''Sentiment analysis on the reviews of various businesses
    '''
    analyzer = SentimentIntensityAnalyzer()

    review_ross = "Tiny store that is poorly set up/out. Musty and has a thrift store vibe to it. However if you're patient and prepared to take some time , there are bargains to be found. The parking lot is really busy so be alert to avoid a driver who is thinking only about shopping. It's right next door to Sprouts and there are plenty of places to eat locally.Not my favorite Ross, it's kinda dark and didn't have the best selection but I got a steal on designer underwear. But then again, no one will ever know :)"
    print(review_ross + ":" + str(analyzer.polarity_scores(review_ross)))
    # {'neg': 0.106, 'neu': 0.805, 'pos': 0.089, 'compound': -0.4009}
    review_sagarexclusive = "Varsha and Ruben were both fantastic and extremely helpful! They helped me find the most beautiful Kanjeevaram Sari! As an outsider to Hindu weddings/ceremony they provided a lot of guidance about proper attire the event and colors to wear. I will be returning for alterations and wedding jewelry! I said, Yes to the dress (sari)!!"
    print(review_sagarexclusive + ":" + str(analyzer.polarity_scores(review_sagarexclusive)))
    # {'neg': 0.0, 'neu': 0.765, 'pos': 0.235, 'compound': 0.9408}

    review_forever21 = "This poor rating is for the closing cashier on 12/12/17. The big, busty and RUDE cashier was showing so much attitude to my aunt who wanted me to grab 1 more scarf off the floor. First of all, she didn't even greet my aunt, and could only talk to her coworker about how she can't even buy a $23 morphe palette without thinking twice about it. Then when I was checking out, she didn't speak one word to me and had the audacity to THROW my bag at me. Not to mention, she wasn't wearing a name tag so I couldn't even get her name.Tip to the supervisors or managers: emphasize customer service, what we saw tonight was extremely unacceptable and rude"
    print(review_forever21 + ":" + str(analyzer.polarity_scores(review_forever21)))
    # {'neg': 0.121, 'neu': 0.879, 'pos': 0.0, 'compound': -0.9366}

    review_forever21_2 = " I never find anything here!!!!! As frustrating as it may be, I can't get myself to bypass this establishment whenever I'm in the area.....First off, this Forever 21 location is always a disaster. ALWAYS. There is no sense of organization or cleanliness whatsoever. Clothing is dangling off the hangers, being trampled on the floor, and everything is jumbled and smooshed together on racks making it extremely hard to find whatever you're looking for.Customer service [for the most part] is nonexistent so don't expect a hello , a smile, or even eye contactThe lines for the fitting rooms are endless so I don't even bother. I buy and hope for the bestThe line at the registers don't get any better-everyone seems to be working in slow-mo and you'd be lucky if there was more than 1 employee ringing up sales. I guess they'd rather have workers watch the sales floor?? This F21 deserves 1 star in my eyes"
    print(review_forever21_2 + ":" + str(analyzer.polarity_scores(review_forever21_2)))
    #{'neg': 0.091, 'neu': 0.86, 'pos': 0.05, 'compound': -0.7602}