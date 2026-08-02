---
title: Deep Image Display with OpenGL
apple_id: TP40016622
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/DeepImageDisplayWithOpenGL/Listings/Sources_GLView_mm.html
archived_at: '2026-07-18T03:06:08.076795Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Deep Image Display with OpenGL](Deep%20Image%20Display%20with%20OpenGL.md)


[Next](Sources-QuadRect.fs.md)[Previous](Sources-CGImageCopy.h.md)

# Sources/GLView.mm

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Custom OpenGL view for the application.
 */

#import <OpenGL/OpenGL.h>
#import <OpenGL/gl3.h>

#import "IOSurface2D.h"

#import "GLQuad.h"
#import "GLTextureDI.h"
#import "GLView.h"

static const GLfloat kGLClearColor[4] = {0.0, 0.0, 0.0, 0.0};

@implementation GLView
{
@private
    GLQuad*      quad;
    GLTextureDI* tex2D;

    NSRect bounds;

    GLsizei _width;
    GLsizei _height;

    IOSurface2D*  _surface;
    NSString*     _resource;
    NSString*     _path;
    NSURL*        _URL;
}

+ (NSOpenGLPixelFormat *) defaultPixelFormat
{
    // Core profile pixel format for deep image support
    const NSOpenGLPixelFormatAttribute attributes[] =
    {
        NSOpenGLPFADoubleBuffer,
        NSOpenGLPFAColorSize, 64,
        NSOpenGLPFAColorFloat,
        NSOpenGLPFAMultisample,
        NSOpenGLPFAOpenGLProfile, NSOpenGLProfileVersion4_1Core,
        0
    };

    return [[[NSOpenGLPixelFormat alloc] initWithAttributes:attributes] autorelease];
} // defaultPixelFormat

// Release assets
- (void) _cleanup
{
    if(tex2D)
    {
        [tex2D release];
    } // if

    if(quad)
    {
        [quad release];
    } // if

    if(_surface)
    {
        [_surface release];
    } // if

    if(_resource)
    {
        [_resource release];
    } // if

    if(_path)
    {
        [_path release];
    } // if

    if(_URL)
    {
        [_URL release];
    } // if

    // If self isn't removed as an observer, the Notification Center
    // will continue sending notification objects to the deallocated
    // object.
    [[NSNotificationCenter defaultCenter] removeObserver:self];
} // _cleanup

// Destructor
- (void) dealloc
{
    [self _cleanup];

    [super dealloc];
} // dealloc

// When application is terminating cleanup the objects
- (void) _terminate:(NSNotification *)notification
{
    [self  _cleanup];
} // terminate

- (void) awakeFromNib
{
    // It's important to clean up our rendering objects before we terminate -- Cocoa will
    // not specifically release everything on application termination, so we explicitly
    // call our cleanup (private object destructor) routines.
    [[NSNotificationCenter defaultCenter] addObserver:self
                                             selector:@selector(_terminate:)
                                                 name:@"NSApplicationWillTerminateNotification"
                                               object:NSApp];
} // awakeFromNib

- (BOOL) isOpaque
{
    return YES;
} // isOpaque

- (BOOL) acceptsFirstResponder
{
    return YES;
} // acceptsFirstResponder

- (BOOL) becomeFirstResponder
{
    return  YES;
} // becomeFirstResponder

- (BOOL) resignFirstResponder
{
    return YES;
} // resignFirstResponder

- (BOOL) applicationShouldTerminateAfterLastWindowClosed:(NSApplication *)theApplication
{
    return YES;
} // applicationShouldTerminateAfterLastWindowClosed

- (void) renewGState
{
    [super renewGState];

    [[self window] disableScreenUpdatesUntilFlush];
} // renewGState

- (void) prepareOpenGL
{
    // Prepare the base class
    [super prepareOpenGL];

    // Extendend dynamic range
    self.wantsExtendedDynamicRangeOpenGLSurface = YES;

    // Set the swap interval
    GLint nSyncVR = GL_TRUE;

    [[self openGLContext] setValues:&nSyncVR
                       forParameter:NSOpenGLCPSwapInterval];

    // Set the bounds
    bounds = [self convertRectToBacking:[self bounds]];

    _width  = GLsizei(bounds.size.width);
    _height = GLsizei(bounds.size.height);

    // Prepare the quad
    quad = [[GLQuad alloc] initWithBounds:bounds];
} // prepareOpenGL

// When the view is resized
- (void) reshape
{
    [super reshape];

    // Get the view bounds
    bounds = [self convertRectToBacking:[self bounds]];

    // Get the bound's width and height
    _width  = GLsizei(bounds.size.width);
    _height = GLsizei(bounds.size.height);

    // Set the viewport to be the entire window
    glViewport(0, 0, _width, _height);
} // reshape

- (void) setSurface:(nullable IOSurface2D *)surface
{
    if(surface != _surface)
    {
        // Release the now obselete texture 2d
        if(tex2D)
        {
            [tex2D release];
        } // if

        // Release the now obselete i/o surface 2d
        if(_surface)
        {
            [_surface release];
        } // if

        // Retain the new i/o surface 2d
        _surface = [surface retain];

        // Create a new texture rectangle from an I/O surface
        tex2D = [[GLTextureDI alloc] initWithSurface:_surface];

        if(tex2D)
        {
            // Texture rectangles require width and height
            quad.size = NSMakeSize(GLfloat(tex2D.width), GLfloat(tex2D.height));
        } // if
    } // if
} // setSurface

- (void) setURL:(nullable NSURL *)URL
{
    if(URL != _URL)
    {
        // Release the now obselete texture 2d
        if(tex2D)
        {
            [tex2D release];
        } // if

        // Release the now obselete image url
        if(_URL)
        {
            [_URL release];
        } // if

        // Retain the new image url
        _URL = [URL retain];

        // Create a new texture 2D from a 2D I/O surface.
        tex2D = [[GLTextureDI alloc] initWithURL:_URL];
    } // if
} // setUrl

- (void) setPath:(nullable NSString *)path
{
    if(path != _path)
    {
        // Release the now obselete texture 2d
        if(tex2D)
        {
            [tex2D release];
        } // if

        // Release the now obselete image pathname
        if(_path)
        {
            [_path release];
        } // if

        // Retain the new image pathname
        _path = [path retain];

        // Create a new texture 2D from a file located at an absolute path.
        tex2D = [[GLTextureDI alloc] initWithFile:_path];
    } // if
} // setResource

- (void) setResource:(nullable NSString *)resource
{
    if(resource != _resource)
    {
        // Release the now obselete texture 2d
        if(tex2D)
        {
            [tex2D release];
        } // if

        // Release the now obselete image path in app's bundle
        if(_resource)
        {
            [_resource release];
        } // if

        // Retain the new image path in app's bundle
        _resource = [resource retain];

        // Create a new texture 2D from a file in the application's bundle.
        tex2D = [[GLTextureDI alloc] initWithResource:_resource];
    } // if
} // setResource

- (void) drawRect:(NSRect)dirtyRect
{
    [[self openGLContext] makeCurrentContext];
    {
        // Set viewport
        glViewport(0, 0, _width, _height);

        // Clear the color buffer
        glClearBufferfv(GL_COLOR, 0, kGLClearColor);

        // Render the textured quad
        if(tex2D)
        {
            [quad render:tex2D.texture];
        } // if
    }
    [[self openGLContext] flushBuffer];
} // drawRect

@end
```

[Next](Sources-QuadRect.fs.md)[Previous](Sources-CGImageCopy.h.md)

