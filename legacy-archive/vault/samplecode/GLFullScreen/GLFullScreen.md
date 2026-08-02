---
title: GLFullScreen
apple_id: DTS40009820
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2010-12-01'
source_url: https://developer.apple.com/library/archive/samplecode/GLFullScreen/Introduction/Intro.html
archived_at: '2026-07-18T03:10:04.849367Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# GLFullScreen

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2010-12-01 Fixed a bug. Be sure to tell the display link to stop before destroying the context. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsobsgawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Mac OS X v10.6 or later, Xcode 3.1 or later |
| __Runtime Requirements:__ | Mac OS X v10.6 or later |

This sample code demonstrates OpenGL drawing to the entire screen.

Mac OS X 10.6 and later offer a simplified mechanism to create full-screen contexts. Earlier versions of Mac OS require additional work to capture the display and set up a special context.

When in the window mode, press the "Go FullScreen" button to switch to the full-screen mode;

When in the full-screen mode, press [ESC] to switch to the window mode;

In both modes, press [space] to toggle rotation of the globe; press [w]/[W] to toggle wireframe rendering; holding and dragging the mouse to change the roll angle and from which the light is coming.

[Next](ReadMe.txt.md)

