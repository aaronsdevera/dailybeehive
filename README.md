# Daily Beehive (@dailybeehive)
An automated daily word puzzle by @aaronsdevera. Distributed daily on Twitter @dailybeehive. Created with RStudio, Python, and the Twitter API.

## Rules
- Make as many words as possible
- All words must use the center letter at least once
- Letters can be used multiple times
- No proper nouns (names, places, companies)
- Every puzzle has at least 1 word that uses each letter at least once
- *Pro:* Words must be longer than 5 letters

## Scoring
- Puzzle Difficulty and the number of solutions are in the footer of each puzzle (eg. **HARD:106**)
- **HARD** puzzles: each word is 3 points.
- **MED** puzzles: each word is 2 points.
- **EASY** puzzles: each word is 1 points.
- Any word that uses each letter gives you a bonus 1 point.


## Letter Frequency (Versions <1.21)
All letters have a frequency that corresponds to how many times statisticians estimate the letter to appear in the English language. Since the algorithm that generates this game depends on the frequencies of letters used in past games I have played in the New York Times magazine, my games should have a pretty good range of letter frequnecy that hopefully allows for some pretty natural word possibility.

**ALF** stands for Average Letter Frequency. This is determined by taking the letter frequency of each letter found in a single game and finding the average. Since it is easier to make words with higher letter frequencies, games with higher ALF will be easier than games with lower ALF.

## Updates

- v2.0 on 5/31/2016
- v1.21 on 2/02/2016
- v1.20 on 2/02/2016
- v1.1 on 1/17/2016