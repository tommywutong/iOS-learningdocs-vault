---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_OpenGL_Utilities_Query_GLUQuery_h.html
archived_at: '2026-07-18T03:17:43.123485Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-OpenGL-Utilities-Query-GLUQuery.mm.md)[Previous](Sources-Model-OpenGL-Utilities-Program-GLUProgram.h.md)

# Sources/Model/OpenGL/Utilities/Query/GLUQuery.h

```objc
/*
 <codex>
 <abstract>
 Utility class for querying OpenGL for vendor, version, and renderer.
 </abstract>
 </codex>
 */

#ifndef _OPENGL_UTILITY_QUERY_H_
#define _OPENGL_UTILITY_QUERY_H_

#import <Cocoa/Cocoa.h>
#import <OpenGL/OpenGL.h>

#import "GLcontainers.h"

#ifdef __cplusplus

namespace GLU
{
    class Query
    {
    public:
        Query();

        virtual ~Query();

        const bool match(GLstring& rKey)   const;
        const bool match(GLstrings& rKeys) const;

        const GLstring& info()     const;
        const GLstring& renderer() const;
        const GLstring& vendor()   const;
        const GLstring& version()  const;

        const bool& isAMD()    const;
        const bool& isATI()    const;
        const bool& isNVidia() const;
        const bool& isIntel()  const;

    private:
        const bool match(const GLuint& i, const GLuint& j) const;
        const bool match(const GLstring& expr) const;

        GLstring createString(const GLenum& name);

    private:
        bool      m_Flag[4];
        GLregex   m_Regex[4];
        GLstring  m_String[4];
    }; // Query
} // GLU

#endif

#endif
```

[Next](Sources-Model-OpenGL-Utilities-Query-GLUQuery.mm.md)[Previous](Sources-Model-OpenGL-Utilities-Program-GLUProgram.h.md)

