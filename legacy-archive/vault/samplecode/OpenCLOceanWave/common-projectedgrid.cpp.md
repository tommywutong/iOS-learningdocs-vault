---
title: OpenCL_OceanWave
apple_id: DTS40009447
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2011-04-13'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_OceanWave/Listings/common_projected_grid_cpp.html
archived_at: '2026-07-18T03:17:47.880582Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL_OceanWave](OpenCLOceanWave.md)


[Next](common-projectedgrid.h.md)[Previous](common-plane.h.md)

Current information on this Developer Library topic can be found here:

- [Performance > Multiprocessing](https://developer.apple.com/referencelibrary/Performance/idxMultiprocessing-date.html)

# common/projected_grid.cpp

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

#include "projected_grid.h"
#include "plane.h"

#include <OpenGL/OpenGL.h>
#include <OpenGL/glu.h>
#include <stdio.h>

#define odd(x) (x%2)

ProjectedGrid::ProjectedGrid() :
    m_bDebug(false),
    m_bIsVisible(false),
    m_afVertexData(0),
    m_afNormalData(0),
    m_afTexCoordData(0),
    m_uiVertexCount(0),
    m_pkProjector(0)
{
    // EMPTY!
}

ProjectedGrid::~ProjectedGrid()
{
    destroyVBO();
    destroyGridMesh();
}

void
ProjectedGrid::destroyGridMesh()
{
    if(m_auiIndexData)
        delete [] m_auiIndexData;
    m_auiIndexData = 0;

    if(m_afVertexData)
        delete [] m_afVertexData;
    m_afVertexData = 0;

    if(m_afNormalData)
        delete [] m_afNormalData;
    m_afNormalData = 0;

    if(m_afTexCoordData)
        delete [] m_afTexCoordData;
    m_afTexCoordData = 0;

    m_uiVertexCount = 0;
    m_uiFaceCount = 0;
}

void
ProjectedGrid::setup(
    uint uiCountX, uint uiCountY)
{
    createGridMesh(uiCountX, uiCountY);
}

void 
ProjectedGrid::update()
{
    if(!m_pkProjector)
        return;

    if(!m_pkProjector->isVisible())
    {
        m_bIsVisible = false;
    }
    else
    {
        m_bIsVisible = true;
        updateGridMesh(m_pkProjector->getProjectedCorners());
        updateVBO();
    }
}

void 
ProjectedGrid::updateGridMesh(
    const float4 afCorners[4])
{
    if(!m_pkProjector)
        return;

    float fSX = 1.0f / (float) (m_uiSizeX - 1);
    float fSY = 1.0f / (float) (m_uiSizeY - 1);

    uint uiIndex = 0;
    for( uint j = 0; j < m_uiSizeY; j++ ) 
    {
        for( uint i = 0; i < m_uiSizeX; i++ )
        {
            float fX = fSX * (float)i;
            float fY = fSY * (float)j;

            float4 fPoint = afCorners[0] * (1.0f - fX) * (1.0f - fY) + 
                            afCorners[1] * fX * (1.0f - fY) + 
                            afCorners[3] * (1.0f - fX) * fY + 
                            afCorners[2] * fX * fY;

            fPoint /= fPoint.w;

            m_afVertexData[uiIndex++] = fPoint.x;
            m_afVertexData[uiIndex++] = fPoint.y;
            m_afVertexData[uiIndex++] = fPoint.z;
            m_afVertexData[uiIndex++] = 1.0f;

        }
    }

    for( uint i = 0; i < m_uiVertexCount; i++ ) 
    {
        m_afTexCoordData[i*2 + 0] = m_afVertexData[i*4 + 0] * 1.0f;
        m_afTexCoordData[i*2 + 1] = m_afVertexData[i*4 + 2] * 1.0f;
    }

    float3 fOpposite, fAdjacent, fRoot, fNormal;
    uint uiAdj = 0, uiOpp = 0, uiNormalIndex = 0;
    for( uint row = 0; row < m_uiSizeY; row++ ) 
    {
        for( uint col = 0; col < m_uiSizeX; col++ ) 
        {
            if( row == m_uiSizeY - 1 ) 
            {
                if( col == m_uiSizeX - 1 ) 
                { 
                    uiAdj = uiNormalIndex - m_uiSizeX;
                    uiOpp = uiNormalIndex - 1;
                }
                else 
                {
                    uiAdj = uiNormalIndex + 1;
                    uiOpp = uiNormalIndex - m_uiSizeX;
                }
            }
            else 
            {
                if( col == m_uiSizeX - 1 ) 
                { 
                    uiAdj = uiNormalIndex - 1;
                    uiOpp = uiNormalIndex + m_uiSizeX;
                }
                else 
                {
                    uiAdj = uiNormalIndex + m_uiSizeX;
                    uiOpp = uiNormalIndex + 1;
                }
            }

            fRoot = make_float3(m_afVertexData[uiNormalIndex * 4 + 0],
                                m_afVertexData[uiNormalIndex * 4 + 1],
                                m_afVertexData[uiNormalIndex * 4 + 2]);

            fAdjacent = make_float3(m_afVertexData[uiAdj * 4 + 0],
                                    m_afVertexData[uiAdj * 4 + 1],
                                    m_afVertexData[uiAdj * 4 + 2]);

            fOpposite = make_float3(m_afVertexData[uiOpp * 4 + 0],
                                    m_afVertexData[uiOpp * 4 + 1],
                                    m_afVertexData[uiOpp * 4 + 2]);

            fNormal = normalize(cross((fAdjacent - fRoot), (fOpposite - fRoot)));


            m_afNormalData[uiNormalIndex * 4 + 0] = fNormal.x;
            m_afNormalData[uiNormalIndex * 4 + 1] = fNormal.y;
            m_afNormalData[uiNormalIndex * 4 + 2] = fNormal.z;
            m_afNormalData[uiNormalIndex * 4 + 3] = 1.0f;

            uiNormalIndex++;
        }
    }
}

void
ProjectedGrid::createGridMesh(
    uint uiCountX, uint uiCountY)
{
    destroyGridMesh();

    m_uiSizeX = uiCountX;
    m_uiSizeY = uiCountY;

    m_uiVertexCount = m_uiSizeX * m_uiSizeY;
    m_afVertexData = new float[4 * m_uiVertexCount];
    m_afNormalData = new float[4 * m_uiVertexCount];
    m_afTexCoordData = new float[2 * m_uiVertexCount];
    m_auiIndexData = new uint[ 2 * (uiCountY - 1) * uiCountX];

    int i = 0;
    for(uint y = 0; y < uiCountY - 1; y++)
    {
        if(odd(y))
        {
            for(int x = uiCountX - 1; x >= 0; x--)
            {
                m_auiIndexData[i++] = (uiCountX*(y+1)+x);
                m_auiIndexData[i++] = (uiCountX*y+x);
            }
        }
        else
        {
            for(uint x = 0; x < uiCountX; x++)
            {
                m_auiIndexData[i++] = (uiCountX*y+x);
                m_auiIndexData[i++] = (uiCountX*(y+1)+x);
            }
        }
    }
    m_uiFaceCount = i-2;

//    updateGridMesh();

}

void 
ProjectedGrid::createVBO()
{
    destroyVBO();

    glGenBuffersARB(1, &m_uiVertexBufferId);
    glBindBufferARB(GL_ARRAY_BUFFER_ARB, m_uiVertexBufferId);
    glBufferDataARB(GL_ARRAY_BUFFER_ARB, m_uiVertexCount*4*sizeof(GLfloat),
                    m_afVertexData, GL_STATIC_DRAW_ARB);
    glBindBufferARB(GL_ARRAY_BUFFER_ARB, 0);

    glGenBuffers(1, &m_uiNormalBufferId);
    glBindBuffer(GL_ARRAY_BUFFER_ARB, m_uiNormalBufferId);
    glBufferData(GL_ARRAY_BUFFER_ARB, m_uiVertexCount*4*sizeof(float), 
                 m_afNormalData, GL_STATIC_DRAW_ARB);
    glNormalPointer(GL_FLOAT, 4 * sizeof(float), 0);
    glBindBuffer( GL_ARRAY_BUFFER_ARB, 0);

    glGenBuffers(1, &m_uiTexCoordBufferId);
    glBindBuffer(GL_ARRAY_BUFFER_ARB, m_uiTexCoordBufferId);
    glBufferData(GL_ARRAY_BUFFER_ARB, m_uiVertexCount*2*sizeof(float),
                 m_afTexCoordData, GL_STATIC_DRAW_ARB);
    glTexCoordPointer(2, GL_FLOAT, 0, 0);
    glBindBuffer( GL_ARRAY_BUFFER_ARB, 0);

    glGenBuffers(1, &m_uiIndexBufferId);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER_ARB, m_uiIndexBufferId);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER_ARB, (m_uiFaceCount+2)*sizeof(uint), 
                    m_auiIndexData, GL_STATIC_DRAW_ARB);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER_ARB, 0);
    glBindBuffer( GL_ARRAY_BUFFER_ARB, 0);
}

