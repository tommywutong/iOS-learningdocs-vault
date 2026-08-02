---
title: ThreadsExportMovie
apple_id: DTS10003172
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2006-01-03'
source_url: https://developer.apple.com/library/archive/samplecode/ThreadsExportMovie/Introduction/Intro.html
archived_at: '2026-07-18T03:26:46.751820Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# ThreadsExportMovie

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0.2, 2006-01-03 Removed specific check for progressOpExportMovie in the movie export progress procedure which caused premature export termination with QT 7.0.3+. |
| __Build Requirements:__ | Xcode 2.1+ (for Universal Binary), Xcode 1.0 or later. |
| __Runtime Requirements:__ | Mac OS X 10.4.x, Mac OS X 10.3.x with QuickTime 6.4 or later. |

ThreadExportMovie is a Cocoa sample which demonstrates exporting Movies using the QuickTime Movie Export Component on separate threads.
Xcode 2.1 Project builds universal binary.
Note: This sample requires Xcode 1.0 or later, Mac OS X 10.3 (Panther) or later with QuickTime 6.4 or later. It will not run on Mac OS X 10.2.x (Jaguar) even with QuickTime 6.4.
QuickTime 6.4 (on MacOS X 10.3 and later) introduces several new features that support execution of background tasks on multiple threads in a preemptive multitasking environment. This makes it possible to offload many tasks from your program's main thread to forestall blocking the user interface.
For more information see "Threaded Programming and QuickTime": http://developer.apple.com/documentation/QuickTime/WhatsNewQT6_4/Chap1/chapter_1_section_7.html

[Next](main.m.md)

