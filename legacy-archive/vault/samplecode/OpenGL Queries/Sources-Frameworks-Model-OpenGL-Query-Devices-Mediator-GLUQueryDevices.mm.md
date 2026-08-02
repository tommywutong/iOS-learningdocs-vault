---
title: OpenGL Queries
apple_id: TP40016611
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenGL_Queries/Listings/Sources_Frameworks_Model_OpenGL_Query_Devices_Mediator_GLUQueryDevices_mm.html
archived_at: '2026-07-18T03:18:14.299758Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenGL Queries](OpenGL%20Queries.md)


[Next](Sources-Frameworks-Model-OpenGL-Query-Constants-GLUQueryConstants.h.md)[Previous](Sources-Frameworks-Model-OpenGL-Query-Devices-Mediator-GLUQueryDevices.h.md)

# Sources/Frameworks/Model/OpenGL/Query/Devices/Mediator/GLUQueryDevices.mm

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Mediator utility class for querying all OpenGL renderers
 */

#import <iostream>

#import <OpenGL/gl3.h>

#import "GLUQueryConstants.h"
#import "GLUQueryDevices.h"

GLU::Query::Devices::Devices(CGLContextObj pContext)
{
    if(pContext != nullptr)
    {
        CGLRendererInfoObj pInfo = nullptr;

        CGLError err = CGLQueryRendererInfo(GLU::Query::kDisplayMask, &pInfo, &mnCount);

        if(err == kCGLNoError)
        {
            GLint  nRID = 0;
            GLuint nIndex;

            for(nIndex = 0; nIndex < mnCount; ++nIndex)
            {
                err = CGLDescribeRenderer(pInfo, nIndex, kCGLRPRendererID, &nRID);

                if(err == kCGLNoError)
                {
                    GLU::Query::Device device(pContext, nIndex);

                    m_Table.emplace(nRID, device);
                    m_Renderers.push_back(nRID);
                } // if
            } // for

            CGLDestroyRendererInfo(pInfo);
        } // if
    } // if
} // Constructor

GLU::Query::Devices::~Devices()
{
    if(!m_Table.empty())
    {
        m_Table.clear();
    } // if

    if(!m_Renderers.empty())
    {
        m_Renderers.clear();
    } // if
} // Destructor

GLU::Query::Devices *GLU::Query::Devices::create(const CGLPixelFormatAttribute * const pAttributes)
{
    GLU::Query::Devices *pDevices = nullptr;

    if(pAttributes != nullptr)
    {
        CGLPixelFormatObj pPixelFmt = nullptr;

        GLint num = 0;

        CGLError err = CGLChoosePixelFormat(pAttributes, &pPixelFmt, &num);

        if(err == kCGLNoError)
        {
            CGLContextObj pContext = nullptr;

            err = CGLCreateContext(pPixelFmt, nullptr, &pContext);

            if(err == kCGLNoError)
            {
                err = CGLSetCurrentContext(pContext);

                if(err == kCGLNoError)
                {
                    pDevices = new (std::nothrow) GLU::Query::Devices(pContext);

                    if(pDevices == nullptr)
                    {
                        NSLog(@">> ERROR: Failed creating a backing-store for devices query object!");
                    } // if
                } // if

                CGLDestroyContext(pContext);
            } // if

            CGLDestroyPixelFormat(pPixelFmt);
        } // if
    } // if

    return pDevices;
} // create

GLU::Query::Devices *GLU::Query::Devices::create()
{
    CGLPixelFormatAttribute attributes[8] =
    {
        kCGLPFAAllRenderers,
        kCGLPFASupportsAutomaticGraphicsSwitching,
        kCGLPFAAllowOfflineRenderers,
        kCGLPFAAcceleratedCompute,
        kCGLPFAOpenGLProfile, CGLPixelFormatAttribute(kCGLOGLPVersion_3_2_Core),
        CGLPixelFormatAttribute(0)
    };

    return create(attributes);
} // create

const GLint& GLU::Query::Devices::count() const
{
    return mnCount;
} // count

const GLint* GLU::Query::Devices::renderers() const
{
    return m_Renderers.data();
} // renderers

GLfeatures GLU::Query::Devices::features(const GLint& nID)
{
    GLfeatures value;

    GLU::Query::DeviceTable::const_iterator pIter = m_Table.find(nID);

    if(pIter != m_Table.end())
    {
        value = pIter->second.features();
    } // if

    return value;
} // features

GLstring GLU::Query::Devices::renderer(const GLint& nID)
{
    GLstring value = "";

    GLU::Query::DeviceTable::const_iterator pIter = m_Table.find(nID);

    if(pIter != m_Table.end())
    {
        value = pIter->second.renderer();
    } // if

    return value;
} // renderer

GLstring GLU::Query::Devices::vendor(const GLint& nID)
{
    GLstring value = "";

    GLU::Query::DeviceTable::const_iterator pIter = m_Table.find(nID);

    if(pIter != m_Table.end())
    {
        value = pIter->second.vendor();
    } // if

    return value;
} // vendor

GLstring GLU::Query::Devices::version(const GLint& nID)
{
    GLstring value = "";

    GLU::Query::DeviceTable::const_iterator pIter = m_Table.find(nID);

    if(pIter != m_Table.end())
    {
        value = pIter->second.version();
    } // if

    return value;
} // version

const bool GLU::Query::Devices::match(const GLint& nID, GLstring& rKey) const
{
    GLU::Query::DeviceTable::const_iterator pIter = m_Table.find(nID);

    bool bSuccess = pIter != m_Table.end();

    if(bSuccess)
    {
        bSuccess = pIter->second.match(rKey);
    } // if

    return bSuccess;
} // match

const bool GLU::Query::Devices::match(const GLint& nID, GLstrings& rKeys) const
{
    GLU::Query::DeviceTable::const_iterator pIter = m_Table.find(nID);

    bool bSuccess = pIter != m_Table.end();

    if(bSuccess)
    {
        bSuccess = pIter->second.match(rKeys);
    } // if

    return bSuccess;
} // match
```

[Next](Sources-Frameworks-Model-OpenGL-Query-Constants-GLUQueryConstants.h.md)[Previous](Sources-Frameworks-Model-OpenGL-Query-Devices-Mediator-GLUQueryDevices.h.md)

