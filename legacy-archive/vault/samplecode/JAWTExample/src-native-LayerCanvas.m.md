---
title: JAWTExample
apple_id: DTS10000683
resource_type: Sample Code
platform: Java|macOS
topic: Cross Platform
technology: null
published: '2011-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/JAWTExample/Listings/src_native_LayerCanvas_m.html
archived_at: '2026-07-18T03:13:08.869536Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [JAWTExample](JAWTExample.md)


[Next](Document%20Revision%20History.md)[Previous](src-native-DrawingCanvas.m.md)

# src/native/LayerCanvas.m

```objc
/*
    File: LayerCanvas.m
Abstract: Native code that attaches a CoreAnimation layer to an AWT Canvas.
 Version: 2.0

Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple
Inc. ("Apple") in consideration of your agreement to the following
terms, and your use, installation, modification or redistribution of
this Apple software constitutes acceptance of these terms.  If you do
not agree with these terms, please do not use, install, modify or
redistribute this Apple software.

In consideration of your agreement to abide by the following terms, and
subject to these terms, Apple grants you a personal, non-exclusive
license, under Apple's copyrights in this original Apple software (the
"Apple Software"), to use, reproduce, modify and redistribute the Apple
Software, with or without modifications, in source and/or binary forms;
provided that if you redistribute the Apple Software in its entirety and
without modifications, you must retain this notice and the following
text and disclaimers in all such redistributions of the Apple Software.
Neither the name, trademarks, service marks or logos of Apple Inc. may
be used to endorse or promote products derived from the Apple Software
without specific prior written permission from Apple.  Except as
expressly stated in this notice, no other rights or licenses, express or
implied, are granted by Apple herein, including but not limited to any
patent rights that may be infringed by your derivative works or by other
works in which the Apple Software may be incorporated.

The Apple Software is provided by Apple on an "AS IS" basis.  APPLE
MAKES NO WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION
THE IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS
FOR A PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND
OPERATION ALONE OR IN COMBINATION WITH YOUR PRODUCTS.

IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL
OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) ARISING IN ANY WAY OUT OF THE USE, REPRODUCTION,
MODIFICATION AND/OR DISTRIBUTION OF THE APPLE SOFTWARE, HOWEVER CAUSED
AND WHETHER UNDER THEORY OF CONTRACT, TORT (INCLUDING NEGLIGENCE),
STRICT LIABILITY OR OTHERWISE, EVEN IF APPLE HAS BEEN ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.

Copyright (C) 2011 Apple Inc. All Rights Reserved.

*/

#import <Cocoa/Cocoa.h>
#import <Quartz/Quartz.h>
#import <QTKit/QTKit.h>
#import <JavaVM/jawt_md.h>
#import <JavaNativeFoundation/JavaNativeFoundation.h>

#include "com_apple_dts_samplecode_jawtexample_LayerBackedCanvas.h"


// forward declaration
@interface ThreePieceDemoLayer : CALayer { }
@end


/*
 * Class:     com_apple_dts_samplecode_jawtexample_LayerBackedCanvas
 * Method:    addNativeCoreAnimationLayer
 * Signature: ()V
 */
JNIEXPORT void JNICALL Java_com_apple_dts_samplecode_jawtexample_LayerBackedCanvas_addNativeCoreAnimationLayer
(JNIEnv *env, jobject canvas) {
#ifdef JAWT_MACOSX_USE_CALAYER // Java for Mac OS X 10.6 Update 4 or later required

JNF_COCOA_ENTER(env);

    // get the AWT
    JAWT awt;
    awt.version = JAWT_VERSION_1_4 | JAWT_MACOSX_USE_CALAYER; // opt into the CALayer model
    jboolean result = JAWT_GetAWT(env, &awt);
    JNF_CHECK_AND_RETHROW_EXCEPTION(env);
    if (result == JNI_FALSE) return; // CALayer support unavailable prior to Java for Mac OS X 10.6 Update 4

    // get the drawing surface
    JAWT_DrawingSurface *ds = awt.GetDrawingSurface(env, canvas);
    JNF_CHECK_AND_RETHROW_EXCEPTION(env);
    assert(ds != NULL);

    // lock the drawing surface
    jint lock = ds->Lock(ds); 
    JNF_CHECK_AND_RETHROW_EXCEPTION(env);
    assert((lock & JAWT_LOCK_ERROR) == 0);

    // get the drawing surface info
    JAWT_DrawingSurfaceInfo *dsi = ds->GetDrawingSurfaceInfo(ds);
    JNF_CHECK_AND_RETHROW_EXCEPTION(env);

    // Check DrawingSurfaceInfo. This can be NULL on Mac OS X if the native 
    // component heirachy has not been made visible yet on the AppKit thread.
    if (dsi != NULL) {
        // create and attach the layer on the AppKit thread
        [JNFRunLoop performOnMainThreadWaiting:YES withBlock:^(){
            // attach the "root layer" to the AWT Canvas surface layers
            id <JAWT_SurfaceLayers> surfaceLayers = (id <JAWT_SurfaceLayers>)dsi->platformInfo;
            surfaceLayers.layer = [[ThreePieceDemoLayer new] autorelease];
        }];

        // free the DrawingSurfaceInfo
        ds->FreeDrawingSurfaceInfo(dsi);
        JNF_CHECK_AND_RETHROW_EXCEPTION(env);
    }

    // unlock the drawing surface
    ds->Unlock(ds); 
    JNF_CHECK_AND_RETHROW_EXCEPTION(env);

    // free the drawing surface
    awt.FreeDrawingSurface(ds);
    JNF_CHECK_AND_RETHROW_EXCEPTION(env);

JNF_COCOA_EXIT(env);

#endif // JAWT_MACOSX_USE_CALAYER
}


@interface RotatingSquareGLLayer : NSOpenGLLayer { }
@end


// a "root layer" that contains three sample layers (Quartz Composistion, OpenGL, and QuickTime)
@implementation ThreePieceDemoLayer

- (id) init {
    self = [super init];
    if (!self) return nil;

    // instance handles it's own layout
    self.layoutManager = self;

    // create a Quartz Composistion layer from the app bundle
    NSString *compositionPath = [[NSBundle mainBundle] pathForResource:@"Clouds" ofType:@"qtz"];
    CALayer *qcLayer = [QCCompositionLayer compositionLayerWithFile:compositionPath];
    [self addSublayer:qcLayer];

    // do some custom GL drawing
    RotatingSquareGLLayer *caGLLayer = [RotatingSquareGLLayer layer];
    caGLLayer.asynchronous = YES;
    [self addSublayer:caGLLayer];

    // play a QuickTime movie from the app bundle
    QTMovie *movie = [QTMovie movieNamed:@"Sample.mov" error:nil];
    QTMovieLayer *qtMovieLayer = [QTMovieLayer layerWithMovie:movie];
    [self addSublayer:qtMovieLayer];
    [movie play];

    return self;
}

- (void)layoutSublayersOfLayer:(CALayer *)layer {
    NSArray *sublayers = layer.sublayers;

    CGRect layerFrame = layer.frame;
    CGFloat width = layerFrame.size.width / [sublayers count];
    CGFloat height = layerFrame.size.height;

    // layout left to right
    CGFloat x = 0;
    for(CALayer *child in sublayers) {
        child.frame = CGRectMake(x, 0, width, height);
        x += width;
    }
}

@end


// rotates a red square when asked to draw
@implementation RotatingSquareGLLayer

// override to draw custom GL content
-(void)drawInCGLContext:(CGLContextObj)glContext
            pixelFormat:(CGLPixelFormatObj)pixelFormat
           forLayerTime:(CFTimeInterval)timeInterval
            displayTime:(const CVTimeStamp *)timeStamp {

    // set the current context
    CGLSetCurrentContext(glContext);

    // draw a single red quad spinning around based on the current time
    GLfloat rotate = timeInterval * 60.0; // 60 degrees per second
    glClear(GL_COLOR_BUFFER_BIT);
    glMatrixMode(GL_MODELVIEW);
    glPushMatrix();
    glRotatef(rotate, 0.0, 0.0, 1.0);
    glBegin(GL_QUADS);
    glColor3f(1.0, 0.0, 0.0);
    glVertex2f(-0.5, -0.5);
    glVertex2f(-0.5,  0.5);
    glVertex2f( 0.5,  0.5);
    glVertex2f( 0.5, -0.5);
    glEnd();
    glPopMatrix();

    // call super to finalize the drawing - by default all it does is call glFlush()
    [super drawInCGLContext:glContext pixelFormat:pixelFormat forLayerTime:timeInterval displayTime:timeStamp];
}

@end
```

[Next](Document%20Revision%20History.md)[Previous](src-native-DrawingCanvas.m.md)

