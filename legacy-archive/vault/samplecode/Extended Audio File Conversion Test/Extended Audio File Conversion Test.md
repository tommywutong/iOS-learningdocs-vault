---
title: Extended Audio File Conversion Test
apple_id: DTS40009222
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2016-09-29'
source_url: https://developer.apple.com/library/archive/samplecode/iPhoneExtAudioFileConvertTest/Introduction/Intro.html
archived_at: '2026-07-18T03:29:40.014929Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ExtendedAudioFileConvertTest-main.m.md)

# Extended Audio File Conversion Test

|  |  |
| --- | --- |
| __Last Revision:__ | Version 5.0, 2016-09-29 Updated to use ARC and remove use of deprecated APIs [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmrsgiwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 8.0 or later; iOS 10.0 SDK or later |
| __Runtime Requirements:__ | iOS 10.0 or later. |

Demonstrates using ExtAudioFile API to convert from one audio format and file type to another.

Four encoding formats may be chosen in the UI along with different sample rates for the produced output.caf file. AAC encoding requires both iOS 3.1 or later and a hardware capable device such as the iPhone 3GS or later. If run on a device which does not support AAC encoding at all, the AAC encoding choice will be dimmed.

Interruption handling during processing is also demonstrated. Hardware assisted encoding requires specific interruption handling since the codec state may change due to the interruption.

All the relevant audio specific code is in the file ExtAudioFileConvert.cpp.

[Next](ExtendedAudioFileConvertTest-main.m.md)

