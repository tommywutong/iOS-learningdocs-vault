---
title: On the value of benchmarks
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2014/08/19/on-the-value-of-benchmarks/'
original_language: en
published: 2014-08-19
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:13e91f214e3b0552'
translated: false
---

> 原文：[On the value of benchmarks](https://www.jessesquires.com/blog/2014/08/19/on-the-value-of-benchmarks/)　·　Jesse Squires

As [_Apples to apples, Part II_](https://www.jessesquires.com/blog/2014/08/06/apples-to-apples-part-two/) made its way around the web, it was [praised](https://twitter.com/SwiftLang/status/497057489766981632) as well as [critiqued](https://twitter.com/benpickering/status/497127012814041088). The latter largely consisted of questions regarding the real-world applications of these benchmarks. In general, benchmarks should be taken with a grain of salt. I want to take a minute to clarify my thoughts on benchmarks and how I think they can be valuable.

Benchmarks in software (and also [in hardware](http://www.macrumors.com/2013/12/15/new-12-core-mac-pro-once-again-shows-up-in-benchmarks/)) inherently do not reflect real-world performance scenarios. Just as with scientific experiments in academia, we have contrived a special situation in a fabricated environment that isolates a particular feature of a particular system, in order to examine it more closely. It does not matter whether we are measuring the speed of sorting large arrays of numbers, or examining the mechanisms of the behavior of _Caenorhaditis elegans_ (i.e. the nematode worm) by [embedding a model of its connectome in a simplified body and environment simulation](http://www.ploscompbiol.org/article/info:doi/10.1371/journal.pcbi.1002890) — limitations and restrictions exist. By virtue of these processes, external factors that are normally present are absent.

But even in these circumstances, I find benchmarks (as well as scientific research) interesting and meaningful. There may not be a direct, one-to-one correspondence in performance between a set of benchmarks and a full app, but they will provide insights into how these languages operate in general, in certain contexts, or under certain conditions. These observations can help guide our troubleshooting abilities and inform our decisions on which toolsets to use. Further, every app will be built differently. Only through the isolation of benchmark testing can we objectively view and examine the qualities of a programming language.

In iOS and OS X development, we are lucky enough to have amazing tools like [Instruments](https://developer.apple.com/xcode/features/) whose purpose is to help make our apps better. We also have a few programming languages to choose from: Objective-C, C, C++, and Swift — all of which can co-exist peacefully in a single app. Instruments can easily tell you where your code is slow, but there is not a “fix me” button that you can click to solve your problems. We often have to be creative with regard to optimizing our apps, and knowing a little about how and why certain languages may be slower or faster, and under what conditions, could go a long way.
