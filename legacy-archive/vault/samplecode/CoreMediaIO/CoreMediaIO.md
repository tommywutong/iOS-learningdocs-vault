---
title: CoreMediaIO
apple_id: DTS40012293
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: null
published: '2012-10-23'
source_url: https://developer.apple.com/library/archive/samplecode/CoreMediaIO/Introduction/Intro.html
archived_at: '2026-07-27T06:57:02.125813Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# CoreMediaIO

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2012-10-23 Demonstrate the usage of an IOSurface-backed CVPixelBufferRef in CMIO::DP::Sample::Stream::GetOutputBuffer(). [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytemrzgmwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Mac OS X v10.7.4 or later, and Xcode 4.4. |
| __Runtime Requirements:__ | Mac OS X v10.7.4 or later |

The CoreMediaIO Device Abstraction Layer (DAL) is analogous to CoreAudio’s Hardware Abstraction Layer (HAL). Just as the HAL deals with audio streams from audio hardware, the DAL handles video (and muxed) streams from video devices. This SDK will demonstrate how to create a user-level DAL plugIn, a user-level “assistant” server process that allows the device to vend its video data to several processes at once, and a kernel extension (KEXT) for manipulating the device’s hardware.

[Next](ReadMe.txt.md)
