---
title: OpenGL Queries
apple_id: TP40016611
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenGL_Queries/Listings/Sources_Frameworks_Model_OpenGL_Containers_GLContainers_h.html
archived_at: '2026-07-18T03:18:13.798559Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenGL Queries](OpenGL%20Queries.md)


[Next](README.md.md)[Previous](Sources-Frameworks-Model-OpenGL-Query-Data-GLUQueryDataSource.h.md)

# Sources/Frameworks/Model/OpenGL/Containers/GLContainers.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 OpenGL container type definitions.
 */

#ifndef _OPENGL_CONTAINERS_H_
#define _OPENGL_CONTAINERS_H_

#import <ostream>
#import <regex>
#import <sstream>
#import <string>
#import <unordered_map>
#import <unordered_set>
#import <vector>

#import <OpenGL/OpenGL.h>

#ifdef __cplusplus

typedef std::string                                         GLstring;
typedef std::ostream                                        GLostream;
typedef std::ostringstream                                  GLosstringstream;
typedef std::regex                                          GLregex;
typedef std::vector<GLint>                                  GLrenderids;
typedef std::vector<GLstring>                               GLstrings;
typedef std::unordered_map<GLstring, GLstring>              GLfeatures;
typedef std::unordered_map<GLuint, GLint>                   GLproperties;
typedef std::unordered_map<GLint, GLproperties>             GLrenderers;
typedef std::unordered_map<CGDirectDisplayID, GLrenderers>  GLdisplays;
typedef std::unordered_map<GLuint, GLstring>                GLpropertynames;
typedef std::unordered_set<GLstring>                        GLstringset;

#endif

#endif
```

[Next](README.md.md)[Previous](Sources-Frameworks-Model-OpenGL-Query-Data-GLUQueryDataSource.h.md)

