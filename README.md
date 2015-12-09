# Daily Beehive (@dailybeehive)
An automated daily word puzzle by @aaronsdevera. Distributed daily on Twitter @dailybeehive. Created with RStudio, Python, and the Twitter API.
## Rules
- Make as many words as possible
- All words must use the center letter at least once
- Letters can be used multiple times
- No proper nouns (names, places, companies)
- *Pro:* Words must be longer than 5 letters

## Letter Frequency
All letters have a frequency that corresponds to how many times statisticians estimate the letter to appear in the English language. Since the algorithm that generates this game depends on the frequencies of letters used in past games I have played in the New York Times magazine, my games should have a pretty good range of letter frequnecy that hopefully allows for some pretty natural word possibility.

**ALF** stands for Average Letter Frequency. This is determined by taking the letter frequency of each letter found in a single game and finding the average. Since it is easier to make words with higher letter frequencies, games with higher ALF will be easier than games with lower ALF.
