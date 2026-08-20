---
title: 'ButtonMadness: Creating and Customizing AppKit Controls'
apple_id: DTS10004430
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-12-21'
source_url: https://developer.apple.com/library/archive/samplecode/ButtonMadness/Listings/ButtonMadness_MyWindowController_m.html
archived_at: '2026-07-18T03:02:21.170462Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ButtonMadness: Creating and Customizing AppKit Controls](ButtonMadness-%20Creating%20and%20Customizing%20AppKit%20Controls.md)


[Next](ButtonMadness-DropDownButton.m.md)[Previous](ButtonMadness-AppDelegate.h.md)

# ButtonMadness/MyWindowController.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The primary NSWindowController object for managing all the buttons and controls.
 */

#import "MyWindowController.h"
#import "DropDownButton.h"

@interface MyWindowController ()
{
//==================================================
// NSPopUpButton

// Nib based controls.
IBOutlet NSPopUpButton *nibBasedPopUpDown;
IBOutlet NSPopUpButton *nibBasedPopUpRight;

IBOutlet NSBox *popupBox;
IBOutlet NSMenu *buttonMenu;

// Code based controls.
IBOutlet NSView *placeHolder1;  // The anchor/reference place for the code-based popup.
NSPopUpButton *codeBasedPopUpDown;

IBOutlet NSView *placeHolder2;
NSPopUpButton *codeBasedPopUpRight;

//==================================================
// NSButton

// Nib based controls.
IBOutlet NSButton *nibBasedButton;
IBOutlet NSButton *nibBasedButtonSquare;

IBOutlet NSBox *buttonBox;

// Code based controls.
IBOutlet NSView *placeHolder3;
NSButton *codeBasedButton;

IBOutlet NSView *placeHolder4;
NSButton *codeBasedButtonSquare;

//==================================================
// NSSegmentedControl

// Nib based control.
IBOutlet NSSegmentedControl *nibBasedSegControl;

IBOutlet NSBox *segmentBox;

// Code based control.
IBOutlet NSView *placeHolder5;
NSSegmentedControl  *codeBasedSegmentControl;

//==================================================
// Placeholder for grouped radio buttons.

IBOutlet NSView *placeHolder6;

//==================================================
// NSColorWell

// Nib based control.
IBOutlet NSColorWell *nibBasedColorWell;

// Placeholder for code-based color well.
IBOutlet NSBox *colorBox;

// Code based control.
IBOutlet NSView *placeHolder7;
NSColorWell *codeBasedColorWell;

//==================================================
// NSLevelIndicator

// Nib based control.
IBOutlet NSLevelIndicator *nibBasedIndicator;

IBOutlet NSBox *indicatorBox;

// Code based control.
IBOutlet NSView *placeHolder8;
NSLevelIndicator *codeBasedIndicator;

IBOutlet NSStepper *levelAdjuster;

//==================================================
// DropDownButton

IBOutlet DropDownButton *dropDownButton;
}

@property (copy) IBOutlet NSMenu *buttonMenu;

// The action methods for all the buttons.
- (IBAction)pullsDownAction:(id)sender;
- (IBAction)popupAction:(id)sender;

- (IBAction)useIconAction:(id)sender;
- (IBAction)buttonAction:(id)sender;

- (IBAction)segmentAction:(id)sender;
- (IBAction)unselectAction:(id)sender;

- (IBAction)colorAction:(id)sender;

- (IBAction)levelAdjustAction:(id)sender;
- (IBAction)levelAction:(id)sender;
- (IBAction)setStyleAction:(id)sender;

- (IBAction)dropDownAction:(id)sender;

@end


#pragma mark -

// -------------------------------------------------------------------------------
//  NSSegmentedControl category to unselect all segments.
//
//  NSSegmentedControl won't unselect all segments if there is currently one
//  segment selected.  So you have to go into the "Momentary tracking mode", unselect
//  each of the cells, then go back to its original mode.
// -------------------------------------------------------------------------------
@interface NSSegmentedControl (SampleAddition)

- (void)unselectAllSegments;

@end


#pragma mark -

@implementation NSSegmentedControl (SampleAddition)

- (void)unselectAllSegments
{
    NSSegmentSwitchTracking current;
    current = self.trackingMode;

    self.trackingMode = NSSegmentSwitchTrackingMomentary;

    for (NSInteger segmendIdx = 0; segmendIdx < self.segmentCount; segmendIdx++)
    {
        [self setSelected:NO forSegment:segmendIdx];
    }

    self.trackingMode = current;
}

