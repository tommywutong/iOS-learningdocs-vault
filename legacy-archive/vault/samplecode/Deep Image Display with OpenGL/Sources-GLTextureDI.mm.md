---
title: Deep Image Display with OpenGL
apple_id: TP40016622
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/DeepImageDisplayWithOpenGL/Listings/Sources_GLTextureDI_mm.html
archived_at: '2026-07-18T03:06:07.817653Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Deep Image Display with OpenGL](Deep%20Image%20Display%20with%20OpenGL.md)


[Next](Sources-QuadRect.vs.md)[Previous](Sources-GLProgram.mm.md)

# Sources/GLTextureDI.mm

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility class for generating a GL texture from an image.
 */

#import <OpenGL/gl3.h>
#import <OpenGL/glext.h>

#import "NSBitmap.h"
#import "GLTextureDI.h"

@implementation GLTextureDI
{
@private
    BOOL     isFinalized;
    BOOL     _bind;
    BOOL     _enable;
    GLuint   _texture;
    GLint    _internal;
    GLenum   _target;
    GLenum   _format;
    GLenum   _type;
    GLsizei  _width;
    GLsizei  _height;
    size_t   _samplesPerPixel;
    size_t   _bitsPerComponent;
}

- (BOOL) _newTexture:(nonnull IOSurface2D *)surface
             context:(nonnull CGLContextObj)context
{
    BOOL success = NO;

    glGenTextures(1, &_texture);

    glEnable(_target);
    {
        glBindTexture(_target, _texture);
        {
            glTexParameteri(_target, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
            glTexParameteri(_target, GL_TEXTURE_MAG_FILTER, GL_LINEAR);

            glTexParameteri(_target, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
            glTexParameteri(_target, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);

            CGLError error = CGLTexImageIOSurface2D(context,
                                                    _target,
                                                    _internal,
                                                    _width,
                                                    _height,
                                                    _format,
                                                    _type,
                                                    surface.surface,
                                                    0);

            success = error == kCGLNoError;

            if(!success)
            {
                // TODO:  Remove the fallback scheme when CGLTexImageIOSurface2D(...) full supports all deep image pixel combinations
                NSLog(@">> MESSAGE[%d]: Fall back scheme for creating a 2d texture from an i/o surface!", error);

                // Lock the input i/o surface
                success = [surface lock:YES];

                // NOTE:  This path works with GL_TEXTURE_RECTANGLE target, even though it isn't
                //        as performant as the live update path.
                if(success)
                {
                    glTexImage2D(_target,
                                 0,
                                 _internal,
                                 _width,
                                 _height,
                                 0,
                                 _format,
                                 _type,
                                 [surface map]);

                    [surface unlock];
                } // if
            } // if
        }
        glBindTexture(_target, 0);
    }
    glDisable(_target);

    return success;
} // _newTexture

- (BOOL) _newTexture:(nullable const GLvoid *)pixels
{
    glGenTextures(1, &_texture);

    glEnable(_target);
    {
        glBindTexture(_target, _texture);
        {
            glTexParameteri(_target, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
            glTexParameteri(_target, GL_TEXTURE_MAG_FILTER, GL_LINEAR);

            glTexParameteri(_target, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
            glTexParameteri(_target, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);

            glTexImage2D(_target,
                         0,
                         _internal,
                         _width,
                         _height,
                         0,
                         _format,
                         _type,
                         pixels);
        }
        glBindTexture(_target, 0);
    }
    glDisable(_target);

    return _texture != 0;
} // _newTexture

- (void) _initProperties
{
    if(_bitsPerComponent == 16)
    {
        _internal = (_samplesPerPixel == 4) ? GL_RGBA16 : GL_RGB16;
        _format   = (_samplesPerPixel == 4) ?   GL_RGBA :   GL_RGB;
        _type     = GL_UNSIGNED_SHORT;
    } // if
    else
    {
        // NOTE:  For 32-bit images and live update to an i/o surface using
        //        CGLTexImageIOSurface2D(...), the correct format should be
        //        GL_BGRA or GL_BGR. However, this combination fails to
        //        create a correct texture, and the live update using the
        //        CGLTexImageIOSurface2D(...) returns no error. But, to
        //        display the 32-bit texture, we deliberately select a
        //        GL_RGBA or GL_RGB to force CGLTexImageIOSurface2D(...)
        //        api to return an error so that the fallback scheme can
        //        generate the texture for us.
        _internal = (_samplesPerPixel == 4) ? GL_RGBA8 : GL_RGB8;
        _format   = (_samplesPerPixel == 4) ?  GL_RGBA :  GL_RGB;
        _type     = GL_UNSIGNED_INT_8_8_8_8_REV;
    } // else
} // _initProperties

- (BOOL) _initTextureWithSurface:(nonnull IOSurface2D *)surface
                         context:(nonnull CGLContextObj)context
{
    BOOL success = NO;

    if(surface && context)
    {
        _samplesPerPixel = surface.samplesPerPixel;

        if((_samplesPerPixel == 3) || (_samplesPerPixel == 4))
        {
            _bitsPerComponent = surface.bitsPerComponent;

            _target = GL_TEXTURE_RECTANGLE;
            _width  = GLsizei(surface.width);
            _height = GLsizei(surface.height);

            [self _initProperties];

            success = [self _newTexture:surface
                                context:context];
        } // if
    } // if

    return success;
} // _initTextureWithImage

- (BOOL) _initTextureWithSurface:(nonnull IOSurface2D *)surface
{
    CGLContextObj context = CGLGetCurrentContext();

    if(context != nullptr)
    {
        return [self _initTextureWithSurface:surface
                                     context:context];
    } // if

    return NO;
} // _initTextureWithSurface

- (BOOL) _initTextureWithImage:(nullable NSImage *)image
{
    BOOL success = NO;

    if(image)
    {
        NSBitmapImageRep* bitmap = [NSBitmap bitmapWithImage:image].bitmap;

        if(bitmap)
        {
            _samplesPerPixel = bitmap.samplesPerPixel;

            if(!bitmap.isPlanar && ((_samplesPerPixel == 3) || (_samplesPerPixel == 4)))
            {
                _bitsPerComponent = bitmap.bitsPerSample;

                _target = GL_TEXTURE_2D;
                _width  = GLsizei(bitmap.pixelsWide);
                _height = GLsizei(bitmap.pixelsHigh);

                [self _initProperties];

                success = [self _newTexture:bitmap.bitmapData];
            } // if
        } // if
    } // if

    return success;
} // _initTextureWithImage

- (BOOL) _initTextureWithFile:(nullable NSString *)path
{
    BOOL success = NO;

    if(path)
    {
        // load the source image and pass it to our windows/views -
        NSImage* image = [[[NSImage alloc] initWithContentsOfFile:path] autorelease];

        success = [self _initTextureWithImage:image];
    } // if

    return success;
} // _initTextureWithFile

- (BOOL) _initTextureWithURL:(nullable NSURL *)url
{
    BOOL success = NO;

    if(url)
    {
        // load the source image and pass it to our windows/views -
        NSImage* image = [[[NSImage alloc] initWithContentsOfURL:url] autorelease];

        success = [self _initTextureWithImage:image];
    } // if

    return success;
} // _initTextureWithFile

- (BOOL) _initTextureWithResource:(nullable NSString *)name
{
    BOOL success = NO;

    if(name)
    {
        // Acquire the absolute pathname to the imge resource in application's bundle
        NSString* resource = [[NSBundle mainBundle] resourcePath];
        NSString* path     = [NSString stringWithFormat:@"%@/%@", resource, name];

        success = [self _initTextureWithFile:path];
    } // if

    return success;
} // initTextureWithResource

- (BOOL) _initTexture
{
    _samplesPerPixel  = 4;
    _bitsPerComponent = 16;

    _texture = 0;
    _target  = GL_TEXTURE_2D;
    _width   = 1920;
    _height  = 1080;

    [self _initProperties];

    return NO;
} // _initTexture

// Default initializer, sets the properties for representation
// of 1920x1080 64-bit RGBA texture 2D deep image
- (nullable instancetype) init
{
    self = [super init];

    if(self)
    {
        isFinalized = [self _initTexture];
    } // if

    return self;
} // init

// Create a texture from a 2D I/O surface using the current CGL context
- (nullable instancetype) initWithSurface:(nonnull IOSurface2D *)surface
{
    self = [super init];

    if(self)
    {
        isFinalized = [self _initTextureWithSurface:surface];
    } // if

    return self;
} // initWithSurface

// Create a texture from a 2D I/O surface using the CGL context object
- (nullable instancetype) initWithSurface:(nonnull IOSurface2D *)surface
                                  context:(nonnull CGLContextObj)context
{
    self = [super init];

    if(self)
    {
        isFinalized = [self _initTextureWithSurface:surface
                                            context:context];
    } // if

    return self;
} // initWithSurface


// Create a texture from an image
- (nullable instancetype) initWithImage:(nullable NSImage *)image
{
    self = [super init];

    if(self)
    {
        isFinalized = [self _initTextureWithImage:image];
    } // if

    return self;
} // initWithImage

// Create a texture from an image file located at an absolute path
- (nullable instancetype) initWithFile:(nullable NSString *)path
{
    self = [super init];

    if(self)
    {
        isFinalized = [self _initTextureWithFile:path];
    } // if

    return self;
} // initWithFile

// Create a texture from an image file located at a URL
- (nullable instancetype) initWithURL:(nullable NSURL *)url
{
    self = [super init];

    if(self)
    {
        isFinalized = [self _initTextureWithURL:url];
    } // if

    return self;
} // initWithURL

// Create a texture from an image file in application's bundle
- (nullable instancetype) initWithResource:(nullable NSString *)name
{
    self = [super init];

    if(self)
    {
        isFinalized = [self _initTextureWithResource:name];
    } // if

    return self;
} // initWithResource

// Destructor
- (void) dealloc
{
    if(_texture)
    {
        glDeleteTextures(1, &_texture);
    } // if

    [super dealloc];
} // dealloc

// Set teture's target type if the texture isn't already
// created by one of the designated initializers
- (void) setTarget:(GLenum)target
{
    if(!isFinalized)
    {
        _target = ((target == GL_TEXTURE_2D) || (target == GL_TEXTURE_RECTANGLE)) ? target : GL_TEXTURE_2D;
    } // if
} // target

// Set samples-per-pixel if the texture is not already
// created by one of the designated initializers
- (void) setSamplesPerPixel:(size_t)samplesPerPixel
{
    if(!isFinalized)
    {
        _samplesPerPixel  = ((samplesPerPixel == 3) || (samplesPerPixel == 4)) ? samplesPerPixel : 4;
    } // if
} // setSamplesPerPixel

// Set bits-per-component if the texture is not already
// created by one of the designated initializers
- (void) setBitsPerComponent:(size_t)bitsPerComponent
{
    if(!isFinalized)
    {
        _bitsPerComponent  = ((bitsPerComponent == 8) || (bitsPerComponent == 16)) ? bitsPerComponent : 16;
    } // if
} // setBitsPerComponent

// Set texture's width if the texture is not already
// created by one of the designated initializers
- (void) setWidth:(GLsizei)width
{
    if(!isFinalized)
    {
        _width = (width != 0) ? width : 1920;
    } // if
} // setWidth

// Set texture's height if the texture is not already
// created by one of the designated initializers
- (void) setHeight:(GLsizei)height
{
    if(!isFinalized)
    {
        _height = (height != 0) ? height : 1080;
    } // if
} // setHeight

// Create a new texture if the properties were set and default
// initializer was used to instantiate the object.
- (BOOL) acquire:(nullable const void *)pixels
{
    if(!isFinalized)
    {
        [self _initProperties];

        isFinalized = [self _newTexture:pixels];
    } // if

    return isFinalized;
} // acquire

- (BOOL) acquire
{
    return [self acquire:nullptr];
} // acquire

// Update the texture
- (BOOL) update:(nonnull const void *)pixels
{
    BOOL success = isFinalized && (pixels != nullptr);

    if(success)
    {
        glTexSubImage2D(_target, 0, 0, 0, _width, _height, _format, _type, pixels);
    } // if

    return success;
} // pixels

// Update the texture starting at an offset
- (BOOL) update:(nonnull const void *)pixels
          point:(const CGPoint)offset
{
    BOOL success = isFinalized && (pixels != nullptr);

    if(success)
    {
        GLint xoffset = GLint(offset.x);
        GLint yoffset = GLint(offset.y);

        glTexSubImage2D(_target, 0, xoffset, yoffset, _width, _height, _format, _type, pixels);
    } // if

    return success;
} // pixels

// Bind/unbind texture target
- (void) setBind:(BOOL)bind
{
    _bind = bind;

    if(_bind)
    {
        glBindTexture(_target, _texture);
    } // if
    else
    {
        glBindTexture(_target, 0);
    } // else
} // setBind

// Enable/disable texture target
- (void) setEnable:(BOOL)enable
{
    _enable = enable;

    if(_enable)
    {
        glEnable(_target);
    } // if
    else
    {
        glDisable(_target);
    } // else
} // setEnable

@end
```

[Next](Sources-QuadRect.vs.md)[Previous](Sources-GLProgram.mm.md)

