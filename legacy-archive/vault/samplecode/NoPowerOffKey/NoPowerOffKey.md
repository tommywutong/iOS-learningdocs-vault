---
title: NoPowerOffKey
apple_id: DTS10000018
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/NoPowerOffKey/Introduction/Intro.html
archived_at: '2026-07-18T03:17:04.400585Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](PatchPowerOff.c.md)

# NoPowerOffKey

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon System 7.5 |

NoPowerOffKey is a sample extension to disable the power-off key. Starting with System 7.5, you can turn off power by pressing the power key, just as you turn on the Macintosh by pressing the power key. This behavior isn't appropriate for some classroom or kiosk settings. Starting with System 7.5.3, there is a programmatic way to turn off the power-off key behavior. This sample uses that call if it is available. This is the technique recommended by DTS. However if the call is unavailable, the sample patches Alert. NOTE: DTS does NOT recommend the patch on Alert, but realizes there may be an unavoidable reason to consider it. Requirements: System 7.5 Keywords: Power Key, kiosk, NoPowerOffKey

[Next](PatchPowerOff.c.md)

