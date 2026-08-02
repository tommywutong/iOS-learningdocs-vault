---
title: SoftVideoOutputComponent
apple_id: DTS10000811
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2005-08-10'
source_url: https://developer.apple.com/library/archive/samplecode/SoftVideoOutputComponent/Introduction/Intro.html
archived_at: '2026-07-18T03:24:57.075738Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](MachOPrefix.h.md)

# SoftVideoOutputComponent

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2005-08-10 Updated to produce a universal binary. Code changes are documented within the project. |
| __Build Requirements:__ | Xcode 2.1 and greater or CodeWarrior Pro 9.5 |
| __Runtime Requirements:__ | Mac OS X 10.4, or Mac OS X 10.3.9 with QuickTime 7 |

SoftVideoOutputComponent is a software implementation of a QuickTime Video Output Component and contains a companion sample QuickTime Transfer Codec called SoftCodec.
A video output component receives video data and delivers data to a video output hardware device for display. If the incoming data is in a format that the video output device can display directly, the video output component can simply send the data to the video output device. If the incoming data cannot be displayed directly, the video output component must use a transfer codec to convert the data to a format that the video output device can display.
A transfer codec is a specialized image decompressor component based on the Base Image Decompressor. It converts one of the supported QuickTime pixel formats to data that the hardware device can display. When this transfer codec is available, the QuickTime Image Compression Manager automatically uses it together with its built-in decompressors.
The companion to this sample is the SimpleVideoOut sample which demonstrates how QuickTime applications can use Video Output Components.
Xcode project builds universal binary.

[Next](MachOPrefix.h.md)

