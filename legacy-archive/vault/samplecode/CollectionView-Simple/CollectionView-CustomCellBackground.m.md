---
title: CollectionView-Simple
apple_id: DTS40012860
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2015-10-22'
source_url: https://developer.apple.com/library/archive/samplecode/CollectionView-Simple/Listings/CollectionView_CustomCellBackground_m.html
archived_at: '2026-07-18T03:03:52.161191Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CollectionView-Simple](CollectionView-Simple.md)


[Next](Document%20Revision%20History.md)[Previous](CollectionView-DetailViewController.m.md)

# CollectionView/CustomCellBackground.m

```objc
/*
Copyright (C) 2015 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Custom UIView to draw a rounded blue box to represent a selected cell.
*/

#import "CustomCellBackground.h"

@implementation CustomCellBackground

- (void)drawRect:(CGRect)rect
{
    // draw a rounded rect bezier path filled with blue
    CGContextRef aRef = UIGraphicsGetCurrentContext();
    CGContextSaveGState(aRef);
    UIBezierPath *bezierPath = [UIBezierPath bezierPathWithRoundedRect:rect cornerRadius:5.0f];
    bezierPath.lineWidth = 5.0f;
    [[UIColor blackColor] setStroke];

    UIColor *fillColor = [UIColor colorWithRed:0.529 green:0.808 blue:0.922 alpha:1]; // color equivalent is #87ceeb
    [fillColor setFill];

    [bezierPath stroke];
    [bezierPath fill];
    CGContextRestoreGState(aRef);
}

@end
```

[Next](Document%20Revision%20History.md)[Previous](CollectionView-DetailViewController.m.md)

