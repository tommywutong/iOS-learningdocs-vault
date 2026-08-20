---
title: GLEssentials
apple_id: DTS40010104
resource_type: Sample Code
platform: iOS|macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-08-07'
source_url: https://developer.apple.com/library/archive/samplecode/GLEssentials/Listings/GLEssentials_Source_Classes_OSX_GLEssentialsFullscreenWindow_m.html
archived_at: '2026-07-18T03:10:01.629513Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLEssentials](GLEssentials.md)


[Next](GLEssentials-Source-Classes-OSX-GLEssentialsWindowController.h.md)[Previous](GLEssentials-Source-Classes-OSX-GLEssentialsGLView.h.md)

# GLEssentials/Source/Classes/OSX/GLEssentialsFullscreenWindow.m

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Fullscreen window class.
  All logic here could have been done in the window controller except that, by default, borderless windows cannot be made key and input cannot go to them.
  Therefore, this class exists to override canBecomeKeyWindow allowing this borderless window to accept inputs.
  This class is not part of the NIB and entirely managed in code by the window controller.
 */

#import "GLEssentialsFullscreenWindow.h"

@implementation GLEssentialsFullscreenWindow

-(instancetype)init
{
    // Create a screen-sized window on the display you want to take over
    NSRect screenRect = [[NSScreen mainScreen] frame];

    // Initialize the window making it size of the screen and borderless
    self = [super initWithContentRect:screenRect
                            styleMask:NSBorderlessWindowMask
                              backing:NSBackingStoreBuffered
                                defer:YES];

    // Set the window level to be above the menu bar to cover everything else
    [self setLevel:NSMainMenuWindowLevel+1];

    // Set opaque
    [self setOpaque:YES];

    // Hide this when user switches to another window (or app)
    [self setHidesOnDeactivate:YES];

    return self;
}

-(BOOL)canBecomeKeyWindow
{
    // Return yes so that this borderless window can receive input
    return YES;
}

- (void)keyDown:(NSEvent *)event
{
    // Implement keyDown since controller will not get [ESC] key event which
    // the controller uses to kill fullscreen
    [[self windowController] keyDown:event];
}

@end
```

[Next](GLEssentials-Source-Classes-OSX-GLEssentialsWindowController.h.md)[Previous](GLEssentials-Source-Classes-OSX-GLEssentialsGLView.h.md)

