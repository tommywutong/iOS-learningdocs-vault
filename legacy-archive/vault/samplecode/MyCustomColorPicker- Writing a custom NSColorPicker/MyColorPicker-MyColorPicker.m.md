---
title: 'MyCustomColorPicker: Writing a custom NSColorPicker'
apple_id: DTS10004111
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: AppKit
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/MyCustomColorPicker/Listings/MyColorPicker_MyColorPicker_m.html
archived_at: '2026-07-18T03:16:34.435079Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MyCustomColorPicker: Writing a custom NSColorPicker](MyCustomColorPicker-%20Writing%20a%20custom%20NSColorPicker.md)


[Next](MyColorPicker-MyColorPicker.h.md)[Previous](TestHost-main.m.md)

# MyColorPicker/MyColorPicker.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Custom NSColorPicker plugin.
 */

#import "MyColorPicker.h"

// Defined control tags for each color radio button.
typedef NS_ENUM(NSInteger, ColorTagType) {
    RedTag = 1,
    GreenTag,
    BlueTag,
    WhiteTag,
    OtherTag
};


#pragma mark -

@interface MyColorPicker ()

@property (weak) IBOutlet NSView  *colorPickerView;
@property (strong) IBOutlet NSPanel *colorPickerPrefs;

@end


#pragma mark -

@implementation MyColorPicker

#pragma mark - NSColorPickingDefault

// The adopted protocol to return our picker icon which is displayed in the NSColorPanel.
- (NSImage *)provideNewButtonImage
{
    NSImage *image = [[NSImage alloc] initWithContentsOfFile:
                        [[NSBundle bundleForClass:[self class]] pathForResource:@"icon" ofType:@"tiff"]];
    [image setSize:NSMakeSize(32.0,32.0)];

    return image;
}

// Provide a tooltip for our color picker icon in the NSColorPanel.
- (NSString *)buttonToolTip
{
    return @"MyColorPicker";
}

// Provide a description string for our color picker.
- (NSString *)description
{
    return NSLocalizedString(@"MyColorPicker - A simple RGB color picker", @"");
}


#pragma mark - NSColorPickingCustom

// You build your own custom color picker as a bundle by subclassing NSColorPicker and adopting the NSColorPickingCustom protocol.
// MyColorPicker is launched by adopting the NSColorPickingCustom's protocol -
//
- (NSView*)provideNewView:(BOOL)initialRequest
{
    // the param "initialRequest" is YES on the very first call, at that moment
    // you ask your NSBundle to load its nib.
    //
    if (initialRequest)
    {
        [[NSBundle bundleWithIdentifier:@"com.apple.MyColorpicker"] loadNibNamed:@"MyColorPicker" owner:self topLevelObjects:nil];
    }

    return self.colorPickerView;
}

// Determine which picking color mode we support (used by the NSColorPanel).
- (BOOL)supportsMode:(NSColorPanelMode)mode
{
    return YES; // we support all modes
}

// Return our current color picker mode (used by the NSColorPanel).
- (NSColorPanelMode)currentMode
{
    return NSColorPanelModeRGB;
}

- (void)setColor:(NSColor *)color
{
    //..
}


#pragma mark - Color Selection

// Map a specific radio button tag to an NSColor.
- (NSColor *)tagToColor:(NSInteger)tag
{
    NSColor *color = nil;
    switch (tag)
    {
        case RedTag:    // red
            color = [NSColor redColor];
            break;

        case GreenTag:  // green
            color = [NSColor greenColor];
            break;

        case BlueTag:   // blue
            color = [NSColor blueColor];
            break;

        case WhiteTag: // white
            color = [NSColor whiteColor];
            break;

        case OtherTag:  // other (default gray)
            color = [NSColor lightGrayColor];
            break;
    }

    return color;
}


#pragma mark - Actions

// User chose a particular color from one of the radio buttons.
- (IBAction)colorChanged:(id)sender
{
    NSColor *color = [self tagToColor:((NSButton *)sender).tag];
    [[self colorPanel] setColor:color];
}

// User clicked the preferences button.
- (IBAction)showPrefs:(id)sender
{
    [self.colorPickerView.window beginSheet:self.colorPickerPrefs completionHandler:nil];
}

// User clicked the OK button from preferences.
- (IBAction)finishPrefs:(id)sender
{
    [self.colorPickerPrefs orderOut:self];
}

@end
```

[Next](MyColorPicker-MyColorPicker.h.md)[Previous](TestHost-main.m.md)

