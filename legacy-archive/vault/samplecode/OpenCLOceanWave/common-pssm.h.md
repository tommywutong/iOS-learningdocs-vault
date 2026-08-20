---
title: OpenCL_OceanWave
apple_id: DTS40009447
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2011-04-13'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_OceanWave/Listings/common_pssm_h.html
archived_at: '2026-07-18T03:17:48.392244Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL_OceanWave](OpenCLOceanWave.md)


[Next](common-shader.cpp.md)[Previous](common-pssm.cpp.md)

Current information on this Developer Library topic can be found here:

- [Performance > Multiprocessing](https://developer.apple.com/referencelibrary/Performance/idxMultiprocessing-date.html)

# common/pssm.h

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

#ifndef __PARALLEL_SPLIT_SHADOW_MAP_H__
#define __PARALLEL_SPLIT_SHADOW_MAP_H__

#include "compute_types.h"
#include "texture.h"
#include "camera.h"
#include "fbo.h"

class ParallelSplitShadowMapper
{

public:

    typedef enum PassType 
    {
        PSSM_DEPTH_PASS,
        PSSM_SHADOW_PASS
    };

public:

    ParallelSplitShadowMapper();
    ~ParallelSplitShadowMapper();

    bool setup(
        uint uiWidth, uint uiHeight, 
        uint uiSplitCount, 
        float fNear, float fFar);

    void update(const Camera &rkCamera);

    bool enable(PassType ePassType, uint uiSplit = 0);

    bool disable(PassType ePassType, uint uiSplit = 0);  

    void setLightPosition(const float3 &rkV);

    void setLightFrame(
        const float3 &rkUp, 
        const float3 &rkView, 
        const float3 &rkLeft);  

    void setShadowMapTextureUnit(GLenum eUnit)      { m_eShadowMapTextureUnit = eUnit; }

    uint getSplitCount() const                      { return m_uiSplitCount; }
    GLenum getShadowMapTextureUnit() const          { return m_eShadowMapTextureUnit; }
    const float3& getLightPosition() const          { return m_kLightCamera.getPosition(); }

protected:
    void destroy();

    float16 computeLightMatrix(
        float4 akFrustumCorners[8],
        const float16& rkModelviewProjectionMatrix,
        float fFov, float fAspect, 
        float fNearClip, float fFarClip);

    void computeSplitDistances(
        float *afDistances, 
        unsigned int uiCount, 
        float fNear, float fFar);

    void computeFrustumCorners(
        float4 akFrustum[8], 
        const float3 &rkPos, 
        const float3 &rkView, 
        const float3 &rkUp,
        float fNear, float fFar, 
        float fScale, float fFov, 
        float fAspect);

    void enableShadowMap(
        float16 &rkProjection, 
        float16 &rkModelView,
        GLenum eTextureUnit);

    void disableShadowMap(void);

    void enableDepthState();

    void disableDepthState();

    void enableDepthCapture(
        float16 &rkProjection,
        float16 &rkModelView);

    void disableDepthCapture();

    void fillDepthMap(
        const float16 &rkProjection,
        const float16 &rkModelView);

    void renderSceneWithShadows(
        const float16 &rkProjection, 
        const float16 &rkModelView, 
        float fNear, float fFar);

    void renderSceneSplit(void);

protected:

    bool m_bInitialized;

    float* m_afSplitDistances;
    float16 *m_akSplitProjections;
    uint m_uiSplitCount;

    float m_fPolygonOffsetScale;
    float m_fPolygonOffsetBias;

    int m_aiViewport[4];

    Camera m_kLightCamera;
    Texture m_kDepthMap;
    FrameBufferObject m_kFrameBuffer;
    GLenum m_eShadowMapTextureUnit;

};

#endif
```

[Next](common-shader.cpp.md)[Previous](common-pssm.cpp.md)

