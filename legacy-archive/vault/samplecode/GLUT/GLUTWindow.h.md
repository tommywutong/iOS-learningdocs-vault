---
title: GLUT
apple_id: DTS10000528
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2008-02-08'
source_url: https://developer.apple.com/library/archive/samplecode/glut/Listings/GLUTWindow_h.html
archived_at: '2026-07-18T03:29:13.808726Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLUT](GLUT.md)


[Next](GLUTWindow.m.md)[Previous](GLUTView.m.md)

# GLUTWindow.h

```objc

/* Copyright (c) Dietmar Planitzer, 1998, 2002 - 2003 */

/* This program is freely distributable without licensing fees 
   and is provided without guarantee or warrantee expressed or 
   implied. This program is -not- in the public domain. */


#import "macx_glut.h"

@class GLUTView;


@interface GLUTWindow : NSWindow
{
@private

   GLUTWindow * _nextFullscreenWindow;  /* weak ref */
   NSString *       _imagePath;
   NSMutableSet *   _viewStorage;
   int              _enabledMouseMovedEvents;
   BOOL             _isFullscreen;
}

+ (id)windowByMorphingWindow: (GLUTWindow *)aWindow operation: (int)op arguments: (NSDictionary *)dict;


- (id)initWithContentRect: (NSRect)rect
      pixelFormat: (NSOpenGLPixelFormat *)pixelFormat
      windowID: (int)winid
      gameMode: (BOOL)gameMode
      fullscreenStereo: (BOOL)pfStereo
      treatAsSingle: (BOOL)treatAsSingle;

- (void)enableMouseMovedEvents;
- (void)disableMouseMovedEvents;

- (BOOL)isFullscreen;
- (BOOL)isAffectedByFullscreenWindow;

- (IBAction)save: (id)sender;
- (IBAction)saveAs: (id)sender;
- (IBAction)copy: (id)sender;

- (NSData *)contentsAsDataOfType: (NSString *)pboardType;

@end

// Window morphing operations
enum {
   kGLUTMorphOperationFullscreen,
   kGLUTMorphOperationRegular
};

// Windoww morphing operands
extern NSString *GLUTWindowFrame;   // kGLUTMorphOperationRegular
```

[Next](GLUTWindow.m.md)[Previous](GLUTView.m.md)

