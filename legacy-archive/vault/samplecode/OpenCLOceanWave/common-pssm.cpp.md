---
title: OpenCL_OceanWave
apple_id: DTS40009447
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2011-04-13'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_OceanWave/Listings/common_pssm_cpp.html
archived_at: '2026-07-18T03:17:48.256460Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL_OceanWave](OpenCLOceanWave.md)


[Next](common-pssm.h.md)[Previous](common-projector.h.md)

Current information on this Developer Library topic can be found here:

- [Performance > Multiprocessing](https://developer.apple.com/referencelibrary/Performance/idxMultiprocessing-date.html)

# common/pssm.cpp

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

#include "pssm.h"

ParallelSplitShadowMapper::ParallelSplitShadowMapper() :
    m_bInitialized(false),
    m_afSplitDistances(0),
    m_akSplitProjections(0),
    m_uiSplitCount(0),
    m_fPolygonOffsetScale(2.0f),
    m_fPolygonOffsetBias(4.0f),
    m_eShadowMapTextureUnit(GL_TEXTURE0_ARB)
{
    // EMPTY!
}

ParallelSplitShadowMapper::~ParallelSplitShadowMapper()
{
    destroy();
}

void ParallelSplitShadowMapper::destroy()
{
    if(m_afSplitDistances)
        delete [] m_afSplitDistances;

    m_afSplitDistances = 0;
    m_uiSplitCount = 0;
    m_bInitialized = false;
}

bool
ParallelSplitShadowMapper::setup(
    uint uiWidth, uint uiHeight, 
    uint uiSplitCount, float fNear, float fFar)
{
    destroy();

    m_afSplitDistances = new float[uiSplitCount];
    if(!m_afSplitDistances)
        return false;

    m_akSplitProjections = new float16[uiSplitCount];
    if(!m_akSplitProjections)
        return false;

    m_uiSplitCount = uiSplitCount;

    m_kLightCamera.setNearClip(fNear);
    m_kLightCamera.setFarClip(fFar);

    bool bOk = m_kDepthMap.setup(uiWidth,
                                 uiHeight,
                                 GL_TEXTURE_2D,
                                 GL_DEPTH_COMPONENT24,
                                 GL_DEPTH_COMPONENT,
                                 GL_FLOAT);

    if(!bOk)
        return false;

    m_kDepthMap.setTextureUnit(m_eShadowMapTextureUnit);
    m_kDepthMap.setFilterMode(GL_LINEAR);
    m_kDepthMap.setWrapMode(GL_CLAMP);
    m_kDepthMap.setCompareFunc(GL_LEQUAL);
    m_kDepthMap.setDepthMode(GL_LUMINANCE);
    m_kDepthMap.update();

    printf("Creating Shadow Map [%d]...\n", m_kDepthMap.getTextureId());
//    m_kDepthMapId = m_kDepthMap.getTextureId();

    bOk = m_kFrameBuffer.setup(uiWidth, uiHeight, false);
    if(!bOk)
        return false;

    m_kFrameBuffer.attach(GL_DEPTH_ATTACHMENT_EXT, 
                          m_kDepthMap.getTarget(), 
                          m_kDepthMap.getTextureId());


    m_bInitialized = true; 
    return true;
}

bool 
ParallelSplitShadowMapper::enable(
    PassType ePassType, uint uiSplit)
{
    if(!m_bInitialized)
        return false;

    if(uiSplit > m_uiSplitCount)
        return false;

    switch (ePassType) 
    {
        case PSSM_DEPTH_PASS:
        {
            float16 kMV = m_kLightCamera.getModelViewMatrix();
            float16 kPM = m_akSplitProjections[uiSplit];
            enableDepthCapture(kPM, kMV);
            break;
        }
        case PSSM_SHADOW_PASS:
        {
            float16 kMV = m_kLightCamera.getModelViewMatrix();
            float16 kPM = m_akSplitProjections[uiSplit];
            enableShadowMap(kPM, kMV, m_eShadowMapTextureUnit);
            break;
        }
        default:
        {
            assert("PSSM: Invalid Pass Type!\n");
            break;
        }
    }

    return false;
}

bool 
ParallelSplitShadowMapper::disable(
    PassType ePassType, uint uiSplit)
{
    if(!m_bInitialized)
        return false;

    if(uiSplit > m_uiSplitCount)
        return false;

    switch (ePassType) 
    {
        case PSSM_DEPTH_PASS:
        {
            disableDepthCapture();
            break;
        }
        case PSSM_SHADOW_PASS:
        {
            disableShadowMap();
            break;
        }
        default:
        {
            assert("PSSM: Invalid Pass Type!\n");
            break;
        }
    }

    return false;
}


float16 
ParallelSplitShadowMapper::computeLightMatrix(
    float4 akFrustumCorners[8],
    const float16& rkModelviewProjectionMatrix,
    float fFov, float fAspect, float fNearClip, float fFarClip)
{
    int i = 0;
    float fFarLight = 0.0f;
    float4 kMin = make_float3( +MAXFLOAT, +MAXFLOAT, +MAXFLOAT);
    float4 kMax = make_float3( -MAXFLOAT, -MAXFLOAT, -MAXFLOAT);
    for(i = 0; i < 8; i++)
    {
        float4 kFP = akFrustumCorners[i]; 
        float4 kTV = rkModelviewProjectionMatrix * kFP;

        kTV.x /= kTV.w;
        kTV.y /= kTV.w;

        kMax = max(kMax, kTV);
        kMin = min(kMin, kTV);
    }

    kMax.x = clamp(kMax.x, -1.0f, 1.0f);
    kMax.y = clamp(kMax.y, -1.0f, 1.0f);

    kMin.x = clamp(kMin.x, -1.0f, 1.0f);
    kMin.y = clamp(kMin.y, -1.0f, 1.0f);

    fFarLight = kMax.z + fNearClip + 1.5f;

//  float16 kPSM = perspective(fFov, fAspect, fNearClip, fFarLight);
    float16 kPSM = ortho(-1.0f, 1.0f, -1.0f, 1.0f, -fFarLight, fFarLight);

    float4 kDiff = (kMax - kMin);
    float4 kSum = (kMax + kMin);

    float2 kScale = make_float2(2.0f, 2.0f) / make_float2(kDiff.x, kDiff.y);

    float2 kOffset = make_float2(kSum.x, kSum.y) * kScale * -0.5f;

    float16 kCVM = make_float16(
                      kScale.x,    0.0f, 0.0f, 0.0f,
                        0.0f,  kScale.y, 0.0f, 0.0f,
                        0.0f,    0.0f, 1.0f, 0.0f,
                     kOffset.x, kOffset.y, 0.0f, 1.0f);

    float16 kResult = kCVM * kPSM;
    return kResult;
}

void 
ParallelSplitShadowMapper::computeSplitDistances(
    float *afDistances, 
    unsigned int uiCount, 
    float fNear, float fFar)
{
    float fLambda = 0.6f;
    float fRatio = fFar / fNear;
    for(uint i = 0; i < uiCount; i++)
    {
        float fInvI = i / (float) uiCount;
        float fLog = fNear * powf(fRatio, fInvI);
        float fUniform = fNear + (fFar - fNear) * fInvI;
        afDistances[i] = fLog * fLambda + fUniform * (1.0f - fLambda);
    }

    afDistances[0] = fNear;
    afDistances[uiCount] = fFar;
}

void 
ParallelSplitShadowMapper::computeFrustumCorners(
    float4 akFrustum[8], 
    const float3 &rkPos, 
    const float3 &rkView, 
    const float3 &rkUp,
    float fNear, float fFar, 
    float fScale, float fFov, 
    float fAspect)
{
    static const float s_fRadians = M_PI / 180.0f;

    float3 kVZ = normalize(rkView - rkPos);
    float3 kVX = normalize(cross(rkUp, kVZ));
    float3 kVY = normalize(cross(kVZ, kVX));

    float fNearHeight = tanf(s_fRadians * fFov * 0.5f) * fNear;
    float fNearWidth = fNearHeight * fAspect;

    float fFarHeight = tanf(s_fRadians * fFov * 0.5f) * fFar;
    float fFarWidth = fFarHeight * fAspect;

    float3 kNPC = rkPos + kVZ * fNear;
    float3 kFPC = rkPos + kVZ * fFar;

    float3 kTX = kVX * fNearWidth;
    float3 kTY = kVY * fNearHeight;

    float3 k0 = kNPC - kTX - kTY;
    float3 k1 = kNPC - kTX + kTY;
    float3 k2 = kNPC + kTX + kTY;
    float3 k3 = kNPC + kTX - kTY;

    kTX = kVX * fFarWidth;
    kTY = kVY * fFarHeight;

    float3 k4 = kFPC - kTX - kTY;
    float3 k5 = kFPC - kTX + kTY;
    float3 k6 = kFPC + kTX + kTY;
    float3 k7 = kFPC + kTX - kTY;

    float3 kC = k0 + k1 + k2 + k3 + k4 + k5 + k6 + k7;
    kC.x /= 8.0f;
    kC.y /= 8.0f;
    kC.z /= 8.0f;

    float fScaleMinusOne = fScale - 1.0f;

    k0 += (k0 - kC) * fScaleMinusOne;
    k1 += (k1 - kC) * fScaleMinusOne;
    k2 += (k2 - kC) * fScaleMinusOne;
    k3 += (k3 - kC) * fScaleMinusOne;
    k4 += (k4 - kC) * fScaleMinusOne;
    k5 += (k5 - kC) * fScaleMinusOne;
    k6 += (k6 - kC) * fScaleMinusOne;
    k7 += (k7 - kC) * fScaleMinusOne;

    akFrustum[0] = k0;
    akFrustum[1] = k1;
    akFrustum[2] = k2;
    akFrustum[3] = k3;
    akFrustum[4] = k4;
    akFrustum[5] = k5;
    akFrustum[6] = k6;
    akFrustum[7] = k7;
}

void
ParallelSplitShadowMapper::enableShadowMap(
    float16 &rkProjection, 
    float16 &rkModelView,
    GLenum eTextureUnit)
{
    const GLfloat afBias[] = {0.5f, 0.0f, 0.0f, 0.0f, 
                              0.0f, 0.5f, 0.0f, 0.0f,
                              0.0f, 0.0f, 0.5f, 0.0f,
                              0.5f, 0.5f, 0.5f, 1.0f};

    const GLdouble x[] = {1.0, 0.0, 0.0, 0.0};
    const GLdouble y[] = {0.0, 1.0, 0.0, 0.0};
    const GLdouble z[] = {0.0, 0.0, 1.0, 0.0};
    const GLdouble w[] = {0.0, 0.0, 0.0, 1.0};

    glEnable( GL_LIGHTING );

    m_kDepthMap.setCompareMode(GL_COMPARE_R_TO_TEXTURE_ARB);
    m_kDepthMap.enable(eTextureUnit);
    m_kDepthMap.update();

    glEnable(GL_TEXTURE_GEN_S);
    glEnable(GL_TEXTURE_GEN_T);
    glEnable(GL_TEXTURE_GEN_R);
    glEnable(GL_TEXTURE_GEN_Q);

    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_EYE_LINEAR);
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_EYE_LINEAR);
    glTexGeni(GL_R, GL_TEXTURE_GEN_MODE, GL_EYE_LINEAR);
    glTexGeni(GL_Q, GL_TEXTURE_GEN_MODE, GL_EYE_LINEAR);

    glTexGendv(GL_S, GL_EYE_PLANE, x);
    glTexGendv(GL_T, GL_EYE_PLANE, y);
    glTexGendv(GL_R, GL_EYE_PLANE, z);
    glTexGendv(GL_Q, GL_EYE_PLANE, w);

    glMatrixMode( GL_TEXTURE );
    glLoadMatrixf( afBias );                   
    glMultMatrixf( rkProjection );                 
    glMultMatrixf( rkModelView );
    glMatrixMode(GL_MODELVIEW);
}

