---
title: glFlush() vs. glFinish()
apple_id: DTS10003299
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2004-10-11'
source_url: https://developer.apple.com/library/archive/qa/qa1158/_index.html
archived_at: '2026-07-18T02:29:59.601103Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1158

# glFlush() vs. glFinish()

## Q:  What's the difference between `glFlush`() and `glFinish`()?

A: OpenGL commands are not executed immediately. Instead, they are submitted to a command buffer that is then fed into to the hardware. The `glFlush`() and `glFinish`() commands are both used to force submission of the command buffer to the hardware for execution. `glFlush`() causes all OpenGL commands currently queued to be submitted to the hardware for execution. This function returns immediately after having transferred the pending OpenGL command queue to the hardware (or software) renderer. These commands are queued for execution in some finite amount of time, but `glFlush`() does not block waiting for command completion.

`glFinish`() has the same effect as `glFlush`(), with the addition that `glFinish`() will block until all commands submitted have been executed. The entire command stream sent to the hardware (or software) renderer is guaranteed to finish execution before `glFinish`() will return.

Care must be taken when using these two functions on Mac OS X due to the asynchronous nature of the Window Server. Visual anomalies may occur if `glFlush`() or `glFinish`() are used inappropriately, as MacOS X's windowing system update mechanism is asynchronous. Partially rendering a scene, followed by a call to `glFlush`() or introducing unnecessary synchronization points with `glFinish`(), can result in the windowing system compositing incorrect draw buffer pixels onto the screen, resulting in flickering or other visual anomalies. This occurs because when a screen update is needed, the window server will asynchronously fetch data from the window's back buffer.

Given the design and operation of the Mac OS X Window Server, it is best to keep the back buffer as current as possible with a complete scene. Since `glFlush`() and `glFinish`() force processing of OpenGL commands submitted, calling either of these after drawing an incomplete scene may result in that scene being rendered in the back buffer, with which the window server may asynchronously update the screen. Obviously, this would cause flickering or flashing as the partially rendered scene is drawn to the screen.

Additionally, if `glFlush`() or `glFinish`() is called when the window server needs to update the front buffer, an implicit swap will take place. This will happen regardless of whether or not the application makes a call to its buffer swapping function (`aglSwapBuffer()` in Carbon, `-flushBuffer` in Cocoa or `cglFlushDrawable()` in CGL). In NSOpenGL and CGL, the term "flush" actually refers to a buffer swap and not just a `glFlush`().

As a general rule for double buffered contexts, the current OpenGL command buffer will not be sent to the graphics processor until `glFlush`() or `glFinish`() is called, a buffer swap is requested or the command buffer is full. This also applies to single buffered contexts, although executing a buffer swap is really just an implicit `glFlush`() to submit the command stream to the hardware. This means that `glFlush`() and `glFinish`() commands are equivalent to a swap, since all rendering is taking place directly in the front buffer. For reference, the command buffer itself is approximately 500k in size and is used for vertices, normals, texture coordinates, etc. but not textures themselves, which are stored "out of line".

In general, most applications will not have to use `glFlush`() or `glFinish`() to perform the normal task of getting image data to the screen. However, there are several cases that absolutely require the use of `glFlush`() and/or `glFinish`() in order to behave properly. One such instance is when an OpenGL application is multithreaded. To keep drawing synchronized across the threads and prevent command buffer corruption, as each thread completes its command submissions it should finish with a call to `glFlush`(). Another such instance is where the drawable is changed during rendering. Before the drawable can be successfully switched to another drawable, a call must be made to `glFlush`() to ensure that all the commands written to the previous drawable's command buffer have been successfully submitted.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2004-10-11 | New document that explanation of the differences between glFlush() and glFinish() |

