---
title: 'MenuItemView: Embedding an NSView inside an NSMenuItem'
apple_id: DTS10004136
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/MenuItemView/Listings/MenuItemView_ViewController_m.html
archived_at: '2026-07-18T03:14:34.705165Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuItemView: Embedding an NSView inside an NSMenuItem](MenuItemView-%20Embedding%20an%20NSView%20inside%20an%20NSMenuItem.md)


[Next](MenuItemView-TrackView.m.md)[Previous](MenuItemView-AppDelegate.m.md)

# MenuItemView/ViewController.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Header file for this sample's main NSViewController.
 */

#import "ViewController.h"
#import "SliderView.h"
#import "TrackView.h"
#import "ImageMenuItemView.h"

@interface ViewController ()

@property (strong) IBOutlet NSView *myButtonView;
@property (strong) IBOutlet NSView *myRadioView;

@property (strong) IBOutlet SliderView *mySliderView;

@property (strong) IBOutlet ImageMenuItemView *myImageMenuItemView;
@property (strong) IBOutlet NSView *myProgressView;
@property (strong) IBOutlet TrackView *myTrackView;

@property (weak) IBOutlet NSImageView *myImageView;
@property (weak) IBOutlet NSPopUpButton *myPopupButton;

@property (strong) NSPopUpButton *myCustomPopupButton;          // popup button from scratch
@property (strong) NSPopUpButton *myCustomPopupButtonPullDown;  // pull down button from scratch

@end


#pragma mark -

@implementation ViewController

// -------------------------------------------------------------------------------
//  addMenuItemViews:menu
//
//  Canned routine used to copy and set each NSView to the right NSMenuItem.
// -------------------------------------------------------------------------------
- (void)addMenuItemViews:(NSMenu *)menu
{
    // button
    NSData *viewCopyData = [NSArchiver archivedDataWithRootObject:self.myButtonView];
    id viewCopy = [NSUnarchiver unarchiveObjectWithData:viewCopyData];
    NSMenuItem *menuItem = [menu itemAtIndex:0];
    menuItem.view = viewCopy;
    menuItem.target = self;

    // radio buttons
    viewCopyData = [NSArchiver archivedDataWithRootObject:self.myRadioView];
    viewCopy = [NSUnarchiver unarchiveObjectWithData:viewCopyData];
    menuItem = [menu itemAtIndex:1];
    menuItem.view = viewCopy;
    menuItem.target = self;

    // slider
    viewCopyData = [NSArchiver archivedDataWithRootObject:self.mySliderView];
    viewCopy = [NSUnarchiver unarchiveObjectWithData:viewCopyData];
    menuItem = [menu itemAtIndex:2];
    menuItem.view = viewCopy;
    menuItem.target = self;

    // image view
    viewCopyData = [NSArchiver archivedDataWithRootObject:self.myImageMenuItemView];
    viewCopy = [NSUnarchiver unarchiveObjectWithData:viewCopyData];
    [viewCopy setupBackgroundImage];
    menuItem = [menu itemAtIndex:3];
    menuItem.view = viewCopy;
    menuItem.target = self;

    // progress view
    viewCopyData = [NSArchiver archivedDataWithRootObject:self.myProgressView];
    viewCopy = [NSUnarchiver unarchiveObjectWithData:viewCopyData];
    menuItem = [menu itemAtIndex:4];
    menuItem.view = viewCopy;
}

