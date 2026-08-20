---
title: Interacting with the Operating System
apple_id: 10000058i
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2006-04-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/OperatingSystem/OperatingSystem.html
archived_at: '2026-07-15T07:17:36.078717Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Host%20Information.md)

# Introduction to Interacting with the Operating System

This topic describes a variety of classes that give you access to some of the functionality of the operating system. With them, you can launch subprocesses, obtain your process’s environment variables, perform domain name lookups, locate the user’s home directory, and more.

This document contains the following articles:

- [Host Information](Host%20Information.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhaydalkcijbusr2fivca) discusses how to perform domain name lookups.
- [Process Information](Process%20Information.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhaydclkciffekr2jizea) discusses the types of information you can obtain about the current process.
- [Task Management](Task%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhaydelkcijbuuqsejbbq) discusses how to launch subprocesses and communicate with them.
- [Signals](Signals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsmrzfvjvomi) discusses operating-system signals and their behavior in processes.
- [Creating and Launching an NSTask](Creating%20and%20Launching%20an%20NSTask.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhaydglkcijbumr2hifcq) shows an example of using an `NSTask` object.
- [Ending an NSTask](Ending%20an%20NSTask.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhaydilkciffeoskiizea) discusses ways to detect when a task exits and how to terminate tasks before they are done.
- [Piping Data Between Tasks](Piping%20Data%20Between%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhaydklkciffekrkcifba) shows an example of how to move data from one task to another using pipes.

Some classes are available for either Objective-C or Java, but not both. The functionality of those classes, though, are provided elsewhere in the other language.

[Next](Host%20Information.md)

