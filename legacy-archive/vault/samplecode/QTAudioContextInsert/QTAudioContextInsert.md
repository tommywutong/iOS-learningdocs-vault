---
title: QTAudioContextInsert
apple_id: DTS10003981
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2008-01-21'
source_url: https://developer.apple.com/library/archive/samplecode/QTAudioContextInsert/Introduction/Intro.html
archived_at: '2026-07-18T03:19:53.340109Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](README.txt.md)

# QTAudioContextInsert

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.3, 2008-01-21 Editorial [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgojygewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 3.0 |
| __Runtime Requirements:__ | Mac OS X 10.5 |

This sample demonstrates how a client application of QuickTime can use the Audio Context Insert APIs to hook in a custom audio processing unit into QuickTime's audio processing chain. By hooking in an insert, an application is able to tap into and optionally manupulate QuickTime's audio stream during playback to device or during extraction of movie audio. Inserts may be attached at the movie or individual track level.

The sample code seeks to establish good practices in using the new APIs. It illustrates steps involved in configuring and registering an insert with the movie or track whose audio data is to be tapped and/or processed.Â The code gives example implementations of the three callbacks - reset , process data, finalize - that need to implemented by an insert's processing logic. Finally, the sample code shows the steps involved in applying an insert to audio being extracted through QuickTime's Movie Audio Extraction APIs.

[Next](README.txt.md)

