---
title: SkyCreator
apple_id: DTS10003668
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2006-04-12'
source_url: https://developer.apple.com/library/archive/samplecode/SkyCreator/Introduction/Intro.html
archived_at: '2026-07-18T03:24:46.444582Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](AboutBox.java.md)

# SkyCreator

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2006-04-12 Updated compiler options to generate 1.4 compatible bytecode. |
| __Build Requirements:__ | Xcode 2.0 or greater |
| __Runtime Requirements:__ | 1.4.2 or later |

This is a very simple demo that creates a random image of a starry sky using several star images of different sizes that are placed randomly on the screen. The user can drag the stars to re-arrange them. This code was written to illustrate the functionallity of QuartzDebug. There is a slow and a fast version. The slow version is commented out by default. The slow version repaints the whole window every time a star is moved, and the fast version only re-paints the dirty region. You can use

QuartzDebug to see the different behavior between the two versions.

[Next](AboutBox.java.md)

