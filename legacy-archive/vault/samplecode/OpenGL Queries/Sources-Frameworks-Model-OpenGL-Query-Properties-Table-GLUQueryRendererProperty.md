---
title: OpenGL Queries
apple_id: TP40016611
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenGL_Queries/Listings/Sources_Frameworks_Model_OpenGL_Query_Properties_Table_GLUQueryRendererProperty_h.html
archived_at: '2026-07-18T03:18:14.433320Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenGL Queries](OpenGL%20Queries.md)


[Next](Sources-Frameworks-Model-OpenGL-Query-Properties-Table-GLUQueryRendererProperty-2.md)[Previous](Sources-Frameworks-Model-Graphics-Displays-List-CGDisplayList.h.md)

# Sources/Frameworks/Model/OpenGL/Query/Properties/Table/GLUQueryRendererProperty.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A utility class for converting a subset of properties into their string equivalent.
 */

#ifndef _OPENGL_UTILITIES_QUERY_RENDERER_PROPERTY_H_
#define _OPENGL_UTILITIES_QUERY_RENDERER_PROPERTY_H_

#import <Cocoa/Cocoa.h>
#import <OpenGL/OpenGL.h>

#import "GLContainers.h"

#ifdef __cplusplus

namespace GLU
{
    namespace Query
    {
        class RendererProperty
        {
        public:
            RendererProperty();

            virtual ~RendererProperty();

            GLstring operator[](const GLuint& nProperty);
            GLstring operator[](const CGLRendererProperty& nProperty);

            size_t length();
            size_t length(const CGLRendererProperty& nProperty);

            GLstring find(const GLuint& nProperty);
            GLstring find(const CGLRendererProperty& nProperty);

        private:
            size_t          mnLength;
            GLpropertynames m_Names;
        }; // RendererProperty
    } // Query
} // GLU

#endif

#endif
```

[Next](Sources-Frameworks-Model-OpenGL-Query-Properties-Table-GLUQueryRendererProperty-2.md)[Previous](Sources-Frameworks-Model-Graphics-Displays-List-CGDisplayList.h.md)