@end


#pragma mark -

@implementation MyWindowController

@synthesize buttonMenu;

// -------------------------------------------------------------------------------
//  initWithPath:newPath
// -------------------------------------------------------------------------------
- (instancetype)initWithPath:(NSString *)newPath
{
    return [super initWithWindowNibName:@"TestWindow"];
}

// -------------------------------------------------------------------------------
//  awakeFromNib
//
//  Note that we copy the 'buttonMenu' outlet whenever we set this copied menu to a
//  particular button.  This will ensure each button has their own unique menu so
//  not to affect each other.
// -------------------------------------------------------------------------------
- (void)awakeFromNib
{
    //===============================
    // NSPopupButton

    // Update its menu (keep original self.buttonMenu untouched).
    NSMenu *newMenu = [self.buttonMenu copy];

    // Add the image menu item back to the first menu item.
    NSMenuItem *menuItem = [[NSMenuItem alloc] initWithTitle:@"" action:nil keyEquivalent:@""];
    menuItem.image = [NSImage imageNamed:@"moof"];
    [newMenu insertItem:menuItem atIndex:0];

    // Create the pull down button pointing DOWN.
    codeBasedPopUpDown = [[NSPopUpButton alloc] initWithFrame:placeHolder1.frame pullsDown:YES];
    ((NSPopUpButtonCell *)codeBasedPopUpDown.cell).arrowPosition = NSPopUpArrowAtBottom;
    ((NSPopUpButtonCell *)codeBasedPopUpDown.cell).bezelStyle = NSShadowlessSquareBezelStyle;
    codeBasedPopUpDown.menu = newMenu;
    [popupBox addSubview:codeBasedPopUpDown];
    [placeHolder1 removeFromSuperview]; // We are done with the place holder, remove it from the window.

    // Create the pull down button pointing RIGHT.
    codeBasedPopUpRight = [[NSPopUpButton alloc] initWithFrame:placeHolder2.frame pullsDown:YES];
    ((NSPopUpButtonCell *)codeBasedPopUpRight.cell).arrowPosition = NSPopUpArrowAtBottom;
    codeBasedPopUpRight.preferredEdge = NSMaxXEdge; // make the popup menu appear to the right
    codeBasedPopUpRight.bezelStyle = NSShadowlessSquareBezelStyle;
    codeBasedPopUpRight.menu = newMenu;
    ((NSButtonCell *)codeBasedPopUpRight.cell).highlightsBy = NSChangeGrayCellMask;
    [popupBox addSubview:codeBasedPopUpRight];
    [placeHolder2 removeFromSuperview]; // We are done with the place holder, remove it from the window.

    // Copy the menu again for 'nibBasedPopUpDown' and 'nibBasedPopUpRight' control.
    nibBasedPopUpDown.menu = newMenu;
    nibBasedPopUpRight.menu = newMenu;

    //===============================
    // NSButton
    NSImage *iconImage = [NSImage imageNamed:@"moof"];

    // Create the non-shadow square button (NSSmallSquareBezelStyle).
    codeBasedButton = [[NSButton alloc] initWithFrame:placeHolder3.frame];
    // Note: this button we want alternate title and image, so we need to use NSMomentaryChangeButton.
    codeBasedButton.buttonType = NSMomentaryChangeButton;
    codeBasedButton.title = NSLocalizedString(@"NSButton", "");
    codeBasedButton.alternateTitle = NSLocalizedString(@"(pressed)", "");
    codeBasedButton.bezelStyle = NSSmallSquareBezelStyle;
    codeBasedButton.imagePosition = NSImageLeft;        // Left align the image.
    codeBasedButton.alignment = NSTextAlignmentCenter;  // Center align the string title.
    codeBasedButton.image = iconImage;
    codeBasedButton.alternateImage = [NSImage imageNamed:@"moof2"];
    codeBasedButton.font = [NSFont systemFontOfSize:[NSFont smallSystemFontSize]];
    codeBasedButton.sound = [NSSound soundNamed:@"Pop"];
    codeBasedButton.target = self;
    codeBasedButton.action = @selector(buttonAction:);
    [buttonBox addSubview:codeBasedButton];
    [placeHolder3 removeFromSuperview]; // We are done with the place holder, remove it from the window.

    // Create the shadow square button (NSShadowlessSquareBezelStyle).
    codeBasedButtonSquare = [[NSButton alloc] initWithFrame:placeHolder4.frame];
    // Note: this button we want alternate title and image, so we need to use NSMomentaryChangeButton.
    codeBasedButtonSquare.buttonType = NSMomentaryChangeButton;
    codeBasedButtonSquare.title = NSLocalizedString(@"NSButton", "");
    codeBasedButtonSquare.alternateTitle = NSLocalizedString(@"(pressed)", "");
    codeBasedButtonSquare.bezelStyle = NSShadowlessSquareBezelStyle;
    codeBasedButtonSquare.imagePosition = NSImageLeft;      // Left align the image.
    codeBasedButtonSquare.alignment = NSTextAlignmentCenter;// Center align the string title.
    codeBasedButtonSquare.image = iconImage;
    codeBasedButtonSquare.alternateImage = [NSImage imageNamed:@"moof2"];
    codeBasedButtonSquare.font = [NSFont systemFontOfSize:[NSFont smallSystemFontSize]];
    codeBasedButtonSquare.sound = [NSSound soundNamed:@"Pop"];
    codeBasedButtonSquare.target = self;
    codeBasedButtonSquare.action = @selector(buttonAction:);
    [buttonBox addSubview:codeBasedButtonSquare];
    [placeHolder4 removeFromSuperview]; // We are done with the place holder, remove it from the window.

    //===============================
    // NSSegmentedControl

    // Create the segmented control button.
    codeBasedSegmentControl = [[NSSegmentedControl alloc] initWithFrame:placeHolder5.frame];
    codeBasedSegmentControl.segmentCount = 3;
    [codeBasedSegmentControl setWidth:[nibBasedSegControl widthForSegment:0] forSegment:0];
    [codeBasedSegmentControl setWidth:[nibBasedSegControl widthForSegment:1] forSegment:1];
    [codeBasedSegmentControl setWidth:[nibBasedSegControl widthForSegment:2] forSegment:2];
    [codeBasedSegmentControl setLabel:NSLocalizedString(@"One", "") forSegment:0];
    [codeBasedSegmentControl setLabel:NSLocalizedString(@"Two", "") forSegment:1];
    [codeBasedSegmentControl setLabel:NSLocalizedString(@"Three", "") forSegment:2];
    codeBasedSegmentControl.target = self;
    codeBasedSegmentControl.action = @selector(segmentAction:);
    [segmentBox addSubview:codeBasedSegmentControl];
    [placeHolder5 removeFromSuperview]; // We are done with the place holder, remove it from the window.

    // Use a menu to the first segment (applied to both nib-based and code-based).
    [codeBasedSegmentControl setMenu:self.buttonMenu forSegment:0];
    [nibBasedSegControl setMenu:self.buttonMenu forSegment:0];

    // Add icons to each segment (applied to both nib-based and code-based).
    iconImage = [[NSWorkspace sharedWorkspace] iconForFileType:NSFileTypeForHFSTypeCode(kComputerIcon)];
    iconImage.size = NSMakeSize(16,16);
    [nibBasedSegControl setImage:iconImage forSegment:0];
    [codeBasedSegmentControl setImage:iconImage forSegment:0];
    iconImage = [[NSWorkspace sharedWorkspace] iconForFileType:NSFileTypeForHFSTypeCode(kDesktopIcon)];
    iconImage.size = NSMakeSize(16,16);
    [nibBasedSegControl setImage:iconImage forSegment:1];
    [codeBasedSegmentControl setImage:iconImage forSegment:1];
    iconImage = [[NSWorkspace sharedWorkspace] iconForFileType:NSFileTypeForHFSTypeCode(kFinderIcon)];
    iconImage.size = NSMakeSize(16,16);
    [nibBasedSegControl setImage:iconImage forSegment:2];
    [codeBasedSegmentControl setImage:iconImage forSegment:2];

    //===============================
    // Radio Group (using NSStackView)

    NSButton *buttonRadio1 = [NSButton radioButtonWithTitle:NSLocalizedString(@"Radio 1", "") target:self action:@selector(radioGroupAction:)];
    buttonRadio1.state = NSOnState;
    NSButton *buttonRadio2 = [NSButton radioButtonWithTitle:NSLocalizedString(@"Radio 2", "") target:self action:@selector(radioGroupAction:)];
    NSStackView *stackView = [NSStackView stackViewWithViews:@[buttonRadio1, buttonRadio2]];
    stackView.orientation = NSUserInterfaceLayoutOrientationVertical;
    [placeHolder6 addSubview:stackView];

    // Set the stack view's vertical and horizontal constraints so that it fits inside placeholder6's frame.
    NSDictionary *views = @{@"stackView": stackView};
    [placeHolder6 addConstraints:[NSLayoutConstraint constraintsWithVisualFormat:@"H:|[stackView]|"
                                                                      options:0
                                                                      metrics:0
                                                                        views:views]];
    [placeHolder6 addConstraints:[NSLayoutConstraint constraintsWithVisualFormat:@"V:|[stackView]|"
                                                                      options:0
                                                                      metrics:0
                                                                        views:views]];

    //===============================
    // NSColorWell

    codeBasedColorWell = [[NSColorWell alloc] initWithFrame:placeHolder7.frame];
    codeBasedColorWell.color = [NSColor blueColor];
    [colorBox addSubview:codeBasedColorWell];
    codeBasedColorWell.action = @selector(colorAction:);
    [placeHolder7 removeFromSuperview]; // We are done with the place holder, remove it from the window.

    //===============================
    // NSLevelIndicator

    codeBasedIndicator = [[NSLevelIndicator alloc] initWithFrame:placeHolder8.frame];
    codeBasedIndicator.maxValue = 10;
    codeBasedIndicator.numberOfMajorTickMarks = 4;
    codeBasedIndicator.numberOfTickMarks = 7;
    codeBasedIndicator.warningValue = 5;
    codeBasedIndicator.criticalValue = 8;
    codeBasedIndicator.levelIndicatorStyle = NSDiscreteCapacityLevelIndicatorStyle;
    codeBasedIndicator.action = @selector(levelAction:);

    [indicatorBox addSubview:codeBasedIndicator];
    [placeHolder8 removeFromSuperview]; // We are done with the place holder, remove it from the window.
}


