---
title: Apples to apples
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2014/06/25/apples-to-apples/'
original_language: en
published: 2014-06-25
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:387e13e5178a99b6'
translated: false
---

> 原文：[Apples to apples](https://www.jessesquires.com/blog/2014/06/25/apples-to-apples/)　·　Jesse Squires

When Craig Federighi arrived at his presentation slide about Objective-C during this year’s [WWDC keynote](http://www.apple.com/apple-events/june-2014/) everyone in the room seemed puzzled, curious, and maybe even a bit uneasy. _What was happening?_ As he continued, he considered what Objective-C would be like **without the C**, and the room abruptly filled with rumblings and whispers ^[[1]](#note1) as developers in the audience confided in those around them. If you had been following the [discussions](http://informalprotocol.com/2014/02/replacing-cocoa/) in our community about the [state of Objective-C](http://nearthespeedoflight.com/article/2014_03_17_objective_next) (and why we [need to replace it](http://ashfurrow.com/blog/we-need-to-replace-objective-c)) during the previous months, you could only have imagined one thing: Objective-C was no more — at least not as we knew it.

##### In This Series

This post is part of a series about Swift performance compared to Objective-C.

1. Apples to apples
2. [Apples to apples, Part II](https://www.jessesquires.com/blog/2014/08/06/apples-to-apples-part-two/)
3. [Apples to apples, Part III](https://www.jessesquires.com/blog/2014/08/21/apples-to-apples-part-three/)

##### [Update](#updated-01-august-2014)  _01 August 2014_

This post has been updated for Xcode6-beta4. All trials were re-run as described below using Xcode6-beta4.

Major changes to the Swift language include the [redesign of arrays](https://developer.apple.com/swift/blog/?id=3) to have full value semantics and new syntactic sugar — introduced in Xcode6-beta3. As of the beta4 release, Swift has seen **dramatic** performance improvements. See the updated results below.

**Note:** because of the new array semantics and syntax, code changes were required for Swift. You can find the previous code on the `xcode6-beta1and2` branch [on GitHub](https://github.com/jessesquires/swift-sorts/branches).

> And then Federighi said, let there be Swift; and there was Swift.
> 
> — WWDC 2014, 1:44:48

The third floor of Moscone West erupted with applause as if we had traveled back in time to Steve Jobs’ [2007 announcement](https://www.youtube.com/watch?v=EHWRkuDlNOE) of _**the**_ iPhone: _“An iPod, a phone, and an Internet communicator”_.

As the keynote continued, we were assured safety, optimizations, clarity, modernity, and speed. But, as some have [already investigated](http://www.splasmata.com/?p=2798), Swift may not be as swift as promised. However, Swift is still in beta (along with Xcode 6, iOS 8, and OS X 10.10), so we will undoubtedly see many improvements and changes in the coming months.

As a fun and interesting [code kata](http://codekata.com), I decided to port my [objc-sorts](https://github.com/jessesquires/objc-sorts) project on GitHub to Swift. Behold, [swift-sorts](https://github.com/jessesquires/swift-sorts). These projects are collections of sorting algorithms implemented in Objective-C and Swift, respectively. I completed a rough version of the Swift project during the week of WWDC and have since refined both. I also shared the results below with Apple engineers in the Swift Labs during WWDC, but more on that later.

### Setup

- _Code:_[Swift Sorts](https://github.com/jessesquires/swift-sorts) and [Objective-C Sorts](https://github.com/jessesquires/objc-sorts)
- _Software:_ OS X Mavericks ~~10.9.3~~ 10.9.4, Xcode6-beta4 ~~beta2~~~~WWDC seed~~
- _Hardware:_ 2008 unibody MacBook Pro, 2.4 Ghz Intel Core 2 Duo, 8 GB 1067 MHz DDR3 memory ^[[2]](#note2)

Each project is a command line app with a debug, release, and unit-test scheme. Build and run, then watch the console for output.

The benchmarks consist of _T_ trials, which are averaged at the end to obtain the average execution time for each algorithm. Each trial begins by generating an array of _N_ random integers in the range `[0, UINT32_MAX)`. Then, each sorting algorithm is passed a copy of this initial array to sort. The current time is logged before and after each sort and the difference between the two yields the execution time for the algorithm for the current trial.

These two programs were carefully crafted to be a true _apples-to-apples_ comparison. All of the algorithms, as well as `main.swift` and `main.m`, are implemented as similarly as possible, bounded only by the confines and paradigms of the languages themselves. In Objective-C, `NSArray` and `NSNumber` are used intentionally as the counterparts to Swift’s `Array` and `Int`. The APIs are language-specific too, for example `exchangeObjectAtIndex: withObjectAtIndex:` versus `swap()`.

The following were used for the standard library sorts:

```
// Swift
var arr: [Int] = // some array
let newArr = sorted(arr);

// Objective-C
NSMutableArray *arr = // some array
[arr sortUsingComparator:^NSComparisonResult(NSNumber *n1, NSNumber *n2) {
    return [n1 compare:n2];
}];
```

Previous Swift std lib sort [implementation here](https://gist.github.com/jessesquires/06b6bd68a7d18810651f/ee5aa0a7427f830fadd4d369c9d04a895fc2b49b).

### Results

Below are the results of running each program over 10 trials with 10,000 integers. The build configuration settings are noted for each run and the execution times are displayed in seconds. The average case runtime complexity for each algorithm is also noted. I realize that 10,000 is relatively small, but you’ll see that Swift was taking quite a long time.

**Table 1**

| _T_ = 10 _N_ = 10,000 Debug | Std lib sort | Quick sort `O(n log n)` | Heap sort `O(n log n)` | Insertion sort `O(n2)` | Selection sort `O(n2)` |
|---|---|---|---|---|---|
| Objective-C `-O0` | ~~0.015813 s~~ 0.015732 s | ~~0.011393 s~~ 0.011395 s | ~~0.023052 s~~ 0.025252 s | ~~1.945385 s~~ 1.931189 s | ~~3.745795 s~~ 3.762144 s |
| Swift `-Onone` | ~~1.460893 s~~ 1.536891 s | ~~1.585898 s~~ 1.633227 s | ~~4.498561 s~~ 4.714571 s | ~~599.164323 s~~ 625.810322 s | ~~507.968824 s~~ 519.386646 s |

**Table 2**

| _T_ = 10 _N_ = 10,000 Release | Std lib sort | Quick sort `O(n log n)` | Heap sort `O(n log n)` | Insertion sort `O(n2)` | Selection sort `O(n2)` |
|---|---|---|---|---|---|
| Objective-C `-O3` | ~~0.012037 s~~ 0.012195 s | ~~0.010317 s~~ 0.010893 s | ~~0.020318 s~~ 0.019672 s | ~~1.777335 s~~ 1.778275 s | ~~3.508259 s~~ 3.521110 s |
| Swift `-O` | ~~0.079272 s~~ 0.019062 s | ~~0.072787 s~~ 0.007888 s | ~~0.212094 s~~ 0.057481 s | ~~28.431325 s~~ 4.407984 s | ~~8.662720 s~~ 7.028199 s |

According to the Apple engineers that I spoke with, `-O3` in Objective-C is essentially the equivalent to `-O` in Swift.

**Table 3**

| _T_ = 10 _N_ = 10,000 Release | Std lib sort | Quick sort `O(n log n)` | Heap sort `O(n log n)` | Insertion sort `O(n2)` | Selection sort `O(n2)` |
|---|---|---|---|---|---|
| Objective-C `-Ofast` | ~~0.012278 s~~ 0.011828 s | ~~0.010448 s~~ 0.010285 s | ~~0.020256 s~~ 0.019763 s | ~~1.787421 s~~ 1.776664 s | ~~3.582407 s~~ 3.497402 s |
| Swift `-Ofast` | ~~0.022573 s~~ 0.001306 s | ~~0.005410 s~~ 0.001426 s | ~~0.005903 s~~ 0.002259 s | ~~0.997563 s~~ 0.297713 s | ~~0.113045 s~~ 0.068731 s |

Note that `-O` is the standard optimization level for Swift and `-Ofast`, though faster, removes **all** safety features (_array bounds-checking, integer overflow checking, etc._) from Swift. In other words, do not ship an entire app compiled with `-Ofast`. More on that below.

##### [Update](#updated-01-august-2014)  _01 August 2014_

We see the following notable changes with Xcode-beta4:

- Swift is now slightly worse without optimizations. (see _Table 1_)
- With optimizations, Swift performance is incredibly better and much closer to Objective-C. However, Objective-C is still faster. (see _Table 2_)
- Swift’s insertion sort has completely turned around, and now outperforms selection sort with significant margins!
- Swift with agressive optimizations is substantially faster than before, and outperforms Objective-C on every sort.

There are a few notable discoveries here:

1. Rather shockingly, debug is incredibly slow in Swift but improves dramatically with compiler flags. The difference in performance between _no_ optimizations and `-Ofast` in Swift is stark. On the other hand, Objective-C sees relatively minor benefits.
2. At the standard optimization level (see _Table 2_), the two languages begin to perform more similarly. Objective-C is still noticeably faster though. Std lib sort is 6.5x faster. Quick sort is 7.0x faster. Heap sort is 10.4x faster. Insertion sort is 16.0x faster. Selection sort is 2.47x faster.
3. Only with `-Ofast` do we begin to experience the swiftness of Swift, and even then the standard library sort in Objective-C is almost twice as fast (1.84x). However, when comparing Swift to Swift the discrepancies are enormous. Swift performs orders of magnitude better than it did without optimizations and puts Objective-C to shame with quick sort, heap sort, insertion sort, and selection sort (see _Table 3_).
4. We all know that selection sort and insertion sort are not particularly optimal algorithms, and Swift does a good job to emphasize this (when not using `-Ofast`, see _Table 1_ and _Table 2_). But why are these two so terrible in Swift? Especially insertion sort — in debug Objective-C is 308.0x faster. I’m still puzzled by this. These two sorting algorithms are not complex, but they stand apart from the other sorts in the following ways: selection sort has nested for-loops and insertion sort has a while-loop nested in a for-loop. Perhaps Swift is having trouble optimizing these? Is this a bug?
5. My mundane quick sort implementation is faster than the standard library sort for both languages. Typically, these library methods would utilize multiple sorting algorithms that are guided by a set of heuristics that help determine the best algorithm to use based on the dataset. I suspect that we would see the standard library sorts perform best with larger datasets and/or with complex objects.

According to the benchmarks presented during the keynote (1:45:30), we should (probably?) be seeing different results here. Federighi noted that for complex object sort, Objective-C performed at 2.8x and Swift performed at 3.9x, using Python as the baseline (1.0x). It is not clear at this time how these benchmarks were achieved. What were the build and optimization settings? What is a “complex object”? In any case, surely Swift should be able to sort integers just as well as “complex objects”, right?

### Swift Labs at WWDC

The Apple engineers hanging out in the Swift Labs at WWDC were interested in these benchmarks and were somewhat surprised to see them. Unfortunately, the engineers that I spoke with did not have an explanation for why we were seeing these results. We filed Radar #17201160, noting most of the points above.

Additionally, I asked what the best practices are regarding using `-Ofast`. They recommended the following approach: (1) profile your app to find out where it is slow, (2) extract this slow code into a separate module/framework, (3) thoroughly test this module, and then (4) compile the module using `-Ofast` and link it to your app. Remember, this removes **all** safety features from Swift.

### Moving forward

The results above seem to indicate that Apple has not (yet) followed through on their promises of speed and safety — at least in the sense that these features can be mutually inclusive. Again, it is still early. Hopefully these benchmarks will improve as Swift nears a 1.0 release. **I plan on updating this post or writing follow-up posts as Apple releases updates for Swift and Xcode6-beta.**

As Brent Simmons [said](http://inessential.com/2014/02/12/on_replacing_objective-c), Objective-C used to be considered slow compared to plain C, but it is not slow compared to Java or Python. I am not sure if the reaction to these results should be _we have faster hardware, so a slower language is fine_, or _nothing will ever be as fast as C_, or somewhere in-between. But after completing these two projects, I do know this: Swift is a pleasure to write and read. Many things came easier and more naturally in Swift, and Playgrounds are pure gold. Swift has a lot of potential. Let’s hope this is the next step that we have all been waiting for, and not another [Copland](http://arstechnica.com/apple/2010/06/copland-2010-revisited/).

### Futher reading

- The _Official_[Apple Swift Blog](https://developer.apple.com/swift/blog/)
- [_Swift?_](http://www.splasmata.com/?p=2798) from Splasm Software
- [_The Foundation Collection Classes_](http://www.objc.io/issue-7/collections.html) by Peter Steinberger, objc.io issue #7

- [[1]](#superscript1) If you turn up the volume and listen closely, you can hear this in the keynote video. It was much louder in person.
- [[2]](#superscript2) If you are thinking, _this guy needs a new MacBook_ — you are correct! :)
