---
title: OpenGL Queries
apple_id: TP40016611
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenGL_Queries/Listings/Sources_Frameworks_Model_OpenGL_Query_Renderers_GLUQueryRenderers_h.html
archived_at: '2026-07-18T03:18:14.502824Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenGL Queries](OpenGL%20Queries.md)


[Next](Sources-Frameworks-Model-OpenGL-Query-Renderers-GLUQueryRenderers.mm.md)[Previous](Sources-Frameworks-Model-OpenGL-Query-Constants-GLUQueryConstants.h.md)

# Sources/Frameworks/Model/OpenGL/Query/Renderers/GLUQueryRenderers.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Query class for OpenGL renderers.
 */

#ifndef _OPENGL_UTILITIES_QUERY_RENDERERS_H_
#define _OPENGL_UTILITIES_QUERY_RENDERERS_H_

#import <Cocoa/Cocoa.h>
#import <OpenGL/OpenGL.h>

#import "GLContainers.h"

#ifdef __cplusplus

namespace GLU
{
    namespace Query
    {
        class Renderers
        {
        public:
            // Create an object for multiple displays
            Renderers(const GLuint& nDisplayMask);

            // Destructor
            virtual ~Renderers();

            // Get renderers
            const GLrenderers& renderers() const;

            // Get a description string representing all the key-value pairs
            // in the hash table
            GLstring& description();

            // Create an instance of this object for all renderers
            static Renderers *create();

            // Print all the key-value pairs
            friend GLostream& operator<<(GLostream &rOutput, Renderers &rRenderers);

        private:
            GLrenderers  m_Renderers;
            GLstring     m_Description;
        }; // Displays
    } // Query
} // GLU

#endif

#endif
```

[Next](Sources-Frameworks-Model-OpenGL-Query-Renderers-GLUQueryRenderers.mm.md)[Previous](Sources-Frameworks-Model-OpenGL-Query-Constants-GLUQueryConstants.h.md)

