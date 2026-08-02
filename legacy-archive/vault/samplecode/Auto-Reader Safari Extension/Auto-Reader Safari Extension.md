---
title: Auto-Reader Safari Extension
apple_id: DTS40011101
resource_type: Sample Code
platform: Safari|macOS
topic: General
technology: null
published: '2011-06-05'
source_url: https://developer.apple.com/library/archive/samplecode/AutoReaderSafariExtension/Introduction/Intro.html
archived_at: '2026-07-18T03:01:35.841543Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# Auto-Reader Safari Extension

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2011-06-05 This extension triggers Safari Reader programmatically, without user action. |
| __Build Requirements:__ | Safari v5.1 or later |
| __Runtime Requirements:__ | Safari v5.1 or later |

This extension enters Safari Reader automatically by listening for and responding to the "available" event. The available event is sent with Reader as the target in the Application Layer when it is determined that Reader is available for the contents of a tab. When an extension listens for the available event, it can automatically enter Reader for every page for which Reader is available.

[Next](ReadMe.txt.md)

