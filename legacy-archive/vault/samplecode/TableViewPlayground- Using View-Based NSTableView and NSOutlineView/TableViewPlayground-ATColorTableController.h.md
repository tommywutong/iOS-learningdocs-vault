---
title: 'TableViewPlayground: Using View-Based NSTableView and NSOutlineView'
apple_id: DTS40010727
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-04-14'
source_url: https://developer.apple.com/library/archive/samplecode/TableViewPlayground/Listings/TableViewPlayground_ATColorTableController_h.html
archived_at: '2026-07-18T03:26:13.163066Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TableViewPlayground: Using View-Based NSTableView and NSOutlineView](TableViewPlayground-%20Using%20View-Based%20NSTableView%20and%20NSOutlineView.md)


[Next](TableViewPlayground-ATObjectTableRowView.h.md)[Previous](TableViewPlayground-ATMainWindowController.h.md)

# TableViewPlayground/ATColorTableController.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A controller used by the ATColorTableController to edit the color property.
 */

@import Cocoa;

@protocol ATColorTableControllerDelegate;

@interface ATColorTableController : NSViewController {

    id <ATColorTableControllerDelegate> __unsafe_unretained _delegate;
}

+ (ATColorTableController *)sharedColorTableController;

- (void)editColor:(NSColor *)color withPositioningView:(NSView *)view;

@property (weak, readonly) NSColor *selectedColor;
@property (weak, readonly) NSString *selectedColorName;

@property(unsafe_unretained) id <ATColorTableControllerDelegate> delegate;

@end


#pragma mark -

@protocol ATColorTableControllerDelegate <NSObject>

@optional
- (void)colorTableController:(ATColorTableController *)controller didChooseColor:(NSColor *)color named:(NSString *)colorName;
@end
```

[Next](TableViewPlayground-ATObjectTableRowView.h.md)[Previous](TableViewPlayground-ATMainWindowController.h.md)

