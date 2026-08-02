---
title: FullScreen
apple_id: DTS10000498
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/FullScreen/Introduction/Intro.html
archived_at: '2026-07-18T03:09:36.509485Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.c.md)

# FullScreen

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 Shows how to use BeginFullScreen and EndFullScreen to enter and exit full-screen mode. |
| __Build Requirements:__ | Mac OS X |
| __Runtime Requirements:__ | Mac OS X or later |

FullScreen is a sample to demonstrate how to run an app in full screen mode on Mac OS X. The sample uses the Quicktime calls BeginFullScreen() and EndFullScreen() to enter and leave full screen mode. The sample also catches kEventAppActivated and kEventAppDeactivated so it knows when to stop or start drawing and hide or show its full screen window so it does not mess with other applications on the system. Requirements: Mac OS X or later Keywords: Full Screen, Hide Dock, Hide Menu

[Next](main.c.md)

