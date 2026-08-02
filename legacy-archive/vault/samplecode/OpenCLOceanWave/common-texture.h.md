---
title: OpenCL_OceanWave
apple_id: DTS40009447
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2011-04-13'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_OceanWave/Listings/common_texture_h.html
archived_at: '2026-07-18T03:17:48.917727Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL_OceanWave](OpenCLOceanWave.md)


[Next](common-timing.h.md)[Previous](common-texture.cpp.md)

Current information on this Developer Library topic can be found here:

- [Performance > Multiprocessing](https://developer.apple.com/referencelibrary/Performance/idxMultiprocessing-date.html)

# common/texture.h

```c
// Version:    <1.0>
//
// Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple Inc. ("Apple")
//             in consideration of your agreement to the following terms, and your use,
//             installation, modification or redistribution of this Apple software
//             constitutes acceptance of these terms.  If you do not agree with these
//             terms, please do not use, install, modify or redistribute this Apple
//             software.
//
//             In consideration of your agreement to abide by the following terms, and
//             subject to these terms, Apple grants you a personal, non - exclusive
//             license, under Apple's copyrights in this original Apple software ( the
//             "Apple Software" ), to use, reproduce, modify and redistribute the Apple
//             Software, with or without modifications, in source and / or binary forms;
//             provided that if you redistribute the Apple Software in its entirety and
//             without modifications, you must retain this notice and the following text
//             and disclaimers in all such redistributions of the Apple Software. Neither
//             the name, trademarks, service marks or logos of Apple Inc. may be used to
//             endorse or promote products derived from the Apple Software without specific
//             prior written permission from Apple.  Except as expressly stated in this
//             notice, no other rights or licenses, express or implied, are granted by
//             Apple herein, including but not limited to any patent rights that may be
//             infringed by your derivative works or by other works in which the Apple
//             Software may be incorporated.
//
//             The Apple Software is provided by Apple on an "AS IS" basis.  APPLE MAKES NO
//             WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION THE IMPLIED
//             WARRANTIES OF NON - INFRINGEMENT, MERCHANTABILITY AND FITNESS FOR A
//             PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND OPERATION
//             ALONE OR IN COMBINATION WITH YOUR PRODUCTS.
//
//             IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL OR
//             CONSEQUENTIAL DAMAGES ( INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
//             SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
//             INTERRUPTION ) ARISING IN ANY WAY OUT OF THE USE, REPRODUCTION, MODIFICATION
//             AND / OR DISTRIBUTION OF THE APPLE SOFTWARE, HOWEVER CAUSED AND WHETHER
//             UNDER THEORY OF CONTRACT, TORT ( INCLUDING NEGLIGENCE ), STRICT LIABILITY OR
//             OTHERWISE, EVEN IF APPLE HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
//
// Copyright ( C ) 2008 Apple Inc. All Rights Reserved.
//
////////////////////////////////////////////////////////////////////////////////////////////////////

#ifndef __TEXTURE_H__
#define __TEXTURE_H__

#include "compute_types.h"
#include <OpenGL/gl.h>

class Texture
{

public:

    Texture();
    ~Texture();

    void enable(GLenum eUnit = GL_TEXTURE0);
    void update();
    void disable();

    void render();

    bool loadCubeMap(
        const char* acFilenames[6],
        GLenum eTarget = GL_TEXTURE_CUBE_MAP, 
        GLenum eInternal = GL_RGB8, 
        GLenum eFormat = GL_RGB, 
        GLenum eDataType = GL_UNSIGNED_BYTE, 
        GLenum eFilterMode = GL_LINEAR, 
        GLenum eWrapMode = GL_REPEAT);

    bool load(
        const char* acFilename, 
        GLenum eTarget = GL_TEXTURE_2D, 
        GLenum eInternal = GL_RGB8, 
        GLenum eFormat = GL_RGB, 
        GLenum eDataType = GL_UNSIGNED_BYTE, 
        GLenum eFilterMode = GL_LINEAR, 
        GLenum eWrapMode = GL_REPEAT, 
        bool bUseMipMaps = true);

    bool setup(
        uint uiWidth, 
        uint uiHeight, 
        GLenum eTarget,           // = GL_TEXTURE_2D,
        GLenum eInternal,         // = GL_RGBA_FLOAT32_APPLE, 
        GLenum eFormat,           // = GL_RGBA, 
        GLenum eDataType,         // = GL_FLOAT,
        bool bUseMipMaps = false,
        void* pvData = 0);   

    bool setup(
        uint uiWidth, 
        uint uiHeight,
        uint uiDepth, 
        GLenum eTarget,           // = GL_TEXTURE_2D,
        GLenum eInternal,         // = GL_RGBA_FLOAT32_APPLE, 
        GLenum eFormat,           // = GL_RGBA, 
        GLenum eDataType,         // = GL_FLOAT
        bool bUseMipMaps = false,
        void* pvData = 0);   

    void capture();

    void setTextureMatrix(const float16 &rkM)           { m_kTextureMatrix = rkM;   }
    void setTextureUnit(GLenum eUnit)                   { m_eTextureUnit = eUnit;   }
    void setFilterMode(GLenum eMode)                    { m_eFilterMode = eMode;    }
    void setWrapMode(GLenum eMode)                      { m_eWrapMode = eMode;      }
    void setCompareMode(GLenum eMode)                   { m_eCompareMode = eMode;   }
    void setCompareFunc(GLenum eFunc)                   { m_eCompareFunc = eFunc;   }
    void setDepthMode(GLenum eMode)                     { m_eDepthMode = eMode;     }
    void setEnvMode(GLenum eMode)                       { m_eEnvMode = eMode;       }

    bool isEnabled() const                              { return m_bIsEnabled;      }
    uint getWidth() const                               { return m_uiWidth;         }
    uint getHeight() const                              { return m_uiHeight;        }
    uint getTextureId() const                           { return m_uiTextureId;     }
    GLenum getTarget() const                            { return m_eTarget;         }
    GLenum getTextureUnit() const                       { return m_eTextureUnit;    }
    GLenum getInternal() const                          { return m_eInternal;       }
    GLenum getFormat() const                            { return m_eFormat;         }
    GLenum getDataType() const                          { return m_eDataType;       }
    GLenum getFilterMode() const                        { return m_eFilterMode;     }
    GLenum getWrapMode() const                          { return m_eWrapMode;       }
    GLenum getCompareMode() const                       { return m_eCompareMode;    }
    GLenum getCompareFunc() const                       { return m_eCompareFunc;    }
    GLenum getEnvMode() const                           { return m_eEnvMode;        }
    GLenum getDepthMode() const                         { return m_eDepthMode;      }

protected:

    void destroy();

    uint createTexture(
        uint uiWidth, 
        uint uiHeight, 
        uint uiDepth, 
        GLenum eTarget,      // = GL_TEXTURE_2D,
        GLenum eInternal,    // = GL_RGBA_FLOAT32_APPLE, 
        GLenum eFormat,      // = GL_RGBA, 
        GLenum eDataType,    // = GL_FLOAT
        void* pvData = 0);

    void checkStatus(const char* acMessage=0);


protected:

    bool m_bIsEnabled;
    uint m_uiWidth;
    uint m_uiHeight;
    uint m_uiDepth;
    uint m_uiTextureId;
    GLenum m_eTarget;
    GLenum m_eTextureUnit;
    GLenum m_eInternal;
    GLenum m_eFormat;
    GLenum m_eDataType;
    GLenum m_eFilterMode;
    GLenum m_eWrapMode;
    GLenum m_eCompareMode;
    GLenum m_eCompareFunc;
    GLenum m_eEnvMode;
    GLenum m_eDepthMode;
    float16 m_kTextureMatrix;
};

#endif
```

[Next](common-timing.h.md)[Previous](common-texture.cpp.md)

