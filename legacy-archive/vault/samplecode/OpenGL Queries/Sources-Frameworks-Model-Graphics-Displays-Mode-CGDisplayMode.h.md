---
title: OpenGL Queries
apple_id: TP40016611
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenGL_Queries/Listings/Sources_Frameworks_Model_Graphics_Displays_Mode_CGDisplayMode_h.html
archived_at: '2026-07-18T03:18:13.561533Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenGL Queries](OpenGL%20Queries.md)


[Next](Sources-Frameworks-Model-Graphics-Displays-Data-CGDisplaysDataSource.mm.md)[Previous](Sources-Frameworks-Model-Graphics-Displays-Mode-CGDisplayMode.mm.md)

# Sources/Frameworks/Model/Graphics/Displays/Mode/CGDisplayMode.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility class to acquire cg display mode properties.
 */

#ifndef _CORE_GRAPHICS_DISPLAY_MODE_H_
#define _CORE_GRAPHICS_DISPLAY_MODE_H_

#import <string>

#import <Cocoa/Cocoa.h>

#ifdef __cplusplus

namespace CG
{
    namespace Display
    {
        struct Size
        {
            size_t width;
            size_t height;
        }; // Size

        class Mode
        {
        public:
            Mode(const CGDisplayModeRef pDisplayMode = nullptr);

            Mode(const Mode& rMode);

            virtual ~Mode();

            Mode& operator=(const Mode& rMode);

            const bool& isUsable() const;

            const Size& points()  const;
            const Size& pixels() const;

            const uint32_t& flags()  const;
            const uint32_t& handle() const;

        private:
            bool         mbIsUsable;
            Size         m_Points;
            Size         m_Pixels;
            uint32_t     mnFlags;
            uint32_t     mnHandle;
        }; // Mode
    } // Display
} // CG

#endif

#endif
```

[Next](Sources-Frameworks-Model-Graphics-Displays-Data-CGDisplaysDataSource.mm.md)[Previous](Sources-Frameworks-Model-Graphics-Displays-Mode-CGDisplayMode.mm.md)

