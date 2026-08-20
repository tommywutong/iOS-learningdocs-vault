---
title: 'Popover: Using NSPopover to display contents of a view controller'
apple_id: DTS40010725
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2015-12-17'
source_url: https://developer.apple.com/library/archive/samplecode/Popover/Listings/MyViewController_m.html
archived_at: '2026-07-18T03:19:22.005480Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Popover: Using NSPopover to display contents of a view controller](Popover-%20Using%20NSPopover%20to%20display%20contents%20of%20a%20view%20controller.md)


[Next](Document%20Revision%20History.md)[Previous](LICENSE.txt.md)

# MyViewController.m

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
  See LICENSE.txt for this sample’s licensing information

  Abstract:
  NSViewController subclass for managing the main app's content. 
 */

#import "MyViewController.h"

@interface MyViewController () <NSPopoverDelegate>

// configuration UI
@property (weak) IBOutlet NSMatrix *popoverType;
@property (weak) IBOutlet NSMatrix *popoverPosition;
@property (weak) IBOutlet NSButton *animatesCheckbox;
@property (weak) IBOutlet NSButton *useCustomDetachedWindow;

@property (strong) NSPopover *myPopover;
@property (strong) MyViewController *popoverViewController;

@property (strong) NSWindow *detachedWindow;
@property (strong) NSPanel *detachedHUDWindow;

@end


#pragma mark -

@implementation MyViewController

// -------------------------------------------------------------------------------
//  viewDidLoad
// -------------------------------------------------------------------------------
- (void)viewDidLoad
{
    [super viewDidLoad];

    // setup the default preferences
    self.animatesCheckbox.state = 1;                        // animates = YES
    self.useCustomDetachedWindow.state = 0;                 // use the built-in window support instead our own windows for detachable popovers

    [self.popoverType setState:1 atRow:0 column:0];         // type = normal
    [self.popoverPosition setState:1 atRow:1 column:0];     // position = NSMinYEdge

    _popoverViewController = [self.storyboard instantiateControllerWithIdentifier:@"PopoverViewController"];

    // To make a popover detachable to a separate window you need:
    // 1) a separate NSWindow instance
    //      - it must not be visible:
    //          (if created by Interface Builder: not "Visible at Launch")
    //          (if created in code: must not be ordered front)
    //      - must not be released when closed
    //      - ideally the same size as the view controller's view frame size
    //
    // 2) NSViewController instance for each window
    //
    // To make the popover detached, simply drag the visible popover away from its attached view
    //
    // For more detailed information, refer to NSPopover.h
    //
    NSRect frame = self.popoverViewController.view.bounds;
    NSUInteger styleMask = NSTitledWindowMask + NSClosableWindowMask;
    NSRect rect = [NSWindow contentRectForFrameRect:frame styleMask:styleMask];
    _detachedWindow = [[NSWindow alloc] initWithContentRect:rect styleMask:styleMask backing:NSBackingStoreBuffered defer:YES];
    self.detachedWindow.contentViewController = self.popoverViewController;
    self.detachedWindow.releasedWhenClosed = NO;

    styleMask = NSTitledWindowMask + NSClosableWindowMask + NSHUDWindowMask + NSUtilityWindowMask;
    _detachedHUDWindow = [[NSPanel alloc] initWithContentRect:rect styleMask:styleMask backing:NSBackingStoreBuffered defer:YES];
    self.detachedHUDWindow.contentViewController = self.popoverViewController;
    self.detachedHUDWindow.releasedWhenClosed = NO;
}

// -------------------------------------------------------------------------------
//  createPopover
// -------------------------------------------------------------------------------
- (void)createPopover
{
    if (self.myPopover == nil)
    {
        // create and setup our popover
        _myPopover = [[NSPopover alloc] init];

        // the popover retains us and we retain the popover,
        // we drop the popover whenever it is closed to avoid a cycle

        self.myPopover.contentViewController = self.popoverViewController;

        switch (self.popoverType.selectedRow)
        {
            case 0:
                self.myPopover.appearance = [NSAppearance appearanceNamed:NSAppearanceNameVibrantLight];
                break;
            case 1:
                self.myPopover.appearance = [NSAppearance appearanceNamed:NSAppearanceNameVibrantDark];
                break;
        }

        self.myPopover.animates = (self.animatesCheckbox).state;

        // AppKit will close the popover when the user interacts with a user interface element outside the popover.
        // note that interacting with menus or panels that become key only when needed will not cause a transient popover to close.
        self.myPopover.behavior = NSPopoverBehaviorTransient;

        // so we can be notified when the popover appears or closes
        self.myPopover.delegate = self;
    }
}

