---
title: OpenGL Queries
apple_id: TP40016611
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenGL_Queries/Listings/Sources_Frameworks_Model_Graphics_Displays_List_CGDisplayList_h.html
archived_at: '2026-07-18T03:18:13.459909Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenGL Queries](OpenGL%20Queries.md)


[Next](Sources-Frameworks-Model-OpenGL-Query-Properties-Table-GLUQueryRendererProperty.md)[Previous](Sources-Frameworks-Model-Graphics-Displays-List-CGDisplayList.mm.md)

# Sources/Frameworks/Model/Graphics/Displays/List/CGDisplayList.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Mediator class to acquire properties usable for desktop gui for all active displays.
 */

#ifndef _CORE_GRAPHICS_DISPLAY_LIST_H_
#define _CORE_GRAPHICS_DISPLAY_LIST_H_

#import <unordered_map>

#import <Cocoa/Cocoa.h>

#import "CGDisplayModes.h"

#ifdef __cplusplus

namespace CG
{
    namespace Display
    {
        typedef std::unordered_map<uint32_t, Modes>  DisplayTable;

        class List
        {
        public:
            List(const uint32_t& nDisplayCount);

            virtual ~List();

            static List *create();

            const uint32_t*     displays() const;
            const uint32_t&     count()    const;
            const DisplayTable& table()    const;

            const Modes modes(const uint32_t& nDisplayID) const;

        private:
            uint32_t*      mpDisplays;
            uint32_t       mnCount;
            DisplayTable   m_Table;
        }; // List
    } // Display
} // CG

#endif

#endif
```

[Next](Sources-Frameworks-Model-OpenGL-Query-Properties-Table-GLUQueryRendererProperty.md)[Previous](Sources-Frameworks-Model-Graphics-Displays-List-CGDisplayList.mm.md)

