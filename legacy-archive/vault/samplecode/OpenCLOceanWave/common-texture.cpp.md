---
title: OpenCL_OceanWave
apple_id: DTS40009447
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2011-04-13'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_OceanWave/Listings/common_texture_cpp.html
archived_at: '2026-07-18T03:17:48.674099Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL_OceanWave](OpenCLOceanWave.md)


[Next](common-texture.h.md)[Previous](common-shader.h.md)

Current information on this Developer Library topic can be found here:

- [Performance > Multiprocessing](https://developer.apple.com/referencelibrary/Performance/idxMultiprocessing-date.html)

# common/texture.cpp

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

#include "texture.h"
#include "data_loader.h"

#include <OpenGL/gl.h>
#include <OpenGL/glu.h>

Texture::Texture() :
    m_bIsEnabled(false),
    m_uiWidth(0),
    m_uiHeight(0),
    m_uiDepth(0),
    m_uiTextureId(0),
    m_eTarget(0),
    m_eTextureUnit(GL_TEXTURE0),
    m_eInternal(0),
    m_eFormat(0),
    m_eDataType(0),
    m_eFilterMode(0),
    m_eWrapMode(0),
    m_eCompareMode(0),
    m_eCompareFunc(0),
    m_eEnvMode(0),
    m_eDepthMode(0)
{
    // EMPTY!
}

Texture::~Texture()
{
    destroy();
}

void
Texture::destroy()
{
    if(m_uiTextureId)
    {
        disable();
        glDeleteTextures( 1, &m_uiTextureId);
    }
    m_uiTextureId = 0;
}

bool
Texture::load(
    const char* acFilename,
    GLenum eTarget,
    GLenum eInternal, 
    GLenum eFormat, 
    GLenum eDataType,
    GLenum eFilterMode,
    GLenum eWrapMode,
    bool bUseMipMaps)
{
    int iWidth, iHeight;

    unsigned char *acRgb = LoadImageFromFile(acFilename, &iWidth, &iHeight);
    if ( acRgb == NULL )
    {
        if(!acRgb)
        {
            printf("Error: Failed to load texture map : %s\n", acFilename);
            return false;
        }
    }

    bool bSuccess = setup(iWidth, iHeight,
                          eTarget, 
                          eInternal, 
                          eFormat, 
                          eDataType,
                          bUseMipMaps, 
                          acRgb);

    free(acRgb);
    return bSuccess;
}

bool
Texture::loadCubeMap(
    const char* acFilenames[6],
    GLenum eTarget, 
    GLenum eInternal, 
    GLenum eFormat, 
    GLenum eDataType, 
    GLenum eFilterMode, 
    GLenum eWrapMode)
{
    int iWidth, iHeight;
    unsigned char *acFace = LoadImageFromFile(acFilenames[0], &iWidth, &iHeight);

    bool bSuccess = setup(iWidth, iHeight,
                          eTarget, 
                          eInternal, 
                          eFormat, 
                          eDataType,
                          false,
                          NULL);
    if(!bSuccess)
        return false;

    const GLenum aeCubeFaces[] = 
    {
        GL_TEXTURE_CUBE_MAP_POSITIVE_X,
        GL_TEXTURE_CUBE_MAP_NEGATIVE_X,
        GL_TEXTURE_CUBE_MAP_POSITIVE_Y,
        GL_TEXTURE_CUBE_MAP_NEGATIVE_Y,
        GL_TEXTURE_CUBE_MAP_POSITIVE_Z,
        GL_TEXTURE_CUBE_MAP_NEGATIVE_Z
    };

    for(uint i = 0; i < 6; i++)
    {
        if(i > 0)
            acFace = LoadImageFromFile(acFilenames[i], &iWidth, &iHeight);

        if ( acFace == NULL )
        {
            printf("Error: Failed to load texture map : %s\n", acFilenames[i]);
            return false;
        }

        glTexImage2D(aeCubeFaces[i], 0, eInternal, iWidth, iHeight, 0, eFormat, eDataType, acFace); 
        checkStatus("Allocating cubemap face texture");

        free(acFace);
    }

    return bSuccess;
}

bool
Texture::setup(
    uint uiWidth, 
    uint uiHeight, 
    GLenum eTarget,
    GLenum eInternal, 
    GLenum eFormat, 
    GLenum eDataType,
    bool bUseMipMaps,
    void* pvData)
{
    destroy();

    uint uiTextureId = createTexture(uiWidth, 
                                     uiHeight, 
                                     0,
                                     eTarget, 
                                     eInternal, 
                                     eFormat,  
                                     eDataType,
                                     pvData); 

    if(uiTextureId == 0)
    {
        printf("Texture: Error Creating Texture!");
        return false;    
    }

    if(bUseMipMaps && pvData)
    {
        gluBuild2DMipmaps(eTarget, eInternal, uiWidth, uiHeight, eFormat, eDataType, pvData  );
        glTexParameteri(eTarget, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST);
        glTexParameteri(eTarget, GL_TEXTURE_MAG_FILTER, GL_LINEAR_MIPMAP_LINEAR);
    }

    m_uiWidth = uiWidth;
    m_uiHeight = uiHeight;
    m_uiTextureId = uiTextureId;
    m_eTarget = eTarget;
    m_eInternal = eInternal;
    m_eFormat = eFormat;
    m_eDataType = eDataType;
    return true;
}

bool
Texture::setup(
    uint uiWidth, 
    uint uiHeight, 
    uint uiDepth,
    GLenum eTarget,
    GLenum eInternal, 
    GLenum eFormat, 
    GLenum eDataType,
    bool bUseMipMaps,
    void* pvData)
{
    destroy();

    uint uiTextureId = createTexture(uiWidth, 
                                     uiHeight, 
                                     uiDepth,
                                     eTarget, 
                                     eInternal, 
                                     eFormat,  
                                     eDataType,
                                     pvData); 

    if(uiTextureId == 0)
    {
        printf("Texture: Error Creating Texture!");
        return false;    
    }

    if(bUseMipMaps && pvData)
    {
        gluBuild3DMipmaps(eTarget, eInternal, uiWidth, uiHeight, uiDepth, eFormat, eDataType, pvData  );
        glTexParameteri(eTarget, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST);
        glTexParameteri(eTarget, GL_TEXTURE_MAG_FILTER, GL_LINEAR_MIPMAP_LINEAR);
    }

    m_uiWidth = uiWidth;
    m_uiHeight = uiHeight;
    m_uiDepth = uiDepth;
    m_uiTextureId = uiTextureId;
    m_eTarget = eTarget;
    m_eInternal = eInternal;
    m_eFormat = eFormat;
    m_eDataType = eDataType;
    return true;
}


void
Texture::render()
{
    int aiViewport[4];
    glGetIntegerv(GL_VIEWPORT, aiViewport);
    glViewport( 0, 0, m_uiWidth, m_uiHeight );

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glDisable(GL_BLEND);
    glDisable(GL_LIGHTING);

    glMatrixMode( GL_PROJECTION );
    glPushMatrix();
    glLoadIdentity();
    gluOrtho2D( -1.0, 1.0, -1.0, 1.0 );

    glMatrixMode( GL_MODELVIEW );
    glPushMatrix();
    glLoadIdentity();

    glMatrixMode( GL_TEXTURE );
    glPushMatrix();
    glLoadIdentity();

    if(m_uiTextureId)
    {
        enable(m_eTextureUnit);
        glTexParameteri(m_eTarget, GL_TEXTURE_COMPARE_MODE_ARB, GL_NONE);

        glColor3f( 1.0f, 1.0f, 1.0f );
        glBegin( GL_QUADS );
        {
            glTexCoord2f( 0.0f, 0.0f );
            glVertex3f( -1.0f, -1.0f, 0.0f );

            glTexCoord2f( 0.0f, 1.0f );
            glVertex3f( -1.0f, +1.0f, 0.0f );

            glTexCoord2f( 1.0f, 1.0f );
            glVertex3f( +1.0f, +1.0f, 0.0f );

            glTexCoord2f( 1.0f, 0.0f );
            glVertex3f( +1.0f, -1.0f, 0.0f );
        }
        glEnd();

        disable();
    }

    glMatrixMode( GL_TEXTURE );
    glPopMatrix();

    glMatrixMode( GL_MODELVIEW );
    glPopMatrix();

    glMatrixMode( GL_PROJECTION );
    glPopMatrix();    

    glViewport(aiViewport[0], aiViewport[1], aiViewport[2], aiViewport[3]);
    glMatrixMode( GL_MODELVIEW );
}

void
Texture::enable(GLenum eTextureUnit)
{
    if(m_uiTextureId == 0)
        return;

    m_eTextureUnit = eTextureUnit;
    checkStatus("Preparing texture unit");

    glActiveTextureARB(m_eTextureUnit);
    checkStatus("Activating texture unit");

    glBindTexture(m_eTarget, m_uiTextureId);
    checkStatus("Binding texture");

    glEnable(m_eTarget);    
    checkStatus("Enabling texture target");
    m_bIsEnabled = true;
}

void
Texture::update()
{
    if(!m_bIsEnabled)
    {
        glActiveTextureARB(m_eTextureUnit);
        checkStatus("Activating texture unit");

        glBindTexture(m_eTarget, m_uiTextureId);
        checkStatus("Binding texture");
    }

    if(m_eFilterMode)
    {
        glTexParameteri(m_eTarget, GL_TEXTURE_MIN_FILTER, m_eFilterMode);
        glTexParameteri(m_eTarget, GL_TEXTURE_MAG_FILTER, m_eFilterMode);
    }

    if(m_eWrapMode)
    {
        if(m_eTarget == GL_TEXTURE_3D)
            glTexParameteri(m_eTarget, GL_TEXTURE_WRAP_R, m_eWrapMode);

        glTexParameteri(m_eTarget, GL_TEXTURE_WRAP_S, m_eWrapMode);
        glTexParameteri(m_eTarget, GL_TEXTURE_WRAP_T, m_eWrapMode);
    }

    if(m_eCompareMode)
        glTexParameteri(m_eTarget, GL_TEXTURE_COMPARE_MODE_ARB, m_eCompareMode);

    if(m_eCompareFunc)
        glTexParameteri(m_eTarget, GL_TEXTURE_COMPARE_FUNC_ARB, m_eCompareFunc);

    if(m_eEnvMode)
        glTexParameteri(m_eTarget, GL_TEXTURE_ENV_MODE, m_eEnvMode);

    if(m_eDepthMode)
        glTexParameteri(m_eTarget, GL_DEPTH_TEXTURE_MODE_ARB, m_eDepthMode);

    checkStatus("Setting texture parameters");

    if(!m_bIsEnabled)
    {
        glBindTexture(m_eTarget, 0);
        checkStatus("Unbinding texture");

        glDisable(m_eTarget);    
        checkStatus("Disabling texture target");
    }
}

void
Texture::disable()
{
//    if(!m_bIsEnabled)
//        return;

    checkStatus("Preparing texture unit for disabling");

    glActiveTextureARB(m_eTextureUnit);
    checkStatus("Activating texture unit for disabling");

    glBindTexture(m_eTarget, 0);
    checkStatus("Unbinding texture");

    glDisable(m_eTarget);    
    checkStatus("Disabling texture target");

    glActiveTextureARB(GL_TEXTURE0);
    checkStatus("Disabling texture unit");
    m_bIsEnabled = false;
}

uint
Texture::createTexture(
    uint uiWidth, 
    uint uiHeight,
    uint uiDepth,
    GLenum eTarget,
    GLenum eInternal,
    GLenum eFormat,
    GLenum eDataType,
    void* pvData)
{
    uint uiTexId = 0;
    glGenTextures(1, &uiTexId);
    if(uiTexId == 0)
        return 0;

    glActiveTextureARB(m_eTextureUnit);
    checkStatus("Activating texture unit");

    glBindTexture(eTarget, uiTexId);
    checkStatus("Binding texture");

    if(eInternal == GL_DEPTH_COMPONENT)
    {   
        int iDepth = 8;
        glGetIntegerv(GL_DEPTH_BITS, &iDepth);      
        if(iDepth == 16)
            eInternal = GL_DEPTH_COMPONENT16;
        else if(iDepth == 24)
            eInternal = GL_DEPTH_COMPONENT24;
        else if(iDepth == 32)
            eInternal = GL_DEPTH_COMPONENT32;
    }

    if(eTarget == GL_TEXTURE_3D)
        glTexImage3D(eTarget, 0, eInternal, uiWidth, uiHeight, uiDepth, 0, eFormat, eDataType, pvData);         

    else if(eTarget == GL_TEXTURE_2D)
        glTexImage2D(eTarget, 0, eInternal, uiWidth, uiHeight, 0, eFormat, eDataType, pvData);          

    else if(eTarget == GL_TEXTURE_RECTANGLE_ARB)
        glTexImage2D(eTarget, 0, eInternal, uiWidth, uiHeight, 0, eFormat, eDataType, pvData);          

    checkStatus("Allocating texture");

    glBindTexture(eTarget, 0);
    checkStatus("Unbinding texture");

    glActiveTextureARB(GL_TEXTURE0);
    checkStatus("Disabling texture unit");

    return uiTexId;
}

void
Texture::capture()
{
    enable();

    if(m_eTarget == GL_TEXTURE_3D)
    {
        // glCopyTexSubImage3D(m_eTarget,0,0,0,0,0,m_uiWidth,m_uiHeight);
    }
    else
    {
        glCopyTexSubImage2D(m_eTarget,0,0,0,0,0,m_uiWidth,m_uiHeight);
    }

    disable();
}

void
Texture::checkStatus(const char *acMessage)
{
    GLenum eError = glGetError();
    if(eError == GL_FALSE)
        return;

    if(acMessage)
        printf("Texture[%d]: OpenGL Error: %s\n", m_uiTextureId, acMessage);

    switch(eError)
    {
    case(GL_INVALID_ENUM):
        printf("Texture[%d]: OpenGL Error: Invalid Enumerate!\n", m_uiTextureId);
        break;
    case(GL_INVALID_VALUE):
        printf("Texture[%d]: OpenGL Error: Invalid Value!\n", m_uiTextureId);
        break;
    case(GL_INVALID_OPERATION):
        printf("Texture[%d]: OpenGL Error: Invalid Operation!\n", m_uiTextureId);
        break;
    case(GL_STACK_OVERFLOW):
        printf("Texture[%d]: OpenGL Error: Stack Overflow!\n", m_uiTextureId);
        break;
    case(GL_STACK_UNDERFLOW):
        printf("Texture[%d]: OpenGL Error: Stack Underflow!\n", m_uiTextureId);
        break;
    case(GL_OUT_OF_MEMORY):
        printf("Texture[%d]: OpenGL Error: Out of Memory!\n", m_uiTextureId);
        break;
    case(GL_INVALID_FRAMEBUFFER_OPERATION_EXT):
        printf("Texture[%d]: OpenGL Error: Invalid framebuffer operation!\n", m_uiTextureId);
        break;
    default:
        printf("Texture[%d]: Unknown OpenGL Error '%d'\n", m_uiTextureId, (int)eError);
        break;
    }

}
```

[Next](common-texture.h.md)[Previous](common-shader.h.md)

