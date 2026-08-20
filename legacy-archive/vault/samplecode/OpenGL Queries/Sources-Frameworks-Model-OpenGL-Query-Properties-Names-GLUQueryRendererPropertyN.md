---
title: OpenGL Queries
apple_id: TP40016611
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenGL_Queries/Listings/Sources_Frameworks_Model_OpenGL_Query_Properties_Names_GLUQueryRendererPropertyNames_h.html
archived_at: '2026-07-18T03:18:14.381617Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenGL Queries](OpenGL%20Queries.md)


[Next](Sources-Frameworks-Model-OpenGL-Query-Devices-Base-GLUQueryDevice.mm.md)[Previous](Sources-Frameworks-Model-OpenGL-Query-Properties-Table-GLUQueryRendererProperty-2.md)

# Sources/Frameworks/Model/OpenGL/Query/Properties/Names/GLUQueryRendererPropertyNames.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Constants for property names.
 */

#ifndef _OPENGL_UTILITIES_QUERY_RENDERER_PROPERTY_NAMES_H_
#define _OPENGL_UTILITIES_QUERY_RENDERER_PROPERTY_NAMES_H_

#import <Cocoa/Cocoa.h>
#import <OpenGL/OpenGL.h>

#import "GLContainers.h"

#ifdef __cplusplus

namespace GLU
{
    namespace Query
    {
        static const GLuint kProperteyCount = 9;

        static const CGLRendererProperty kProperty[kProperteyCount] =
        {
            kCGLRPMajorGLVersion,
            kCGLRPOnline,
            kCGLRPVideoMemoryMegabytes,
            kCGLRPTextureMemoryMegabytes,
            kCGLRPSampleAlpha,
            kCGLRPMaxAuxBuffers,
            kCGLRPMaxSamples,
            kCGLRPMaxSampleBuffers,
            kCGLRPAcceleratedCompute
        };

        static const GLstring kPropertyNames[kProperteyCount] =
        {
            "Major GL Version",
            "Renderer Online",
            "Video Memory (MB)",
            "Texture Memory (MB)",
            "Sample Alpha",
            "Max Aux Buffers",
            "Max Samples",
            "Max Sample Buffers",
            "Accelerated Compute"
        };
    } // Query
} // GLU

#endif

#endif
```

[Next](Sources-Frameworks-Model-OpenGL-Query-Devices-Base-GLUQueryDevice.mm.md)[Previous](Sources-Frameworks-Model-OpenGL-Query-Properties-Table-GLUQueryRendererProperty-2.md)

