---
title: RosyWriter
apple_id: DTS40011110
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/RosyWriter/Listings/Classes_Utilities_GL_ShaderUtilities_h.html
archived_at: '2026-07-18T03:22:19.103454Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [RosyWriter](RosyWriter.md)


[Next](Classes-Utilities-GL-matrix.c.md)[Previous](Classes-Utilities-GL-ShaderUtilities.c.md)

# Classes/Utilities/GL/ShaderUtilities.h

```c

/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Shader compiler and linker utilities
 */


#ifndef RosyWriter_ShaderUtilities_h
#define RosyWriter_ShaderUtilities_h

#include <OpenGLES/ES2/gl.h>
#include <OpenGLES/ES2/glext.h>

GLint glueCompileShader(GLenum target, GLsizei count, const GLchar **sources, GLuint *shader);
GLint glueLinkProgram(GLuint program);
GLint glueValidateProgram(GLuint program);
GLint glueGetUniformLocation(GLuint program, const GLchar *name);

GLint glueCreateProgram(const GLchar *vertSource, const GLchar *fragSource,
                        GLsizei attribNameCt, const GLchar **attribNames, 
                        const GLint *attribLocations,
                        GLsizei uniformNameCt, const GLchar **uniformNames,
                        GLint *uniformLocations,
                        GLuint *program);

#endif
```

[Next](Classes-Utilities-GL-matrix.c.md)[Previous](Classes-Utilities-GL-ShaderUtilities.c.md)

