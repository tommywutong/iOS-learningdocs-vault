---
title: FileNotification
apple_id: DTS10003143
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: CoreServices
published: '2005-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/FileNotification/Introduction/Intro.html
archived_at: '2026-07-18T03:08:30.416043Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](Main.c.md)

# FileNotification

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2005-10-27 Updated to produce a universal binary. No code changes were required. |
| __Build Requirements:__ | Xcode |
| __Runtime Requirements:__ | Mac OS X 10.3 |

Demonstrates how to use the kqueue mechanism to be notified when the contents of a folder change. Efficient method for detecting when a file is added, deleted, or renamed. This sample creates a simple MP thread which watches a few defined locations for modifications, then posts the event back to the main queue to display the relevant kevent information to the main window.

[Next](Main.c.md)

