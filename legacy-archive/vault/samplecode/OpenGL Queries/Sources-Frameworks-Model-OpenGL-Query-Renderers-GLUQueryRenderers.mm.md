---
title: OpenGL Queries
apple_id: TP40016611
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenGL_Queries/Listings/Sources_Frameworks_Model_OpenGL_Query_Renderers_GLUQueryRenderers_mm.html
archived_at: '2026-07-18T03:18:14.606189Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenGL Queries](OpenGL%20Queries.md)


[Next](Sources-Frameworks-Model-OpenGL-Query-Data-GLUQueryDataSource.mm.md)[Previous](Sources-Frameworks-Model-OpenGL-Query-Renderers-GLUQueryRenderers.h.md)

# Sources/Frameworks/Model/OpenGL/Query/Renderers/GLUQueryRenderers.mm

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Query class for OpenGL renderers.
 */

#pragma mark -
#pragma mark Private - Headers

#import <iostream>

#import <OpenGL/gl3.h>

#import "GLUQueryConstants.h"
#import "GLUQueryRendererPropertyNames.h"
#import "GLUQueryRendererProperty.h"
#import "GLUQueryRenderers.h"

#pragma mark -
#pragma mark Private - Utilities - Properties

static GLproperties GLUQueryPropertiesCreate(CGLRendererInfoObj pInfo,
                                             const GLint& nRendNum)
{
    GLuint k;

    GLint     nResult = 0;
    CGLError  nError  = kCGLNoError;

    GLproperties properties;

    for(k = 0; k < GLU::Query::kProperteyCount; ++k)
    {
        // Get the properties for each renderer
        nError = CGLDescribeRenderer(pInfo, nRendNum, GLU::Query::kProperty[k], &nResult);

        if(nError == kCGLNoError)
        {
            properties.emplace(GLuint(GLU::Query::kProperty[k]), nResult);
        } // if
    } // for

    return properties;
} // GLUQueryPropertiesCreate

#pragma mark -
#pragma mark Private - Utilities - Renderers

static GLrenderers GLUQueryRenderersCreate(CGLRendererInfoObj pInfo,
                                           const GLuint& nRendCnt)
{
    GLuint j;

    GLint     nRID   = 0;
    CGLError  nError = kCGLNoError;

    GLrenderers renderers;

    for(j = 0; j < nRendCnt; ++j)
    {
        // For each renderer get the renderer id
        nError = CGLDescribeRenderer(pInfo, j, kCGLRPRendererID, &nRID);

        if(nError == kCGLNoError)
        {
            renderers.emplace(nRID, GLUQueryPropertiesCreate(pInfo, j));
        } // if
    } // for

    return renderers;
} // GLUQueryRenderersCreate

#pragma mark -
#pragma mark Public - Constructor

// Create an object for multiple displays
GLU::Query::Renderers::Renderers(const GLuint& nDisplayMask)
{
    GLint  nCount = 0;

    CGLRendererInfoObj  pInfo = nullptr;

    // For every OpenGL display mask get their renderer info object
    CGLError nError = CGLQueryRendererInfo(nDisplayMask, &pInfo, &nCount);

    if(nError == kCGLNoError)
    {
        m_Renderers = GLUQueryRenderersCreate(pInfo, nCount);
    } // if

    CGLDestroyRendererInfo(pInfo);
} // Constructor

#pragma mark -
#pragma mark Public - Destructor

GLU::Query::Renderers::~Renderers()
{
    if(!m_Description.empty())
    {
        m_Description.clear();
    } // if

    if(!m_Renderers.empty())
    {
        for(auto& renderer:m_Renderers)
        {
            if(!renderer.second.empty())
            {
                renderer.second.clear();
            } // if
        } // for

        m_Renderers.clear();
    } // if
} // Destructor

#pragma mark -
#pragma mark Public - Factory

// Create an instance of this object for all renderers
GLU::Query::Renderers *GLU::Query::Renderers::create()
{
    return new GLU::Query::Renderers(GLU::Query::kDisplayMask);
} // create

#pragma mark -
#pragma mark Public - Accessors

// Get renderer key-values associated with a direct display id
const GLrenderers& GLU::Query::Renderers::renderers() const
{
    return m_Renderers;
} // renderers

#pragma mark -
#pragma mark Public - Utilities

// Get a description string representing all the key-value pairs
// in the hash table
GLstring& GLU::Query::Renderers::description()
{
    if(m_Description.empty())
    {
        GLuint j = 1;
        GLuint k = 1;

        GLosstringstream stream;

        GLU::Query::RendererProperty properties;

        for(auto& renderer:m_Renderers)
        {
            GLproperties  properties = renderer.second;

            stream << "[" << j << "]\tRender id = 0x" << std::hex << renderer.first << std::endl << std::endl;

            for(auto& property:properties)
            {
                stream << "\t[" << j << "." << k << "]\t" << properties[property.first] << " = " << std::dec << property.second << std::endl;

                k++;
            } // for

            stream << std::endl;

            k = 1;

           j++;
        } // for

        m_Description = stream.str();
    } // if

    return m_Description;
} // description

#pragma mark -
#pragma mark Public - Output Stream

// Print all the key-value pairs
std::ostream& GLU::Query::operator<<(GLostream& rOutput,
                                     GLU::Query::Renderers &rRenderers)
{
    rOutput << rRenderers.description();

    return rOutput;
} // operator<<
```

[Next](Sources-Frameworks-Model-OpenGL-Query-Data-GLUQueryDataSource.mm.md)[Previous](Sources-Frameworks-Model-OpenGL-Query-Renderers-GLUQueryRenderers.h.md)

