---
title: OpenCL_OceanWave
apple_id: DTS40009447
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2011-04-13'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_OceanWave/Listings/common_frustum_cpp.html
archived_at: '2026-07-18T03:17:47.015701Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL_OceanWave](OpenCLOceanWave.md)


[Next](common-frustum.h.md)[Previous](common-fbo.h.md)

Current information on this Developer Library topic can be found here:

- [Performance > Multiprocessing](https://developer.apple.com/referencelibrary/Performance/idxMultiprocessing-date.html)

# common/frustum.cpp

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


#include "frustum.h"


Frustum::Frustum()
{
    // EMPTY!
}

void
Frustum::update(
    const Camera &rkCamera)
{
    float16 kClipSpace = rkCamera.getModelViewProjectionMatrix();

    float4 kC0 = kClipSpace.getColumn(0);
    float4 kC1 = kClipSpace.getColumn(1);
    float4 kC2 = kClipSpace.getColumn(2);
    float4 kC3 = kClipSpace.getColumn(3);

    m_akPlanes[RIGHT ] = kC3 - kC0;
    m_akPlanes[LEFT  ] = kC3 + kC0;

    m_akPlanes[TOP   ] = kC3 - kC1;
    m_akPlanes[BOTTOM] = kC3 + kC1;

    m_akPlanes[BACK  ] = kC3 - kC2;
    m_akPlanes[FRONT ] = kC3 + kC2;

/*
    float4 *pkPlane = &m_akPlanes[RIGHT];
    pkPlane->x = kClipSpace[0][3] - kClipSpace[0][0];
    pkPlane->y = kClipSpace[1][3] - kClipSpace[1][0];
    pkPlane->z = kClipSpace[2][3] - kClipSpace[2][0];
    pkPlane->w = kClipSpace[3][3] - kClipSpace[3][0];

    pkPlane = &m_akPlanes[LEFT];
    pkPlane->x = kClipSpace[0][3] + kClipSpace[0][0];
    pkPlane->y = kClipSpace[1][3] + kClipSpace[1][0];
    pkPlane->z = kClipSpace[2][3] + kClipSpace[2][0];
    pkPlane->w = kClipSpace[3][3] + kClipSpace[3][0];

    pkPlane = &m_akPlanes[BOTTOM];
    pkPlane->x = kClipSpace[0][3] + kClipSpace[0][1];
    pkPlane->y = kClipSpace[1][3] + kClipSpace[1][1];
    pkPlane->z = kClipSpace[2][3] + kClipSpace[2][1];
    pkPlane->w = kClipSpace[3][3] + kClipSpace[3][1];

    pkPlane = &m_akPlanes[TOP];
    pkPlane->x = kClipSpace[0][3] - kClipSpace[0][1];
    pkPlane->y = kClipSpace[1][3] - kClipSpace[1][1];
    pkPlane->z = kClipSpace[2][3] - kClipSpace[2][1];
    pkPlane->w = kClipSpace[3][3] - kClipSpace[3][1];

    pkPlane = &m_akPlanes[BACK];
    pkPlane->x = kClipSpace[0][3] - kClipSpace[0][2];
    pkPlane->y = kClipSpace[1][3] - kClipSpace[1][2];
    pkPlane->z = kClipSpace[2][3] - kClipSpace[2][2];
    pkPlane->w = kClipSpace[3][3] - kClipSpace[3][2];

    pkPlane = &m_akPlanes[FRONT];
    pkPlane->x = kClipSpace[0][3] + kClipSpace[0][2];
    pkPlane->y = kClipSpace[1][3] + kClipSpace[1][2];
    pkPlane->z = kClipSpace[2][3] + kClipSpace[2][2];
    pkPlane->w = kClipSpace[3][3] + kClipSpace[3][2];
*/
    for(uint i = 0; i < 6; i++)
    { 
        float fD = sqrtf(m_akPlanes[i].x * m_akPlanes[i].x +
                         m_akPlanes[i].y * m_akPlanes[i].y + 
                         m_akPlanes[i].z * m_akPlanes[i].z );
        if(fD > 0.0f)
            m_akPlanes[i] /= fD;
    }
}

bool
Frustum::isSphereVisible(
    const float3 &rkCenter,
    float fRadius) const
{
    for(uint i = 0; i < 6; i++ )    
    {
        float fD = m_akPlanes[i].x * rkCenter.x + 
                   m_akPlanes[i].y * rkCenter.y + 
                   m_akPlanes[i].z * rkCenter.z + 
                   m_akPlanes[i].w;

        if( fD <= -fRadius )
        {
            return false;
        }
    }

    return true;
}
```

[Next](common-frustum.h.md)[Previous](common-fbo.h.md)

