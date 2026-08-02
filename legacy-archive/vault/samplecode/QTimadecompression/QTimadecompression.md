---
title: QTimadecompression
apple_id: DTS10000912
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QTimadecompression/Introduction/Intro.html
archived_at: '2026-07-18T03:21:23.717608Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](headers-DBFFErrors.h.md)

# QTimadecompression

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 Create a QuickTime atom to decompress IMA compressed WAVE files. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

This sample is designed to show you how to create the required QuickTime atom and send it to the IMA decompression codecs so that you can decompress IMA compressed WAVE files using the Sound Manager's SoundConvert routines and the QuickTime IMA codecs. This sample also shows a tecnique of playing a sound that doesn't rely on doing any work, other than setting a flag, at interrupt time. Use this tecnique if you want to be a friendly application, but not if you can't stand to have sound dropouts. The interesting bits are in PlaySound, DoIdle, and SoundCallBackFcn. While this code has a basic knowledge of the structure of a WAVE file, I would not use this code as a sample showing the most correct and complete way to parse a WAVE file.

[Next](headers-DBFFErrors.h.md)

