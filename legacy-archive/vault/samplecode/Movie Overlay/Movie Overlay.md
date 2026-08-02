---
title: Movie Overlay
apple_id: DTS10000770
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AppKit
published: '2008-07-25'
source_url: https://developer.apple.com/library/archive/samplecode/Movie_Overlay/Introduction/Intro.html
archived_at: '2026-07-18T03:16:23.985145Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# Movie Overlay

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2008-07-25 Updated for QTMovieView. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydanzxgawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 2.5, Mac OS X 10.4 Tiger |
| __Runtime Requirements:__ | Mac OS X 10.4 Tiger |

This sample shows how to overlay text & graphics and perform animation on an QTMovieView through a floating overlay window. This is accomplished by first creating a new window and adding subviews to this window. These subviews are used to draw the images and perform the animation. The new overlay window is then added as a child window to the QTMovieView window with the NSWindowAbove ordering so it will be ordered on top of the movie window. Any subsequent drawing in the overlay window subviews will then draw on top of the QTMovieView window, giving the overlay effect.

[Next](ReadMe.txt.md)

