---
title: AppList
apple_id: DTS40008859
resource_type: Sample Code
platform: macOS
topic: General
technology: AppKit
published: '2014-05-06'
source_url: https://developer.apple.com/library/archive/samplecode/AppList/Introduction/Intro.html
archived_at: '2026-07-18T03:01:06.755131Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# AppList

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2014-05-06 Upgrade for Xcode 5.0, OS X 10.9, now uses ARC (Automatic Reference Counting) and Auto Layout. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqobvhewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 5.0, OS X 10.9 |
| __Runtime Requirements:__ | OS X 10.8 or later |

"AppList" is a Cocoa sample application that demonstrates how to use the NSRunningApplication class provided by NSWorkspace. NSRunningApplication can be used for inspecting and manipulating running applications on the system. An array of these objects can be obtained from NSWorkspace, by doing:

NSArray \*appList = [[NSWorkspace sharedWorkspace] runningApplications];

Only user applications can be tracked; this does not provide information about every process on the system.

[Next](ReadMe.txt.md)