// -------------------------------------------------------------------------------
//  showPopoverAction:sender
// -------------------------------------------------------------------------------
- (IBAction)showPopoverAction:(id)sender
{
    switch (self.popoverType.selectedRow)
    {
        case 0:
            if (self.detachedHUDWindow.visible == YES)
            {
                [self.detachedHUDWindow close];
            }

            if (self.detachedWindow.visible)
            {
                // popover is already detached to a separate window, so select its window instead
                [self.detachedWindow makeKeyAndOrderFront:self];
                return;
            }
            break;
        case 1:
            if (self.detachedWindow.visible == YES)
            {
                [self.detachedWindow close];
            }

            if (self.detachedHUDWindow.visible)
            {
                // dark style popover is already detached to a separate window, so select its window instead
                [self.detachedHUDWindow makeKeyAndOrderFront:self];
                return;
            }
            break;
    }

    [self createPopover];

    NSButton *targetButton = (NSButton *)sender;

    // configure the preferred position of the popover
    NSRectEdge prefEdge = self.popoverPosition.selectedRow;

    [self.myPopover showRelativeToRect:targetButton.bounds ofView:sender preferredEdge:prefEdge];
}


#pragma mark - NSApplicationDelegate

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


#pragma mark - NSPopoverDelegate

// -------------------------------------------------------------------------------
// Invoked on the delegate when the NSPopoverWillShowNotification notification is sent.
// This method will also be invoked on the popover.
// -------------------------------------------------------------------------------
- (void)popoverWillShow:(NSNotification *)notification
{
    NSPopover *popover = notification.object;
    if (popover != nil)
    {
        //... operate on that popover
    }
}

// -------------------------------------------------------------------------------
// Invoked on the delegate when the NSPopoverDidShowNotification notification is sent.
// This method will also be invoked on the popover.
// -------------------------------------------------------------------------------
- (void)popoverDidShow:(NSNotification *)notification
{
    // add new code here after the popover has been shown
}

// -------------------------------------------------------------------------------
// Invoked on the delegate when the NSPopoverWillCloseNotification notification is sent.
// This method will also be invoked on the popover.
// -------------------------------------------------------------------------------
- (void)popoverWillClose:(NSNotification *)notification
{
    NSString *closeReason = [notification.userInfo valueForKey:NSPopoverCloseReasonKey];
    if (closeReason)
    {
        // closeReason can be:
        //      NSPopoverCloseReasonStandard
        //      NSPopoverCloseReasonDetachToWindow
        //
        // add new code here if you want to respond "before" the popover closes
        //
    }
}

// -------------------------------------------------------------------------------
// Invoked on the delegate when the NSPopoverDidCloseNotification notification is sent.
// This method will also be invoked on the popover.
// -------------------------------------------------------------------------------
- (void)popoverDidClose:(NSNotification *)notification
{
    NSString *closeReason = [notification.userInfo valueForKey:NSPopoverCloseReasonKey];
    if (closeReason)
    {
        // closeReason can be:
        //      NSPopoverCloseReasonStandard
        //      NSPopoverCloseReasonDetachToWindow
        //
        // add new code here if you want to respond "after" the popover closes
        //
    }

    // release our popover since it closed
    _myPopover = nil;
}

// -------------------------------------------------------------------------------
// Invoked on the delegate to give permission to detach popover as a separate window.
// -------------------------------------------------------------------------------
- (BOOL)popoverShouldDetach:(NSPopover *)popover
{
    return YES;
}

// -------------------------------------------------------------------------------
// Invoked on the delegate to when the popover was detached.
// Note: Invoked only if AppKit provides the window for this popover.
// -------------------------------------------------------------------------------
- (void)popoverDidDetach:(NSPopover *)popover
{
    NSLog(@"popoverDidDetach");
}

// -------------------------------------------------------------------------------
// Invoked on the delegate asked for the detachable window for the popover.
// -------------------------------------------------------------------------------
- (NSWindow *)detachableWindowForPopover:(NSPopover *)popover
{
    NSWindow *window = nil;

    if (self.useCustomDetachedWindow.state)
    {
        window = self.detachedWindow;
        if ([popover.appearance.name isEqualToString:NSAppearanceNameVibrantDark])
        {
            // use the dark window (style HUD)
            window = self.detachedHUDWindow;
        }
    }

    return window;
}

@end
```

[Next](Document%20Revision%20History.md)[Previous](LICENSE.txt.md)

