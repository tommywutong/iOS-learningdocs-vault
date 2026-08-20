---
title: TheElements
apple_id: DTS40007419
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: null
published: '2015-08-25'
source_url: https://developer.apple.com/library/archive/samplecode/TheElements/Listings/Classes_AtomicElementView_h.html
archived_at: '2026-07-18T03:26:45.575903Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TheElements](TheElements.md)


[Next](Classes-ElementsSortedByStateDataSource.h.md)[Previous](Classes-ElementsSortedByAtomicNumberDataSource.h.md)

# Classes/AtomicElementView.h

```objc
/*
Copyright (C) 2015 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Displays the Atomic Element information in a large format tile.
*/

@import UIKit;

@class AtomicElement;
@class AtomicElementViewController;

@interface AtomicElementView : UIView

@property (nonatomic,strong) AtomicElement *element;
@property (nonatomic, weak) AtomicElementViewController *viewController;

+ (CGSize)preferredViewSize;
- (UIImage *)reflectedImageRepresentationWithHeight:(NSUInteger)height;

@end
```

[Next](Classes-ElementsSortedByStateDataSource.h.md)[Previous](Classes-ElementsSortedByAtomicNumberDataSource.h.md)

