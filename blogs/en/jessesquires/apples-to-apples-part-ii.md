---
title: Apples to apples, Part II
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2014/08/06/apples-to-apples-part-two/'
original_language: en
published: 2014-08-06
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:c1805c54ec8deae9'
translated: false
---

> 原文：[Apples to apples, Part II](https://www.jessesquires.com/blog/2014/08/06/apples-to-apples-part-two/)　·　Jesse Squires

If at first you don’t succeed, try, try again. Practice makes perfect. These proverbs have encouraged us all in many different contexts. But in software development, they tug at our heartstrings uniquely. Programmers persevere through countless nights of fixing bugs. Companies march vigilantly toward an [MVP](http://en.wikipedia.org/wiki/Minimum_viable_product). But after 1.0 there is no finish line, there is no bottom of the 9th inning. There are more bugs to be fixed. There are new releases ahead. The march continues, because software is not a _product_, it is a _process_.

##### In This Series

This post is part of a series about Swift performance compared to Objective-C.

1. [Apples to apples](https://www.jessesquires.com/blog/2014/06/25/apples-to-apples/)
2. Apples to apples, Part II
3. [Apples to apples, Part III](https://www.jessesquires.com/blog/2014/08/21/apples-to-apples-part-three/)

This week, Apple has reminded us of the value of this iterative process and its rewards with the fifth beta release of Xcode 6, iOS 8, OS X Yosemite, and most importantly — _Swift_. This update includes a [number of improvements](http://adcdownload.apple.com//Developer_Tools/xcode_6_beta_5_za4gu6/xcode_6_beta_5_release_notes.pdf), but perhaps the most interesting are those not listed. Swift was rough around the edges during its launch at [WWDC](https://developer.apple.com/wwdc/), but it is **definitely** beginning to live up to its name.

If you missed my first post, [_Apples to Apples_](https://www.jessesquires.com/blog/2014/06/25/apples-to-apples/), you should head over there now to catch up.

### Setup

The setup is the same as before, but I’ll reiterate for clarity.

> - **Code:**[swift-sorts](https://github.com/jessesquires/swift-sorts), [objc-sorts](https://github.com/jessesquires/objc-sorts), and [std lib sort](https://gist.github.com/jessesquires/06b6bd68a7d18810651f#file-sorts-m) implementations
> - **Software:** OS X Mavericks 10.9.4, Xcode 6 beta 5
> - **Hardware:** 2008 unibody MacBook Pro, 2.4 Ghz Intel Core 2 Duo, 8 GB 1067 MHz DDR3 memory
> 
> The benchmarks consist of _**T**_ trials, which are averaged at the end to obtain the average execution time for each algorithm. Each trial begins by generating an array of _**N**_ random integers in the range `[0, UINT32_MAX)`. Then, each sorting algorithm is passed a copy of this initial array to sort. The current time is logged before and after each sort and the difference between the two yields the execution time for the algorithm for the current trial.
> 
> These two programs were carefully crafted to be a true _apples-to-apples_ comparison. All of the algorithms, as well as `main.swift` and `main.m`, are implemented as similarly as possible, bounded only by the confines and paradigms of the languages themselves. In Objective-C, `NSArray` and `NSNumber` are used intentionally as the counterparts to Swift's `Array` and `Int`. The APIs are language-specific too, for example `exchangeObjectAtIndex: withObjectAtIndex:` versus `swap()`.

### Results

Below are the results of running each program over 10 trials with 10,000 integers. The build configuration settings are noted for each run and the average execution times are displayed in seconds. The average case runtime complexity for each algorithm is also noted.

The final row in each table is the difference in speed of Swift compared to Objective-C. A positive value indicates that Swift is faster, while a negative value indicates that Swift is slower. For example, if Objective-C runs in 3.6 seconds and Swift runs in 1.2 seconds, then Swift is 3 times (3x) faster.

**Table 1**

| _T_ = 10 _N_ = 10,000 Debug | Std lib sort | Quick sort `O(n log n)` | Heap sort `O(n log n)` | Insertion sort `O(n2)` | Selection sort `O(n2)` |
|---|---|---|---|---|---|
| Objective-C `-O0` | 0.015161 s | 0.011438 s | 0.023984 s | 1.917997 s | 3.685714 s |
| Swift `-Onone` | 1.300011 s | 1.364851 s | 3.974969 s | 524.086557 s | 400.251450 s |
| Difference | -85.7x | -119.3x | -165.7x | -273.2x | -108.6x |

When not optimized, Swift is nothing to write home about. You can see that Objective-C performs substantially better. But this is ok — since you will be shipping with optimized builds. With no optimizations, this is what we should expect to see. The swiftness of Swift is in the compiler — [LLVM](http://www.llvm.org) and [Clang](http://clang.llvm.org). Mike Ash’s _Friday Q&A_ last month on the [_Secrets of Swift’s Speed_](https://mikeash.com/pyblog/friday-qa-2014-07-04-secrets-of-swifts-speed.html) provides a good overview of how better performance can be achieved with Swift versus Objective-C with compiler optimizations. We can see these optimizations in action below.

**Table 2**

| _T_ = 10 _N_ = 10,000 Release | Std lib sort | Quick sort `O(n log n)` | Heap sort `O(n log n)` | Insertion sort `O(n2)` | Selection sort `O(n2)` |
|---|---|---|---|---|---|
| Objective-C `-O3` | 0.011852 s | 0.010419 s | 0.019587 s | 1.741661 s | 3.439606 s |
| Swift `-O` | 0.001072 s | 0.001316 s | 0.002580 s | 0.279190 s | 0.193269 s |
| Difference | 11.1x | 7.9x | 7.6x | 6.2x | 17.8x |

If you recall the results from the [previous post](https://www.jessesquires.com/apples-to-apples/), then this should be quite shocking (in a good way). Take a deep breath. Yes, yes this is real life. The tables have completely turned (no pun intended). I’ve been running these trials since the first beta, and this is the _first time_ that Swift has performed **better than Objective-C** for every single algorithm, with standard optimizations. And not only is Swift faster, but it is faster by significant margins.

**Table 3**

| _T_ = 10 _N_ = 10,000 Release | Std lib sort | Quick sort `O(n log n)` | Heap sort `O(n log n)` | Insertion sort `O(n2)` | Selection sort `O(n2)` |
|---|---|---|---|---|---|
| Objective-C `-Ofast` | 0.012596 s | 0.010147 s | 0.019617 s | 1.763124 s | 3.504833 s |
| Swift `-Ounchecked` | 0.000773 s | 0.001011 s | 0.002073 s | 0.261637 s | 0.099996 s |
| Difference | 16.3x | 10.0x | 9.5x | 6.7x | 35.0x |

As of beta 5, the Swift optimization level of `-Ofast` has been deprecated in favor `-Ounchecked`. This renaming is a delightful change. Previously it read as, _"Ooooh fast!"_, begging for misuse and misunderstanding. But now it's more like _"Oh... unchecked?"_, which better reflects its unsafe nature.

This should come as no surprise. Swift performance at this optimization level was always better than Objective-C, with the exception of the std lib sort — which no longer the case.

The benchmarks above were gathered with `N = 10,000` to be consistent with the previous post. However, this is no longer a challenge for Swift. Let’s see what happens when `N = 100,000`. Given that most, if not all, developers will be compliling their modules and apps at the standard optimization level, the trials below were only run with `-O` and release. As expected, Swift comes out on top.

**Table 4**

| _T_ = 10 _N_ = 100,000 Release | Std lib sort | Quick sort `O(n log n)` | Heap sort `O(n log n)` | Insertion sort `O(n2)` | Selection sort `O(n2)` |
|---|---|---|---|---|---|
| Objective-C `-O3` | 0.151701 s | 0.121619 s | 0.251310 s | 175.421688 s | 349.182743 s |
| Swift `-O` | 0.013933 s | 0.015712 s | 0.036932 s | 27.532488 s | 18.969978 s |
| Difference | 10.9x | 7.7x | 6.8x | 6.4x | 18.4x |

### Full speed ahead

When Apple introduced Swift, we were assured safety, clarity, modernity, and speed. It is clear to me that they have delivered and are continuing to deliver on these promises. The refinements and enhancements made over the past few months have been absolutely great. Some highlights for me include array value semantics, array and dictionary syntactic sugar, the `..<` operator replacing the `..` operator, and the performance improvements seen here. I think Swift is coming along quite nicely and I am more excited than ever for the next beta.

Swift is a breath of fresh air that makes reading and writing Objective-C feel archaic. I cannot wait for 1.0 and the moment when I can say goodbye to Objective-C.

**The _Apples to apples_ series will continue as betas are released. Stay tuned for updates and new posts!**
