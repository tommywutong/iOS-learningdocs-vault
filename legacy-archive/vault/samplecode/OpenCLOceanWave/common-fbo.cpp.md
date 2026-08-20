---
title: OpenCL_OceanWave
apple_id: DTS40009447
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2011-04-13'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_OceanWave/Listings/common_fbo_cpp.html
archived_at: '2026-07-18T03:17:46.835628Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL_OceanWave](OpenCLOceanWave.md)


[Next](common-fbo.h.md)[Previous](common-dataloader.m.md)

Current information on this Developer Library topic can be found here:

- [Performance > Multiprocessing](https://developer.apple.com/referencelibrary/Performance/idxMultiprocessing-date.html)

# common/fbo.cpp

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

#include "fbo.h"

#include <OpenGL/gl.h>
#include <OpenGL/glu.h>

FrameBufferObject::FrameBufferObject() :
    m_bIsEnabled(false),
    m_uiWidth(0),
    m_uiHeight(0),
    m_uiFramebufferId(0),
    m_uiRenderbufferId(0)
{
    memset(m_abAttached, false, 64 * sizeof(bool));
}

FrameBufferObject::~FrameBufferObject()
{
    destroy();
}

void
FrameBufferObject::destroy()
{
    disable();

    if(m_uiRenderbufferId)
    {
        glDeleteRenderbuffersEXT(1, &m_uiRenderbufferId);
        m_uiRenderbufferId = 0;
    }   

    if(m_uiFramebufferId)
    {
        glDeleteFramebuffersEXT(1, &m_uiFramebufferId);
        m_uiFramebufferId = 0;
    }   

    memset(m_abAttached, false, 64 * sizeof(bool));
}

bool
FrameBufferObject::setup(
    uint uiWidth, uint uiHeight, bool bUseRenderbuffer)
{
    destroy();

    m_uiWidth = uiWidth;
    m_uiHeight = uiHeight;

    if(bUseRenderbuffer)
    {
        m_uiRenderbufferId = createRenderbuffer(uiWidth, uiHeight);
        if(m_uiRenderbufferId == 0)
            return false;
    }

    m_uiFramebufferId = createFramebuffer();   
    if(m_uiFramebufferId == 0)
        return false;

    return true;
}

void
FrameBufferObject::enable(bool bClear)
{
    if(m_bIsEnabled)
        return;

    if(m_uiFramebufferId == 0)
        return;

    glBindFramebufferEXT(GL_FRAMEBUFFER_EXT, m_uiFramebufferId);
//    checkFramebufferStatus("Binding framebuffer");

    if(m_uiRenderbufferId != 0)
    {
        glFramebufferRenderbufferEXT(GL_FRAMEBUFFER_EXT, 
                                     GL_DEPTH_ATTACHMENT_EXT, 
                                     GL_RENDERBUFFER_EXT, 
                                     m_uiRenderbufferId);

        checkFramebufferStatus("Binding render buffer");
    }

    if(bClear)
    {
        glViewport(0, 0, m_uiWidth, m_uiHeight);

        GLbitfield bfBuffers = 0;
        if(isColorUsed())
            bfBuffers |= GL_COLOR_BUFFER_BIT;

        if(isDepthUsed())
            bfBuffers |= GL_DEPTH_BUFFER_BIT;

        if(isStencilUsed())
            bfBuffers |= GL_STENCIL_BUFFER_BIT;

        if(bfBuffers)
            glClear(bfBuffers);

        checkFramebufferStatus("Clearing framebuffer");
    }

    m_bIsEnabled = true;
}

void
FrameBufferObject::disable()
{
    if(!m_bIsEnabled)
        return;

//    checkFramebufferStatus("Disabling framebuffer");
    glBindFramebufferEXT(GL_FRAMEBUFFER_EXT, 0);    
    m_bIsEnabled = false;
}

void
FrameBufferObject::attach(
    GLenum eAttachment, 
    GLenum eTarget, 
    uint uiTextureId)
{
    printf("FrameBufferObject: Attaching Framebuffer [%d] Texture [%d] %d \n", 
        m_uiFramebufferId, uiTextureId, (int)eTarget);

    enable();

    glFramebufferTexture2DEXT(GL_FRAMEBUFFER_EXT, 
                              eAttachment, eTarget, 
                              uiTextureId, 0);

    uint uiIndex = (uint)eAttachment - (uint)GL_COLOR_ATTACHMENT0_EXT;
    m_abAttached[uiIndex] = true;

    if(isDepthUsed() && !isColorUsed())
    {
        glReadBuffer(GL_NONE);
        glDrawBuffer(GL_NONE);

        printf("FrameBufferObject: Disabling read and draw buffers\n");
    }

    checkFramebufferStatus("Attaching texture");

    disable();
}

void
FrameBufferObject::detach(
    GLenum eAttachment,
    GLenum eTarget)
{
    printf("FrameBufferObject: Detaching Framebuffer [%d] Texture [x] %d\n", 
        m_uiFramebufferId, (int)eTarget);

    glFramebufferTexture2DEXT(GL_FRAMEBUFFER_EXT, 
                              eAttachment, 
                              eTarget, 
                              0, 0);

    uint uiIndex = (uint)eAttachment - (uint)GL_COLOR_ATTACHMENT0_EXT;
    m_abAttached[uiIndex] = false;
}

bool
FrameBufferObject::isAttached(
    GLenum eAttachment)
{
    uint uiIndex = (uint)eAttachment - (uint)GL_COLOR_ATTACHMENT0_EXT;
    if(uiIndex >= GL_COLOR_ATTACHMENT0_EXT && uiIndex < 64)
        return m_abAttached[uiIndex];

    return false;
}

bool
FrameBufferObject::isColorUsed()
{
    for(uint i = (uint)GL_COLOR_ATTACHMENT0_EXT; i <= (uint)GL_COLOR_ATTACHMENT15_EXT; i++)
    {
        uint uiIndex = i - (uint)GL_COLOR_ATTACHMENT0_EXT;
        if(m_abAttached[uiIndex])
            return true;
    }

    return false;
}

bool
FrameBufferObject::isDepthUsed()
{
    if(m_uiRenderbufferId)
        return true;

    uint uiIndex = (uint)GL_DEPTH_ATTACHMENT_EXT - (uint)GL_COLOR_ATTACHMENT0_EXT;
    if(m_abAttached[uiIndex])
        return true;

    return false;
}

bool
FrameBufferObject::isStencilUsed()
{
    uint uiIndex = (uint)GL_STENCIL_ATTACHMENT_EXT - (uint)GL_COLOR_ATTACHMENT0_EXT;
    if(m_abAttached[uiIndex])
        return true;

    return false;
}

uint 
FrameBufferObject::createFramebuffer()
{
    uint uiFboId = 0;
    glGenFramebuffersEXT(1, &uiFboId);

    printf("FrameBufferObject: Created Framebuffer %d\n", uiFboId);

    return uiFboId;
}

uint 
FrameBufferObject::createRenderbuffer(
    uint uiWidth, uint uiHeight)
{
    uint uiRboId = 0;

    GLint iDepthBits = 0;
    GLenum eDepthType = GL_DEPTH_COMPONENT24_ARB;

    glGetIntegerv(GL_DEPTH_BITS, &iDepthBits);
    if (iDepthBits == 16)
        eDepthType = GL_DEPTH_COMPONENT16_ARB;
    else if(iDepthBits == 24)
        eDepthType = GL_DEPTH_COMPONENT24_ARB;
    else if(iDepthBits == 32)
        eDepthType = GL_DEPTH_COMPONENT32_ARB;

    glGenRenderbuffersEXT(1, &uiRboId);
    glBindRenderbufferEXT(GL_RENDERBUFFER_EXT, uiRboId);
    glRenderbufferStorageEXT(GL_RENDERBUFFER_EXT, eDepthType, uiWidth, uiHeight);

    printf("FrameBufferObject: Created Renderbuffer %d\n", uiRboId);

    return uiRboId;
}

void
FrameBufferObject::checkFramebufferStatus(const char *acMessage)
{
    GLenum eStatus = glCheckFramebufferStatusEXT(GL_FRAMEBUFFER_EXT);
    if(eStatus == GL_FRAMEBUFFER_COMPLETE_EXT)
        return;

    if(acMessage)
        printf("FrameBufferObject: FBO Error: %s\n", acMessage);

    switch(eStatus) 
    {                                          
    case GL_FRAMEBUFFER_COMPLETE_EXT: 
        break;                                                
    case GL_FRAMEBUFFER_UNSUPPORTED_EXT:                   
        printf("FrameBufferObject: FBO Error: Format Unsupported!\n");
        break;       
    case GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT_EXT:
        printf("FrameBufferObject: FBO Error: Incomplete Attachment!\n");
        break;                                      
    case GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT_EXT:
        printf("FrameBufferObject: FBO Error: Incomplete Missing Attachment!\n");
        break;                              
    case GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS_EXT:
        printf("FrameBufferObject: FBO Error: Incomplete Dimensions!\n");
        break;                              
    case GL_FRAMEBUFFER_INCOMPLETE_FORMATS_EXT:
        printf("FrameBufferObject: FBO Error: Incomplete Formats!\n");
        break;                              
    case GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER_EXT:
        printf("FrameBufferObject: FBO Error: Incomplete Draw Buffer!\n");
        break;                                  
    case GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER_EXT:
        printf("FrameBufferObject: FBO Error: Incomplete Read Buffer!\n");
        break;                                  
    default:
        printf("FrameBufferObject: Unknown FBO Status Error '%d'\n", (int)eStatus);
        break;
    }

    GLenum eError = glGetError();
    switch(eError)
    {
    case(0):
        break;
    case(GL_INVALID_FRAMEBUFFER_OPERATION_EXT):
        printf("FrameBufferObject: OpenGL Error: Invalid Framebuffer Operation!\n");
        break;
    case(GL_INVALID_ENUM):
        printf("FrameBufferObject: OpenGL Error: Invalid Enumerate!\n");
        break;
    case(GL_INVALID_VALUE):
        printf("FrameBufferObject: OpenGL Error: Invalid Value!\n");
        break;
    case(GL_INVALID_OPERATION):
        printf("FrameBufferObject: OpenGL Error: Invalid Operation!\n");
        break;
    case(GL_STACK_OVERFLOW):
        printf("FrameBufferObject: OpenGL Error: Stack Overflow!\n");
        break;
    case(GL_STACK_UNDERFLOW):
        printf("FrameBufferObject: OpenGL Error: Stack Underflow!\n");
        break;
    case(GL_OUT_OF_MEMORY):
        printf("FrameBufferObject: OpenGL Error: Out of Memory!\n");
        break;
    default:
        printf("FrameBufferObject: Unknown OpenGL Error '%d'\n", (int)eError);
        break;
    }

}
```

[Next](common-fbo.h.md)[Previous](common-dataloader.m.md)

