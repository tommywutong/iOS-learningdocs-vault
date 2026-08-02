---
title: OpenCL_OceanWave
apple_id: DTS40009447
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2011-04-13'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_OceanWave/Listings/common_csm_cpp.html
archived_at: '2026-07-18T03:17:46.402767Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL_OceanWave](OpenCLOceanWave.md)


[Next](common-csm.h.md)[Previous](common-computetypes.h.md)

Current information on this Developer Library topic can be found here:

- [Performance > Multiprocessing](https://developer.apple.com/referencelibrary/Performance/idxMultiprocessing-date.html)

# common/csm.cpp

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

#include "csm.h"

////////////////////////////////////////////////////////////////////////////////

CascadedShadowMapper::CascadedShadowMapper() :
    m_bInitialized(false),
    m_afSplitDistances(0),
    m_akSplitPartitions(0),
    m_akSplitProjections(0),
    m_uiSplitCount(0),
    m_uiShadowMapResolution(0),
    m_fPolygonOffsetScale(1.0f),
    m_fPolygonOffsetBias(4096.0f),
    m_eShadowMapTextureUnit(GL_TEXTURE0_ARB)
{
    // EMPTY!
}

CascadedShadowMapper::~CascadedShadowMapper()
{
    destroy();
}

void CascadedShadowMapper::destroy()
{
    if(m_afSplitDistances)
        delete [] m_afSplitDistances;

    m_afSplitDistances = 0;
    m_uiSplitCount = 0;
    m_bInitialized = false;
}

bool
CascadedShadowMapper::setup(
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

    m_akSplitPartitions = new FrustumPartition[uiSplitCount];
    if(!m_akSplitPartitions)
        return false;

    m_uiSplitCount = uiSplitCount;       
    m_uiShadowMapResolution = max(uiWidth, uiHeight);

    bool bOk = m_kDepthMap.setup(uiWidth,
                                 uiHeight,
                                 GL_TEXTURE_2D,
                                 GL_DEPTH_COMPONENT24,
                                 GL_DEPTH_COMPONENT,
                                 GL_UNSIGNED_INT);

    if(!bOk)
        return false;

    m_kDepthMap.setTextureUnit(m_eShadowMapTextureUnit);
    m_kDepthMap.setFilterMode(GL_NEAREST);
    m_kDepthMap.setWrapMode(GL_CLAMP_TO_EDGE);
    m_kDepthMap.setCompareFunc(GL_LEQUAL);
    m_kDepthMap.setDepthMode(GL_LUMINANCE);
    m_kDepthMap.update();

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
CascadedShadowMapper::enableDepthPass(
    uint uiSplit, bool bUseActiveFramebuffer)
{
    if(!m_bInitialized)
        return false;

    if(uiSplit > m_uiSplitCount)
        return false;

    bool bClear = true; // (uiSplit == 0) ? true : false;
    float16 kPM = m_akSplitProjections[uiSplit];
    enableDepthCapture(kPM, m_kLightModelView, bUseActiveFramebuffer, bClear);
    return true;
}

bool 
CascadedShadowMapper::enableShadowPass(
    uint uiSplit)
{
    if(!m_bInitialized)
        return false;

    if(uiSplit > m_uiSplitCount)
        return false;

    float16 kPM = m_akSplitProjections[uiSplit];
    enableShadowMap(kPM, m_kLightModelView, m_eShadowMapTextureUnit);
    return true;
}

bool 
CascadedShadowMapper::disableDepthPass(
    uint uiSplit)
{
    if(!m_bInitialized)
        return false;

    if(uiSplit > m_uiSplitCount)
        return false;

    disableDepthCapture();
    return true;
}

bool 
CascadedShadowMapper::disableShadowPass(
    uint uiSplit)
{
    if(!m_bInitialized)
        return false;

    if(uiSplit > m_uiSplitCount)
        return false;

    disableShadowMap();
    return true;
}

float16
CascadedShadowMapper::computeOrthoCropMatrix(
    const FrustumPartition &rkPartition, 
    const float16 &rkLightModelview,
    float fNear, float fFar)
{
    int i = 0;    

    float16 kMVP = rkLightModelview * ortho(-1.0f, 1.0f, -1.0f, 1.0f, fNear, fFar);

    float3 kMin = make_float3( +MAXFLOAT, +MAXFLOAT, +MAXFLOAT);
    float3 kMax = make_float3( -MAXFLOAT, -MAXFLOAT, -MAXFLOAT);

    for(i = 0; i < 8; i++)
    {
        float4 kFP = rkPartition.corners[i]; 
        float4 kTV = kMVP * kFP;

        kTV.x /= kTV.w;
        kTV.y /= kTV.w;

        float3 kV = make_float3(kTV.x, kTV.y, kTV.z);

        kMax = max(kMax, kV);
        kMin = min(kMin, kV);
    }

    float3 kDiff = (kMax - kMin);
    float3 kSum = (kMax + kMin);
    float3 kTwo = make_float3(2.0f, 2.0f, 2.0f);

    float3 kScale = kTwo / kDiff;
    float3 kOffset = kSum * kScale * -0.5f;

    float16 kCropMatrix = make_float16(
          kScale.x,      0.0f, 0.0f, 0.0f,
              0.0f,  kScale.y, 0.0f, 0.0f,
              0.0f,      0.0f, 1.0f, 0.0f,
         kOffset.x, kOffset.y, 0.0f, 1.0f);

    return kCropMatrix;
}

float16
CascadedShadowMapper::computeProjectionMatrix(
    const float16 &rkOrthoCropMatrix,
    float fNear, float fFar)
{
    float16 kOrthoProjection = ortho( -1.0f, 1.0f, -1.0f, 1.0f, fNear, fFar );
    float16 kTrimmedProjection = rkOrthoCropMatrix * kOrthoProjection;
    return kTrimmedProjection;
}

void
CascadedShadowMapper::computeSplitDistances(
    FrustumPartition *akPartitions,
    unsigned int uiCount, 
    float fNear, float fFar)
{
    const float fWeight = 0.95f;
    float fLambda = fWeight;
    float fRatio = fFar / fNear;

    akPartitions[0].near = fNear;

    for(uint i = 1; i < uiCount; i++)
    {
        float fInvI = i / (float) uiCount;
        float fLog = fNear * powf(fRatio, fInvI);
        float fUniform = fNear + (fFar - fNear) * fInvI;

        akPartitions[i].near = fLog * fLambda + fUniform * (1.0f - fLambda);
        akPartitions[i-1].far = akPartitions[i].near * 1.0025f;
    }

    akPartitions[uiCount-1].far = fFar;
}

void
CascadedShadowMapper::computeFrustumCorners(
    FrustumPartition &rkPartition, 
    const float3 &rkCenter, 
    const float3 &rkView, 
    const float3 &rkUp )
{
    float3 kFarCenter = rkCenter + rkView * rkPartition.far;
    float3 kNearCenter = rkCenter + rkView * rkPartition.near;

    float3 kRight = normalize( cross(rkView, rkUp) );
    float3 kUp = normalize( cross( kRight, rkView ) );

    float fNearHeight = tanf(rkPartition.fov * 0.5f) * rkPartition.near;
    float fNearWidth = fNearHeight * rkPartition.aspect;

    float fFarHeight = tanf(rkPartition.fov * 0.5f) * rkPartition.far;
    float fFarWidth = fFarHeight * rkPartition.aspect;

    rkPartition.corners[0] = kNearCenter - rkUp * fNearHeight - kRight * fNearWidth;
    rkPartition.corners[1] = kNearCenter + rkUp * fNearHeight - kRight * fNearWidth;
    rkPartition.corners[2] = kNearCenter + rkUp * fNearHeight + kRight * fNearWidth;
    rkPartition.corners[3] = kNearCenter - rkUp * fNearHeight + kRight * fNearWidth;

    rkPartition.corners[4] = kFarCenter - rkUp * fFarHeight - kRight * fFarWidth;
    rkPartition.corners[5] = kFarCenter + rkUp * fFarHeight - kRight * fFarWidth;
    rkPartition.corners[6] = kFarCenter + rkUp * fFarHeight + kRight * fFarWidth;
    rkPartition.corners[7] = kFarCenter - rkUp * fFarHeight + kRight * fFarWidth;
}


void
CascadedShadowMapper::enableShadowMap(
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

    glColorMask( GL_TRUE, GL_TRUE, GL_TRUE, GL_TRUE );
    glDepthMask( GL_TRUE );

    glEnable( GL_LIGHTING );

    glEnable( GL_CULL_FACE );
    glFrontFace( GL_CCW );

    glEnable( GL_DEPTH_TEST );
    glDepthFunc( GL_LEQUAL );

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
//    glMultMatrixf( m_kCameraInverseModelView.v );
    glMatrixMode(GL_MODELVIEW);
}

void 
CascadedShadowMapper::disableShadowMap(void)
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
CascadedShadowMapper::enableDepthState()
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
CascadedShadowMapper::disableDepthState()
{
    glDisable(GL_CULL_FACE);
    glDepthFunc(GL_LEQUAL);

    glDisable(GL_POLYGON_OFFSET_FILL);

    glEnable(GL_LIGHTING);
    glColorMask(GL_TRUE,GL_TRUE,GL_TRUE,GL_TRUE);
    glShadeModel(GL_SMOOTH);
}


void 
CascadedShadowMapper::enableDepthCapture(
    float16 &rkProjection,
    float16 &rkModelView,
    bool bUseActiveFramebuffer,
    bool bClear)
{        
    glGetIntegerv(GL_VIEWPORT, m_aiViewport);

    if(!bUseActiveFramebuffer)
        m_kFrameBuffer.enable(bClear);

    glMatrixMode( GL_PROJECTION );
    glLoadMatrixf( rkProjection );

    glMatrixMode(GL_MODELVIEW);
    glLoadMatrixf( rkModelView );

    if(!bUseActiveFramebuffer)
        enableDepthState();
}

void
CascadedShadowMapper::disableDepthCapture()
{
    if(m_kFrameBuffer.isEnabled())
    {
        disableDepthState();
        m_kFrameBuffer.disable();
        glViewport(m_aiViewport[0], m_aiViewport[1], m_aiViewport[2], m_aiViewport[3]);
    }
}



void 
CascadedShadowMapper::update(
    const Camera &rkCamera, float fShadowNear, float fShadowFar)
{
    if(!m_bInitialized)
        return;

//    m_kCameraInverseModelView = rkCamera.getInverseModelViewMatrix();

    for ( uint i = 0; i < m_uiSplitCount; i++)
    {
        m_akSplitPartitions[i].fov = radians(rkCamera.getFovInDegrees());
        m_akSplitPartitions[i].aspect = rkCamera.getAspect();

    }

    computeSplitDistances(m_akSplitPartitions,
                          m_uiSplitCount, 
                          rkCamera.getNearClip(),  
                          rkCamera.getFarClip());

    for ( uint i = 0; i < m_uiSplitCount; i++ )
    {
        computeFrustumCorners(
            m_akSplitPartitions[i], 
            rkCamera.getPosition(), 
            rkCamera.getViewDirection(), 
            rkCamera.getUpDirection() );

        float16 kCropMatrix = computeOrthoCropMatrix(
                                    m_akSplitPartitions[i], 
                                    m_kLightModelView,
                                    fShadowNear,
                                    fShadowFar);

        m_akSplitProjections[i] = computeProjectionMatrix(
                                    kCropMatrix, 
                                    fShadowNear, 
                                    fShadowFar);
    }   
}

void
CascadedShadowMapper::setLightDirection(const float3 &rkV)
{
    static const float3 s_kZero = make_float3(0.0f, 0.0f, 0.0f);
    static const float3 s_kNegX = make_float3(-1.0f, 0.0f, 0.0f);

    m_kLightModelView = lookat( s_kZero, -rkV, s_kNegX);
}
```

[Next](common-csm.h.md)[Previous](common-computetypes.h.md)

