---
title: QTCarbonShell
apple_id: DTS10003611
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2009-03-19'
source_url: https://developer.apple.com/library/archive/samplecode/QTCarbonShell/Introduction/Intro.html
archived_at: '2026-07-18T03:20:01.976808Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.c.md)

# QTCarbonShell

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1.1, 2009-03-19 Minor editorial corrections. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnrrgewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 1.5+ |
| __Runtime Requirements:__ | Mac OS X 10.3.x, Mac OS X 10.4, QuickTime 6.x, QuickTime 7 |

A skeleton of a modern Carbon QuickTime application. QTCarbonShell is a simple QuickTime player framework demonstrating how to incorporate QuickTime Movie support into a Carbon application. The sample demonstrates playback, editing and saving of QuickTime Movies. It is NIB-based for user-interface elements and uses the Carbon Movie Controller. This sample supersedes the older Macintosh QTShell and qtshellCEvents samples.
NOTE: While the Carbon Movie Control is available on both Mac OS X 10.3.x w/ QuickTime 6.x or QuickTime 7 and Mac OS X 10.4+ w/QuickTime 7, if you're specifically targeting a Carbon QuickTime application for 10.4 or greater the preferred control for Movie playback is HIMovieView.
HIMovieView however, is not available on Mac OS X 10.3.x even with the latest version of QuickTime installed and may not be appropriate in every instance. Therefore using the Carbon Movie Control depending on the situation is quite valid. See TN2140 for a full description of the Carbon Movie Control.

[Next](main.c.md)

