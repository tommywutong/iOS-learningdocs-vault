---
title: QT QDesign decomp
apple_id: DTS10000911
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QT_QDesign_decomp/Introduction/Intro.html
archived_at: '2026-07-18T03:21:23.034386Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](headers-AIFF.h.md)

# QT QDesign decomp

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 Decompressing QDesign compressed files using the Sound Manager's SoundConvert routines and QuickTime QDesign codecs. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

QDesign decompression information: Version 1.0.1 fixes a hard coded constant, the source format (inputFormat.format), to be read from the AIFF file decompression atom instead. This fixes a bug where not all QDesign sounds would decompress. This sample is designed to show you how to create the required QuickTime atom and send it to the QDesign decompression codecs so that you can decompress QDesign compressed AIFF files using the Sound Manager's SoundConvert routines and the QuickTime QDesign codecs. This sample also shows a tecnique of playing a sound that doesn't rely on doing any work, other than setting a flag, at interrupt time. Use this tecnique if you want to be a friendly application, but not if you can't stand to have sound dropouts. The interesting bits are in PlaySound and SoundCallBackFcn.

[Next](headers-AIFF.h.md)

