---
title: OpenCL_OceanWave
apple_id: DTS40009447
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2011-04-13'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_OceanWave/Listings/common_fbo_h.html
archived_at: '2026-07-18T03:17:46.956217Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL_OceanWave](OpenCLOceanWave.md)


[Next](common-frustum.cpp.md)[Previous](common-fbo.cpp.md)

Current information on this Developer Library topic can be found here:

- [Performance > Multiprocessing](https://developer.apple.com/referencelibrary/Performance/idxMultiprocessing-date.html)

# common/fbo.h

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

#ifndef __FBO_H__
#define __FBO_H__

#include "compute_types.h"
#include <OpenGL/gl.h>

class FrameBufferObject
{

public:

    FrameBufferObject();
    ~FrameBufferObject();

    bool setup(uint uiWidth, uint uiHeight, bool bUseRenderbuffer = false);

    void enable(bool bClear = false);
    void disable();

    void attach(GLenum eAttachment, GLenum eTarget, uint uiTextureId);
    void detach(GLenum eAttachment, GLenum eTarget);

    uint getWidth()                                     { return m_uiWidth; }
    uint getHeight()                                    { return m_uiHeight; }
    bool isEnabled()                                    { return m_bIsEnabled; }
    bool isAttached(GLenum eAttachment);
    bool isColorUsed();
    bool isDepthUsed();
    bool isStencilUsed();

protected:

    void destroy();
    uint createFramebuffer();
    uint createRenderbuffer(uint uiWidth, uint uiHeight);
    void checkFramebufferStatus(const char *acMessage=0);

protected:

    bool m_bIsEnabled;
    bool m_abAttached[64];
    GLint m_aiViewport[4];

    uint m_uiWidth;
    uint m_uiHeight;

    uint m_uiFramebufferId;
    uint m_uiRenderbufferId;
};

#endif
```

[Next](common-frustum.cpp.md)[Previous](common-fbo.cpp.md)