void
ProjectedGrid::updateVBO()
{
    if(!m_uiVertexBufferId)
        createVBO();

    glBindBufferARB(GL_ARRAY_BUFFER_ARB, m_uiVertexBufferId);
    glBufferSubData(GL_ARRAY_BUFFER_ARB, 0, m_uiVertexCount*4*sizeof(float), m_afVertexData);
    glBindBufferARB(GL_ARRAY_BUFFER_ARB, 0);

    glBindBuffer(GL_ARRAY_BUFFER_ARB, m_uiNormalBufferId);
    glBufferSubData(GL_ARRAY_BUFFER_ARB, 0, m_uiVertexCount*4*sizeof(float), m_afNormalData);
    glBindBuffer( GL_ARRAY_BUFFER_ARB, 0);

    glBindBuffer(GL_ARRAY_BUFFER_ARB, m_uiTexCoordBufferId);
    glBufferSubData(GL_ARRAY_BUFFER_ARB, 0, m_uiVertexCount*2*sizeof(float), m_afTexCoordData);
    glBindBuffer( GL_ARRAY_BUFFER_ARB, 0);

}

void 
ProjectedGrid::destroyVBO()
{
    if(m_uiVertexBufferId)
        glDeleteBuffersARB(1, &m_uiVertexBufferId);

    if(m_uiTexCoordBufferId)
        glDeleteBuffersARB(1, &m_uiTexCoordBufferId);

    if(m_uiNormalBufferId)
        glDeleteBuffersARB(1, &m_uiNormalBufferId);

    if(m_uiIndexBufferId)
        glDeleteBuffersARB(1, &m_uiIndexBufferId);
}