// -------------------------------------------------------------------------------
//  createPopupButtons
//
//  Creates the two popup button controls from scratch.
// -------------------------------------------------------------------------------
- (void)createPopupButtons
{
    _myCustomPopupButton =
        [[NSPopUpButton alloc] initWithFrame:NSMakeRect(18.0, 30.0, 60.0, 40.0) pullsDown:NO];
    _myCustomPopupButtonPullDown =
        [[NSPopUpButton alloc] initWithFrame:NSMakeRect(102.0, 30.0, 60.0, 40.0) pullsDown:YES];

    [(NSPopUpButtonCell *)self.myCustomPopupButton.cell setBezelStyle:NSRegularSquareBezelStyle];
    [(NSPopUpButtonCell *)self.myCustomPopupButtonPullDown.cell setBezelStyle:NSRegularSquareBezelStyle];

    // set the arrow indicator position
    [[self.myCustomPopupButton cell] setArrowPosition:NSPopUpArrowAtBottom];
    [self.myCustomPopupButton setPreferredEdge:NSMaxXEdge];

    // set the arrow indicator position
    [[self.myCustomPopupButtonPullDown cell] setArrowPosition:NSPopUpArrowAtBottom];
    [self.myCustomPopupButtonPullDown setPreferredEdge:NSMinYEdge];

    // these two controls do not use an item from the menu for its own title
    [[self.myCustomPopupButton cell] setUsesItemFromMenu:NO];
    [[self.myCustomPopupButtonPullDown cell] setUsesItemFromMenu:NO];

    // set the button icon for both controls
    NSMenuItem *item = [[NSMenuItem allocWithZone:nil] initWithTitle:@"" action:NULL keyEquivalent:@""];
    NSImage *iconImage = [NSImage imageNamed:@"NSApplicationIcon"];
    iconImage.size = NSMakeSize(32,32);
    item.image = iconImage;
    item.onStateImage = nil;
    item.mixedStateImage = nil;
    [[self.myCustomPopupButton cell] setMenuItem:item];
    [[self.myCustomPopupButtonPullDown cell] setMenuItem:item];

    [self.view addSubview:self.myCustomPopupButton];
    [self.view addSubview:self.myCustomPopupButtonPullDown];
}

