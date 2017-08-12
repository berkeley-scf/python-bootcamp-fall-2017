---
title: Python bootcamp project 
...

Background
============

The file **fetch_senator_tweets.py** downloads tweets using the Python twitter package to interact with Twitter's API. You will only be able to run that code if you set up your own Twitter account and follow the instructions at the start of the file regarding filling in the authentication information (CONSUMER_KEY, CONSUMER_SECRET, etc.).

I've already run the code and downloaded the data for you.  The downloaded information on the senators' twitter accounts is in *senators-list.json*, while the downloaded tweets are in *timelines.json*. Note that there are only 200 tweets for each senator because of limits on how many tweets can be accessed in a given request. *timelines.json* is too big to put in the Github repository. You can find it at <http://www.stat.berkeley.edu/~paciorek/transfer/timelines.json>.

Questions
===========

1. Load the *senators-list.json* and *timelines.json* files as objects called *senators* and *timelines*.

2. What type of datastructure is *timelines*? How many timelines are there? What does each timeline correspond to?

3. Make a list of the number of followers each senator has.

4. What is the screen name of the senator with the largest number of followers.

5. Make a list of lists where the outer list represents senators and the inner list contains the text of each senator's tweets, and call it *tweets*.

6. Write a function, called *remove_punct*, that takes a word and returns the word with all punctuation characters removed, except for those that occur within a word.

7. Write a function that takes tweet and returns a cleaned up version of the tweet. Here is an example function to get you started:

    ``` {.sourceCode .bash}
    def clean(tweet):
        cleaned_words = [word.lower() for word in tweet.split() if
                     'http' not in word and
                     word.isalpha() and
                     word != 'RT']
        return ' '.join(cleaned_words)
                                                                               
    clean(tweets[0][0])
    ```

    Note that the function I've provided is a bit buggy - it has some problems with some tweets. If your goal is to convert the tweet into a discrete set of words, what is going wrong here? Fix up and extend the example function.


8. Use the following file to create a list, called *stopwords*, that contains common english words.  <http://www.textfixer.com/resources/common-english-words.txt>.
Make sure to pull the data into Python by writing Python code to download and suck the data into Python.

9. Write a function, called *tokenize*, which takes a tweet, cleans it, and removes all punctuation and stopwords.

10. Create a list of lists, tweets_content, using your *tokenize* function.

11. Create a list, *tokens*, where all 200 of each senator's tweets are made into a single string.

12. Create a Pandas dataFrame with the following columns: senator name or handle, party of the senator, and number of times a prominent politician is mentioned in each senator's tweets. You might count the number of 'Obama', 'Trump', or 'Clinton' references.

    You can use this to create the party column (1=Republican, 0=Democratic):
    ``` {.sourceCode .bash}
    party = np.array([1,1,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,0,0,0,1,1,1,1,0,1,0,
    1,1,1,0,0,0,0,0,0,1,0,1,1,1,0,1,1,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0,1,
    1,0,0,0,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,1,1,0,0,1,0,1,0,0,1,1,1,0,1])
    ```

    That should correspond to the ordering in `timelines` but of course it would be more robust to create a dataFrame that has user names and party as columns and merge that with the count information. 

13. Use a Poisson GLM to assess the relationship between party and number of Obama/Trump/Clinton mentions. Does one party tend to mention Obama/Trump/Clinton more in their tweets? Can you deduce a pattern by considering the party of the senator and the party of Obama/Trump/Clinton?

    Here's some syntax to help you get started:
    ``` {.sourceCode .bash}
    import statsmodels.api as sm
    model = sm.GLM(endog = .,  exog = ., family = sm.families.Poisson())
    model.fit()
    ```

    Does the statistical result make sense in light of the number of total mentions of Obama/Trump/Clinton by Republicans and the number of total mentions by Democrats?

14. Use *matplotlib* to make histograms of the number of Obama mentions by senator, stratified by party.

    Is this consistent with the results of your statistical analysis?


