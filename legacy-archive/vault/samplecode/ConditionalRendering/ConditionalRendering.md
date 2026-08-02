---
title: ConditionalRendering
apple_id: DTS40010087
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2014-06-17'
source_url: https://developer.apple.com/library/archive/samplecode/ConditionalRendering/Introduction/Intro.html
archived_at: '2026-07-18T03:04:13.494936Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](Readme.txt.md)

# ConditionalRendering

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2014-06-17 Updated with Core Profile and GLKit Math Utilities. Moved shader setup to -prepareOpenGL to ensure that the OpenGL framebuffer is valid at the time and thus avoid validation failure. Replaced the NSTimer with a CVDisplayLink to drive the rendering loop. Cleaned up code. |
| __Build Requirements:__ | OS X v10.9 or later, Xcode 5.0 or later |
| __Runtime Requirements:__ | OS X v10.7 or later |

This sample demonstrates how to do conditional rendering based on an occlusion query. The NV_conditional_render extension defines two functions, BeginConditionalRenderNV and EndConditionalRenderNV, between which rendering commands may be discarded based on the results of an occlusion query. If the specified occlusion query returns a non-zero value, rendering commands between these calls are executed; otherwise, they are all discarded.

[Next](Readme.txt.md)

