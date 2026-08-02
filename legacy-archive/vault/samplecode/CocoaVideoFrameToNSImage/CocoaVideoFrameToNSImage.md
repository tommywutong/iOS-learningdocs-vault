---
title: CocoaVideoFrameToNSImage
apple_id: DTS10000764
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/CocoaVideoFrameToNSImage/Introduction/Intro.html
archived_at: '2026-07-18T03:03:49.955351Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# CocoaVideoFrameToNSImage

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 Demonstrates how to create an NSImage for each frame of a QuickTime movie. |
| __Build Requirements:__ | Mac OS X |
| __Runtime Requirements:__ | Mac OS X Mac OS X |

This sample demonstrates how to step frame-by-frame through a QuickTime movie using the GetNextInterestingTime function, drawing each frame of the movie into a GWorld using a decompression sequence. The contents of the GWorld are then converted into a NSImage object. Finally, the NSImage is composited with a background image and drawn into a NSQuickDrawView using the NSImage drawRect method. Simply launch the application, and press the "NextFrame" button to advance frame-by-frame through the movie (note: for MPEG-4 movies the above technique will work, but not MPEG-1 or 2 because with these movie files all frames are treated as a single large sample in the movie). Requirements: Mac OS X Keywords: NSQuickDrawView NSImage GetNextInterestingTime video frame step

[Next](main.m.md)

