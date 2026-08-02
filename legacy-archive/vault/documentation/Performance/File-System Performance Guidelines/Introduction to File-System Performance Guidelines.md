---
title: File-System Performance Guidelines
apple_id: 10000161i
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: null
published: '2014-03-10'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/FileSystem/FileSystem.html
archived_at: '2026-07-18T01:48:45.286010Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](File-System%20Performance%20Tips.md)

# Introduction to File-System Performance Guidelines

Accessing file data is one of the biggest bottlenecks to performance on any computer system. Most computers are capable of executing millions of instructions before the hard drive heads are even in position and ready to read a piece of data. As a result, it is imperative that you examine your application’s file-system interactions and do what you can to improve them.

This programming topic contains the following articles:

- [File-System Performance Tips](File-System%20Performance%20Tips.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhe4dolkdjjbeqskjjjaq) provides some general tips for improving your application’s file-related code.
- [Overview of OS X File Systems](Overview%20of%20OS%20X%20File%20Systems.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhe4dqlkdjjbekrcfivbq) provides a brief overview of OS X file-system performance and how it can impact your application.
- [Examining File-System Usage](Examining%20File-System%20Usage.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhe4dslkdjjbeursjirca) describes techniques for analyzing your application’s file-system interactions.
- [Mapping Files Into Memory](Mapping%20Files%20Into%20Memory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhe4talkdjjbeursjirca) describes techniques for minimizing the work done when reading files into memory.
- [Iterating Directory Contents](Iterating%20Directory%20Contents.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhe4tclkdjjbeursjirca) provides an example of how to iterate directories efficiently.
- [Resolving Domain Names](Resolving%20Domain%20Names.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhe4telkdjjbeursjirca) describes better-performing alternatives to getting network-based information.
- [Tracking File-System Changes](Tracking%20File-System%20Changes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhe4tglkdjjbeursjirca) describes the approach your application should take when monitoring the file system for changes to individual files and directories.

[Next](File-System%20Performance%20Tips.md)

