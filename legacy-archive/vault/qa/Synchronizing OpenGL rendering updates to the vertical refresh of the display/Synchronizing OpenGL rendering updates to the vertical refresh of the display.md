---
title: Synchronizing OpenGL rendering updates to the vertical refresh of the display
apple_id: DTS10004262
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2007-07-16'
source_url: https://developer.apple.com/library/archive/qa/qa1521/_index.html
archived_at: '2026-07-18T02:32:05.186643Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1521

# Synchronizing OpenGL rendering updates to the vertical refresh of the display

## Q:  How do I avoid tearing in OpenGL?

A: Tearing is a visual artifact that occurs when the display begins reading from a buffer before your application's rendering to that buffer has completed.

You can use the swap interval context parameter to avoid tearing. This parameter is zero by default. If you set it to a non-zero value, OpenGL will synchronize buffer swaps with a vertical retrace event.

One potential reason to have a zero swap interval is to measure the maximum possible number of frames that can be rendered within a given time. This is because setting swap interval to a non-zero value caps the effective frame rate of your application to an integer divisor of the display's refresh rate. For instance, if your application can complete its rendering within one display refresh period, the frame rate will be capped at the refresh rate. If, however, your application takes longer than one refresh period, then the buffer swap will have to wait until the next refresh event. This effectively drops your frame rate to 1 / [time to render a frame rounded up to nearest vertical retrace period].

Listing 1 shows how to enable and disable synchronization in an NSOpenGLContext.

__Listing 1__  Synchronizing buffer swaps to VBL in an NSOpenGLView.

```
long swapInterval = 1; // request synchronization
//long swapInterval = 0; // disable synchronization

[[self openGLContext] setValues:&swapInterval forParameter: NSOpenGLCPSwapInterval];
```


Listing 2 shows how to enable and disable synchronization using the AGL API.

__Listing 2__  Synchronizing buffer swaps to VBL in the current AGL Context.

```
long swapInterval = 1; // request synchronization
//long swapInterval =0; // disable synchronization

AGLContext ctx = aglGetCurrentContext();
if (NULL != ctx) aglSetInteger(ctx, AGL_SWAP_INTERVAL, &swapInterval);
```


Listing 3 shows how to enable and disable synchronization using the CGL API.

__Listing 3__  Synchronizing buffer swaps to VBL in the current CGL Context

```
long swapInterval = 1; // request synchronization
//long swapInterval = 0; // disable synchronization

CGLContextObj ctx = CGLGetCurrentContext();
if (NULL != ctx) CGLSetParameter(ctx, kCGLCPSwapInterval, &swapInterval);
```


GLUT based programs have the additional convenience of a default setting. The default setting is only evaluated during application launch, so for the change to take effect the application must be restarted.

GLUT defaults can be accessed on their application menus:

__Figure 1__  Accessing the preferences of a GLUT application

!

To enable synchronization to VBL by default select "Default Synchronize to Vertical Blank" and restart the application.

__Figure 2__  Selecting synchronization default.

!

The [OpenGL Programming Guide for Mac OS X](https://developer.apple.com/documentation/GraphicsImaging/Conceptual/OpenGL-MacProgGuide/) has a section about this topic under the best practices area of improving performance.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2007-07-16 | New document that how to avoid tearing by synchronizing your rendering to the display VBL |

