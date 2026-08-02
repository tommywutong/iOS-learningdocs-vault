---
title: OpenCL_OceanWave
apple_id: DTS40009447
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2011-04-13'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_OceanWave/Listings/common_memory_buffer_cpp.html
archived_at: '2026-07-18T03:17:47.272405Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL_OceanWave](OpenCLOceanWave.md)


[Next](common-memorybuffer.h.md)[Previous](common-gridmesh.h.md)

Current information on this Developer Library topic can be found here:

- [Performance > Multiprocessing](https://developer.apple.com/referencelibrary/Performance/idxMultiprocessing-date.html)

# common/memory_buffer.cpp

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

#include "memory_buffer.h"

/////////////////////////////////////////////////////////////////////////////

MemoryBuffer::MemoryBuffer() :
    m_uiElementSizeInBytes(0),
    m_uiElementCount(0),
    m_pvData(0)
{
    // EMPTY!
}

MemoryBuffer::~MemoryBuffer()
{
    if(m_pvData)
        destroy();
}

bool 
MemoryBuffer::allocate(
    uint uiElementSizeInBytes, 
    uint uiElementCount,
    bool bSetToZero)
{
    uint uiTotalBytes = uiElementSizeInBytes * uiElementCount;
    if(uiTotalBytes * uiElementCount > getTotalSizeInBytes())
        destroy();

    m_pvData = (void*) new char[uiTotalBytes];
    if(m_pvData == 0)
        return false;

    if(bSetToZero)
        memset(m_pvData, 0, uiTotalBytes);

    m_uiElementSizeInBytes = uiElementSizeInBytes;
    m_uiElementCount = uiElementCount;
    return true;
}

void
MemoryBuffer::destroy()
{
    if(m_pvData)
    {
        char* pcData = (char*)m_pvData;
        delete [] pcData;
    }

    m_uiElementSizeInBytes = 0;
    m_uiElementCount = 0;
    m_pvData = 0;
}

void
MemoryBuffer::printFloatData(uint uiComponents)
{
    if(m_pvData == 0)
        return;

    float* pfData = (float*) m_pvData;
    for(uint i = 0; i < m_uiElementCount; i++)
    {
        printf("[%d] ", i);
        for(uint c = 0; c < uiComponents; c++)
        {
            printf("%3.2f ", *pfData++);
        }
        printf("\n");
    }
}

void
MemoryBuffer::printUIntData(uint uiComponents)
{
    if(m_pvData == 0)
        return;

    uint* puiData = (uint*) m_pvData;
    for(uint i = 0; i < m_uiElementCount; i++)
    {
        printf("[%u] ", i);
        for(uint c = 0; c < uiComponents; c++)
        {
            printf("%u ", *puiData++);
        }
        printf("\n");
    }
}


/////////////////////////////////////////////////////////////////////////////
```

[Next](common-memorybuffer.h.md)[Previous](common-gridmesh.h.md)

