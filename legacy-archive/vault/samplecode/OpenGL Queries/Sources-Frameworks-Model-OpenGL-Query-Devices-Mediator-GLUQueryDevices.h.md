---
title: OpenGL Queries
apple_id: TP40016611
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenGL_Queries/Listings/Sources_Frameworks_Model_OpenGL_Query_Devices_Mediator_GLUQueryDevices_h.html
archived_at: '2026-07-18T03:18:14.243408Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenGL Queries](OpenGL%20Queries.md)


[Next](Sources-Frameworks-Model-OpenGL-Query-Devices-Mediator-GLUQueryDevices.mm.md)[Previous](Sources-Frameworks-Model-OpenGL-Query-Devices-Base-GLUQueryDevice.h.md)

# Sources/Frameworks/Model/OpenGL/Query/Devices/Mediator/GLUQueryDevices.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Mediator utility class for querying all OpenGL renderers
 */

#ifndef _OPENGL_UTILITIES_QUERY_DEVICES_H_
#define _OPENGL_UTILITIES_QUERY_DEVICES_H_

#import "GLUQueryDevice.h"

#ifdef __cplusplus

namespace GLU
{
    namespace Query
    {
        typedef std::unordered_map<GLint, Device> DeviceTable;

        class Devices
        {
        public:
            Devices(CGLContextObj pContext);

            virtual ~Devices();

            static Devices *create();
            static Devices *create(const CGLPixelFormatAttribute * const pAttributes);

            const GLint& count()     const;
            const GLint* renderers() const;

            const bool match(const GLint& nID, GLstring& rKey)   const;
            const bool match(const GLint& nID, GLstrings& rKeys) const;

            GLfeatures features(const GLint& nID);
            GLstring   renderer(const GLint& nID);
            GLstring   vendor(const GLint& nID);
            GLstring   version(const GLint& nID);

        private:
            GLint        mnCount;
            DeviceTable  m_Table;
            GLrenderids  m_Renderers;
        }; // Devices
    } // Query
} // GLU

#endif

#endif
```

[Next](Sources-Frameworks-Model-OpenGL-Query-Devices-Mediator-GLUQueryDevices.mm.md)[Previous](Sources-Frameworks-Model-OpenGL-Query-Devices-Base-GLUQueryDevice.h.md)

