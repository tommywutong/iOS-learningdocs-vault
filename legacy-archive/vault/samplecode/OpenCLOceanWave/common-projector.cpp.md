---
title: OpenCL_OceanWave
apple_id: DTS40009447
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2011-04-13'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_OceanWave/Listings/common_projector_cpp.html
archived_at: '2026-07-18T03:17:48.065812Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL_OceanWave](OpenCLOceanWave.md)


[Next](common-projector.h.md)[Previous](common-projectedgrid.h.md)

Current information on this Developer Library topic can be found here:

- [Performance > Multiprocessing](https://developer.apple.com/referencelibrary/Performance/idxMultiprocessing-date.html)

# common/projector.cpp

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

#include "projector.h"
#include "plane.h"

#include <OpenGL/OpenGL.h>
#include <OpenGL/glu.h>
#include <stdio.h>

Projector::Projector() :
    m_bDebug(false),
    m_bSimple(true),
    m_bIsVisible(false),
    m_fElevation(7.0f),
    m_fStrength(0.9f),
    m_fUpperLimit(+0.1f),
    m_fLowerLimit(-0.1f),
    m_pkCamera(0)
{
    // EMPTY!
}

Projector::~Projector()
{
    // EMPTY!
}

void
Projector::setup()
{
    // EMPTY!
}   

void 
Projector::update()
{
    if(!m_pkCamera)
        return;

    updateOrientation();
    updateModelViewMatrix();
    updateProjectionMatrix();

    float16 kViewPrj = m_kModelViewMatrix * m_kProjectionMatrix;
    float16 kInvViewPrj = inverse(kViewPrj);    

    findFrustumCorners(m_akFrustum, kInvViewPrj);
    m_uiIntersectionCount = findPlanarIntersections(m_akIntersections, m_akFrustum);
    if(m_uiIntersectionCount > 0)
    {
        m_kRange = findProjectedRange(m_uiIntersectionCount, m_akIntersections, kViewPrj);
        findProjectedCorners(m_akCorners, m_kRange, kInvViewPrj);
        updateRangeMatrix(m_kRange);
        m_bIsVisible = true;
    }
    else
    {
        m_bIsVisible = false;
    }
}

void
Projector::updateOrientation()
{
    float3 kNormal = make_float3(0.0f, 1.0f, 0.0f);

    Plane kBasePlane = Plane(make_float3(0.0f, 0.0f, 0.0f), kNormal);
    Plane kUpperPlane = Plane(kNormal, m_fUpperLimit);
    Plane kLowerPlane = Plane(kNormal, m_fLowerLimit);

    m_kUp = m_pkCamera->getUpDirection(); 
    m_kView = m_pkCamera->getViewDirection();
    m_kPosition = m_pkCamera->getPosition();
    m_kLookAt = m_kPosition + m_kView;

    if(m_bSimple)
    {
        m_kUp = make_float3(0.0f, 1.0f, 0.0f);
        m_kPosition = m_kPosition - m_kView * 5.0f;
        m_kLookAt = m_kPosition + m_kView;
    }
    else
    {   
        float fHeight = kLowerPlane.distance(m_kPosition);

        bool bBelow = fHeight < 0.0f;

        if(fHeight < (m_fStrength + m_fElevation))
        {
            if(bBelow)
            {
                m_kPosition += kNormal * ((m_fStrength + m_fElevation) - 2.0f * fHeight);
            }
            else
            {
                m_kPosition += kNormal * ((m_fStrength + m_fElevation) - fHeight);        
            }
        }

        if (!kBasePlane.findIntersection(m_kLookAt, m_kPosition, m_kPosition + m_kView))
        {
            float3 kFlip = m_kView - kNormal * dot(m_kView, kNormal) * 2.0f;
            kBasePlane.findIntersection(m_kLookAt, m_kPosition, m_kPosition + kFlip);
        }

        float fD = fabs( kBasePlane.dotNormal(m_kView) );
        float fZ = (m_pkCamera->getFarClip() - m_pkCamera->getNearClip()) * 0.5f;

        float3 kAim = (m_kPosition + m_kView * fZ);
        kAim = kAim - kNormal * dot(kAim, kNormal);

        m_kLookAt = ((m_kLookAt * fD + kAim * (1.0f - fD)));
        m_kView = (m_kLookAt - m_kPosition);
    }
}

void
Projector::updateProjectionMatrix()
{
    if(!m_pkCamera)
        return;

    float fRatio = ((float)m_pkCamera->getViewportWidth() / (float)m_pkCamera->getViewportHeight());

    glMatrixMode(GL_PROJECTION);
    glPushMatrix();
    glLoadIdentity(); 
    gluPerspective(
        m_pkCamera->getFovInDegrees() + 35.0f,
        m_pkCamera->getAspect() * fRatio,
        m_pkCamera->getNearClip(),
        m_pkCamera->getFarClip());

    glGetFloatv(GL_PROJECTION_MATRIX, m_kProjectionMatrix);
    glGetDoublev(GL_PROJECTION_MATRIX, m_adProjection);  
    glPopMatrix();
}

void
Projector::updateModelViewMatrix()
{
    if(!m_pkCamera)
        return;

    glMatrixMode(GL_MODELVIEW);
    glPushMatrix();
    glLoadIdentity();
    gluLookAt(
        m_kPosition.x, m_kPosition.y, m_kPosition.z,
        m_kLookAt.x, m_kLookAt.y, m_kLookAt.z,
        m_kUp.x, m_kUp.y, m_kUp.z);

    glGetFloatv(GL_MODELVIEW_MATRIX, m_kModelViewMatrix);
    glGetDoublev(GL_MODELVIEW_MATRIX, m_adModelView);
    glPopMatrix();
}

void 
Projector::updateRangeMatrix(
    const float4 &rkRange)
{
    float fDX = rkRange.z - rkRange.x;
    float fDY = rkRange.w - rkRange.y;

    m_kRangeMatrix = make_float16(
         fDX, 0.0f, 0.0f, rkRange.x,
        0.0f,  fDY, 0.0f, rkRange.y,
        0.0f, 0.0f, 1.0f, 0.0f,
        0.0f, 0.0f, 0.0f, 1.0f);

    m_kRangeMatrix = transpose(m_kRangeMatrix);
    m_kInverseModelViewProjectionMatrix = inverse((m_kModelViewMatrix * m_kProjectionMatrix));
}

uint 
Projector::findPlanarIntersections(
    float4 akIntersections[24],
    const float4 akFrustum[8])
{
    float fBasePlane = 0.5f * (m_fUpperLimit - m_fLowerLimit);    
    float4 kPosition = m_kPosition;
    float4 kView = m_kView;

    uint uiCount = 0;
    for(unsigned int i = 0; i < 4; i++)
    {
        float4 kUpper; 
        if(findLinePlaneIntersection(m_fUpperLimit, kPosition, akFrustum[i], kUpper))
        {
            kUpper.y = fBasePlane;
            akIntersections[uiCount++] = kUpper;
        }

        float4 kLower; 
        if(findLinePlaneIntersection(m_fLowerLimit, kPosition, akFrustum[i], kLower))
        {
            kLower.y = fBasePlane;
            akIntersections[uiCount++] = kLower;
        }

        float4 kUpperSide; 
        uint uiNext = (i == 3) ? (0) : (i+1);
        if(findLinePlaneIntersection(m_fUpperLimit, akFrustum[i], akFrustum[uiNext], kUpperSide))

        {
            kUpperSide.y = fBasePlane;
            akIntersections[uiCount++] = kUpperSide;
        }

        float4 kLowerSide; 
        if(findLinePlaneIntersection(m_fLowerLimit, akFrustum[i], akFrustum[uiNext], kLowerSide))

        {
            kLowerSide.y = fBasePlane;
            akIntersections[uiCount++] = kLowerSide;
        }

        float fY = akFrustum[1].y;
        if((fY > m_fLowerLimit) && (fY < m_fUpperLimit))
        {
            float4 kCorner = akFrustum[i];
            kCorner.y = fBasePlane;
            akIntersections[uiCount++] = kCorner;
        }
    }
    return uiCount;
}

bool 
Projector::findLinePlaneIntersection(
    float fPlaneY, 
    const float4 &rkPoint1, 
    const float4 &rkPoint2, 
    float4 &rkIntersection)
{
    if(rkPoint2[1] != rkPoint1[1])
    {
        float fK = (fPlaneY - rkPoint1.y) / (rkPoint2.y - rkPoint1.y);

        float fMinY = rkPoint1.y;
        float fMaxY = rkPoint2.y;

        if(fMaxY < fMinY)
        {
            float fTmp = fMinY;
            fMinY = fMaxY;
            fMaxY = fTmp;
        }

        if((fK >= 0.0f) && (fMinY <= fPlaneY) && (fMaxY >= fPlaneY))
        {
            rkIntersection.x = rkPoint1.x + fK * (rkPoint2.x - rkPoint1.x);
            rkIntersection.y = fPlaneY;
            rkIntersection.z = rkPoint1.z + fK * (rkPoint2.z - rkPoint1.z);
            rkIntersection.w = 1.0f;

            return true;
        } 
    }
    return false; 
}

float4 
Projector::findProjectedRange(
    uint uiIntersectionCount,
    float4 akIntersections[32],
    const float16 &rkViewPrj)
{
    GLint aiViewport[4];
    glGetIntegerv(GL_VIEWPORT, aiViewport);

    uint uiProjectedCount = 0;
    float4 akProjected[32];

    for( uint i = 0; i < uiIntersectionCount; i++)
    {
        float4 kDW = rkViewPrj * akIntersections[i];
        kDW /= kDW.w;

        float dWX = kDW.x;
        float dWY = kDW.y;
        float dWZ = kDW.z;

        float4 kP;
        kP.x = (2.0 * (dWX - aiViewport[0]) / aiViewport[2]) - 1.0;
        kP.y = (2.0 * (dWY - aiViewport[1]) / aiViewport[3]) - 1.0;
        kP.z = 2.0 * dWZ - 1.0;
        kP.w = 1.0;

        akProjected[uiProjectedCount++] = kP;
    }     

    float2 kMin = make_float2(+1.0f, +1.0f);
    float2 kMax = make_float2(-1.0f, -1.0f);

    if(uiProjectedCount > 0)
    {       
        for( uint i = 0; i < uiProjectedCount; i++)
        {
            if(akProjected[i].x < kMin.x) kMin.x = akProjected[i].x;
            if(akProjected[i].y < kMin.y) kMin.y = akProjected[i].y;

            if(akProjected[i].x > kMax.x) kMax.x = akProjected[i].x;
            if(akProjected[i].y > kMax.y) kMax.y = akProjected[i].y;
        }        

        kMin.x -= 0.01f;
        kMin.y -= 0.01f;

        kMax.x += 0.01f;
        kMax.y += 0.01f;
    }
    else
    {
        kMin = make_float2(-1.0f, -1.0f);
        kMax = make_float2(+1.0f, +1.0f);
    }

    if(kMin.x < -1.0f) kMin.x = -1.0f;
    if(kMin.y < -1.0f) kMin.y = -1.0f;

    if(kMax.x < +1.0f) kMax.x = +1.0f;
    if(kMax.y < +1.0f) kMax.y = +1.0f;

    if(fabs(kMin.x - kMax.x) < 0.000001)
    {
        kMin.x = -1.0;
        kMax.x = +1.0;
    }

    if(fabs(kMin.y - kMax.y) < 0.000001)
    {
        kMin.y = -1.0;
        kMax.y = +1.0;
    }

    float4 kRange = make_float4(kMin.x, kMin.y, kMax.x, kMax.y);
    return kRange;
}

void
Projector::findFrustumCorners(
    float4 afFrustum[8],
    const float16 &rkInvViewPrj)
{
    GLint aiViewport[4];
    glGetIntegerv(GL_VIEWPORT, aiViewport);

    float fVW = (float) m_pkCamera->getViewportWidth();
    float fVH = (float) m_pkCamera->getViewportHeight();

    float4 akFrustum[4];
    float4 akCorners[] = 
    {
        make_float4(0.0f, 0.0f, 1.0f, 1.0f),
        make_float4(0.0f, fVH,  1.0f, 1.0f),
        make_float4(fVW,  fVH,  1.0f, 1.0f),
        make_float4(fVW,  0.0f, 1.0f, 1.0f)
    };

    for( uint i = 0; i < 4; i++ )
    {    
        float4 kDW = rkInvViewPrj * akCorners[i];
        kDW /= kDW.w;

        akFrustum[i] = kDW; 
    }
}

void
Projector::findProjectedCorners(
    float4 afCorners[4], 
    const float4 &rfRange,
    const float16 &rfInvViewPrj)
{
    float2 fMin = make_float2(rfRange.x, rfRange.y);
    float2 fMax = make_float2(rfRange.z, rfRange.w);

    afCorners[0] = make_float4(fMin.x, fMin.y, 0.0f, 1.0f);
    afCorners[1] = make_float4(fMax.x, fMin.y, 0.0f, 1.0f);
    afCorners[2] = make_float4(fMax.x, fMax.y, 0.0f, 1.0f);
    afCorners[3] = make_float4(fMin.x, fMax.y, 0.0f, 1.0f);

//    printf("Projected Grid: Find Projected Corners...\n");

    for (uint i = 0; i < 4; i++)
    {
        float4 fA = afCorners[i];
        float4 fB = afCorners[i];

        fA.z = -1.0f;
        fB.z = +1.0f;

        fA = rfInvViewPrj * fA;
        fB = rfInvViewPrj * fB;

        fB -= fA;

        float fT = -fA.y / fB.y;
        afCorners[i] = fA + fB * fT;

/*
        printf("[%2d] %8.5f %8.5f %8.5f %8.5f\n", i,
            afCorners[i].x / afCorners[i].w, 
            afCorners[i].y / afCorners[i].w, 
            afCorners[i].z / afCorners[i].w, 
            afCorners[i].w / afCorners[i].w);
*/
    }
}

void
Projector::drawFrustum()
{
    static const float4 akPoints[24] = 
    { 
        make_float4(-1.0f, -1.0f, -1.0f, 1.0f),
        make_float4(+1.0f, -1.0f, -1.0f, 1.0f),
        make_float4(-1.0f, -1.0f, -1.0f, 1.0f),
        make_float4(-1.0f, +1.0f, -1.0f, 1.0f),
        make_float4(+1.0f, -1.0f, -1.0f, 1.0f),
        make_float4(+1.0f, +1.0f, -1.0f, 1.0f),
        make_float4(-1.0f, +1.0f, -1.0f, 1.0f),
        make_float4(+1.0f, +1.0f, -1.0f, 1.0f),

        make_float4(-1.0f, -1.0f, +1.0f, 1.0f),
        make_float4(+1.0f, -1.0f, +1.0f, 1.0f),
        make_float4(-1.0f, -1.0f, +1.0f, 1.0f),
        make_float4(-1.0f, +1.0f, +1.0f, 1.0f),
        make_float4(+1.0f, -1.0f, +1.0f, 1.0f),
        make_float4(+1.0f, +1.0f, +1.0f, 1.0f),
        make_float4(-1.0f, +1.0f, +1.0f, 1.0f),
        make_float4(+1.0f, +1.0f, +1.0f, 1.0f),

        make_float4(-1.0f, -1.0f, -1.0f, 1.0f),
        make_float4(-1.0f, -1.0f, +1.0f, 1.0f),
        make_float4(+1.0f, -1.0f, -1.0f, 1.0f),
        make_float4(+1.0f, -1.0f, +1.0f, 1.0f),
        make_float4(-1.0f, +1.0f, -1.0f, 1.0f),
        make_float4(-1.0f, +1.0f, +1.0f, 1.0f),
        make_float4(+1.0f, +1.0f, -1.0f, 1.0f),
        make_float4(+1.0f, +1.0f, +1.0f, 1.0f)
    };

    float16 kInvViewPrj = inverse((m_kModelViewMatrix * m_kProjectionMatrix));

    glPushAttrib(GL_LIGHTING_BIT);
    glPushAttrib(GL_CURRENT_BIT);
    glDisable(GL_DEPTH_TEST);

    glPushMatrix();
    {
        glPointSize(10.0f);
        glColor3f(1.0f, 1.0f, 0.0f);
        glBegin(GL_POINTS);
        for(uint i = 0; i < 4; i ++)
        {
            float4 kP = m_akCorners[i];
            kP /= kP.w;

            glVertex3f(kP.x, kP.y, kP.z);
        }
        glEnd();

        glBegin(GL_LINES);
        for(uint i = 0; i < 4; i ++)
        {
            uint u = i;
            uint v = (i >= 3) ? 0 : (i + 1);

            float4 kP0 = m_akCorners[u];
            float4 kP1 = m_akCorners[v];

            kP0 /= kP0.w;
            kP1 /= kP1.w;

            glVertex3f(kP0.x, kP0.y, kP0.z);
            glVertex3f(kP1.x, kP1.y, kP1.z);
        }
        glEnd();

        glColor3f(1.0f, 0.0f, 0.0f);
        glBegin(GL_LINES);
        for(uint i = 0; i < 24; i ++)
        {
            float4 kP = kInvViewPrj * akPoints[i];
            kP /= kP.w;

            glVertex3f(kP.x, kP.y, kP.z);
        }
        glEnd();
    }
    glPopMatrix();

    glEnable(GL_DEPTH_TEST);
    glPopAttrib();
    glPopAttrib();
}
```

[Next](common-projector.h.md)[Previous](common-projectedgrid.h.md)

