---
title: BrideOfMungGrab
apple_id: DTS10003504
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2005-08-12'
source_url: https://developer.apple.com/library/archive/samplecode/BrideOfMungGrab/Introduction/Intro.html
archived_at: '2026-07-18T03:02:17.663595Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.c.md)

# BrideOfMungGrab

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0.1, 2005-08-12 This sample code has been updated to include a project that produces a universal binary. No code changes were required. |
| __Build Requirements:__ | Xcode 2.1, Xcode 1.5+ |
| __Runtime Requirements:__ | Mac OS 10.4, Mac OS X 10.3.x with QuickTime 7, iSight, DV Camera or QuickTime compatible capture device |

This sample runs the Sequence Grabber in record mode using a Sequence Grabber DataProc to get at the captured data. It also uses an Overlay Window and CoreGraphics to draw on top of the capture video.
This example is based on the SGDataProcSample (a companion sample to this one which contains Minimung, MungGrab and SonOfMungGrab).
While the code in the SGDataProcSample used an offscreen GWorld and some QuickDraw calls to draw text on top of video, this sample removes the need for the extra GWorld by using Overlay windows and Core Graphics to draw some text and graphics on top of the video image being captured.
The graphs in the upper left of the window display the following stats (shorter is better): Number of frames in the queue. Number of skipped frames. Difference between the TimeBase time and the dataProc frame time. Difference between the last frame time and the current frame time.
The status string prints out the time, a min:seconds:frames representation of time, frames per second and average frames per second. The dataProc in this case will also drop frames under certain situations.
Xcode 2.1 project builds universal binary.

[Next](main.c.md)

