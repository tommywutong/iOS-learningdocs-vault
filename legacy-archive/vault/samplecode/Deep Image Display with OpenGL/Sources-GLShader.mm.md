---
title: Deep Image Display with OpenGL
apple_id: TP40016622
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/DeepImageDisplayWithOpenGL/Listings/Sources_GLShader_mm.html
archived_at: '2026-07-18T03:06:07.643938Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Deep Image Display with OpenGL](Deep%20Image%20Display%20with%20OpenGL.md)


[Next](Sources-NSBitmap.h.md)[Previous](Sources-GLView.h.md)

# Sources/GLShader.mm

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility class for compiling a GL shader from a source string.
 */

#import <iostream>

#import <OpenGL/gl3.h>

#import "NSTextFile.h"
#import "GLShader.h"

@implementation GLShader
{
@private
    GLuint _shader;
}

- (GLuint) _newShaderWithSource:(const GLchar *)source
                           type:(const GLenum)type
{
    GLuint shader = 0;

    if(source != nullptr)
    {
        GLint isCompiled = 0;

        shader = glCreateShader(type);

        glShaderSource(shader, 1, &source, nullptr);
        glCompileShader(shader);

        glGetShaderiv(shader, GL_COMPILE_STATUS, &isCompiled);

        if(!isCompiled)
        {
            GLint maxLength = 0;

            glGetShaderiv(shader, GL_INFO_LOG_LENGTH, &maxLength);

            GLchar* infoLog = new (std::nothrow) char[maxLength];

            if(infoLog != nullptr)
            {
                glGetShaderInfoLog(shader, maxLength, &maxLength, infoLog);

                NSLog(@">> ERROR: {\n%s\n}\n",infoLog);

                delete [] infoLog;
            } // if

            shader = 0;
        } // if
    } // if

    return shader;
} // _newShaderWithSource

// Create a shader from a source file
- (nullable instancetype) initWithSource:(nullable const GLchar *)source
                                    type:(GLenum)type
{
    self = [super init];

    if(self)
    {
        _shader = [self _newShaderWithSource:source
                                        type:type];
    } // if

    return self;
} // initWithSource

+ (nullable instancetype) shaderWithSource:(nullable const GLchar *)source
                                      type:(const GLenum)type
{
    return [[[GLShader allocWithZone:[self zone]] initWithSource:source type:type] autorelease];
} // shaderWithSource

// Create a shader from a source file located at a URL
- (nullable instancetype) initWithURL:(nullable NSURL *)url
                                 type:(const GLenum)type
{
    self = [super init];

    if(self)
    {
        NSTextFile* text = [NSTextFile textWithURL:url];

        if(text)
        {
            _shader = [self _newShaderWithSource:text.source
                                            type:type];
        } // if
    } // if

    return self;
} // initWithURL

+ (nullable instancetype) shaderWithURL:(nullable NSURL *)url
                                   type:(const GLenum)type
{
    return [[[GLShader allocWithZone:[self zone]] initWithURL:url type:type] autorelease];
} // shaderWithURL

// Create a shader from a source file located at an absolute path
- (nullable instancetype) initWithFile:(nullable NSString *)path
                                  type:(const GLenum)type
{
    self = [super init];

    if(self)
    {
        NSTextFile* text = [NSTextFile textWithFile:path];

        if(text)
        {
            _shader = [self _newShaderWithSource:text.source
                                            type:type];
        } // if
    } // if

    return self;
} // initWithFile

+ (nullable instancetype) shaderWithFile:(nullable NSString *)path
                                    type:(const GLenum)type
{
    return [[[GLShader allocWithZone:[self zone]] initWithFile:path type:type] autorelease];
} // shaderWithFile

// Create a shader from a source file in application's bundle
- (nullable instancetype) initWithResource:(nullable NSString *)name
                                      type:(const GLenum)type
{
    self = [super init];

    if(self)
    {
        NSString* ext = (type == GL_VERTEX_SHADER) ? @"vs" : @"fs";

        NSTextFile* text = [NSTextFile textWithResource:name ext:ext];

        if(text)
        {
            _shader = [self _newShaderWithSource:text.source
                                            type:type];
        } // if
    } // if

    return self;
} // initWithResource

+ (nullable instancetype) shaderWithResource:(nullable NSString *)name
                                        type:(const GLenum)type
{
    return [[[GLShader allocWithZone:[self zone]] initWithResource:name type:type] autorelease];
} // shaderWithResource

// Destructor
- (void) dealloc
{
    if(_shader)
    {
        glDeleteShader(_shader);
    } // if

    [super dealloc];
} // dealloc

@end
```

[Next](Sources-NSBitmap.h.md)[Previous](Sources-GLView.h.md)

