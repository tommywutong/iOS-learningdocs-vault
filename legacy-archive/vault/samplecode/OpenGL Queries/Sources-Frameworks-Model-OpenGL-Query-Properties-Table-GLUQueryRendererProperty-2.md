---
title: OpenGL Queries
apple_id: TP40016611
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenGL_Queries/Listings/Sources_Frameworks_Model_OpenGL_Query_Properties_Table_GLUQueryRendererProperty_mm.html
archived_at: '2026-07-18T03:18:14.461912Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenGL Queries](OpenGL%20Queries.md)


[Next](Sources-Frameworks-Model-OpenGL-Query-Properties-Names-GLUQueryRendererPropertyN.md)[Previous](Sources-Frameworks-Model-OpenGL-Query-Properties-Table-GLUQueryRendererProperty.md)

# Sources/Frameworks/Model/OpenGL/Query/Properties/Table/GLUQueryRendererProperty.mm

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A utility class for converting a subset of properties into their string equivalent.
 */

#import "GLUQueryRendererPropertyNames.h"
#import "GLUQueryRendererProperty.h"

static const size_t kPadSpace = 10;

GLU::Query::RendererProperty::RendererProperty()
{
    GLuint i;

    for(i = 0; i < kProperteyCount; ++i)
    {
        mnLength = std::max(mnLength, kPropertyNames[i].length());

        m_Names.emplace(GLuint(kProperty[i]), kPropertyNames[i]);
    } // for

    mnLength += kPadSpace;
} // Constructor

GLU::Query::RendererProperty::~RendererProperty()
{
    if(!m_Names.empty())
    {
        for(auto& name:m_Names)
        {
            if(!name.second.empty())
            {
                name.second.clear();
            } // if
        } // for

        m_Names.clear();
    } // if
} // Destructor

GLstring GLU::Query::RendererProperty::find(const GLuint& nProperty)
{
    GLstring value;

    GLpropertynames::const_iterator pIter = m_Names.find(nProperty);

    if(pIter != m_Names.end())
    {
        value = pIter->second;
    } // if

    return value;
} // find

GLstring GLU::Query::RendererProperty::find(const CGLRendererProperty& nProperty)
{
    return find(GLuint(nProperty));
} // find

GLstring GLU::Query::RendererProperty::operator [](const GLuint& nProperty)
{
    return find(nProperty);
} // operator []

GLstring GLU::Query::RendererProperty::operator [](const CGLRendererProperty& nProperty)
{
    return find(nProperty);
} // operator []

size_t GLU::Query::RendererProperty::length()
{
    return mnLength;
} // length

size_t GLU::Query::RendererProperty::length(const CGLRendererProperty& nProperty)
{
    GLstring value = find(nProperty);

    return value.length();
} // length
```

[Next](Sources-Frameworks-Model-OpenGL-Query-Properties-Names-GLUQueryRendererPropertyN.md)[Previous](Sources-Frameworks-Model-OpenGL-Query-Properties-Table-GLUQueryRendererProperty.md)