#pragma mark - NSPopUpButton

// -------------------------------------------------------------------------------
//  popupAction:
//
//  User chose a menu item from one of the popups.
//  Note that all four popup buttons share the same action method.
// -------------------------------------------------------------------------------
- (IBAction)popupAction:(id)sender
{
    // Menu item chosen.
}

// -------------------------------------------------------------------------------
//  changePopupState:
//
//  Change the given NSPopupButton as "popup" or "pull down" style.
// -------------------------------------------------------------------------------
- (void)changePopupState:(NSPopUpButton *)popup asPullDown:(BOOL)pullDown
{
    // Hide the button first to invalidate its old size.
    popup.hidden = YES;

    NSRect buttonFrame = popup.frame;

    if (pullDown)
    {
        // Change the button to pull down style.

        // Make the popup a larger square to fit the moof image, and move its origin.
        buttonFrame.size.height += 36;      
        buttonFrame.origin.y -= 36;

        // Update its menu (keep original self.buttonMenu untouched).
        NSMenu *newMenu = [self.buttonMenu copy];

        // Add the image menu item back to the first menu item.
        NSMenuItem *menuItem = [[NSMenuItem alloc] initWithTitle:@"" action:nil keyEquivalent:@""];
        menuItem.image = [NSImage imageNamed:@"moof"];
        [newMenu insertItem:menuItem atIndex:0];

        popup.menu = newMenu;
    }
    else
    {
        // Change the button with a popup style.

        // Shrink the popup down to menu height size and move its origin upwards.
        buttonFrame.size.height -= 36;  
        buttonFrame.origin.y += 36;

        // Update its menu (keep original self.buttonMenu untouched).
        NSMenu *newMenu = [self.buttonMenu copy];
        popup.menu = newMenu;
    }   

    popup.pullsDown = pullDown;

    // Change the button's frame size and make it visible again.
    popup.frame = buttonFrame;
    popup.hidden = NO;
}

