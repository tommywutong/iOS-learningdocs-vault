---
title: 'MenuItemView: Embedding an NSView inside an NSMenuItem'
apple_id: DTS10004136
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/MenuItemView/Listings/MenuItemView_AppDelegate_m.html
archived_at: '2026-07-18T03:14:34.361246Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuItemView: Embedding an NSView inside an NSMenuItem](MenuItemView-%20Embedding%20an%20NSView%20inside%20an%20NSMenuItem.md)


[Next](MenuItemView-ViewController.m.md)[Previous](MenuItemView-ViewController.h.md)

# MenuItemView/AppDelegate.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Header file for this sample's application delegate.
 */

#import "AppDelegate.h"

@interface AppDelegate ()

@property (strong) NSMenu *appDockMenu;

@end


#pragma mark -

@implementation AppDelegate

// -------------------------------------------------------------------------------
//  aboutDockAction:sender
// -------------------------------------------------------------------------------
- (void)aboutDockAction:(id)sender
{
    [[NSApplication sharedApplication] orderFrontStandardAboutPanel:self];
}

// -------------------------------------------------------------------------------
//  applicationDidFinishLaunching:notification
// -------------------------------------------------------------------------------
- (void)applicationDidFinishLaunching:(NSNotification *)notification
{
    // add an "About" menu item to our Dock menu
    _appDockMenu = [[NSMenu alloc] initWithTitle:NSLocalizedString(@"DocMenu", @"")];
    [self.appDockMenu setAutoenablesItems:NO];

    NSMenuItem *newItem = [[NSMenuItem alloc] initWithTitle:NSLocalizedString(@"About", @"")
                                                                               action:@selector(aboutDockAction:)
                                                                        keyEquivalent:@""];
    newItem.target = self;
    [self.appDockMenu addItem:newItem];
}


// -------------------------------------------------------------------------------
//  applicationDockMenu:sender
// -------------------------------------------------------------------------------
// This NSApplication delegate method is called when the user clicks and holds on
// the application icon in the dock.
//
- (NSMenu *)applicationDockMenu:(NSApplication *)sender
{
    return self.appDockMenu;
}

@end
```

[Next](MenuItemView-ViewController.m.md)[Previous](MenuItemView-ViewController.h.md)

