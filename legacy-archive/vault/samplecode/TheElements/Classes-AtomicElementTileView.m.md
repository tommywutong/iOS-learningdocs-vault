---
title: TheElements
apple_id: DTS40007419
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: null
published: '2015-08-25'
source_url: https://developer.apple.com/library/archive/samplecode/TheElements/Listings/Classes_AtomicElementTileView_m.html
archived_at: '2026-07-18T03:26:45.418037Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TheElements](TheElements.md)


[Next](Classes-AtomicElement.h.md)[Previous](Classes-ElementsSortedBySymbolDataSource.h.md)

# Classes/AtomicElementTileView.m

```objc
/*
Copyright (C) 2015 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Draws the small tile view displayed in the tableview rows.
*/


#import "AtomicElementTileView.h"
#import "AtomicElement.h"


@implementation AtomicElementTileView

- (instancetype)initWithFrame:(CGRect)frame {

    if (self = [super initWithFrame:frame]) {
        _element = nil;
    }
    return self;
}

- (void)drawRect:(CGRect)rect {

    CGPoint point;

    // get the image that represents the element physical state and draw it
    UIImage *backgroundImage = self.element.stateImageForAtomicElementTileView;
    CGRect elementSymbolRectangle = CGRectMake(0,0, [backgroundImage size].width, [backgroundImage size].height);
    [backgroundImage drawInRect:elementSymbolRectangle];

    [[UIColor whiteColor] set];

    // draw the element number
    NSDictionary *font = @{NSFontAttributeName: [UIFont boldSystemFontOfSize:11]};
    point = CGPointMake(3,2);
    [[self.element.atomicNumber stringValue] drawAtPoint:point withAttributes:font];

    // draw the element symbol
    font = @{NSFontAttributeName: [UIFont boldSystemFontOfSize:18]};
    CGSize stringSize = [self.element.symbol sizeWithAttributes:font];
    point = CGPointMake((elementSymbolRectangle.size.width-stringSize.width)/2, 14.0);

    [self.element.symbol drawAtPoint:point withAttributes:font];
}

@end
```

[Next](Classes-AtomicElement.h.md)[Previous](Classes-ElementsSortedBySymbolDataSource.h.md)

