---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_OpenGL_Utilities_Program_GLUProgram_h.html
archived_at: '2026-07-18T03:17:42.626104Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-OpenGL-Utilities-Query-GLUQuery.h.md)[Previous](Sources-Model-OpenGL-Utilities-Program-GLUProgram.mm.md)

# Sources/Model/OpenGL/Utilities/Program/GLUProgram.h

```objc
/*
 <codex>
 <abstract>
 Utility method for creating an OpenGL program object.
 </abstract>
 </codex>
 */

#ifndef _OPENGL_UTILITY_PROGRAM_H_
#define _OPENGL_UTILITY_PROGRAM_H_

#import <Cocoa/Cocoa.h>
#import <OpenGL/OpenGL.h>

#import "GLcontainers.h"

#ifdef __cplusplus

namespace GLU
{
    class Program
    {
    public:
        Program(CFStringRef pName);

        Program(CFStringRef     pName,
                const GLenum&   inType,
                const GLenum&   outType,
                const GLsizei&  vertOut);

        Program(const Program& rProgram);

        virtual ~Program();

        Program& operator=(const Program& rProgram);

        void enable();
        void disable();

        const GLuint& program() const;

    private:
        GLuint     mnProgram;
        GLenum     mnInType;
        GLenum     mnOutType;
        GLsizei    mnOutVert;
        GLsources  m_Sources;
    }; // Program
} // GLU

#endif

#endif
```

[Next](Sources-Model-OpenGL-Utilities-Query-GLUQuery.h.md)[Previous](Sources-Model-OpenGL-Utilities-Program-GLUProgram.mm.md)

