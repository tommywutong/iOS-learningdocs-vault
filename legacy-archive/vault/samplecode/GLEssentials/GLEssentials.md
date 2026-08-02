---
title: GLEssentials
apple_id: DTS40010104
resource_type: Sample Code
platform: iOS|macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-08-07'
source_url: https://developer.apple.com/library/archive/samplecode/GLEssentials/Introduction/Intro.html
archived_at: '2026-07-18T03:10:01.229129Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](GLEssentials-Source-main.m.md)

# GLEssentials

|  |  |
| --- | --- |
| __Last Revision:__ | Version 3.0, 2015-08-07 Updated to use storyboards, ARC, and modern App coding practices. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytamjqgqwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | OS X 10.8 or later. Xcode 5 or later. iOS SDK 5.0 or later. |
| __Runtime Requirements:__ | OS X 10.8 or later. iOS 5.0 or later (with OpenGL ES 2.0 support). |

This sample provides an example of some essential OpenGL functionality. There are usages of Vertex Buffer Objects (VBOs), Vertex Array Objects (VAOs), Framebuffer Objects (FBO), and GLSL Program Objects. It creates a VAO and VBOs from model data loaded in. It creates a texture for the model from image data
and GLSL shaders from source also loaded in. It also creates an FBO and texture to render a reflection of the model. It uses an environment mapping GLSL program to apply the reflection texture to a plane. This sample also demonstrates sharing of OpenGL source code between iOS and OS X. Additionally, it implements fullscreen rendering, retina display support, and demonstrates how to obtain and use an OpenGL Core Profile rendering context on OS X.

[Next](GLEssentials-Source-main.m.md)

