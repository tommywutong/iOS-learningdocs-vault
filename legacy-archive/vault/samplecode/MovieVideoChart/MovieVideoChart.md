---
title: MovieVideoChart
apple_id: DTS10003678
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2006-07-11'
source_url: https://developer.apple.com/library/archive/samplecode/MovieVideoChart/Introduction/Intro.html
archived_at: '2026-07-18T03:16:19.286056Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.c.md)

# MovieVideoChart

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0.1, 2006-07-11 Corrected edit label enumeration [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnrxhawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 2.1 or later |
| __Runtime Requirements:__ | Mac OS X 10.4 |

Displays a scrolling chart showing the internal structure of a movie's video track. Frame thumbnails are displayed in decode order, display order, and track order; the reordering due to display offsets and track edits is illustrated. Information about individual samples is obtained using GetMediaSample2; information about many samples is obtained at once by using CopyMediaMutableSampleTable. Frames are decompressed at thumbnail size using ICMDecompressionSessions.
Xcode 2.1 project builds universal binary.

[Next](main.c.md)

