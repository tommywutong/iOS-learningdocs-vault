---
title: Creating IOSurface-backed CVPixelBuffers for accessing video data in OpenGL
  ES
apple_id: DTS40014217
resource_type: QA
platform: iOS
topic: Graphics & Animation
technology: CoreVideo
published: '2014-03-17'
source_url: https://developer.apple.com/library/archive/qa/qa1781/_index.html
archived_at: '2026-07-18T02:34:43.868186Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1781

# Creating IOSurface-backed CVPixelBuffers for accessing video data in OpenGL ES

## Q:  Why is `CVOpenGLESTextureCacheCreateTextureFromImage()` returning an error of -6683?

A: The reason `CVOpenGLESTextureCacheCreateTextureFromImage()` is returning the `kCVReturnPixelBufferNotOpenGLCompatible` (-6683) error is that the source pixel buffer is not IOSurface-backed.

To create a `CVOpenGLESTexture` object successfully, the pixel buffer passed to `CVOpenGLESTextureCacheCreateTextureFromImage()` must be backed by an IOSurface. To do that, you must specify `kCVPixelBufferIOSurfacePropertiesKey` in the `pixelBufferAttributes` dictionary when creating the pixel buffer using `CVPixelBufferCreate()`. See Listing 1 for an example:

__Listing 1__  Creating an IOSurface-backed CVPixelBuffer with `CVPixelBufferCreate()`

```
NSDictionary *pixelBufferAttributes = [NSDictionary dictionaryWithObjectsAndKeys:
    [NSDictionary dictionary], (id)kCVPixelBufferIOSurfacePropertiesKey,
    nil];
// you may add other keys as appropriate, e.g. kCVPixelBufferPixelFormatTypeKey, kCVPixelBufferWidthKey, kCVPixelBufferHeightKey, etc.

CVPixelBufferRef pixelBuffer;
CVPixelBufferCreate(... (CFDictionaryRef)pixelBufferAttributes,  &pixelBuffer);
```

Alternatively, you can make IOSurface-backed CVPixelBuffers using `CVPixelBufferPoolCreatePixelBuffer()` from an existing pixel buffer pool, if the `pixelBufferAttributes` dictionary provided to `CVPixelBufferPoolCreate()` includes `kCVPixelBufferIOSurfacePropertiesKey`.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-03-17 | New document that describes how to create an IOSurface-backed CVPixelBuffer to create a CVOpenGLESTexture from it. |

