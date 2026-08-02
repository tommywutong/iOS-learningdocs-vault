---
title: QuickTime Initialization Guide
apple_id: TP40001435
resource_type: Guide
platform: macOS
topic: null
technology: QuickTime
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/QuickTime/Conceptual/QT_InitializingQT/InitializingQTAIntroduction/Introduction_intro.html
archived_at: '2026-07-18T02:04:19.258010Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Initializing%20QuickTime.md)

# Introduction to QuickTime Initialization Guide

Before you can call QuickTime functions, your application must initialize QuickTime. You may also want to check the version of QuickTime installed on the user’s computer to verify that it supports all the features your application uses.

If you are working on a Windows platform, you also need to verify that QuickTime is installed and initialize the QuickTime Media Layer (QTML).

If you are writing a threaded application, and intend to call QuickTime functions from multiple threads, you need to initialize QuickTime for each worker thread explicitly.

This document describes how and when to initialize QuickTime and the QuickTime Media Layer, and how to check to see if QuickTime is installed, as well as what version is installed.

If you are a QuickTime developer writing procedural C to create QuickTime applications or QuickTime components, you should read this document.

[Next](Initializing%20QuickTime.md)

