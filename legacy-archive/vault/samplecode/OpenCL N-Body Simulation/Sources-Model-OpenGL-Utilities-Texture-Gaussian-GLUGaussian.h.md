---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_OpenGL_Utilities_Texture_Gaussian_GLUGaussian_h.html
archived_at: '2026-07-18T03:17:43.492017Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-OpenGL-Utilities-Texture-Gaussian-GLUGaussian.mm.md)[Previous](Sources-Model-OpenGL-Utilities-Text-GLUText.mm.md)

# Sources/Model/OpenGL/Utilities/Texture/Gaussian/GLUGaussian.h

```objc
/*
 <codex>
 <abstract>
 Utility methods for creating a Gaussian texture.
 </abstract>
 </codex>
 */

#ifndef _OPENGL_UTILITY_GAUSSIAN_H_
#define _OPENGL_UTILITY_GAUSSIAN_H_

#import <OpenGL/OpenGL.h>

#ifdef __cplusplus

namespace GLU
{
    class Gaussian
    {
    public:
        Gaussian(const GLuint& nTexRes = 64);

        Gaussian(const Gaussian& rGaussian);

        virtual ~Gaussian();

        Gaussian& operator=(const Gaussian& rGaussian);

        void enable();
        void disable();

        const GLuint& texture() const;
        const GLenum& target()  const;

    private:
        GLuint  mnTexture;
        GLuint  mnTexRes;
        GLenum  mnTarget;
    }; // Gaussian
} // GLU

#endif

#endif
```

[Next](Sources-Model-OpenGL-Utilities-Texture-Gaussian-GLUGaussian.mm.md)[Previous](Sources-Model-OpenGL-Utilities-Text-GLUText.mm.md)

