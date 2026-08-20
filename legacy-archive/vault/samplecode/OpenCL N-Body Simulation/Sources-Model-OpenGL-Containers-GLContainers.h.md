---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_OpenGL_Containers_GLContainers_h.html
archived_at: '2026-07-18T03:17:42.204438Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](README.md.md)[Previous](Sources-Model-OpenGL-Utilities-Texture-2D-GLUTexture.h.md)

# Sources/Model/OpenGL/Containers/GLContainers.h

```objc
/*
 <codex>
 <abstract>
 OpenGL container type definitions.
 </abstract>
 </codex>
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

typedef std::string GLstring;
typedef std::regex  GLregex;

typedef std::ostream        GLostream;
typedef std::ostringstream  GLosstringstream;

typedef std::vector<GLuint>   GLuints;
typedef std::vector<GLenum>   GLenums;
typedef std::vector<GLstring> GLstrings;

typedef GLuints  GLhandles;
typedef GLuints  GLshaders;
typedef GLenums  GLtargets;

typedef std::unordered_map<GLuint, GLuint>        GLproperties;
typedef std::unordered_map<GLint, GLproperties>   GLrenderers;
typedef std::unordered_map<GLuint, GLrenderers>   GLdisplays;
typedef std::unordered_map<GLuint, GLstring>      GLpropertynames;
typedef std::unordered_map<GLenum, GLstring>      GLsources;

typedef std::unordered_set<GLstring>  GLstringset;

#endif

#endif
```

[Next](README.md.md)[Previous](Sources-Model-OpenGL-Utilities-Texture-2D-GLUTexture.h.md)

