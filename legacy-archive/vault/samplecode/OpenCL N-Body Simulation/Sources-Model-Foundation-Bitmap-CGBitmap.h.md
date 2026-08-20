---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_Foundation_Bitmap_CGBitmap_h.html
archived_at: '2026-07-18T03:17:35.611470Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-Foundation-Files-CFFile.mm.md)[Previous](Sources-Model-Foundation-Bitmap-CGBitmap.mm.md)

# Sources/Model/Foundation/Bitmap/CGBitmap.h

```objc
/*
 <codex>
 <abstract>
 Utility methods acquiring CG bitmap contexts.
 </abstract>
 </codex>
 */

#ifndef _CORE_GRAPHICS_BITMAP_H_
#define _CORE_GRAPHICS_BITMAP_H_

#import <Cocoa/Cocoa.h>
#import <OpenGL/OpenGL.h>

#ifdef __cplusplus

namespace CG
{
    class Bitmap
    {
    public:
        Bitmap(CFStringRef pName,
               CFStringRef pExt);

        Bitmap(const Bitmap& rBitmap);
        Bitmap(const Bitmap * const pBitmap);

        virtual ~Bitmap();

        Bitmap& operator=(const Bitmap& rBitmap);

        const size_t& width()    const;
        const size_t& height()   const;
        const size_t& rowBytes() const;

        const CGContextRef context() const;

        const CGBitmapInfo& bitmapInfo() const;

        bool copy(const CGContextRef pContext);

        void* data();

    private:
        size_t        mnWidth;
        size_t        mnHeight;
        size_t        mnRowBytes;
        CGBitmapInfo  mnBMPI;
        CGContextRef  mpContext;
    }; // Bitmap
} // CG

#endif

#endif
```

[Next](Sources-Model-Foundation-Files-CFFile.mm.md)[Previous](Sources-Model-Foundation-Bitmap-CGBitmap.mm.md)

