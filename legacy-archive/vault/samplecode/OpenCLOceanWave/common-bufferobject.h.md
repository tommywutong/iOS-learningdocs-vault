---
title: OpenCL_OceanWave
apple_id: DTS40009447
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2011-04-13'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_OceanWave/Listings/common_buffer_object_h.html
archived_at: '2026-07-18T03:17:44.353292Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL_OceanWave](OpenCLOceanWave.md)


[Next](common-camera.cpp.md)[Previous](common-bufferobject.cpp.md)

Current information on this Developer Library topic can be found here:

- [Performance > Multiprocessing](https://developer.apple.com/referencelibrary/Performance/idxMultiprocessing-date.html)

# common/buffer_object.h

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

#ifndef __BUFFER_OBJECT_H__
#define __BUFFER_OBJECT_H__

#include <OpenGL/gl.h>
#include <map>

class BufferObject
{

public:

    struct ClientArrayInfo
    {
        GLenum type;
        GLuint stride;
        GLvoid* address;

        ClientArrayInfo(
            GLenum eArrayType = 0,
            GLuint uiArrayStride = 0,
            GLvoid* pvAddress = 0)
        {
            type = eArrayType;
            stride = uiArrayStride;
            address = pvAddress;
        }
    };


    typedef std::map<GLenum, ClientArrayInfo>::const_iterator ClientArrayMapConstIter;
    typedef std::map<GLenum, ClientArrayInfo>::iterator ClientArrayMapIter;
    typedef std::map<GLenum, ClientArrayInfo> ClientArrayMap;

public:

    BufferObject();
    ~BufferObject();

    void destroy();

    void* map(GLenum eAccess) const;
    void unmap() const;

    bool enable() const;
    bool disable() const;

    bool allocate(
        GLenum eTarget, 
        GLuint uiCount, 
        GLuint uiComponents, 
        GLenum eDataType,
        GLvoid* pvData,
        GLenum eUsage);

    bool addClientArray(
        GLenum eClientArrayType,
        GLuint uiStride,
        GLvoid *pvAddress);

    bool removeClientArray(
        GLenum eClientArrayType);

    ClientArrayInfo getClientArrayInfo(GLenum eClientArrayType);

    GLuint getEntryCount() const           { return m_uiCount;         }
    GLuint getComponents() const           { return m_uiComponents;    }
    GLuint getEntrySizeInBytes() const     { return m_uiComponents * getSizeOfDataType(m_eDataType); }
    GLuint getTotalSizeInBytes() const     { return m_uiBytes;         }
    GLuint getBufferId() const             { return m_uiBufferId;      }

    GLenum getDataType() const             { return m_eDataType;       }
    GLenum getUsage() const                { return m_eUsage;          }
    GLenum getTarget() const               { return m_eTarget;         }


protected:

    void
    checkStatus(const char* acMessage) const;

    size_t 
    getSizeOfDataType(
        GLenum eDataType) const;

protected:

    GLuint m_uiCount;
    GLuint m_uiComponents;
    GLuint m_uiBytes;

    GLenum m_eDataType;
    GLenum m_eUsage;
    GLenum m_eTarget;
    GLuint m_uiBufferId;

    ClientArrayMap m_kClientArrayMap;

};

#endif // __BUFFER_OBJECT_H__
```

[Next](common-camera.cpp.md)[Previous](common-bufferobject.cpp.md)

