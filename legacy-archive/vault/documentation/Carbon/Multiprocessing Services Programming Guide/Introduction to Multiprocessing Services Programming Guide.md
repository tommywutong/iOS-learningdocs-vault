---
title: Multiprocessing Services Programming Guide
apple_id: TP40000853
resource_type: Guide
platform: macOS
topic: null
technology: CoreServices
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/Multitasking_MultiproServ/01introduction/introduction.html
archived_at: '2026-07-15T05:23:35.297524Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](About%20Multitasking%20on%20the%20Mac%20OS.md)

# Introduction to Multiprocessing Services Programming Guide

Multiprocessing Services is a technology that allows your application to create tasks that run independently on one or more microprocessors. For example, you can have your application perform graphical calculations while writing data to a hard drive. Unlike the cooperative model (such as used by the Thread Manager or the Mac OS Process Manager), Multiprocessing Services automatically divides processor time among available tasks so no particular task can “hog” the system. On computers with multiple microprocessors, you can actually perform multiple tasks simultaneously. This feature allows you to divide up time-intensive calculations among several microprocessors.

This document is a complete guide to Multiprocessing Services 2.1 . This technology is available with Mac OS 9.0 and later (including Mac OS X), although some functions may work with earlier system software versions.

You should read this document if you want to add multitasking capability to Mac OS applications. This document assumes you are familiar with programming Macintosh computers. For more information about how the Mac OS handles applications in memory, see the documents Inside Macintosh: Processes and Mac OS Runtime Architectures.

This document covers Multiprocessing Services in the following chapters:

- [About Multitasking on the Mac OS](About%20Multitasking%20on%20the%20Mac%20OS.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenryfvjvomi) describes the basics of multitasking and multiprocessing, as well as information about how Multiprocessing Services implements these capabilities on the Mac OS.
- [Using Multiprocessing Services](Using%20Multiprocessing%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenrxfvjvomi) contains programming examples and other detailed information about adding Multiprocessing Services to your application.
- [Preemptive Task–Safe Mac OS System Software Functions](Preemptive%20Task%E2%80%93Safe%20Mac%20OS%20System%20Software%20Functions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenrwfvjvomi) lists Mac OS system software functions that you can call from preemptive tasks.
- [Calculating the Intertask Signaling Time](Calculating%20the%20Intertask%20Signaling%20Time.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenrvfvjvomi) contains sample code you can use to determine the amount of time it takes to notify a task.
- [Changes From Previous Versions of Multiprocessing Services](Changes%20From%20Previous%20Versions%20of%20Multiprocessing%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenrufvjvomi)describes changes and additions to the Multiprocessing Services API between version 1.4 and 2.1.

For more information about multithreading on Mac OS X, see _[Threading Programming Guide](../../Cocoa/Threading%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2i)_ in Carbon Process Management documentation.

For additional information about Multiprocessing Services, you should check the Apple Developer Web site: [http://developer.apple.com](https://developer.apple.com/)

[Next](About%20Multitasking%20on%20the%20Mac%20OS.md)

