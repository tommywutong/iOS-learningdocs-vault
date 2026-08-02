---
title: GLChildWindowDemo
apple_id: DTS10000526
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2003-04-21'
source_url: https://developer.apple.com/library/archive/samplecode/GLChildWindowDemo/Introduction/Intro.html
archived_at: '2026-07-18T03:09:58.142507Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# GLChildWindowDemo

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-04-21 Shows using Cocoa's child windows and Quartz Extreme to provide 2D/3D overlays above 3D content. |
| __Build Requirements:__ | Mac OS X ProjectBuilder |
| __Runtime Requirements:__ | Mac OS X 10.2 or later. |

This demo shows off a way of using Cocoa's child windows along with Quartz Extreme to provide 2D or 3D overlays above 3D content. The user interface is fairly straightforward, with some colorwell objects on the right to let you play with the OpenGL lighting on the cube, a radio button to switch between 2D and 3D overlay, and a checkbox to make the background of the 3D cube view opaque or transparent. The 2D and 3D overlay views both do basically the same thing, except that the 2D code also does a little bit of text rendering. The DemoOverlayView superclass handles the line animation, while the Demo2DOverlayView and DemoGLOverlayView subclasses handle the actual drawing for the two different rendering APIs. Probably the most interesting code lives in the NSViewOverlays.m source file. This code contains a number of utility NSWindow and NSView subclasses that help implement a category on NSView that adds the ability to transparently add an "overlay" view to another view. The API is actually very small and should be obvious in it's use (check out NSViewOverlays.h for the API). Getting everything right can be a little bit tricky, and this code goes to great lengths to ensure a flicker-free display when resizing the content along with the child windows. This app uses a convenient call in Carbon.framework that can be used to temporarily disable screen updates while we repaint a number of windows and views. Once that's done, screen updates are re-enabled and everything is updated on the screen at once. Comments and bugs are welcome at: <http://developer.apple.com/bugreporter> Requirements: ProjectBuilder, Mac OS X 10.2 or later. Keywords: OpenGL, Cocoa, child window

[Next](ReadMe.txt.md)

