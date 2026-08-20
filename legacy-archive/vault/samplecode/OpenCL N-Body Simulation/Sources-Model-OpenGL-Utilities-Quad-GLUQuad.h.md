---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_OpenGL_Utilities_Quad_GLUQuad_h.html
archived_at: '2026-07-18T03:17:42.921403Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-OpenGL-Utilities-Quad-GLUQuad.mm.md)[Previous](Sources-Model-OpenGL-Utilities-Query-GLUQuery.mm.md)

# Sources/Model/OpenGL/Utilities/Quad/GLUQuad.h

```objc
/*
 <codex>
 <abstract>
 Utility methods for managing a VBO based an OpenGL quad.
 </abstract>
 </codex>
 */

#ifndef _OPENGL_QUAD_H_
#define _OPENGL_QUAD_H_

#import <Cocoa/Cocoa.h>
#import <OpenGL/OpenGL.h>

#ifdef __cplusplus

namespace GLU
{
    // Quad opaque data reference
    typedef struct Quad  *QuadRef;

    // Construct a quad with a usage enumerated type
    QuadRef QuadCreate(const GLenum& nUsage);

    // Retain a quad
    QuadRef QuadRetain(QuadRef pQuad);

    // Release a quad
    void QuadRelease(QuadRef pQuad);

    // Is the quad finalized?
    bool QuadIsFinalized(QuadRef pQuad);

    // Set the quad to be inverted
    bool QuadSetIsInverted(const bool& bIsInverted,
                           QuadRef pQuad);

    // Set the quad bounds
    bool QuadSetBounds(const CGRect& bounds,
                       QuadRef pQuad);

    // Finalize and acquire a vbo for the quad
    bool QuadFinalize(QuadRef pQuad);

    // Update the quad if either the bounds changed or
    // the inverted flag was changed
    void QuadUpdate(QuadRef pQuad);

    // Map to get the base address of the quad's vbo
    bool QuadMap(QuadRef pQuad);

    // Unmap to invalidate the base address of the quad's vbo
    bool QuadUnmap(QuadRef pQuad);

    // Get the base address of the quad's vbo
    GLfloat* QuadBuffer(QuadRef pQuad);

    // Draw the quad
    void QuadDraw(QuadRef pQuad);
} // GLU

#endif

#endif
```

[Next](Sources-Model-OpenGL-Utilities-Quad-GLUQuad.mm.md)[Previous](Sources-Model-OpenGL-Utilities-Query-GLUQuery.mm.md)

