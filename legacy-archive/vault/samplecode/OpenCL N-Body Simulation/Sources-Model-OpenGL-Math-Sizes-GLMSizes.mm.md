---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_OpenGL_Math_Sizes_GLMSizes_mm.html
archived_at: '2026-07-18T03:17:42.381794Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-OpenGL-Math-Constants-GLMConstants.mm.md)[Previous](Sources-Model-OpenGL-Math-Sizes-GLMSizes.h.md)

# Sources/Model/OpenGL/Math/Sizes/GLMSizes.mm

```objc
/*
 <codex>
 <import>GLMSizes.h</import>
 </codex>
 */

#import "GLMSizes.h"

#define GLSizeChar           sizeof(GLchar)
#define GLSizeChrPtr         sizeof(GLchar *)
#define GLSizeFloat          sizeof(GLfloat)
#define GLSizeDouble         sizeof(GLdouble)
#define GLSizeSignedByte     sizeof(GLbyte)
#define GLSizeSignedBytePtr  sizeof(GLbyte *)
#define GLSizeSignedShort    sizeof(GLshort)
#define GLSizeSignedInt      sizeof(GLint)
#define GLSizeUnsignedByte   sizeof(GLubyte)
#define GLSizeUnsignedShort  sizeof(GLushort)
#define GLSizeUnsignedInt    sizeof(GLuint)
#define GLSizeLong           sizeof(long)
#define GLSizeULong          sizeof(unsigned long)

GLuint GLM::Size::kByte    = GLSizeSignedByte;
GLuint GLM::Size::kBytePtr = GLSizeSignedBytePtr;
GLuint GLM::Size::kChar    = GLSizeChar;
GLuint GLM::Size::kCharPtr = GLSizeChrPtr;
GLuint GLM::Size::kFloat   = GLSizeFloat;
GLuint GLM::Size::kHFloat  = GLSizeFloat / 2;
GLuint GLM::Size::kDouble  = GLSizeDouble;
GLuint GLM::Size::kShort   = GLSizeSignedShort;
GLuint GLM::Size::kInt     = GLSizeSignedInt;
GLuint GLM::Size::kLong    = GLSizeLong;
GLuint GLM::Size::kUByte   = GLSizeUnsignedByte;
GLuint GLM::Size::kUInt    = GLSizeUnsignedInt;
GLuint GLM::Size::kULong   = GLSizeULong;
GLuint GLM::Size::kUShort  = GLSizeUnsignedShort;
```

[Next](Sources-Model-OpenGL-Math-Constants-GLMConstants.mm.md)[Previous](Sources-Model-OpenGL-Math-Sizes-GLMSizes.h.md)

