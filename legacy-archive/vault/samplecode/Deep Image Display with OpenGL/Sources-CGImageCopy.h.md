---
title: Deep Image Display with OpenGL
apple_id: TP40016622
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/DeepImageDisplayWithOpenGL/Listings/Sources_CGImageCopy_h.html
archived_at: '2026-07-18T03:06:06.952927Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Deep Image Display with OpenGL](Deep%20Image%20Display%20with%20OpenGL.md)


[Next](Sources-GLView.mm.md)[Previous](README.md.md)

# Sources/CGImageCopy.h

```
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility methods for "fast-string" memory copy.
 */

#ifndef _CG_IMAGE_COPY_H_
#define _CG_IMAGE_COPY_H_

#ifdef __cplusplus

namespace CG
{
    // Copy from a source to destination image using base addresses
    void* memcpy(const size_t& rSize,
                 const void* pIn,
                 void* pOut);

    // Copy from a source to destination image using base addresses
    uint8_t* memcpy(const size_t& rSize,
                    const uint8_t* pSrc,
                    uint8_t* pDst);

    // Error condtions for i/o surface copy
    extern IOReturn kIOReturnCpySuccess;
    extern IOReturn kIOReturnCpyErrSrcRef;
    extern IOReturn kIOReturnCpyErrDstRef;
    extern IOReturn kIOReturnCpyErrHeight;
    extern IOReturn kIOReturnCpyErrRowBytes;
    extern IOReturn kIOReturnCpyErrSize;
    extern IOReturn kIOReturnCpyErrSrcPtr;
    extern IOReturn kIOReturnCpyErrDstPtr;

    // Copy from a source to destination i/o surface at plane 0
    IOSurfaceRef s2dcpy(const IOSurfaceRef pSrc,
                        IOSurfaceRef pDst,
                        IOReturn& nResult);

    // Copy from a source to destination i/o surface at a plane given by a source
    // index to a destination i/o surface at a plane  given by a destination index
    IOSurfaceRef s2dcpy(const size_t& nSrcIdx,
                        const IOSurfaceRef pSrc,
                        const size_t& nDstIdx,
                        IOSurfaceRef pDst,
                        IOReturn& nResult);
} // CG

#endif

#endif
```

[Next](Sources-GLView.mm.md)[Previous](README.md.md)

