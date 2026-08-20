---
title: 'CocoaSlideCollection: Using NSCollectionView on OS X 10.11'
apple_id: TP40016149
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/CocoaSlideCollection/Listings/CocoaSlideCollection_View_AAPLSlideTableBackgroundView_m.html
archived_at: '2026-07-18T03:03:44.360354Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CocoaSlideCollection: Using NSCollectionView on OS X 10.11](CocoaSlideCollection-%20Using%20NSCollectionView%20on%20OS%20X%2010.11.md)


[Next](CocoaSlideCollection-View-AAPLSlideBorderView.h.md)[Previous](CocoaSlideCollection-View-AAPLFooterView.h.md)

# CocoaSlideCollection/View/AAPLSlideTableBackgroundView.m

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This is the "SlideTableBackgroundView" class implementation.
*/

#import "AAPLSlideTableBackgroundView.h"

@implementation AAPLSlideTableBackgroundView

- (instancetype)initWithFrame:(NSRect)frameRect {
    self = [super initWithFrame:frameRect];
    if (self) {
        NSColor *centerColor = [NSColor colorWithCalibratedRed:0.94 green:0.99 blue:0.98 alpha:1.0];
        NSColor *outerColor = [NSColor colorWithCalibratedRed:0.91 green:1.0 blue:0.98 alpha:1.0];
        gradient = [[NSGradient alloc] initWithStartingColor:centerColor endingColor:outerColor];
    }
    return self;
}

- (BOOL)isOpaque {
    return YES;
}

- (NSImage *)image {
    return image;
}

- (void)setImage:(NSImage *)newImage {
    if (image != newImage) {
        image = newImage;
        [self setNeedsDisplay:YES];
    }
}

- (void)drawRect:(NSRect)dirtyRect {
    if (image) {
        // Draw an image, scaled proportionally to fill the view's entire bounds.
        NSSize imageSize = image.size;
        NSRect bounds = self.bounds;
        CGFloat scaleToFillWidth = bounds.size.width / imageSize.width;
        CGFloat scaleToFillHeight = bounds.size.height / imageSize.height;

        // Choose the greater of the scale factor required to fill the view's width, and the scale factor required to fill the view's height, and compute the destination rect accordingly.
        NSRect destRect;
        if (scaleToFillWidth > scaleToFillHeight) {
            destRect = NSMakeRect(bounds.origin.x, NSMidY(bounds) - 0.5 * scaleToFillWidth * imageSize.height, bounds.size.width, scaleToFillWidth * imageSize.height);
        } else {
            destRect = NSMakeRect(NSMidX(bounds) - 0.5 * scaleToFillHeight * imageSize.width, bounds.origin.y, scaleToFillHeight * imageSize.width, bounds.size.height);
        }
        [image drawInRect:destRect fromRect:NSMakeRect(0, 0, imageSize.width, imageSize.height) operation:NSCompositeSourceOver fraction:1.0];
    } else {
        // Draw a slight radial gradient.
        [gradient drawInRect:self.bounds relativeCenterPosition:NSZeroPoint];
    }
}

@end
```

[Next](CocoaSlideCollection-View-AAPLSlideBorderView.h.md)[Previous](CocoaSlideCollection-View-AAPLFooterView.h.md)

