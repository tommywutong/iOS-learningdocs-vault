---
title: OpenGL Queries
apple_id: TP40016611
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenGL_Queries/Listings/Sources_Frameworks_Model_OpenGL_Query_Devices_Base_GLUQueryDevice_mm.html
archived_at: '2026-07-18T03:18:14.145748Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenGL Queries](OpenGL%20Queries.md)


[Next](Sources-Frameworks-Model-OpenGL-Query-Devices-Base-GLUQueryDevice.h.md)[Previous](Sources-Frameworks-Model-OpenGL-Query-Properties-Names-GLUQueryRendererPropertyN.md)

# Sources/Frameworks/Model/OpenGL/Query/Devices/Base/GLUQueryDevice.mm

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility class for querying OpenGL device information.
 */

#pragma mark -
#pragma mark Private - Headers

#import <OpenGL/gl3.h>

#import "GLUQueryDevice.h"

#pragma mark -
#pragma mark Private - Enumerated Types

enum CLUQueryStrings
{
    eGLUQueryStringRenderer = 0,
    eGLUQueryStringVendor,
    eGLUQueryStringVersion,
    eGLUQueryStringMax
};

enum CLUQueryFeatures
{
    eGLUQueryFeatureApple = 0,
    eGLUQueryFeatureARB,
    eGLUQueryFeatureEXT,
    eGLUQueryFeatureMax
};

#pragma mark -
#pragma mark Private - Constants

static const GLchar *kGLUQueryFeatureType[eGLUQueryFeatureMax] =
{
    "GL_APPLE",
    "GL_ARB",
    "GL_EXT"
};

static const GLuint kGLUQueryFeatureTypeSize[eGLUQueryFeatureMax] = { 8, 6, 6 };

static const GLenum kGLUDeviceInfoType[eGLUQueryStringMax] =
{
    GL_RENDERER,
    GL_VENDOR,
    GL_VERSION
};

#pragma mark -
#pragma mark Private - Utilities

// Found Apple feature
static bool GLUQueryStringCompare(const GLuint& nType,
                                  const GLchar * const pExtension)
{
    return( strncmp(pExtension, kGLUQueryFeatureType[nType], kGLUQueryFeatureTypeSize[nType]) == 0 );
} // GLUQueryStringIsApple

// Add EXT feature
static void GLUQueryAddFeature(const GLuint& nType,
                               const GLchar * const pFeature,
                               GLfeatures& rFeatures)
{
    GLstring key(pFeature);
    GLstring value(kGLUQueryFeatureType[nType]);

    rFeatures.emplace(key, value);
} // GLUQueryAddFeatureEXT

// Query OpenGL and get a string representation of extension (or feature).
static void GLUQueryAppendFeature(const GLuint &rExtIdx,
                                  GLfeatures& rFeatures)
{
    const GLchar *pFeature = (const GLchar *)glGetStringi(GL_EXTENSIONS, rExtIdx);

    if( pFeature != nullptr )
    {
        if( GLUQueryStringCompare(eGLUQueryFeatureApple, pFeature) )
        {
            GLUQueryAddFeature(eGLUQueryFeatureApple, pFeature, rFeatures);
        } // if
        else if( GLUQueryStringCompare(eGLUQueryFeatureARB, pFeature) )
        {
            GLUQueryAddFeature(eGLUQueryFeatureARB, pFeature, rFeatures);
        } // else if
        else if( GLUQueryStringCompare(eGLUQueryFeatureEXT, pFeature) )
        {
            GLUQueryAddFeature(eGLUQueryFeatureEXT, pFeature, rFeatures);
        } // else if
    } // if
} // GLUQueryAppendFeature

// Create a table of extensions (or features)
static GLfeatures GLUQueryCreateFeatures(GLint& nFeatures)
{
    GLfeatures features;

    GLint nExtCnt = 0;

    glGetIntegerv(GL_NUM_EXTENSIONS, &nExtCnt);

    if(nExtCnt)
    {
        GLuint nExtIdx = 0;

        for(nExtIdx = 0; nExtIdx < nExtCnt; ++nExtIdx)
        {
            GLUQueryAppendFeature(nExtIdx, features);
        } // for

        nFeatures = nExtCnt;
    } // if

    return features;
} // GLUQueryCreateFeatures

#pragma mark -
#pragma mark Public - Constructor

GLU::Query::Device::Device(CGLContextObj pContext,
                           const GLint& nScreen)
{
    if(pContext != nullptr)
    {
        mbNoError = CGLSetVirtualScreen(pContext, nScreen) == kCGLNoError;

        if(mbNoError)
        {
            GLuint i;

            for(i = 0; i < eGLUQueryStringMax; ++i)
            {
                m_DeviceInfo[i] = (const char *)glGetString(kGLUDeviceInfoType[i]);
            } // for

            m_Features = GLUQueryCreateFeatures(mnEntries);
        } // if
    } // if
} // Constructor

#pragma mark -
#pragma mark Public - Destructor

GLU::Query::Device::~Device()
{
    GLuint i;

    for(i = 0; i < eGLUQueryStringMax; ++i)
    {
        if(!m_DeviceInfo[i].empty())
        {
            m_DeviceInfo[i].clear();
        } // if
    } // for
} // Destructor

#pragma mark -
#pragma mark Public - Utility

bool GLU::Query::Device::find(const GLstring& rFeature)
{
    GLfeatures::const_iterator pIter = m_Features.find(rFeature);

    return pIter != m_Features.end();
} // find

#pragma mark -
#pragma mark Public - Accessors

const bool& GLU::Query::Device::noError() const
{
    return mbNoError;
} // noError

const GLfeatures& GLU::Query::Device::features() const
{
    return m_Features;
} // features

const GLstring& GLU::Query::Device::renderer() const
{
    return m_DeviceInfo[eGLUQueryStringRenderer];
} // renderer

const GLstring& GLU::Query::Device::vendor() const
{
    return m_DeviceInfo[eGLUQueryStringVendor];
} // vendor

const GLstring& GLU::Query::Device::version() const
{
    return m_DeviceInfo[eGLUQueryStringVersion];
} // version

const bool GLU::Query::Device::match(GLstring& rKey) const
{
    bool bSuccess = !rKey.empty();

    if(bSuccess)
    {
        std::size_t found = m_DeviceInfo[eGLUQueryStringRenderer].find(rKey);

        bSuccess = found != std::string::npos;
    } // if

    return bSuccess;
} // match

const bool GLU::Query::Device::match(GLstrings& rKeys) const
{
    bool bSuccess = !rKeys.empty();

    if(bSuccess)
    {
        GLstring expr;

        size_t i;
        size_t iMax = rKeys.size() - 1;

        for(i = 0; i < iMax; ++i)
        {
            expr += rKeys[i] + "|";
        } // for

        expr += rKeys[iMax];

        GLregex regex(expr);

        bSuccess = std::regex_match(m_DeviceInfo[eGLUQueryStringRenderer], regex);
    } // if

    return bSuccess;
} // match
```

[Next](Sources-Frameworks-Model-OpenGL-Query-Devices-Base-GLUQueryDevice.h.md)[Previous](Sources-Frameworks-Model-OpenGL-Query-Properties-Names-GLUQueryRendererPropertyN.md)

