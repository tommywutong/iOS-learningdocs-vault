---
title: ThreadsImportMovie
apple_id: DTS10003224
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2005-07-26'
source_url: https://developer.apple.com/library/archive/samplecode/ThreadsImportMovie/Introduction/Intro.html
archived_at: '2026-07-18T03:26:49.440790Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# ThreadsImportMovie

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0.1, 2005-07-26 Updated to produce a universal binary. No code changes were required. |
| __Build Requirements:__ | Xcode 2.1 (for Universal Binary), Xcode 1.1+ |
| __Runtime Requirements:__ | Mac OS X 10.4.x, Mac OS X 10.3.x with QuickTime 6.4 or later. |

QuickTime 6.4 (on MacOS X 10.3 and later) introduces several new features that support execution of background tasks on multiple threads in a preemptive multitasking environment. This makes it possible to offload many tasks from your program's main thread to forestall blocking the user interface.
ThreadImportMovie demonstrates importing and displaying QuickTime Movies on separate threads. For demonstration purposes only, this sample will also allow the use of non-thread safe components on separate threads.
Xcode 2.1 Project builds Universal Binary
For more information see "Threaded Programming and QuickTime":
http://developer.apple.com/documentation/QuickTime/WhatsNewQT6_4/Chap1/chapter_1_section_7.html

[Next](main.m.md)

