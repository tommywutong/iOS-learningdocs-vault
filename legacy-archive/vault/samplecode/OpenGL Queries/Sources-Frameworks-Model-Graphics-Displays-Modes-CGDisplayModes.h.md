---
title: OpenGL Queries
apple_id: TP40016611
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenGL_Queries/Listings/Sources_Frameworks_Model_Graphics_Displays_Modes_CGDisplayModes_h.html
archived_at: '2026-07-18T03:18:13.671551Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenGL Queries](OpenGL%20Queries.md)


[Next](Sources-Frameworks-Model-Graphics-Displays-Mode-CGDisplayMode.mm.md)[Previous](Sources-Frameworks-Model-Graphics-Displays-Modes-CGDisplayModes.mm.md)

# Sources/Frameworks/Model/Graphics/Displays/Modes/CGDisplayModes.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility class to acquire all cg display modes usable for desktop gui.
 */

#ifndef _CORE_GRAPHICS_DISPLAY_MODES_H_
#define _CORE_GRAPHICS_DISPLAY_MODES_H_

#import <unordered_map>
#import <vector>

#import <Cocoa/Cocoa.h>

#import "CGDisplayMode.h"

#ifdef __cplusplus

namespace CG
{
    namespace Display
    {
        typedef std::vector<uint32_t>               ModeIDs;
        typedef std::unordered_map<uint32_t, Mode>  ModeTable;

        class Modes
        {
        public:
            Modes(const CGDirectDisplayID& nDisplay = 0);

            Modes(const Modes& rModes);

            virtual ~Modes();

            Modes& operator=(const Modes& rModes);

            const size_t&    count()   const;
            const uint32_t&  display() const;
            const ModeIDs&   modes()   const;
            const ModeTable& table()   const;

            const Mode mode(const uint32_t& nID) const;

        private:
            ModeIDs    m_Modes;
            ModeTable  m_Table;
            uint32_t   mnDDID;
            size_t     mnCount;
        }; // Mode
    } // Display
} // CG

#endif

#endif
```

[Next](Sources-Frameworks-Model-Graphics-Displays-Mode-CGDisplayMode.mm.md)[Previous](Sources-Frameworks-Model-Graphics-Displays-Modes-CGDisplayModes.mm.md)