void 
ParallelSplitShadowMapper::disableShadowMap(void)
{
    glMatrixMode( GL_TEXTURE );
    glLoadIdentity();    
    glMatrixMode( GL_MODELVIEW );

    glDisable(GL_TEXTURE_GEN_S);
    glDisable(GL_TEXTURE_GEN_T);
    glDisable(GL_TEXTURE_GEN_R);
    glDisable(GL_TEXTURE_GEN_Q);

    m_kDepthMap.setCompareMode(GL_NONE);
    m_kDepthMap.update();
    m_kDepthMap.disable();
}

void 
ParallelSplitShadowMapper::enableDepthState()
{
    glDisable(GL_LIGHTING);
    glDisable(GL_TEXTURE_2D);
    glDisable(GL_ALPHA_TEST);

    glPolygonOffset(m_fPolygonOffsetScale, m_fPolygonOffsetBias);
    glEnable(GL_POLYGON_OFFSET_FILL);

    glDepthMask( GL_TRUE );
    glClearDepth(1.0f);

    glDepthFunc(GL_LESS);
    glEnable(GL_CULL_FACE);
    glCullFace(GL_BACK);

    glColorMask(GL_FALSE,GL_FALSE,GL_FALSE,GL_FALSE);
    glShadeModel(GL_FLAT);

}