// -------------------------------------------------------------------------------
//  viewDidLoad
//
//  Create the custom menu and add the NSViews to each menu item.
//
//  Note: since we want each control and menubar to have their own custom menus and views,
//  we need to copy them using NSArchiver/NSUnarchiver.
// -------------------------------------------------------------------------------
- (void)viewDidLoad
{
    [super viewDidLoad];

    // create a new menu from scratch and add it to the app's menu bar
    NSMenuItem *newItem = [[NSMenuItem alloc] initWithTitle:NSLocalizedString(@"Custom", @"")
                                                                               action:NULL
                                                                        keyEquivalent:@""];
    NSMenu *newMenu = [[NSMenu alloc] initWithTitle:NSLocalizedString(@"Custom", @"")];
    newItem.enabled = YES;
    newItem.submenu = newMenu;
    [[NSApp mainMenu] insertItem:newItem atIndex:3];

    // create the menu items for this menu

    // this menu item will have a view with one NSButton
    newItem = [[NSMenuItem alloc] initWithTitle:NSLocalizedString(@"Popup Menu", @"")
                                                                   action:@selector(menuItem1Action:)
                                                            keyEquivalent:@""];
    newItem.enabled = YES;
    newItem.view = self.myButtonView;
    newItem.target = self;
    [newMenu addItem:newItem];

    // this menu item will have a view with radio buttons
    newItem = [[NSMenuItem alloc] initWithTitle:NSLocalizedString(@"Custom Item 2", @"")
                                                                   action:@selector(menuItem2Action:)
                                                            keyEquivalent:@""];
    newItem.enabled = YES;
    newItem.view = self.myRadioView;
    newItem.target = self;
    [newMenu addItem:newItem];

    // this menu item will have a view with a slider
    newItem = [[NSMenuItem alloc] initWithTitle:NSLocalizedString(@"Custom Item 3", @"")
                                                                   action:nil
                                                            keyEquivalent:@""];
    newItem.enabled = YES;
    newItem.view = self.mySliderView;
    [newMenu addItem:newItem];

    // this menu item will have a view with a picture background
    newItem = [[NSMenuItem alloc] initWithTitle:NSLocalizedString(@"Custom Item 4", @"")
                                                                   action:nil
                                                            keyEquivalent:@""];
    newItem.enabled = YES;
    newItem.view = self.myImageMenuItemView;
    [self.myImageMenuItemView setupBackgroundImage];
    [newMenu addItem:newItem];

    // this menu item will have a view with a progress indicator
    newItem = [[NSMenuItem alloc] initWithTitle:NSLocalizedString(@"Custom Item 5", @"")
                                                                   action:nil
                                                            keyEquivalent:@""];
    newItem.enabled = YES;
    newItem.view = self.myProgressView;
    [newMenu addItem:newItem];

    // this menu item will have a view with tracking areas (much like Finder's label menu item)
    newItem = [[NSMenuItem alloc] initWithTitle:NSLocalizedString(@"Custom Item 6", @"")
                                                                   action:nil
                                                            keyEquivalent:@""];
    newItem.enabled = YES;
    newItem.view = self.myTrackView;
    [newMenu addItem:newItem];

    // copy the custom NSMenu and its embedded NSViews
    NSData *menuCopyData = [NSArchiver archivedDataWithRootObject:newMenu];
    id menuCopy = [NSUnarchiver unarchiveObjectWithData:menuCopyData];
    [menuCopy removeItemAtIndex:5];         // don't use the label view menu item here
    [self addMenuItemViews:menuCopy];       // add the NSViews to all the menu items
    self.myPopupButton.menu = menuCopy; // set the newly copied menu to the popup button

    // setup more customized popup buttons from scratch
    [self createPopupButtons];

    // copy and add the custom menu to the popup button
    menuCopyData = [NSArchiver archivedDataWithRootObject:menuCopy];
    id finalMenu = [NSUnarchiver unarchiveObjectWithData:menuCopyData];
    [self addMenuItemViews:finalMenu];              // add the NSViews to all the menu items
    self.myCustomPopupButton.menu = finalMenu;      // set the newly copied menu to the popup button

    // copy and add the custom menu to the pull down button
    menuCopyData = [NSArchiver archivedDataWithRootObject:menuCopy];
    finalMenu = [NSUnarchiver unarchiveObjectWithData:menuCopyData];
    [self addMenuItemViews:finalMenu];                  // add the NSViews to all the menu items
    self.myCustomPopupButtonPullDown.menu = finalMenu;  // set the newly copied menu to the pulldown button

    // copy and add the custom menu as the NSImageView's contextual menu
    menuCopyData = [NSArchiver archivedDataWithRootObject:menuCopy];
    finalMenu = [NSUnarchiver unarchiveObjectWithData:menuCopyData];
    [self addMenuItemViews:finalMenu];          // add the NSViews to all the menu items
    self.myImageView.menu = finalMenu;      // set the newly copied menu to the image view
}

// -------------------------------------------------------------------------------
//  menuItem1Action:sender
//
//  User clicked the button in the button menu item view
// -------------------------------------------------------------------------------
- (IBAction)menuItem1Action:(id)sender
{
    NSAlert *alert = [[NSAlert alloc] init];
    alert.messageText = NSLocalizedString(@"NSMenuItem button", @"");

    [alert addButtonWithTitle:NSLocalizedString(@"Wow", @"")];
    alert.informativeText = NSLocalizedString(@"This is what happens when you put a button in an NSMenuItem.", @"");

    [alert runModal];

    // dismiss the menu
    NSMenu *menu = [[sender enclosingMenuItem] menu];
    [menu cancelTracking];
}

// -------------------------------------------------------------------------------
//  menuItem2Action:sender
//
//  User clicked one of the radio buttons in the radio menu item view
// -------------------------------------------------------------------------------
- (IBAction)menuItem2Action:(id)sender
{
}

// -------------------------------------------------------------------------------
//  radiosAction:sender
//
//  Action method for all the radio buttons (cold to hot).
// -------------------------------------------------------------------------------
- (IBAction)radiosAction:(id)sender
{
}

@end
```

[Next](MenuItemView-TrackView.m.md)[Previous](MenuItemView-AppDelegate.m.md)

