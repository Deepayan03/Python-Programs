def findfreq(s):
    count=1
    words=s.split();
    for word in words:
        for i in range(words.index(word)+1,len(words)-words.index(word)):
            if(word==words[i]):
                count+=1;
        print(word+"------>  "+str(count));
        count=1

findfreq("I am a good boy I")