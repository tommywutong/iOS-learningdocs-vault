---
title: 'TableViewPlayground: Using View-Based NSTableView and NSOutlineView'
apple_id: DTS40010727
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-04-14'
source_url: https://developer.apple.com/library/archive/samplecode/TableViewPlayground/Listings/TableViewPlayground_ATTableCellView_m.html
archived_at: '2026-07-18T03:26:14.272470Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TableViewPlayground: Using View-Based NSTableView and NSOutlineView](TableViewPlayground-%20Using%20View-Based%20NSTableView%20and%20NSOutlineView.md)


[Next](TableViewPlayground-ATMainWindowController.h.md)[Previous](TableViewPlayground-ATDesktopEntity.h.md)

# TableViewPlayground/ATTableCellView.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A basic subclass of NSTableCellView that adds some properties strictly for allowing access to the items in code.
 */

#import "ATTableCellView.h"
#import "ATColorView.h"

@interface ATTableCellView ()

@property (assign) BOOL isSmallSize;
@property (weak) IBOutlet NSButton *removeButton;

@end


#pragma mark -

@implementation ATTableCellView

- (void)layoutViewsForSmallSize:(BOOL)smallSize animated:(BOOL)animated {
    if (self.isSmallSize != smallSize) {
        _isSmallSize = smallSize;
        CGFloat targetAlpha = self.isSmallSize ? 0 : 1;
        if (animated) {
            self.removeButton.animator.alphaValue = targetAlpha;
            self.colorView.animator.alphaValue = targetAlpha;
            self.subTitleTextField.animator.alphaValue = targetAlpha;
        } else {
            self.removeButton.alphaValue = targetAlpha;
            self.colorView.alphaValue = targetAlpha;
            self.subTitleTextField.alphaValue = targetAlpha;
        }
    }
}

- (NSArray *)draggingImageComponents {
    // Start with what is already there (this is an image and text component).
    NSMutableArray *result = [super.draggingImageComponents mutableCopy];

    // Snapshot the color view and add it in.
    NSRect viewBounds = self.colorView.bounds;
    NSBitmapImageRep *imageRep = [self.colorView bitmapImageRepForCachingDisplayInRect:viewBounds];
    [self.colorView cacheDisplayInRect:viewBounds toBitmapImageRep:imageRep];

    NSImage *draggedImage = [[NSImage alloc] initWithSize:imageRep.size];
    [draggedImage addRepresentation:imageRep];

    // Add in another component.
    NSDraggingImageComponent *colorComponent = [NSDraggingImageComponent draggingImageComponentWithKey:@"Color"];
    colorComponent.contents = draggedImage;

    // Convert the frame to our coordinate system.
    viewBounds = [self convertRect:viewBounds fromView:self.colorView];
    colorComponent.frame = viewBounds;

    [result addObject:colorComponent];
    return result;
}

@end
```

[Next](TableViewPlayground-ATMainWindowController.h.md)[Previous](TableViewPlayground-ATDesktopEntity.h.md)

