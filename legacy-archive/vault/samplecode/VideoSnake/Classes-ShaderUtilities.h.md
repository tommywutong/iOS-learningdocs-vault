---
title: VideoSnake
apple_id: DTS40012327
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/VideoSnake/Listings/Classes_ShaderUtilities_h.html
archived_at: '2026-07-18T03:27:54.316457Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [VideoSnake](VideoSnake.md)


[Next](Classes-MovieRecorder.h.md)[Previous](Classes-ShaderUtilities.c.md)

# Classes/ShaderUtilities.h

```c
/*
 <codex>
 <abstract>Shader compiler and linker utilities</abstract>
 </codex>
 */

#ifndef VideoSnake_ShaderUtilities_h
#define VideoSnake_ShaderUtilities_h

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

[Next](Classes-MovieRecorder.h.md)[Previous](Classes-ShaderUtilities.c.md)

