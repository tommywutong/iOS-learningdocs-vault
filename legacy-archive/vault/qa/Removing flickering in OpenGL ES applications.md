---
title: Removing flickering in OpenGL ES applications
apple_id: DTS40009769
resource_type: QA
platform: iOS
topic: Graphics & Animation
technology: OpenGLES
published: '2010-03-24'
source_url: https://developer.apple.com/library/archive/qa/qa1650/_index.html
archived_at: '2026-07-18T02:33:17.303450Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1650

# Removing flickering in OpenGL ES applications

## Q:  My OpenGL ES application flickers. Especially when running on iPhone 3GS, the flickering seems to happen every frame. How do I fix this problem?

A: My OpenGL ES application flickers. Especially when running on iPhone 3GS, the flickering seems to happen every frame. How do I fix this problem?

By default, the contents of a renderbuffer are invalidated after it is presented to the screen (by calling `-EAGLContext/presentRenderbuffer:`). Your application must completely redraw the contents of the renderbuffer every time you draw a frame, otherwise you may observe flickering or other unexpected results.

You must provide a color to every pixel on the screen. At the beginning of your drawing code, it is a good idea to use `glClear()` to initialize the color buffer. A full-screen clear of each of your color, depth, and stencil buffers (if you're using them) at the start of a frame can also generally improve your application's performance.

If your application needs to preserve the drawable contents between frames, you can add the option `kEAGLDrawablePropertyRetainedBacking = YES` to your `CAEAGLLayer` object's `drawableProperties` property. Using this option requires additional memory and can reduce your application's performance.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-03-24 | New document that demonstrates how to solve the flickering problem in OpenGL ES applications |

