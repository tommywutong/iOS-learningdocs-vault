---
title: GLCarbonSharedPbuffer
apple_id: DTS10003149
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2004-03-26'
source_url: https://developer.apple.com/library/archive/samplecode/GLCarbonSharedPbuffer/Introduction/Intro.html
archived_at: '2026-07-18T03:09:54.856909Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.c.md)

# GLCarbonSharedPbuffer

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2004-03-26 Demostrates sharing a single OpenGL pixel buffer with multiple other contexts. |
| __Build Requirements:__ | Xcode |
| __Runtime Requirements:__ | Mac OS X v10.3 |

This is a simple sample showing the use of pixel buffers (pbuffers) on Mac OS X v10.3 Panther and later. It renders content into the off screen pbuffer and then uses this as the texture for drawing other objects in the application. In this example a single pbuffer is shared between multiple on screen contexts to provide a texture for all to use. The pbuffer has its own context and the on screen contexts are each associated with a window for their drawing. Texturing is accomplished through AGLs standard context object sharing mechanism. This sample also builds on the GLCarbonAGLWindow sample thus has much of the same support code. See that sample for more information on the surrounding supporting code.
One note when using multiple contexts will want to be followed. One should always flush (glFlush) or swap (aglSwapBuffers) between drawing to different contexts. This means if the scene is finished and you are using a double buffered context aglSwapBuffers should be called, otherwise ensure the commands sent are flushed prior to setting the current context to a different context and drawing.

[Next](main.c.md)

