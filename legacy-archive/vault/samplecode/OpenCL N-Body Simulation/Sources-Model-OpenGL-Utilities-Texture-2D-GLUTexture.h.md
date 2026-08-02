---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_OpenGL_Utilities_Texture_2D_GLUTexture_h.html
archived_at: '2026-07-18T03:17:43.384121Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-OpenGL-Containers-GLContainers.h.md)[Previous](Sources-Model-OpenGL-Utilities-Texture-2D-GLUTexture.mm.md)

# Sources/Model/OpenGL/Utilities/Texture/2D/GLUTexture.h

```objc
/*
 <codex>
 <abstract>
 Utility methods for creating 2D OpenGL textures.
 </abstract>
 </codex>
 */

#ifndef _OPENGL_UTILITY_TEXTURE_H_
#define _OPENGL_UTILITY_TEXTURE_H_

#import <Cocoa/Cocoa.h>
#import <OpenGL/OpenGL.h>

#import "CGBitmap.h"

#ifdef __cplusplus

namespace GLU
{
    class Texture
    {
    public:
        Texture(CFStringRef   pName,
                CFStringRef   pExt,
                const GLenum& nTarget = GL_TEXTURE_2D,
                const bool&   bMipmap = true);

        Texture(const Texture& rTexture);

        virtual ~Texture();

        Texture& operator=(const Texture& rTexture);

        void enable();
        void disable();

        const GLuint& texture() const;
        const GLenum& target()  const;

    private:
        bool         mbMipmaps;
        GLuint       mnTexture;
        GLenum       mnTarget;
        GLsizei      mnWidth;
        GLsizei      mnHeight;
        CG::Bitmap  *mpBitmap;
    }; // Texture
} // GLU

#endif

#endif
```

[Next](Sources-Model-OpenGL-Containers-GLContainers.h.md)[Previous](Sources-Model-OpenGL-Utilities-Texture-2D-GLUTexture.mm.md)