// -------------------------------------------------------------------------------
//  pullsDownAction:sender
//
//  User checked "Pull Down" checkbox to change the popup button's appearance:
//      1) as a drop down menu, or 2) as popup menu.
//
//  This is an example on how to change the attributes of these popup buttons,
//  so that they appear correctly.
//
//  If checkbox is not checked:
//      Shrink the button height to appear as a popup button.
//      We also remove the moof image in this casae.
//  If checkbox is checked:
//      Make the button square to fit the moof image.
//      Put back the moof image menu item.
//  
// -------------------------------------------------------------------------------
- (IBAction)pullsDownAction:(id)sender
{
    BOOL pullDown = [[sender selectedCell] state];

    [self changePopupState:codeBasedPopUpDown asPullDown:pullDown];
    [self changePopupState:codeBasedPopUpRight asPullDown:pullDown];

    [self changePopupState:nibBasedPopUpDown asPullDown:pullDown];
    [self changePopupState:nibBasedPopUpRight asPullDown:pullDown];
}


#pragma mark - NSButton

// -------------------------------------------------------------------------------
//  setIconPosition:useIcon
// -------------------------------------------------------------------------------
- (void)setIconPosition:(NSButton*)button useIcon:(BOOL)useIcon
{
    button.imagePosition = useIcon ? NSImageLeft: NSNoImage;
    button.cell.alignment = useIcon ? NSTextAlignmentLeft : NSTextAlignmentCenter;
}

