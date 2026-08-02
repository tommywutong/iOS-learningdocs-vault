---
title: VideoHardwareInfo
apple_id: DTS10003442
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2007-05-14'
source_url: https://developer.apple.com/library/archive/samplecode/VideoHardwareInfo/Introduction/Intro.html
archived_at: '2026-07-18T03:27:50.731194Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# VideoHardwareInfo

|  |  |
| --- | --- |
| __Last Revision:__ | Version 2.0, 2007-05-14 The extensions list now reflects the display selected in the popup, not just the main display. Added support for checking for Quartz Extreme, GLSL and the GLSL version. Cleaned up the UI. Updated to Xcode and Universal Binary. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbugiwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | XCode 2.4 |
| __Runtime Requirements:__ | Mac OS X 10.3 or later |

Applications may need to query the system about VRAM, video hardware, Quartz Extreme support, OpenGL extensions and renderer, GLSL version and support so that they can determine which output devices are best suited for their needs. VideoHardwareInfo shows how to query the system for these properties, and how to be notified about changes to the display configuration.

[Next](main.m.md)

