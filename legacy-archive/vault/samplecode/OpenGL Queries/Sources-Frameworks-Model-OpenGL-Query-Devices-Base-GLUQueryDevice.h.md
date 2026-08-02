---
title: OpenGL Queries
apple_id: TP40016611
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenGL_Queries/Listings/Sources_Frameworks_Model_OpenGL_Query_Devices_Base_GLUQueryDevice_h.html
archived_at: '2026-07-18T03:18:14.103496Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenGL Queries](OpenGL%20Queries.md)


[Next](Sources-Frameworks-Model-OpenGL-Query-Devices-Mediator-GLUQueryDevices.h.md)[Previous](Sources-Frameworks-Model-OpenGL-Query-Devices-Base-GLUQueryDevice.mm.md)

# Sources/Frameworks/Model/OpenGL/Query/Devices/Base/GLUQueryDevice.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility class for querying OpenGL device information.
 */

#ifndef _OPENGL_UTILITIES_QUERY_DEVICE_H_
#define _OPENGL_UTILITIES_QUERY_DEVICE_H_

#import "GLContainers.h"

#ifdef __cplusplus

namespace GLU
{
    namespace Query
    {
        class Device
        {
        public:
            Device(CGLContextObj pContext, const GLint& nScreen = 0);

            virtual ~Device();

            const bool match(GLstring& rKey)   const;
            const bool match(GLstrings& rKeys) const;

            bool find(const GLstring& rFeature);

            const bool&        noError()  const;
            const GLfeatures&  features() const;
            const GLstring&    renderer() const;
            const GLstring&    vendor()   const;
            const GLstring&    version()  const;

        private:
            bool        mbNoError;
            GLint       mnEntries;
            GLfeatures  m_Features;
            GLstring    m_DeviceInfo[3];
        }; // Device
    } // Query
} // GLU

#endif

#endif
```

[Next](Sources-Frameworks-Model-OpenGL-Query-Devices-Mediator-GLUQueryDevices.h.md)[Previous](Sources-Frameworks-Model-OpenGL-Query-Devices-Base-GLUQueryDevice.mm.md)

