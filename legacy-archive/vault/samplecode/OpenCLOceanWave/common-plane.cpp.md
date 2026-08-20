---
title: OpenCL_OceanWave
apple_id: DTS40009447
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2011-04-13'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_OceanWave/Listings/common_plane_cpp.html
archived_at: '2026-07-18T03:17:47.762393Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL_OceanWave](OpenCLOceanWave.md)


[Next](common-plane.h.md)[Previous](common-meshrenderer.h.md)

Current information on this Developer Library topic can be found here:

- [Performance > Multiprocessing](https://developer.apple.com/referencelibrary/Performance/idxMultiprocessing-date.html)

# common/plane.cpp

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

#include "plane.h"
#include <stdio.h>

Plane::Plane()
{
    // EMPTY!
}

Plane::Plane(const Plane& rfPlane) :
    m_kNormal(rfPlane.m_kNormal),
    m_fConstant(rfPlane.m_fConstant)
{
    // EMPTY!
}

Plane::Plane(const float3& rkNormal, float fConstant) :
    m_kNormal(rkNormal),
    m_fConstant(fConstant)
{
    // EMPTY!
}

Plane::Plane(const float3 &rkPoint, const float3 &rkNormal) :
    m_kNormal(rkNormal)
{
    m_fConstant = dot(rkNormal, rkPoint);
}

Plane::Plane(
    const float3& rfP0, 
    const float3& rfP1,
    const float3& rfP2)
{
    float3 fE0 = rfP1 - rfP0;
    float3 fE1 = rfP2 - rfP0;
    m_kNormal = normalize(cross(fE0, fE1));
    m_fConstant = dot(m_kNormal, rfP0);
}

Plane& 
Plane::operator= (const Plane& rfPlane)
{
    m_kNormal = rfPlane.m_kNormal;
    m_fConstant = rfPlane.m_fConstant;
    return *this;
}

int 
Plane::side (
    const float3& rkPoint) const
{
    float fDistance = distance(rkPoint);

    if (fDistance < 0.0f)
    {
        return -1;
    }

    if (fDistance > 0.0f)
    {
        return +1;
    }

    return 0;
}

float 
Plane::distance(
    const float3& rkPoint) const
{
    return dot(m_kNormal, rkPoint) - m_fConstant;
}

float
Plane::dotNormal(
    const float3 &rkNormal) const
{
    return dot(m_kNormal, rkNormal);
}

bool
Plane::findIntersection(
    float3 &rkIntersection,
    const float3 &rkPoint,
    const float3 &rkDir,
    float fZeroEpsilon) const
{
    if(dot(rkDir, m_kNormal) == 0.0f)
        return false;

    float fT = (m_fConstant - dot(m_kNormal, rkPoint)) / (dot(m_kNormal, rkDir));
    rkIntersection = rkPoint + rkDir * fT;
    return true;
}

bool
Plane::findIntersection(
    float &rfT,
    const float3 &rkPoint, 
    const float3 &rkDirection,
    float fEpsilon) const
{
    float fD = dot(rkDirection, m_kNormal);
    float fS = distance(rkPoint);
    if (fabs(fD) > fEpsilon)
    {
        rfT = -fS/fD;
//        printf("Plane: Intersection at %8.3f\n", rfT);
        return true;
    }

    if (fabs(fS) <= fEpsilon)
    {
        rfT = 0.0f;
//        printf("Plane: Intersection at %8.3f\n", rfT);
        return true;
    }

//    printf("Plane: No Intersection!\n", rfT);

    return false;
}

bool 
Plane::intersects(
    const float3 &rkPoint, 
    const float3 &rkDirection, 
    float fEpsilon) const
{
    float fD = dot(rkDirection, m_kNormal);
    if (fabs(fD) > fEpsilon)
    {
        return true;
    }

    fD = distance(rkPoint);
    if (fabs(fD) <= fEpsilon)
    {
        return true;
    }

    return false;
}
```

[Next](common-plane.h.md)[Previous](common-meshrenderer.h.md)

