---
title: Deep Image Display with OpenGL
apple_id: TP40016622
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/DeepImageDisplayWithOpenGL/Listings/Sources_GLTextureDI_h.html
archived_at: '2026-07-18T03:06:07.747465Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Deep Image Display with OpenGL](Deep%20Image%20Display%20with%20OpenGL.md)


[Next](Sources-GLDIDAppDelegate.mm.md)[Previous](Sources-QuadRect.vs.md)

# Sources/GLTextureDI.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility class for generating a GL texture from an image.
 */

#import <OpenGL/OpenGL.h>

#import "IOSurface2D.h"

@interface GLTextureDI : NSObject

// NOTE: Default initializer, sets the properties for representation
//       of 1920x1080 64-bit RGBA texture 2D deep image

// Create a texture from a 2D I/O surface using the current CGL context
- (nullable instancetype) initWithSurface:(nonnull IOSurface2D *)surface;

// Create a texture from a 2D I/O surface using the CGL context object
- (nullable instancetype) initWithSurface:(nonnull IOSurface2D *)surface
                                  context:(nonnull CGLContextObj)context;

// Create a texture from an image
- (nullable instancetype) initWithImage:(nullable NSImage *)image;

// Create a texture from an image file located at a URL
- (nullable instancetype) initWithURL:(nullable NSURL *)url;

// Create a texture from an image file located at an absolute path
- (nullable instancetype) initWithFile:(nullable NSString *)path;

// Create a texture from an image file in application's bundle
- (nullable instancetype) initWithResource:(nullable NSString *)name;

// Texture id
@property (nonatomic, readonly) GLuint texture;

// Texture internal format
@property (nonatomic, readonly) GLint  internal;

// Texture format
@property (nonatomic, readonly) GLenum format;

// Texture pixel type
@property (nonatomic, readonly) GLenum type;

// Set teture's target type if the texture isn't already
// created by one of the designated initializers
@property (nonatomic) GLenum target;

// Set samples-per-pixel if the texture is not already
// created by one of the designated initializers
@property (nonatomic)  size_t  samplesPerPixel;

// Set bits-per-component if the texture is not already
// created by one of the designated initializers
@property (nonatomic)  size_t  bitsPerComponent;

// Set texture's width if the texture is not already
// created by one of the designated initializers
@property (nonatomic) GLsizei width;

// Set texture's height if the texture is not already
// created by one of the designated initializers
@property (nonatomic) GLsizei height;

// Bind/unbind texture target
@property (nonatomic) BOOL bind;

// Enable/disable texture target
@property (nonatomic) BOOL enable;

// Create a new texture if the properties were set and default
// initializer was used to instantiate the object.
- (BOOL) acquire;
- (BOOL) acquire:(nullable const void *)pixels;

// Update the texture
- (BOOL) update:(nonnull const void *)pixels;

// Update the texture starting at an offset
- (BOOL) update:(nonnull const void *)pixels
          point:(const CGPoint)offset;

@end
```

[Next](Sources-GLDIDAppDelegate.mm.md)[Previous](Sources-QuadRect.vs.md)

