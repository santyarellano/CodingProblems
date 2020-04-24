# Kana and Dragon Quest game (1337B)
## Description
Kana was just an ordinary high school girl before a talent scout discovered her. Then, she became an idol. But different from the stereotype, she is also a gameholic.

One day Kana gets interested in a new adventure game called Dragon Quest. In this game, her quest is to beat a dragon.


 
The dragon has a hit point of x initially. When its hit point goes to 0 or under 0, it will be defeated. In order to defeat the dragon, Kana can cast the two following types of spells.

- Void Absorption
Assume that the dragon's current hit point is h, after casting this spell its hit point will become ⌊h2⌋+10. Here ⌊h2⌋ denotes h divided by two, rounded down.

- Lightning Strike
This spell will decrease the dragon's hit point by 10. Assume that the dragon's current hit point is h, after casting this spell its hit point will be lowered to h−10.

Due to some reasons Kana can only cast no more than n Void Absorptions and m Lightning Strikes. She can cast the spells in any order and doesn't have to cast all the spells. Kana isn't good at math, so you are going to help her to find out whether it is possible to defeat the dragon.

### Input
The first line contains a single integer t (1≤t≤1000)  — the number of test cases.

The next t lines describe test cases. For each test case the only line contains three integers x, n, m (1≤x≤105, 0≤n,m≤30)  — the dragon's intitial hit point, the maximum number of Void Absorptions and Lightning Strikes Kana can cast respectively.

### Output
If it is possible to defeat the dragon, print "YES" (without quotes). Otherwise, print "NO" (without quotes).

You can print each letter in any case (upper or lower).

# :crystal_ball: :bulb: Solution :bulb: :crystal_ball:

If you read carefully how the void absorption spell works, you will notice it falls in a wanna-be-logarithmic function. This way, there are 2 things to consider:

1. The dragon's health can decrease rapidly.
2. The dragon's health cannot get to 0 without a lightning strike.

With these considerations a rule can be defined:
> In order to kill the dragon one must use enough void absorption spells to reach 10 times the amount of lightning strikes available.

And that's it! All we have to do is iterate over every case using void absorption spells until we reach that number. If we run out of void absorption spells, then the dragon won't be killed.

- Exception: One must check first if the dragon can be killed only with the lightning strikes.