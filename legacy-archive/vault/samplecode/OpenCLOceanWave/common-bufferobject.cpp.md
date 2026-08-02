---
title: OpenCL_OceanWave
apple_id: DTS40009447
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2011-04-13'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_OceanWave/Listings/common_buffer_object_cpp.html
archived_at: '2026-07-18T03:17:44.242798Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL_OceanWave](OpenCLOceanWave.md)


[Next](common-bufferobject.h.md)[Previous](common-aabb.h.md)

Current information on this Developer Library topic can be found here:

- [Performance > Multiprocessing](https://developer.apple.com/referencelibrary/Performance/idxMultiprocessing-date.html)

# common/buffer_object.cpp

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

#include "buffer_object.h"
#include <assert.h>

BufferObject::BufferObject() :
    m_uiCount(0),
    m_uiComponents(0),
    m_uiBytes(0),
    m_eDataType(0),
    m_eUsage(0),
    m_eTarget(0),
    m_uiBufferId(0)
{
    m_kClientArrayMap.clear();
}

BufferObject::~BufferObject()
{
    destroy();
}

bool
BufferObject::allocate(
    GLenum eTarget, 
    GLuint uiCount, 
    GLuint uiComponents, 
    GLenum eDataType,
    GLvoid *pvData,
    GLenum eUsage)
{
    destroy();

    GLuint uiId = 0;
    glGenBuffers(1, &uiId);
    if(!uiId)
        return false;

    m_uiBufferId = uiId;
    m_eTarget = eTarget;
    m_eUsage = eUsage;
    m_uiCount = uiCount;
    m_uiComponents = uiComponents;
    m_eDataType = eDataType;
    m_uiBytes = getSizeOfDataType(eDataType) * uiComponents * uiCount;

    glBindBuffer(m_eTarget, m_uiBufferId);
    glBufferData(m_eTarget, m_uiBytes, pvData, eUsage);
    glBindBuffer(m_eTarget, 0);
    return true;
}

void
BufferObject::destroy()
{
    disable();

    if(m_uiBufferId)
        glDeleteBuffers(1, &m_uiBufferId);
    m_uiBufferId = 0;

    m_uiCount = 0;
    m_uiComponents = 0;
    m_uiBytes = 0;
    m_eDataType = 0;
    m_eUsage = 0;
    m_eTarget = 0;

    m_kClientArrayMap.clear();
}

void* BufferObject::map(
    GLenum eAccess) const
{
    if(!m_uiBufferId)
        return NULL;

    glBindBuffer(m_eTarget, m_uiBufferId);
    void* pvData = glMapBuffer(m_eTarget, eAccess);
    return pvData;
}

void BufferObject::unmap() const
{
    glUnmapBuffer(m_eTarget);
    glBindBuffer(m_eTarget, 0);
}

bool
BufferObject::enable() const
{
    if(!m_uiBufferId)
        return false;

    glBindBuffer(m_eTarget, m_uiBufferId);

    ClientArrayMapConstIter pkIter;
    for(pkIter = m_kClientArrayMap.begin(); pkIter != m_kClientArrayMap.end(); pkIter++)
    {
        ClientArrayInfo kInfo = pkIter->second;

        switch(kInfo.type)
        {
            case(GL_VERTEX_ARRAY):
            {   
                glVertexPointer(m_uiComponents, m_eDataType, kInfo.stride, kInfo.address);
                glEnableClientState(GL_VERTEX_ARRAY);
                break;
            }
            case(GL_COLOR_ARRAY):
            {   
                glColorPointer(m_uiComponents, m_eDataType, kInfo.stride, kInfo.address);
                glEnableClientState(GL_COLOR_ARRAY);
                break;
            }
            case(GL_NORMAL_ARRAY):
            {
                glNormalPointer( m_eDataType, kInfo.stride, kInfo.address);
                glEnableClientState(GL_NORMAL_ARRAY);
                break;
            }
            case(GL_TEXTURE_COORD_ARRAY):
            {
                glTexCoordPointer(m_uiComponents, m_eDataType, kInfo.stride, kInfo.address);
                glEnableClientState(GL_TEXTURE_COORD_ARRAY);        
                break;
            }
            case(GL_INDEX_ARRAY):
            case(GL_EDGE_FLAG_ARRAY):
            default:
                break;
        };
    }

    return true;
}

bool
BufferObject::disable() const
{
    glBindBuffer(m_eTarget, 0);

    ClientArrayMapConstIter pkIter;
    for(pkIter = m_kClientArrayMap.begin(); pkIter != m_kClientArrayMap.end(); pkIter++)
    {
        ClientArrayInfo kInfo = pkIter->second;

        switch(kInfo.type)
        {
            case(GL_VERTEX_ARRAY):
            {   
                glDisableClientState(GL_VERTEX_ARRAY);
                break;
            }
            case(GL_COLOR_ARRAY):
            {   
                glDisableClientState(GL_COLOR_ARRAY);
                break;
            }
            case(GL_NORMAL_ARRAY):
            {
                glDisableClientState(GL_NORMAL_ARRAY);
                break;
            }
            case(GL_TEXTURE_COORD_ARRAY):
            {
                glDisableClientState(GL_TEXTURE_COORD_ARRAY);        
                break;
            }
            case(GL_INDEX_ARRAY):
            case(GL_EDGE_FLAG_ARRAY):
            default:
                break;
        };
    }

    return true;
}

bool
BufferObject::addClientArray(
    GLenum eArrayType,
    GLuint uiStride,
    GLvoid *pvAddress)
{
    bool bValid = false;
    switch(eArrayType)
    {
        case(GL_VERTEX_ARRAY):
        case(GL_COLOR_ARRAY):
        case(GL_NORMAL_ARRAY):
        case(GL_TEXTURE_COORD_ARRAY):
        {
            bValid = true;
            break;
        }
        case(GL_INDEX_ARRAY):
        case(GL_EDGE_FLAG_ARRAY):
        default:
        {
            bValid = false;
            break;
        }
    }

    if(!bValid)
        return false;

    m_kClientArrayMap[eArrayType] = ClientArrayInfo(eArrayType, uiStride, pvAddress);
    return true;
}

bool
BufferObject::removeClientArray(
    GLenum eArrayType) 
{
    ClientArrayMapIter pkIter = m_kClientArrayMap.find(eArrayType);
    if(pkIter == m_kClientArrayMap.end())  
        return false;

    m_kClientArrayMap.erase(pkIter);
    return true;
}

BufferObject::ClientArrayInfo 
BufferObject::getClientArrayInfo(
    GLenum eClientArrayType)
{
    static ClientArrayInfo s_kNotFound;

    ClientArrayMapIter pkIter = m_kClientArrayMap.find(eClientArrayType);
    if(pkIter == m_kClientArrayMap.end())
        return s_kNotFound;

    return pkIter->second;  
}

void
BufferObject::checkStatus(
    const char* acMessage) const
{
    GLenum eError = glGetError();

    if(eError)
        printf("BufferObject: OpenGL Error: %s\n", acMessage);

    switch(eError)
    {
    case(0):
        break;
    case(GL_INVALID_FRAMEBUFFER_OPERATION_EXT):
        printf("BufferObject: OpenGL Error: Invalid Framebuffer Operation!\n");
        break;
    case(GL_INVALID_ENUM):
        printf("BufferObject: OpenGL Error: Invalid Enumerate!\n");
        break;
    case(GL_INVALID_VALUE):
        printf("BufferObject: OpenGL Error: Invalid Value!\n");
        break;
    case(GL_INVALID_OPERATION):
        printf("BufferObject: OpenGL Error: Invalid Operation!\n");
        break;
    case(GL_STACK_OVERFLOW):
        printf("BufferObject: OpenGL Error: Stack Overflow!\n");
        break;
    case(GL_STACK_UNDERFLOW):
        printf("BufferObject: OpenGL Error: Stack Underflow!\n");
        break;
    case(GL_OUT_OF_MEMORY):
        printf("BufferObject: OpenGL Error: Out of Memory!\n");
        break;
    default:
        printf("BufferObject: Unknown OpenGL Error '%d'\n", (int)eError);
        break;
    }
}

size_t
BufferObject::getSizeOfDataType(
    GLenum eDataType) const
{
    switch(eDataType)
    {
        case (GL_BYTE):                 
            return sizeof(GLbyte);
        case (GL_UNSIGNED_BYTE):                 
            return sizeof(GLubyte);
        case (GL_SHORT):                      
            return sizeof(GLshort);
        case (GL_UNSIGNED_SHORT):                
            return sizeof(GLushort);
        case (GL_INT):                 
            return sizeof(GLint);
        case (GL_UNSIGNED_INT):                   
            return sizeof(GLuint);
        case (GL_FLOAT):                          
            return sizeof(GLfloat);
        case (GL_DOUBLE):
            return sizeof(GLdouble);
        default:
            assert("Vertex Buffer Object: Invalid data type!\n");
    };

    return 0;
}
```

[Next](common-bufferobject.h.md)[Previous](common-aabb.h.md)

