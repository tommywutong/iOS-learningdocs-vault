---
title: MeterTest
apple_id: DTS10000909
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-03-14'
source_url: https://developer.apple.com/library/archive/samplecode/MeterTest/Introduction/Intro.html
archived_at: '2026-07-18T03:14:59.120694Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](MeterTest.c.md)

# MeterTest

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-03-14 Sampling of sound input using SPBGetDeviceInfo(). Metering is then turned on and sampling is repeated. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon Sound Manager 3.2.1 or later |

This snippet demonstrates record metering through the use of SPBGetDeviceInfo() and SPBSetDeviceInfo() using the siLevelMeterOnOff selector. The code calls SPBSetDeviceInfo() to initially set metering to off, then does a quick sampling of sound input using SPBGetDeviceInfo(). Metering is then turned on and sampling is repeated. This is an SIOW application and could be done more elegantly using a graphical representation for sound input levels. But you get the idea. . . Requirements: Sound Manager 3.2.1 or later Keywords: sound, record, MeterTest

[Next](MeterTest.c.md)

