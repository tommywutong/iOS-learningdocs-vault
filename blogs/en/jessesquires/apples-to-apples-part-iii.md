---
title: Apples to apples, Part III
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2014/08/21/apples-to-apples-part-three/'
original_language: en
published: 2014-08-21
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:09d44f2655b91eb1'
translated: false
---

> 原文：[Apples to apples, Part III](https://www.jessesquires.com/blog/2014/08/21/apples-to-apples-part-three/)　·　Jesse Squires

_When I find my code is slow or troubled, friends and colleagues comfort me. Speaking words of wisdom, write in C._ It is understood that foregoing the features and abstractions of [high-level](http://en.wikipedia.org/wiki/High-level_programming_language) programming languages in favor of their [low-level](http://en.wikipedia.org/wiki/Low-level_programming_language) counterparts can yield faster, more efficient code. If you abandon your favorite runtime, forget about garbage collection, eschew dynamic typing, and leave message passing behind; then you will be left with scalar operations, manual memory management, and raw pointers. However, the closer we get to the hardware, the further we get from readability, safety, and maintainability.

##### In This Series

This post is part of a series about Swift performance compared to Objective-C.

1. [Apples to apples](https://www.jessesquires.com/blog/2014/06/25/apples-to-apples/)
2. [Apples to apples, Part II](https://www.jessesquires.com/blog/2014/08/06/apples-to-apples-part-two/)
3. Apples to apples, Part III

In [_Apples to apples, Part II_](https://www.jessesquires.com/blog/2014/08/06/apples-to-apples-part-two/), we discovered that Swift was finally performing better than Objective-C. As expected, some common [reactions](https://twitter.com/OldManKris/status/497102303833255936) and [responses](https://twitter.com/mpweiher/status/497066155224608768) on Twitter were, _then how does it compare to C?_ This is precisely what we are investigating today to welcome this week’s arrival of [Xcode 6 beta 6](https://developer.apple.com/xcode/downloads/).

### Setup

- _Code:_[swift-sorts](https://github.com/jessesquires/swift-sorts) and [c-sorts](https://github.com/jessesquires/c-sorts)
- _Software:_ OS X Mavericks 10.9.4, Xcode 6 beta 6
- _Hardware:_ 2008 unibody MacBook Pro, 2.4 Ghz Intel Core 2 Duo, 8 GB 1067 MHz DDR3 memory

The benchmarks consist of _**T**_ trials, which are averaged at the end to obtain the average execution time for each algorithm. Each trial begins by generating an array of _**N**_ random integers in the range `[0, UINT32_MAX)`. Then, each sorting algorithm is passed a copy of this initial array to sort. The current time is logged before and after each sort and the difference between the two yields the execution time for the algorithm for the current trial. Each execution time is saved to find the average time and standard deviation after all trials are complete.

The sorting algorithms are written as [textbook implementations](http://en.wikipedia.org/wiki/Introduction_to_Algorithms) for clarity, objectivity, and fairness to each language. The standard library sort for Swift uses the `sorted()` [function](https://gist.github.com/jessesquires/06b6bd68a7d18810651f#file-sorts-m) while C uses `qsort()` from [cstdlib](http://www.cplusplus.com/reference/cstdlib/qsort/).

### Results

Below are the results of running each program over 20 trials with 100,000 integers. The average execution times are displayed in seconds with the standard deviation listed underneath. All trials were run with the release build configuration, since we know Swift would be too slow in debug. The final row in each table is the difference in speed of Swift compared to C. A positive value indicates that Swift is faster, while a negative value indicates that Swift is slower. For example, if C runs in 1.2 seconds and Swift runs in 3.6 seconds, then Swift is 3 times (-3x) slower. Also note that the different compiler optimization levels have no affect on C, but are listed for consistency.

**Table 1**

| _T_ = 20 _N_ = 100,000 Release | Std lib sort | Quick sort `O(n log n)` | Heap sort `O(n log n)` | Insertion sort `O(n2)` | Selection sort `O(n2)` |
|---|---|---|---|---|---|
| C `-O3` | 0.020853 s (± 0.000191) | 0.011243 s (± 0.000042) | 0.014909 s (± 0.000360) | 7.575798 s (± 0.016685) | 6.981794 s (± 0.004399) |
| Swift `-O` | 0.014114 s (± 0.000413) | 0.016745 s (± 0.000202) | 0.042325 s (± 0.003881) | 33.819305 s (± 0.120471) | 25.255743 s (± 0.084152) |
| Difference | 1.48x | -1.48x | -2.84x | -4.46x | -3.62x |

**Note:** I should point out that Swift has **slightly regressed** in beta 6 — but it is still substantially faster than Objective-C on all algorithms. When comparing the results above with [_Table 4_ from Part II](https://www.jessesquires.com/apples-to-apples-part-two/), we see that Swift is slower for each sort by the following rates: 1.01x, 1.06x, 1.15x, 1.23x, 1.33x, respectively. Remember, Swift is still in beta. Things happen. If previous releases are any indication, we will surely see improvements.

Unexpectedly, **Swift outperforms C** for the standard library sort. This may reveal more about the standard library sorting algorithms than it does about the languages, but it is fascinating nonetheless. Examining the other sorts, C comes out ahead as most would have guessed — but its **margins are small**, relatively speaking. Recall how Swift nailed Objective-C in the previous post. At its slowest, Swift was still 6x faster than Objective-C, which means that Objective-C could not dream of performing this well. This is a big deal.

**Table 2**

| _T_ = 20 _N_ = 100,000 Release | Std lib sort | Quick sort `O(n log n)` | Heap sort `O(n log n)` | Insertion sort `O(n2)` | Selection sort `O(n2)` |
|---|---|---|---|---|---|
| C `-Ofast` | 0.020861 s (± 0.000216) | 0.011245 s (± 0.000044) | 0.014932 s (± 0.000308) | 7.578673 s (± 0.012784) | 6.985793 s (± 0.004598) |
| Swift `-Ounchecked` | 0.009508 s (± 0.000367) | 0.011953 s (± 0.000603) | 0.033006 s (± 0.002562) | 30.831836 s (± 0.057725) | 9.660987 s (± 0.078939) |
| Difference | 2.19x | -1.06x | -2.21x | -4.07x | -1.38x |

Here we see what we should expect from `-Ounchecked`, given the results in _Table 1_. There is a similar pattern, only amplified. Swift gets even faster and even closer to C.

### Approaching the speed of C

It’s serendipitous that `c` denotes [the speed of light](http://en.wikipedia.org/wiki/Speed_of_light) in physics, isn’t it? A common view in the programming community is that _nothing beats C_, and rightly so. It paved the road ahead and has endured the decades since its inception. I doubt that C is going anywhere, but this new kid on the block is pretty swift.

As programmers, we have a choice with regard to our toolsets. Programming languages come in a variety of forms with a [variety of features](https://www.destroyallsoftware.com/talks/wat). The opportunity costs of choosing one language are the features that you are foregoing in another. Swift is no C when it comes to speed, but when considering the features of each language, Swift’s superiority is undisputed.

And now we must patiently wait for the next beta.
