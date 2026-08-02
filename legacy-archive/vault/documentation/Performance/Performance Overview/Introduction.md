---
title: Performance Overview
apple_id: TP40001410
resource_type: Guide
platform: watchOS|iOS|macOS
topic: Performance
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/PerformanceOverview/Introduction/Introduction.html
archived_at: '2026-07-18T01:49:36.487319Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Developing%20for%20Performance.md)

# Introduction

Performance is an important design factor in all software products. If a program runs slowly or displays a spinning cursor, users are likely to become frustrated with the program and look for alternatives. Maintaining a reasonable level of performance requires some diligence on your part, but the earlier you start considering it, the easier it is to catch and fix problems.

_Performance Overview_ is an essential guide for developers who are new to the area of software performance analysis. This document gives an overview of the factors that govern performance and offers an approach for identifying and fixing common performance problems. It also introduces you to the specific tools and documentation you can use to identify and fix performance problems.

This document has the following chapters:

- [Developing for Performance](Developing%20for%20Performance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytimjqfvbuqmrqgmwugsscivdeosch) describes the factors that constitute performance and the approaches to achieving the best performance in your software.
- [Basic Performance Tips](Basic%20Performance%20Tips.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytimjqfvbuqmrqgqwueqsdi5bumr2g) describes the common areas of your code to analyze and offers some fundamental performance techniques.
- [Performance Tools](Performance%20Tools.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytimjqfvbuqmrqguwueq2jjfeecqkk) describes the available tools for doing a performance analysis of your program.
- [Doing an Initial Performance Evaluation](Doing%20an%20Initial%20Performance%20Evaluation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytimjqfvbuqmrqgywugsscizeeercc) walks you through the basics of some key tools and shows you how to use them to find performance problems.

If you have feedback about the documentation, you can provide it using the built-in feedback form at the bottom of every page.

If you encounter bugs in Apple software or documentation, you are encouraged to report them to Apple. You can also file enhancement requests to indicate features you would like to see in future revisions of a product or document. To file bugs or enhancement requests, go to the Bug Reporting page of the [Apple Developer website](https://developer.apple.com/):

[http://developer.apple.com/bugreporter/](https://developer.apple.com/bugreporter/)

To file bugs, you must be registered as an Apple Developer. You can obtain a login name for free by following the instructions on the [Apple Developer Registration page](https://developer.apple.com/programs/start/register/create.php).

In addition to this document, there are several documents that cover more specific aspects of performance. You should investigate these documents for detailed tips on how to analyze and solve performance problems.

- _[Code Size Performance Guidelines](../Code%20Size%20Performance%20Guidelines/Introduction%20to%20Code%20Size%20Performance%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2ds2i)_ offers advice on how to improve the memory footprint of your program.
- _[Code Speed Performance Guidelines](../Code%20Speed%20Performance%20Guidelines/Introduction%20to%20Code%20Speed%20Performance%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2ta2i)_ offers advice on how to tune your algorithms and find performance bottlenecks.
- _[Drawing Performance Guidelines](../Drawing%20Performance%20Guidelines/Introduction%20to%20Drawing%20Performance%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2tc2i)_ offers advice on how to optimize your program’s drawing-related code.
- _[File-System Performance Guidelines](../File-System%20Performance%20Guidelines/Introduction%20to%20File-System%20Performance%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3dc2i)_ offers advice on how to access files more efficiently.
- _[Launch Time Performance Guidelines](../Launch%20Time%20Performance%20Guidelines/Introduction%20to%20Launch%20Time%20Performance%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2dq2i)_ offers advice on how to speed up the launch time of your application.
- _[Memory Usage Performance Guidelines](../Memory%20Usage%20Performance%20Guidelines/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3da2i)_ offers advice on how to use memory more efficiently and on how to analyze your current memory usage.
- _[Concurrency Programming Guide](../../General/Concurrency%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4daojr)_ provides detailed information and examples about how to execute tasks in parallel.
- _[64-Bit Transition Guide](../../Darwin/64-Bit%20Transition%20Guide/Introduction%20to%2064-Bit%20Transition%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanru)_ discusses the performance impacts of 64-bit binaries and provides guidance on when creating such binaries is appropriate.
[Next](Developing%20for%20Performance.md)

