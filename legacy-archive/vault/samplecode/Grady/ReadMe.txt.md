---
title: Grady
apple_id: DTS10004135
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: AppKit
published: '2012-03-21'
source_url: https://developer.apple.com/library/archive/samplecode/Grady/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:10:56.832962Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Grady](Grady.md)


[Next](main.m.md)[Previous](Grady.md)

# ReadMe.txt

```objc
Grady
=====

"Grady" is a Cocoa sample application that demonstrates how to use the NSGradient class.  The NSGradient class provides support for drawing gradient fill colors, also known as shadings in Quartz.  This class provides convenience methods for drawing radial or linear (axial) gradients for rectangles and NSBezierPath objects.  This sample is intended to show how to use the different features and aspects of this rendering class which include using the methods:

    - (void)drawInRect:(NSRect)rect angle:(CGFloat)angle
    Fills the specified rectangle with a linear gradient at a particular angle (in degrees).

    - (void)drawInRect:(NSRect)rect relativeCenterPosition:(NSPoint)relativeCenterPosition;
    Draws a radial gradient gradient starting at the center of the specified rectangle.

    - (void)drawInBezierPath:(NSBezierPath*)path angle:(CGFloat)angle;
    Fills the specified path with a linear gradient at a particular angle (in degrees).

    - (void)drawInBezierPath:(NSBezierPath*)path relativeCenterPosition:(NSPoint)relativeCenterPosition
    Draws a radial gradient starting at the center point of the specified path.

All renderings are performed using a start and end color specified by the user.
Radial gradient rendering can be altered by changing the center position using the mouse.


Sample Requirements
The supplied Xcode project was created using Xcode v4.3 or later running under Mac OS X 10.7.x or later.


Using the Sample
Simply build and run the sample using Xcode.


Changes from Previous Versions
1.1 - Upgraded to Xcode 4.3 and Mac OS X 10.7.
1.0 - First Version

Copyright (C) 2006-2012, Apple Inc.
```

[Next](main.m.md)[Previous](Grady.md)