void 
ParallelSplitShadowMapper::disableDepthState()
{
    glDisable(GL_CULL_FACE);
    glDepthFunc(GL_LEQUAL);

    glDisable(GL_POLYGON_OFFSET_FILL);

    glEnable(GL_LIGHTING);
    glColorMask(GL_TRUE,GL_TRUE,GL_TRUE,GL_TRUE);
    glShadeModel(GL_SMOOTH);
}

void 
ParallelSplitShadowMapper::enableDepthCapture(
    float16 &rkProjection,
    float16 &rkModelView)
{        
    glGetIntegerv(GL_VIEWPORT, m_aiViewport);

    m_kFrameBuffer.enable(true);

    glMatrixMode( GL_PROJECTION );
    glLoadMatrixf( rkProjection );

    glMatrixMode(GL_MODELVIEW);
    glLoadMatrixf( rkModelView );

    enableDepthState();
}

void
ParallelSplitShadowMapper::disableDepthCapture()
{
    disableDepthState();
    m_kFrameBuffer.disable();
    glViewport(m_aiViewport[0], m_aiViewport[1], m_aiViewport[2], m_aiViewport[3]);
}

void 
ParallelSplitShadowMapper::update(
    const Camera &rkCamera)
{
    if(!m_bInitialized)
        return;

    m_kLightCamera.update();

    computeSplitDistances(m_afSplitDistances, m_uiSplitCount, 
                          m_kLightCamera.getNearClip(),  
                          m_kLightCamera.getFarClip());

    float16 kLMVP = m_kLightCamera.getModelViewProjectionMatrix();

    for( uint i = 0; i < m_uiSplitCount; i++)
    {
        float4 akFrustum[8];

        float fFar = m_afSplitDistances[i + 1];

        computeFrustumCorners(akFrustum, 
                              rkCamera.getPosition(), 
                              rkCamera.getViewDirection(), 
                              rkCamera.getUpDirection(), 
                              1.0f, fFar, 1.0f, 45.0f, rkCamera.getAspect());


        float16 kLightMatrix = computeLightMatrix(akFrustum, kLMVP,
                                                  m_kLightCamera.getFovInDegrees(), 1.0f,
                                                  m_kLightCamera.getNearClip(), 
                                                  m_kLightCamera.getFarClip());

        m_akSplitProjections[i] = kLightMatrix;
    }    
}

void
ParallelSplitShadowMapper::setLightPosition(const float3 &rkV)
{
    m_kLightCamera.setPosition(rkV);
}

void
ParallelSplitShadowMapper::setLightFrame(
    const float3 &rkUp, 
    const float3 &rkView, 
    const float3 &rkLeft)
{
    m_kLightCamera.setFrame(rkUp, rkView, rkLeft);
}
```

[Next](common-pssm.h.md)[Previous](common-projector.h.md)

