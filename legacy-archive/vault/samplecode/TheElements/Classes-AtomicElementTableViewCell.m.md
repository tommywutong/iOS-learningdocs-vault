---
title: TheElements
apple_id: DTS40007419
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: null
published: '2015-08-25'
source_url: https://developer.apple.com/library/archive/samplecode/TheElements/Listings/Classes_AtomicElementTableViewCell_m.html
archived_at: '2026-07-18T03:26:45.345656Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TheElements](TheElements.md)


[Next](Classes-TheElementsAppDelegate.h.md)[Previous](Classes-ElementsSortedByAtomicNumberDataSource.m.md)

# Classes/AtomicElementTableViewCell.m

```objc
/*
Copyright (C) 2015 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Draws the tableview cell and lays out the subviews.
*/


#import "AtomicElementTableViewCell.h"
#import "AtomicElement.h"
#import "AtomicElementTileView.h"

@implementation AtomicElementTableViewCell

// the element setter
// we implement this because the table cell values need to be updated when this property
// changes, and this allows for the changes to be encapsulated
//
- (void)setElement:(AtomicElement *)anElement {

    if (anElement != _element) {
        _element = anElement;
    }

    AtomicElementTileView *elementTileView = (AtomicElementTileView *)[self.contentView viewWithTag:1];
    elementTileView.element = _element;

    UILabel *labelView = (UILabel *)[self.contentView viewWithTag:2];
    labelView.text = _element.name;

    [elementTileView setNeedsDisplay];
    [labelView setNeedsDisplay];
}

@end
```

[Next](Classes-TheElementsAppDelegate.h.md)[Previous](Classes-ElementsSortedByAtomicNumberDataSource.m.md)

