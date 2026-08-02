---
title: QTKitCreateMovie
apple_id: DTS10003671
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: QTKit
published: '2007-08-31'
source_url: https://developer.apple.com/library/archive/samplecode/QTKitCreateMovie/Introduction/Intro.html
archived_at: '2026-07-18T03:20:53.737967Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# QTKitCreateMovie

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2007-08-31 Added support for the new initToWritableFile: method available in QuickTime 7.2.1. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnrxgewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Mac OS X 10.4, Xcode 2.4 |
| __Runtime Requirements:__ | Mac OS X 10.4, QuickTime 7 |

The QTKitCreateMovie sample demonstrates how to create a QuickTime movie from a series of jpeg images using the QTKit APIs. This is accomplished by creating an "empty" movie, using the -addImage: method to add images to the movie, and finally using the -updateMovieFile: method to save the movie to a file on disk (or flattening the movie to a different file with the -writeToFile method).

[Next](main.m.md)

