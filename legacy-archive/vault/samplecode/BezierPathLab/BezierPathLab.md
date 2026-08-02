---
title: BezierPathLab
apple_id: DTS40008880
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: AppKit
published: '2012-06-05'
source_url: https://developer.apple.com/library/archive/samplecode/BezierPathLab/Introduction/Intro.html
archived_at: '2026-07-18T03:01:53.074872Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](BezierPathLabmain.m.md)

# BezierPathLab

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2012-06-05 Updated for Mac OS X 10.7 [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqobygawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 4.0 or later, Mac OS X v10.7 or later |
| __Runtime Requirements:__ | Mac OS X v10.7 or later |

BezierPathLab is a simple example demonstrating some of the features of NSBezierPath. Various features of NSBezierPath are used to create the different line patterns and cap styles. NSGraphicsContext and NSAffineTransform are used to rotate the path.

The buttons, sliders, and color wells are used to set the attributes of the path. Their actions are sent to a subclass of NSView, BezierView, which manages all the attributes of the bezier path. This subclass overrides the -drawRect: method to apply the various settings to the path and draw the path to the view.

[Next](BezierPathLabmain.m.md)

