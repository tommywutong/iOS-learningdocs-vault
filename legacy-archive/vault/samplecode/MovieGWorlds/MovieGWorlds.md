---
title: MovieGWorlds
apple_id: DTS10000771
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-12-18'
source_url: https://developer.apple.com/library/archive/samplecode/MovieGWorlds/Introduction/Intro.html
archived_at: '2026-07-18T03:16:04.916601Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](carb.r.md)

# MovieGWorlds

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-12-18 Demonstrates movie drawing-complete functions, movie compositing and using SetTrackGWorld to draw into a specific graphics world. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon (both 9 and X) QuickTime 6 |

This sample contains 3 targets: MovieProc, MovieGWorlds and TrackGWorlds which demonstrate the following QuickTime programming techniques: - Assigning a drawing-complete function to a movie using the SetMovieDrawingCompleteProc function - Drawing movie content into a separate graphics world for compositing, then copying the result to the screen - Using the SetTrackGWorld function to force a track to draw into a particular graphics world. A Track-transfer procedure is specified here. When the movie is drawn, QuickTime calls the transfer callback to copy the track to the actual movie graphics world. Requirements: QuickTime 6 Keywords: drawing complete SetMovieDrawingCompleteProc track transfer SetTrackGWorld

[Next](carb.r.md)

