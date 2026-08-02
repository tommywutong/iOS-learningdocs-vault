---
title: InstancedArrays
apple_id: DTS40010090
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2013-08-22'
source_url: https://developer.apple.com/library/archive/samplecode/InstancedArrays/Introduction/Intro.html
archived_at: '2026-07-18T03:12:59.169693Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](Readme.txt.md)

# InstancedArrays

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2013-08-22 Updated with Core Profile. Moved shader setup to -prepareOpenGL to ensure that the OpenGL framebuffer is valid at the time and thus avoid validation failure. Replaced the NSTimer with a CVDisplayLink to drive the rendering loop. Cleaned up code and removed static analyzer warnings. |
| __Build Requirements:__ | OS X v10.8 or later, Xcode 4.6 or later |
| __Runtime Requirements:__ | OS X v10.8 or later |

A common use case in OpenGL is to be able to draw a group of similar objects that share vertex data, primitive count and type, multiple times. The ARB_instanced_arrays extension provides a means of accelerating such use cases while minimizing the number of draw calls and the amount of duplicate data. This extension introduces an array "divisor" for generic vertex array attributes, which when non-zero specifies that the attribute is "instanced". An instanced attribute does not advance per-vertex as usual, but rather after every <divisor> instances are rendered.

This sample demonstrates how to use instancing. By specifying transform data in instanced attributes, one can, in concert with the instancing draw call, draw multiple instances of an object with one draw call.

[Next](Readme.txt.md)

