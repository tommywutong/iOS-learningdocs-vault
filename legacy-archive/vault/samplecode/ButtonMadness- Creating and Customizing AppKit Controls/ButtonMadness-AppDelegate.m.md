---
title: 'ButtonMadness: Creating and Customizing AppKit Controls'
apple_id: DTS10004430
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-12-21'
source_url: https://developer.apple.com/library/archive/samplecode/ButtonMadness/Listings/ButtonMadness_AppDelegate_m.html
archived_at: '2026-07-18T03:02:21.011006Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ButtonMadness: Creating and Customizing AppKit Controls](ButtonMadness-%20Creating%20and%20Customizing%20AppKit%20Controls.md)


[Next](ButtonMadness-MyWindowController.h.md)[Previous](ReadMe.md.md)

# ButtonMadness/AppDelegate.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Main app controller object using adopting the NSApplicationDelegate protocol.
 */

#import "AppDelegate.h"
#import "MyWindowController.h"

@interface AppDelegate ()

@property (strong) MyWindowController *myWindowController;

@end

#pragma mark -

@implementation AppDelegate

// -------------------------------------------------------------------------------
//  applicationShouldTerminateAfterLastWindowClosed:sender
//
//  NSApplication delegate method placed here so the sample conveniently quits
//  after we close the window.
// -------------------------------------------------------------------------------
- (BOOL)applicationShouldTerminateAfterLastWindowClosed:(NSApplication *)sender
{
    return YES;
}

// -------------------------------------------------------------------------------
//  applicationDidFinishLaunching:notification
// -------------------------------------------------------------------------------
- (void)applicationDidFinishLaunching:(NSNotification *)notification
{
    // Load the app's main window for display.
    _myWindowController = [[MyWindowController alloc] initWithWindowNibName:@"TestWindow"];
    [self.myWindowController showWindow:self];
}

@end
```

[Next](ButtonMadness-MyWindowController.h.md)[Previous](ReadMe.md.md)

