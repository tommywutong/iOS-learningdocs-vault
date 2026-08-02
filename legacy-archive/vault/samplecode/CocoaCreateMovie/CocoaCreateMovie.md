---
title: CocoaCreateMovie
apple_id: DTS10000762
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: QTKit
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/CocoaCreateMovie/Introduction/Intro.html
archived_at: '2026-07-18T03:03:36.983575Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# CocoaCreateMovie

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 Demonstrates how to create a QuickTime movie from a set of Cocoa JPEG NSImage objects. |
| __Build Requirements:__ | Carbon |
| __Runtime Requirements:__ | Carbon |

This sample demonstrates how to create a QuickTime movie from a set of Cocoa jpeg NSImage objects. Specifically, the movie video track is built from the images. This is accomplished by creating a QuickDraw GWorld, copying the raw jpeg data from the NSImage into the GWorld, re-compressing the data using the QuickTime CompressImage function, and adding it to the video track of the movie. We use the NSBitmapImageRep -bitmapData method to access the raw jpeg NSImage data. The 24-bit image data is simply copied into the 32-bit GWorld (with zeros for the alpha component). Finally, the resulting movie is displayed in a window using the NSMovieView.

[Next](main.m.md)

