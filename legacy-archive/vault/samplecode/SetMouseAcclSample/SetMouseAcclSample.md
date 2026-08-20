---
title: SetMouseAcclSample
apple_id: DTS10003957
resource_type: Sample Code
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2006-11-28'
source_url: https://developer.apple.com/library/archive/samplecode/SetMouseAcclSample/Introduction/Intro.html
archived_at: '2026-07-18T03:23:41.802472Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# SetMouseAcclSample

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2006-11-28 Find HID System Manager and get/set cursor acceleration |
| __Build Requirements:__ | Xcode 2.2.1 running Mac OS X 10.4.6 and will create a Universal Binary application. The sample should be buildable using Xcode 2.2 running Mac OS X 10.4.x to create a version of the application for Power PC based Macintosh systems. |
| __Runtime Requirements:__ | The supplied sample application runs as is on Mac OS X 10.2.8 and greater on both Power PC and Intel based Macintosh systems. |

Cocoa based sample to demonstrate how to find the HID System Manager. The HID System Manager is used to control the cursor acceleration curve among other actions which can be controlled by functions defines in IOHIDLib.h. Setting the cursor acceleration with the HIS System Manager affects all relative positioning devices attached to the system (e.g Portable trackpad, as well as attached USB mouse).

[Next](main.m.md)

