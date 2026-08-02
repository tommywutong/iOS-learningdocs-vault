---
title: CIRAWFilterSample
apple_id: DTS40009217
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: QuartzCore
published: '2009-09-08'
source_url: https://developer.apple.com/library/archive/samplecode/CIRAWFilterSample/Listings/ImageView_m.html
archived_at: '2026-07-18T03:02:40.803462Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CIRAWFilterSample](CIRAWFilterSample.md)


[Next](ImageWindowController.h.md)[Previous](ImageView.h.md)

# ImageView.m

```objc
/*

 @file ImageView.m

 @abstract The place where all the display happens.

 @version 1.1

 ©  Copyright 2006-2009 Apple, Inc. All rights reserved.

 IMPORTANT: This Apple software is supplied to you by Apple Computer,
 Inc. ("Apple") in consideration of your agreement to the following
 terms, and your use, installation, modification or redistribution of
 this Apple software constitutes acceptance of these terms.  If you do
 not agree with these terms, please do not use, install, modify or
 redistribute this Apple software.

 In consideration of your agreement to abide by the following terms,
 and subject to these terms, Apple grants you a personal,
 non-exclusive license, under Apple's copyrights in this original
 Apple software (the "Apple Software"), to use, reproduce, modify and
 redistribute the Apple Software, with or without modifications, in
 source and/or binary forms; provided that if you redistribute the
 Apple Software in its entirety and without modifications, you must
 retain this notice and the following text and disclaimers in all such
 redistributions of the Apple Software.  Neither the name, trademarks,
 service marks or logos of Apple Computer, Inc. may be used to endorse
 or promote products derived from the Apple Software without specific
 prior written permission from Apple.  Except as expressly stated in
 this notice, no other rights or licenses, express or implied, are
 granted by Apple herein, including but not limited to any patent
 rights that may be infringed by your derivative works or by other
 works in which the Apple Software may be incorporated.

 The Apple Software is provided by Apple on an "AS IS" basis.  APPLE
 MAKES NO WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION
 THE IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY AND
 FITNESS FOR A PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS
 USE AND OPERATION ALONE OR IN COMBINATION WITH YOUR PRODUCTS.

 IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT,
 INCIDENTAL OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
 PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
 PROFITS; OR BUSINESS INTERRUPTION) ARISING IN ANY WAY OUT OF THE USE,
 REPRODUCTION, MODIFICATION AND/OR DISTRIBUTION OF THE APPLE SOFTWARE,
 HOWEVER CAUSED AND WHETHER UNDER THEORY OF CONTRACT, TORT (INCLUDING
 NEGLIGENCE), STRICT LIABILITY OR OTHERWISE, EVEN IF APPLE HAS BEEN
 ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

 */

#import "ImageView.h"

#import "ImageDocument.h"

#import <OpenGL/OpenGL.h>
#import <Quartz/Quartz.h>
#import <QuartzCore/QuartzCore.h>
#import <libkern/OSAtomic.h>


@interface ImageView ( Private )

- (CGFloat)scale;

- (NSSize)scaledImageSize;

- (CGRect)scaledDrawRect;

- (ImageDocument *)document;

- (CIFilter *)rawFilter;

- (NSController *)outputFilterController;

@end

@interface ImageView ( OpenGL )

+ (NSOpenGLPixelFormat *)defaultPixelFormat;

- (void)prepareOpenGL;

- (void)updateMatrices;

/*! Returns the CoreImage rendering context using the view's OpenGL context as its destination. */
- (CIContext *)coreImageContext;

@end

@implementation ImageView

- (id)initWithFrame:(NSRect)frameRect
{
    self = [super initWithFrame:frameRect];
    if (self != nil)
    {
        fullImageSize = NSMakeSize(0.f, 0.f);
    }
    return self;
}

- (void) dealloc
{
    [[self outputFilterController] removeObserver:self
                                       forKeyPath:@"content.outputImage"];
    [[self rawFilter] removeObserver:self
                          forKeyPath:kCIInputDecoderVersionKey];
    [rawFilter release], rawFilter = nil;
    [outputFilterController release], outputFilterController = nil;
    [coreImageContext release], coreImageContext = nil;
    [super dealloc];
}


- (void)awakeFromNib
{
    // Register, so we know when the output image changes.
    [[self outputFilterController] addObserver:self
                                    forKeyPath:@"content.outputImage"
                                       options:0
                                       context:nil];
    // Full image size might change for different versions
    [[self rawFilter] addObserver:self
                       forKeyPath:kCIInputDecoderVersionKey
                          options:0
                          context:nil]; 
}

- (void)observeValueForKeyPath:(NSString *)keyPath
                      ofObject:(id)object
                        change:(NSDictionary *)change
                       context:(void *)context
{
    if ((object == [self outputFilterController]) &&
        ([keyPath isEqualToString:@"content.outputImage"]))
    {
            [self setNeedsDisplay:YES];
    }
    else if ((object == [self rawFilter]) &&
             ([keyPath isEqualToString:kCIInputDecoderVersionKey]))
    {
        // Full image size might have changed. This will force recalculation:
        fullImageSize = NSMakeSize(0.f, 0.f);
    }
    else
    {
        [super observeValueForKeyPath:keyPath
                             ofObject:object
                               change:change
                              context:context];
    }
}

- (BOOL) isOpaque
{
    return YES;
}

- (BOOL)acceptsFirstMouse:(NSEvent *)theEvent
{
    return NO;
}

- (void)drawRect:(NSRect)rect inCIContext:(CIContext *)context
{
    [[self rawFilter] setValue:[NSNumber numberWithDouble:[self scale]] forKey:kCIInputScaleFactorKey];

    CIImage *outputImage = [[self outputFilterController] valueForKeyPath:@"content.outputImage"];

    CGRect draw = [self scaledDrawRect];
    CGRect imageRect = [outputImage extent];
    [context drawImage:outputImage inRect:draw fromRect:imageRect];
}

- (void)drawRect:(NSRect)rect
{
    [[self openGLContext] makeCurrentContext];

    CGRect ir = CGRectIntegral(*(CGRect *)&rect);

    if ([NSGraphicsContext currentContextDrawingToScreen])
    {
        [self updateMatrices];

        /* Clear the specified subrect of the OpenGL surface then
        * render the image into the view. Use the GL scissor test to
        * clip to * the subrect. Ask CoreImage to generate an extra
        * pixel in case * it has to interpolate (allow for hardware
                                                 * inaccuracies) */

        CGRect rr = CGRectIntersection(CGRectInset (ir, -1.0f, -1.0f),
                                       *((CGRect *) (&lastBounds)));

        glScissor(ir.origin.x, ir.origin.y, ir.size.width, ir.size.height);
        glEnable(GL_SCISSOR_TEST);

        glClear(GL_COLOR_BUFFER_BIT);

        [self drawRect:*(NSRect *)&rr inCIContext:[self coreImageContext]];

        glDisable(GL_SCISSOR_TEST);

        /* Flush the OpenGL command stream. If the view is double buffered this should be replaced by [[self openGLContext] flushBuffer]. */

        glFlush ();
    }
    else
    {
        /* Printing the view contents. Render using CG, not OpenGL. */
        [self drawRect:*(NSRect *)&ir inCIContext:[self coreImageContext]];
    }
}

- (void)mouseDown:(NSEvent *)event
{
    NSPoint loc = [self convertPoint:[event locationInWindow] fromView:nil];

    // Based on the scaling of the image we need to compute the actual point in the image
    // where the user clicked.
    CGRect draw = [self scaledDrawRect];
    if (!NSPointInRect(loc, NSMakeRect(draw.origin.x, draw.origin.y, draw.size.width, draw.size.height)))
    {
        [super mouseDown:event]; // Ingore
    }

    loc.x -= draw.origin.x;
    loc.y -= draw.origin.y;

    // We use the "click on neutral" method. Tell filter to use neutral WB at the mouse click location
    // adjusted for scaling and offset
    CIVector *neutralPoint = [CIVector vectorWithX:loc.x Y:loc.y];
    [[self rawFilter] setValue:neutralPoint forKey:kCIInputNeutralLocationKey];
}

@end

@implementation ImageView ( Private )

- (CGFloat)scale {
    if (fullImageSize.width < 1.f) {
        // Get the full size image:
        NSNumber *oldScale = [[[self rawFilter] valueForKey:kCIInputScaleFactorKey] retain];
        [[self rawFilter] setValue:[NSNumber numberWithDouble:1.f] forKey:kCIInputScaleFactorKey];
        CIImage *output = [[self rawFilter] valueForKey:kCIOutputImageKey];
        [[self rawFilter] setValue:oldScale forKey:kCIInputScaleFactorKey];
        [oldScale release];
        // Store its size:
        CGRect extent = [output extent];
        fullImageSize.width = extent.size.width;
        fullImageSize.height = extent.size.height;
    }
    NSRect bounds = [self bounds];
    CGFloat scale = fminf(NSWidth(bounds) / fullImageSize.width,
                        NSHeight(bounds) / fullImageSize.height);
    return scale;
}

- (NSSize)scaledImageSize {
    CGFloat scale = [self scale];
    if (fullImageSize.width > 0.f) {
        return NSMakeSize(fullImageSize.width * scale,
                          fullImageSize.height * scale);
    }
    return NSMakeSize(1.f, 1.f);
}

- (CGRect)scaledDrawRect {
    CGRect rect;
    NSSize const scaledImageSize = [self scaledImageSize];
    rect.size = *(CGSize *) &scaledImageSize;
    rect.origin.x = (NSWidth([self bounds]) - rect.size.width) / 2.f;
    rect.origin.y = (NSHeight([self bounds]) - rect.size.height) / 2.f;
    return rect;
}

- (ImageDocument *)document {
    NSWindowController *windowController = [[self window] windowController];
    ImageDocument *document = (ImageDocument *) [windowController document];
    if (![document isKindOfClass:[ImageDocument class]])
        return nil;
    return document;
}

- (CIFilter *)rawFilter {
    if (rawFilter == nil) {
        // We need to cache this here, so that we can unbind inside dealloc
        rawFilter = [[[self document] rawFilter] retain];
    }
    return rawFilter;
}

- (NSController *)outputFilterController {
    if (outputFilterController == nil) {
        // We need to cache this here, so that we can unbind inside dealloc
        outputFilterController = [[[self document] outputFilterController] retain];
    }
    return outputFilterController;
}

@end

@implementation ImageView ( OpenGL )

+ (NSOpenGLPixelFormat *)defaultPixelFormat
{
    static NSOpenGLPixelFormat *pf;

    if (pf == nil)
    {
        /* Making sure the context's pixel format doesn't have a recovery
         * renderer is important - otherwise CoreImage may not be able to
         * create deeper context's that share textures with this one. */

        static const NSOpenGLPixelFormatAttribute attr[] = 
        {
            NSOpenGLPFAAccelerated,
            NSOpenGLPFANoRecovery,
            NSOpenGLPFAColorSize, 32,
#if MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_5
            NSOpenGLPFAAllowOfflineRenderers,  /* allow use of offline renderers               */
#endif
            0
        };

        NSOpenGLPixelFormat *newFormat = [[NSOpenGLPixelFormat alloc] initWithAttributes:(void *)&attr];
        if (!OSAtomicCompareAndSwapPtrBarrier(NULL, newFormat, (void **) &pf)) {
            [newFormat release];
        }
    }

    return pf;
}

- (void)prepareOpenGL
{
    GLint parm = 1;

    /* Enable beam-synced updates. */

    [[self openGLContext] setValues:(void *)&parm forParameter:NSOpenGLCPSwapInterval];

    /* Make sure that everything we don't need is disabled. Some of these
     * are enabled by default and can slow down rendering. */

    glDisable(GL_ALPHA_TEST);
    glDisable(GL_DEPTH_TEST);
    glDisable(GL_SCISSOR_TEST);
    glEnable(GL_BLEND);
    glDisable(GL_DITHER);
    glDisable(GL_CULL_FACE);
    glColorMask(GL_TRUE, GL_TRUE, GL_TRUE, GL_TRUE);
    glDepthMask(GL_FALSE);
    glStencilMask(0);
    glClearColor(0.0f, 0.0f, 0.0f, 0.0f);
    glHint(GL_TRANSFORM_HINT_APPLE, GL_FASTEST);
}

- (void)updateMatrices
{
    NSRect newBounds = [self bounds];
    if (!NSEqualRects(newBounds, lastBounds))
    {
        [[self openGLContext] update];

        /* Install an orthographic projection matrix (no perspective)
         * with the origin in the bottom left and one unit equal to one
         * device pixel. */

        glViewport(0, 0, newBounds.size.width, newBounds.size.height);

        glMatrixMode (GL_PROJECTION);
        glLoadIdentity();
        glOrtho(0, newBounds.size.width, 0, newBounds.size.height, -1, 1);

        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();

        lastBounds = newBounds;
    }
}

- (CIContext *)coreImageContext
{
    if (coreImageContext == nil)
    {
        NSOpenGLPixelFormat *pixelFormat = [self pixelFormat];
        if (pixelFormat == nil)
        {
            pixelFormat = [[self class] defaultPixelFormat];
            [self setPixelFormat:pixelFormat];
        }

        NSDictionary *contextOptions = [NSDictionary dictionary];
#if MAC_OS_X_VERSION_MAX_ALLOWED <= MAC_OS_X_VERSION_10_5
        CIContext *newContext = [[CIContext contextWithCGLContext:CGLGetCurrentContext()
                                                      pixelFormat:[pixelFormat CGLPixelFormatObj]
                                                          options:contextOptions] retain];
#else       
        // For 10.6 onwards we use the new API but do not pass in a colorspace as. 
        // Since the cgl context will be rendered to the display, it is valid to rely on CI to get the colorspace from the context.
        CIContext *newContext = [[CIContext contextWithCGLContext:CGLGetCurrentContext()
                                                      pixelFormat:[pixelFormat CGLPixelFormatObj]
                                                       colorSpace:nil   
                                                          options:contextOptions] retain]; 
#endif
        if (!OSAtomicCompareAndSwapPtrBarrier(NULL, newContext, (void **) &coreImageContext)) {
            [newContext release];
        }
    }
    return coreImageContext;
}

@end
```

[Next](ImageWindowController.h.md)[Previous](ImageView.h.md)

