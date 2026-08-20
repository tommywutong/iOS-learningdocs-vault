---
title: GLEssentials
apple_id: DTS40010104
resource_type: Sample Code
platform: iOS|macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-08-07'
source_url: https://developer.apple.com/library/archive/samplecode/GLEssentials/History/History.html
archived_at: '2026-07-18T03:10:01.190845Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLEssentials](GLEssentials.md)


[Previous](LICENSE.txt.md)

# Document Revision History

This table describes the changes to _GLEssentials_.

| __Date__ | __Notes__ |
| 2015-08-07 | Updated to use storyboards, ARC, and modern App coding practices. |
| 2018-06-07 | Updated to use storyboards, ARC, and modern App coding practices. |
| 2013-07-09 | Changes in this version include: 1) WIth OSX demonstrate going to fullscreen and back. Add window controller and fullscreen window classes. When the user types the 'F' key, the window controller hides the non-fullscreen window, creates a fullscreen window, and sets the OpenGL view this new fullscreen window. 2) Add support for retina displays on OSX. Call [NSOpenGLView setsWantsBestResolutionOpenGLSurface:YES] at view init. Also use [NSView convertRectToBacking] in order to get the OpenGL surface size in pixels not points, allowing the app to properly set the viewport and make other pixel dimension based calculations. 3) Fix flickering on window resize on OSX. Implement the [NSOpenGView drawRect:] in our OpenGL View so that we continue rendering as resize occurs. Also implement [NSOpenGView renewGState] with a calls to [NSwindow disableScreenUpdatesUntilFlush]. This will synchronize our rendering with that of other rendering in the system and avoid flickering and tearing. 4) Fix problem where OpenGL Errors were reported after closing the window on OSX(but not quitting the app) since the display link was still active, spawning rendering without any drawable present. To fix this, add the view to the notification center for a windowWillClose event which allows us to stop the display link and terminate our rendering. 5) On OSX, add example of kCGLCECrashOnRemovedFunctions to demonstrate how we can force a crash if a legacy function is called in a Core Profile context. This allows us to quickly see erroneous usage of legacy OpenGL without having to check for errors. 6) Make iOS App Universal. 7) Simplify clean up of shaders. Delete the shader objects after they've been attach to a GLSL program, which won't actually delete the shaders until the GLSL program is delated. 8) Use auto-synthesis for properties. |
| 2012-12-05 | Fix various bugs in matrix and vector utility functions. Fix issues found by static analyzer. Update Support for iOS 6.0 and iPhone 5 |
| 2012-01-25 | Fixed a number of issues found when building with XCode 4.2 and Clang. Fixed an issue with stopping CVDisplayLink after releasing classes called during the display link callback resulting in an occasional crash on exit Added demonstration of using the OpenGL 3.2 Core Profile. |
| 2011-03-09 | Demonstrates obtaining and using an OpenGL 3.2 context on Mac OS X Lion. |
| 2011-02-08 | First public release. |

[Previous](LICENSE.txt.md)

