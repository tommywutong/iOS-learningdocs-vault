---
title: GLSL Basics Cocoa
apple_id: DTS10004403
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2008-07-30'
source_url: https://developer.apple.com/library/archive/samplecode/GLSLBasicsCocoaDL/Introduction/Intro.html
archived_at: '2026-07-18T03:10:10.545388Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# GLSL Basics Cocoa

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2008-07-30 Refactored the sample code to better demonstrate the interaction of OpenGL APIs with an OpenGL view. Moved the GLSL program object instantiation into its own basic class. Moved the GLSL hardware check code into its a separate file. Consistent use of float math library functions for pattern and palette generation. Animation continues during window resizing. Consistent use of doubles and their OpenGL equivalents during geometry generation. Updated the Xcode project to use the new format. Updated the NIB to use the new format. Added a simple GLUT string class. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbqgmwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 3.x |
| __Runtime Requirements:__ | Mac OS X 10.5 |

Demonstrates the use of GLSL fragment and vertex shaders using a custom NSOpenGLView. This application further demonstrates simple animation technique in a custom NSOpenGLView using a timer, a selector, and Cocoa "drawRect:" method.

[Next](ReadMe.txt.md)

