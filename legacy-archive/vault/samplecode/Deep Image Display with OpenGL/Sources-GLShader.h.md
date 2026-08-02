---
title: Deep Image Display with OpenGL
apple_id: TP40016622
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/DeepImageDisplayWithOpenGL/Listings/Sources_GLShader_h.html
archived_at: '2026-07-18T03:06:07.600867Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Deep Image Display with OpenGL](Deep%20Image%20Display%20with%20OpenGL.md)


[Next](Sources-GLQuad.mm.md)[Previous](Sources-IOSurface2D.mm.md)

# Sources/GLShader.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility class for compiling a GL shader from a source string.
 */

#import <OpenGL/OpenGL.h>

@interface GLShader : NSObject

// Create a shader from a source file
- (nullable instancetype) initWithSource:(nullable const GLchar *)source
                                    type:(const GLenum)type;

+ (nullable instancetype) shaderWithSource:(nullable const GLchar *)source
                                      type:(const GLenum)type;

// Create a shader from a source file located at a URL
- (nullable instancetype) initWithURL:(nullable NSURL *)url
                                 type:(const GLenum)type;

+ (nullable instancetype) shaderWithURL:(nullable NSURL *)url
                                   type:(const GLenum)type;

// Create a shader from a source file located at an absolute path
- (nullable instancetype) initWithFile:(nullable NSString *)path
                                  type:(const GLenum)type;

+ (nullable instancetype) shaderWithFile:(nullable NSString *)path
                                    type:(const GLenum)type;

// Create a shader from a source file in application's bundle
- (nullable instancetype) initWithResource:(nullable NSString *)name
                                      type:(const GLenum)type;

+ (nullable instancetype) shaderWithResource:(nullable NSString *)name
                                        type:(const GLenum)type;

// Shader id
@property (nonatomic, readonly) GLuint shader;

@end
```

[Next](Sources-GLQuad.mm.md)[Previous](Sources-IOSurface2D.mm.md)

