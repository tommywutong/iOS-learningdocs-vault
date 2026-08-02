---
title: OpenCL_OceanWave
apple_id: DTS40009447
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2011-04-13'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_OceanWave/Listings/common_projected_grid_h.html
archived_at: '2026-07-18T03:17:48.015707Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL_OceanWave](OpenCLOceanWave.md)


[Next](common-projector.cpp.md)[Previous](common-projectedgrid.cpp.md)

Current information on this Developer Library topic can be found here:

- [Performance > Multiprocessing](https://developer.apple.com/referencelibrary/Performance/idxMultiprocessing-date.html)

# common/projected_grid.h

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

#ifndef __PROJECTED_GRID__
#define __PROJECTED_GRID__

#include "compute_types.h"
#include "compute_math.h"
#include "projector.h"

#include <OpenGL/gl.h>

////////////////////////////////////////////////////////////////////////////////

class ProjectedGrid
{

public:
    ProjectedGrid();
    ~ProjectedGrid();

    void update();
    void setup(uint uiSizeX, uint uiSizeY);
    void render(GLenum eElementType = GL_TRIANGLE_STRIP, bool bUseVBO = true);

    bool isVisible()                                        { return m_bIsVisible;          }
    void setProjector(Projector *pkProjector)               { m_pkProjector = pkProjector;  }

protected:

    void createGridMesh(uint uiCountX, uint uiCountY);
    void updateGridMesh(const float4 afCorners[4]);
    void destroyGridMesh();

    void createVBO();
    void updateVBO();
    void destroyVBO();
    void destroy();

protected:

    bool m_bDebug;
    bool m_bIsVisible;

    uint m_uiSizeX;
    uint m_uiSizeY;

    float* m_afVertexData; 
    float* m_afNormalData; 
    float* m_afTexCoordData; 
    uint m_uiVertexCount;    

    uint* m_auiIndexData;  
    uint m_uiIndexCount;       

    uint m_uiVertexBufferId;
    uint m_uiNormalBufferId;
    uint m_uiTexCoordBufferId;
    uint m_uiIndexBufferId;
    uint m_uiFaceCount;           

    Projector *m_pkProjector;
};

////////////////////////////////////////////////////////////////////////////////

#endif
```

[Next](common-projector.cpp.md)[Previous](common-projectedgrid.cpp.md)

