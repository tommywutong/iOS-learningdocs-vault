---
title: GLUT
apple_id: DTS10000528
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2008-02-08'
source_url: https://developer.apple.com/library/archive/samplecode/glut/Listings/GLUTClipboardController_h.html
archived_at: '2026-07-18T03:29:12.125822Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLUT](GLUT.md)


[Next](GLUTClipboardController.m.md)[Previous](glutbitmap.h.md)

# GLUTClipboardController.h

```objc

/* Copyright (c) Dietmar Planitzer, 1998. */

/* This program is freely distributable without licensing fees
   and is provided without guarantee or warrantee expressed or
   implied. This program is -not- in the public domain. */


#import <Cocoa/Cocoa.h>


@interface GLUTClipboardController : NSWindowController
{
   IBOutlet NSScrollView *      _scrollView;
   IBOutlet NSTextField *       _infoText;
            NSTimer *           _updateTimer;
            int                 _lastChangeCount;       /* PBoards change count when we created the last view */
            BOOL                    _firstTime;
}

- (IBAction)toggleWindow:(id)sender;

- (BOOL)isClipboardWindowVisible;
- (void)updateClipboardWindow;

@end
```

[Next](GLUTClipboardController.m.md)[Previous](glutbitmap.h.md)

