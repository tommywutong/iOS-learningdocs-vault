---
title: CocoaVideoFrameToGWorld
apple_id: DTS10000763
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/CocoaVideoFrameToGWorld/Introduction/Intro.html
archived_at: '2026-07-18T03:03:49.413264Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# CocoaVideoFrameToGWorld

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 Demonstrates how to draw each frame of a QuickTime movie into a Cocoa NSQuickDrawView. |
| __Build Requirements:__ | Mac OS X |
| __Runtime Requirements:__ | Mac OS X Mac OS X |

This sample demonstrates how to step frame-by-frame through a QuickTime movie using the GetNextInterestingTime function, drawing each frame of the movie into a GWorld using a decompression sequence. Finally, the contents of the GWorld are drawn into a Cocoa NSQuickDrawView. Simply launch the application, and at the prompt, select a movie file to display. Press the "NextFrame" button to advance frame-by-frame through the movie (note: for MPEG-4 movies the above technique will work, but not MPEG-1 or 2 because with these movie files all frames are treated as a single large sample in the movie). Requirements: Mac OS X Keywords: NSQuickDrawView video frame step GetNextInterestingTime

[Next](main.m.md)

