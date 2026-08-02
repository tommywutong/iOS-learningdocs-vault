---
title: Movie Overlay
apple_id: DTS10000770
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AppKit
published: '2008-07-25'
source_url: https://developer.apple.com/library/archive/samplecode/Movie_Overlay/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:16:24.380341Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Movie Overlay](Movie%20Overlay.md)


[Next](main.m.md)[Previous](Movie%20Overlay.md)

# ReadMe.txt

```
READ ME

Movie Overlay
v1.1

This sample shows how to overlay text & graphics and perform animation on an QTMovieView through a floating "overlay" window. This is accomplished by first creating a new window and adding subviews to this window. These subviews are used to draw the images and perform the animation. The new overlay window is then added as a child window to the QTMovieView window with the NSWindowAbove ordering so it will be ordered on top of the movie window. Any subsequent drawing in the overlay window subviews will then draw on top of the QTMovieView window, giving the overlay effect we desire. 


*IMPORTANT*
While this technique is good for overlaying text & graphics on top of a QTMovieView, with Mac OS X 10.5 Leopard the recommended technique is to instead use a Core Animation layer-backed QTMovieView. For more information, see the Core Animation documentation. 

Also, the following sample code is available:

Core Animation QuickTime Layer
http://developer.apple.com/samplecode/CoreAnimationQuickTimeLayer/index.html

MyMovieFilter
http://developer.apple.com/samplecode/MyMovieFilter/
```

[Next](main.m.md)[Previous](Movie%20Overlay.md)