// -------------------------------------------------------------------------------
//  useIconAction:sender
//
//  User checked "Use Icon" checkbox - add or remove the moof icon.
// -------------------------------------------------------------------------------
- (IBAction)useIconAction:(id)sender
{
    BOOL useIcon = [sender cell].state;

    [self setIconPosition:nibBasedButton useIcon:useIcon];
    [self setIconPosition:nibBasedButtonSquare useIcon:useIcon];
    [self setIconPosition:codeBasedButton useIcon:useIcon];
    [self setIconPosition:codeBasedButtonSquare useIcon:useIcon];
}

// -------------------------------------------------------------------------------
//  buttonAction:sender
//
//  User clicked one of the NSButttons.
//  Note that all four buttons share the same action method.
// -------------------------------------------------------------------------------
- (IBAction)buttonAction:(id)sender
{
    NSLog(@"Button was clicked");
}


#pragma mark - NSSegmentedControl

// -------------------------------------------------------------------------------
//  segmentAction:sender
//
//  User clicked one of the segments.
//  Note that both segmented controls share the same action method.
// -------------------------------------------------------------------------------
- (IBAction)segmentAction:(id)sender
{
    // Segment control was clicked: [sender selectedSegment];
}

// -------------------------------------------------------------------------------
//  unselectAction:sender
//
//  User clicked on the button to unselect all segments.
//  Use our category to NSSegmentedControl to unselect the cells.
// -------------------------------------------------------------------------------
- (IBAction)unselectAction:(id)sender
{
    [nibBasedSegControl unselectAllSegments];
    [codeBasedSegmentControl unselectAllSegments];
}


#pragma mark - Radio Groups

// -------------------------------------------------------------------------------
//  radioGroupAction:sender
//
//  User clicked one of the radio buttons in the NSStackView.
// -------------------------------------------------------------------------------
- (IBAction)radioGroupAction:(id)sender
{
    NSLog(@"%@ was clicked", ((NSButton *)sender).title);
}


#pragma mark - NSColorWell

// -------------------------------------------------------------------------------
//  colorAction:sender
//
//  User clicked one of the NSColorWell.
// -------------------------------------------------------------------------------
- (IBAction)colorAction:(id)sender
{
    // User chose a color, use [sender color].
}


#pragma mark - NSLevelIndicator

// -------------------------------------------------------------------------------
//  levelAdjustAction:sender
//
//  User clicked the up/down arrow to adjust the level.
// -------------------------------------------------------------------------------
- (IBAction)levelAdjustAction:(id)sender
{
    // Change level values.
    nibBasedIndicator.integerValue = [sender integerValue];
    codeBasedIndicator.integerValue = [sender integerValue];
}

// -------------------------------------------------------------------------------
//  levelAction:sender
//
//  User clicked on the actual level indicator to change its value.
// -------------------------------------------------------------------------------
- (IBAction)levelAction:(id)sender
{
    // Level clicked, use [sender integerValue].
}

// -------------------------------------------------------------------------------
//  setStyleAction:sender
//
//  User wants to change the level indicator's style.
// -------------------------------------------------------------------------------
- (IBAction)setStyleAction:(id)sender
{
    NSInteger tag = [[sender selectedCell] tag];
    nibBasedIndicator.levelIndicatorStyle = tag;
    codeBasedIndicator.levelIndicatorStyle = tag;
}


#pragma mark - DropDownButton

// -------------------------------------------------------------------------------
//  dropDownAction:sender
//
//  User clicked the DropDownButton.
// -------------------------------------------------------------------------------
- (IBAction)dropDownAction:(id)sender
{
    // Drop down button clicked.
}

@end
```

[Next](ButtonMadness-DropDownButton.m.md)[Previous](ButtonMadness-AppDelegate.h.md)