void 
ProjectedGrid::render(GLenum eElementType, bool bUseVBO)
{
    if(!m_bIsVisible)
        return;

    if(bUseVBO)
    {
        if(!m_uiVertexBufferId)
            createVBO();

        glPushMatrix();
        glBindBufferARB(GL_ARRAY_BUFFER_ARB, m_uiVertexBufferId);
        glVertexPointer(4, GL_FLOAT, 0, 0);
        glEnableClientState(GL_VERTEX_ARRAY);

        glBindBuffer(GL_ARRAY_BUFFER_ARB, m_uiNormalBufferId);
        glNormalPointer(GL_FLOAT, 4 * sizeof(float), 0);
        glEnableClientState(GL_NORMAL_ARRAY);

        glBindBuffer(GL_ARRAY_BUFFER_ARB, m_uiTexCoordBufferId);
        glTexCoordPointer(2, GL_FLOAT, 0, 0);
        glEnableClientState(GL_TEXTURE_COORD_ARRAY);

        glBindBufferARB(GL_ELEMENT_ARRAY_BUFFER_ARB, m_uiIndexBufferId);
        glDrawElements(eElementType, m_uiFaceCount+2, GL_UNSIGNED_INT, 0);

        glDisableClientState(GL_TEXTURE_COORD_ARRAY);
        glDisableClientState(GL_NORMAL_ARRAY);
        glDisableClientState(GL_VERTEX_ARRAY);

        glBindBufferARB(GL_ARRAY_BUFFER_ARB, 0);
        glBindBufferARB(GL_ELEMENT_ARRAY_BUFFER_ARB, 0);
        glPopMatrix();
    }
    else
    {
        glPushMatrix();
        glEnableClientState(GL_VERTEX_ARRAY);
        glEnableClientState(GL_NORMAL_ARRAY);
        glEnableClientState(GL_TEXTURE_COORD_ARRAY);

        glVertexPointer(4, GL_FLOAT, 0, m_afVertexData);
        glTexCoordPointer(2, GL_FLOAT, 0, m_afTexCoordData);
        glNormalPointer(GL_FLOAT, 4 * sizeof(float), m_afNormalData);
        glDrawElements(eElementType, m_uiFaceCount+2, GL_UNSIGNED_INT, m_auiIndexData);

        glDisableClientState(GL_TEXTURE_COORD_ARRAY);
        glDisableClientState(GL_NORMAL_ARRAY);
        glDisableClientState(GL_VERTEX_ARRAY);
        glPopMatrix();
    }
}
```

[Next](common-projectedgrid.h.md)[Previous](common-plane.h.md)

