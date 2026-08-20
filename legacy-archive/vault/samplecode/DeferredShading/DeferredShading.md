---
title: DeferredShading
apple_id: DTS40010088
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2015-07-08'
source_url: https://developer.apple.com/library/archive/samplecode/DeferredShading/Introduction/Intro.html
archived_at: '2026-07-18T03:06:11.108287Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# DeferredShading

|  |  |
| --- | --- |
| __Last Revision:__ | Version 2.0, 2015-07-08 Updated to OpenGL Core Profile, Xcode 10.10 SDK. |
| __Build Requirements:__ | OS X 10.10 SDK or later |
| __Runtime Requirements:__ | OS X 10.8 or later |

This example demonstrates deferred shading. In deferred shading, no shading is performed in the first pass of the vertex and pixel shaders. Shading is deferred until a second pass. On the first pass, information needed for shading (position, normal, depth, albedo) are rendered into the geometry buffer (G-buffer) as a series of textures. After this, a pixel shader computes the direct and indirect lighting at each pixel using the information of the texture buffers in screen space.

[Next](main.m.md)

