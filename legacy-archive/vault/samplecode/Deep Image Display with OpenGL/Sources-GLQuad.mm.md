---
title: Deep Image Display with OpenGL
apple_id: TP40016622
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/DeepImageDisplayWithOpenGL/Listings/Sources_GLQuad_mm.html
archived_at: '2026-07-18T03:06:07.437279Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Deep Image Display with OpenGL](Deep%20Image%20Display%20with%20OpenGL.md)


[Next](Sources-NSTextFile.h.md)[Previous](Sources-GLShader.h.md)

# Sources/GLQuad.mm

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility class for rendering a textured quad.
 */

#import <iostream>

#import <OpenGL/gl3.h>

#import "GLShader.h"
#import "GLProgram.h"
#import "GLQuad.h"

enum : long
{
    eGLAttributeVertex,
    eGLAttributeTexCoords,
    eGLAttributeCount
};

static const GLsizei kGLSizeFloat = sizeof(GLfloat);

// Get the buffer offset
static GLchar* GLUBufferOffset(const GLintptr& nOffset)
{
    return((GLchar *)nullptr + nOffset);
} // GLUBufferOffset

@implementation GLQuad
{
@private
    BOOL   _bind;
    GLenum _mode;
    GLenum _target;
    GLuint _pid;
    GLuint _vao;
    NSRect _bounds;
    NSSize _size;

    BOOL       isTexture2D;
    GLuint     vbo;
    GLProgram* program;
}

- (GLProgram*) _newProgram
{
    GLProgram* aProgram = nil;

    NSString* rsrc = (_target == GL_TEXTURE_2D) ? @"Quad2D" : @"QuadRect";

    // Create a vertex shader
    GLShader* vertex = [GLShader shaderWithResource:rsrc
                                               type:GL_VERTEX_SHADER];

    if(vertex)
    {
        // Create a fragment shader
        GLShader* fragment = [GLShader shaderWithResource:rsrc
                                                     type:GL_FRAGMENT_SHADER];

        if(fragment)
        {
            aProgram = [GLProgram new];

            if(aProgram)
            {
                aProgram.shader = vertex.shader;
                aProgram.shader = fragment.shader;

                aProgram.attribute = "vertex";
                aProgram.attribute = "texCoord";

                if(![aProgram link])
                {
                    [aProgram  release];
                } // if
            } // if
        } // if
    } // if

    return aProgram;
} // _newProgram

- (void) _acquireVAO
{
    // Create a vertex array
    glGenVertexArrays(1, &_vao);

    glBindVertexArray(_vao);

    GLfloat s = GLfloat(_size.width);
    GLfloat t = GLfloat(_size.height);

    GLfloat data[] =
    {//   x     y        s    t
        -1.0, -1.0,     0.0,   t,
        -1.0,  1.0,     0.0, 0.0,
         1.0, -1.0,       s,   t,
         1.0,  1.0,       s, 0.0
    };

    glGenBuffers(1, &vbo);

    glBindBuffer(GL_ARRAY_BUFFER, vbo);
    glBufferData(GL_ARRAY_BUFFER, sizeof(data), data, GL_STATIC_DRAW);

    GLsizei stride = 4 * kGLSizeFloat;

    // Vertices
    glVertexAttribPointer(eGLAttributeVertex, 2, GL_FLOAT, GL_FALSE, stride, GLUBufferOffset(0));

    // Texture coordinates
    glVertexAttribPointer(eGLAttributeTexCoords, 2, GL_FLOAT, GL_FALSE, stride, GLUBufferOffset(2 * kGLSizeFloat));
} // _acquireVAO

- (void) _acquireQuad:(const NSRect)bounds
{
    // Set the quad bounds
    _bounds = bounds;

    // Is this a quad for texture 2D?
    isTexture2D = (_size.width == 1.0) && (_size.height == 1.0);

    // Texture target
    _target = (isTexture2D) ? GL_TEXTURE_2D : GL_TEXTURE_RECTANGLE;

    // Draw Mode
    _mode = GL_TRIANGLE_STRIP;

    // Create a _program object for shaders
    program = [self _newProgram];

    if(program)
    {
        // Get the program id
        _pid = program.pid;
    } // if
} // _acquireQuad

- (nullable instancetype) init
{
    self = [super init];

    if(self)
    {
        NSSize size   = NSMakeSize(1.0, 1.0);
        NSRect bounds = NSMakeRect(0.0, 0.0, size.width, size.height);

        _size = size;

        [self _acquireQuad:bounds];
        [self _acquireVAO];
    } // if

    return self;
} // init

// Create a quad with the bounds
- (nullable instancetype) initWithBounds:(const NSRect)bounds
{
    self = [super init];

    if(self)
    {        
        [self _acquireQuad:bounds];
    } // if

    return self;
} // initWithSize

// Destructor
- (void) dealloc
{
    glDeleteBuffers(1, &vbo);
    glDeleteVertexArrays(1,&_vao);

    if(program)
    {
        [program release];
    } // if

    [super dealloc];
} // dealloc

// Set the image size. For texture 2D the default coordinates are used.
// For texture rectangle you need to set the original image size.
- (void) setSize:(NSSize)size
{
    if(!isTexture2D && ((size.width != _size.width) && (size.height != _size.height)))
    {
        // Set the image size
        _size = size;

        // Create a new vao for the texture rectangle
        [self _acquireVAO];
    } // if
} // setSize

// Render the textured quad
- (void) render:(const GLuint)texture
{
    if(texture)
    {
        glUseProgram(_pid);
        {
            glEnable(_target);
            {
                glBindTexture(_target, texture);
                {
                    glBindVertexArray(_vao);

                    glEnableVertexAttribArray(eGLAttributeVertex);
                    glEnableVertexAttribArray(eGLAttributeTexCoords);

                    glDrawArrays(_mode, 0, 4);

                    glDisableVertexAttribArray(eGLAttributeTexCoords);
                    glDisableVertexAttribArray(eGLAttributeVertex);
                }
                glBindTexture(_target, 0);
            }
            glDisable(_target);
        }
        glUseProgram(0);
    } // if
} // render

@end
```

[Next](Sources-NSTextFile.h.md)[Previous](Sources-GLShader.h.md)

