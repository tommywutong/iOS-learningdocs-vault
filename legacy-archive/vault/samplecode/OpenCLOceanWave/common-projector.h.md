---
title: OpenCL_OceanWave
apple_id: DTS40009447
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2011-04-13'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_OceanWave/Listings/common_projector_h.html
archived_at: '2026-07-18T03:17:48.206383Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL_OceanWave](OpenCLOceanWave.md)


[Next](common-pssm.cpp.md)[Previous](common-projector.cpp.md)

Current information on this Developer Library topic can be found here:

- [Performance > Multiprocessing](https://developer.apple.com/referencelibrary/Performance/idxMultiprocessing-date.html)

# common/projector.h

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

#ifndef __PROJECTOR__
#define __PROJECTOR__

#include "compute_types.h"
#include "compute_math.h"
#include "camera.h"

#include <OpenGL/gl.h>

////////////////////////////////////////////////////////////////////////////////

class Projector
{

public:
    Projector();
    ~Projector();

    void setup();
    void update();
    void drawFrustum();

    bool isVisible()                                        { return m_bIsVisible;          }

    void setSimpleCorrection(bool bSimple)                  { m_bSimple = bSimple;          }
    void setElevation(float fV)                             { m_fElevation = fV;            }
    void setStrength(float fV)                              { m_fStrength = fV;             }
    void setUpperLimit(float fV)                            { m_fUpperLimit = fV;           }
    void setLowerLimit(float fV)                            { m_fLowerLimit = fV;           }
    void setReferenceCamera(Camera *pkCamera)               { m_pkCamera = pkCamera;        }

    const float16& getInverseModelViewProjectionMatrix()    { return m_kInverseModelViewProjectionMatrix; }
    const float16& getRangeMatrix()                         { return m_kRangeMatrix;        }
    const float4* getProjectedCorners()                     { return m_akCorners;           }
    const float4& getProjectedRange()                       { return m_kRange;              }

    float getElevation()                                    { return m_fElevation;          }
    float getStrength()                                     { return m_fStrength;           }
    float getUpperLimit()                                   { return m_fUpperLimit;         }
    float getLowerLimit()                                   { return m_fLowerLimit;         }
    bool getDebug()                                         { return m_bDebug;              }
    bool getSimpleCorrection()                              { return m_bSimple;             }

protected:

    void updateOrientation();
    void updateModelViewMatrix();
    void updateProjectionMatrix();
    void updateRangeMatrix(const float4 &rkRange);

    void findFrustumCorners(
        float4 akFrustum[8],
        const float16 &rkInvViewPrj);

    float4 findProjectedRange(
        uint uiIntersectionCount,
        float4 akIntersections[32],
        const float16 &rkViewPrj);

    uint findPlanarIntersections(
        float4 akIntersections[24],
        const float4 akFrustum[8]);

    bool findLinePlaneIntersection(
        float fPlaneY, 
        const float4 &rkPoint1, 
        const float4 &rkPoint2, 
        float4 &rkIntersection);

    void findProjectedCorners(
        float4 akCorners[4], 
        const float4 &rfRange,
        const float16 &rfInvViewPrj);


protected:

    bool m_bDebug;
    bool m_bSimple;
    bool m_bIsVisible;

    float m_fElevation;
    float m_fStrength;
    float m_fUpperLimit;
    float m_fLowerLimit;

    uint m_uiIntersectionCount;
    float4 m_akIntersections[32];
    float4 m_akCorners[4];
    float4 m_akFrustum[8];
    float4 m_kRange;

    float3 m_kUp; 
    float3 m_kView;
    float3 m_kLookAt;
    float3 m_kPosition;

    float16 m_kRangeMatrix;
    float16 m_kModelViewMatrix;
    float16 m_kProjectionMatrix;
    float16 m_kInverseModelViewProjectionMatrix;

    GLdouble m_adProjection[16];
    GLdouble m_adModelView[16];

    Camera *m_pkCamera;
};

////////////////////////////////////////////////////////////////////////////////

#endif
```

[Next](common-pssm.cpp.md)[Previous](common-projector.cpp.md)

