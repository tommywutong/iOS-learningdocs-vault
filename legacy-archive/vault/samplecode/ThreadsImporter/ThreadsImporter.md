---
title: ThreadsImporter
apple_id: DTS10003146
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2005-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/ThreadsImporter/Introduction/Intro.html
archived_at: '2026-07-18T03:26:51.527971Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# ThreadsImporter

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0.1, 2005-07-22 Updated to produce a universal binary. No code changes were required. |
| __Build Requirements:__ | Xcode 2.1, Xcode 1.1+ |
| __Runtime Requirements:__ | Mac OS X 10.3 or later with QuickTime 6.4 or later. |

ThreadImporter demonstrates importing and displaying still images on separate threads. For demonstration purposes only, this sample will also allow the use of non-thread safe components on separate threads.
QuickTime 6.4 (on MacOS X 10.3 and later) introduces several new features that support execution of background tasks on multiple threads in a preemptive multitasking environment. This makes it possible to offload many tasks from your applications main thread to forestall blocking the user interface.
For more information see Threaded Programming and QuickTime:
http://developer.apple.com/documentation/QuickTime/WhatsNewQT6_4/Chap1/chapter_1_section_7.html
Note:
This sample will NOT run on Mac OS X 10.2.x (Jaguar) even with QuickTime 6.4 installed.
XCode 2.1 project builds universal binary.

[Next](main.m.md)

