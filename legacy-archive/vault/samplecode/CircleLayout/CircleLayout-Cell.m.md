---
title: CircleLayout
apple_id: DTS40012315
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2015-07-31'
source_url: https://developer.apple.com/library/archive/samplecode/CircleLayout/Listings/CircleLayout_Cell_m.html
archived_at: '2026-07-18T03:03:20.202382Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CircleLayout](CircleLayout.md)


[Next](CircleLayout-AppDelegate.h.md)[Previous](CircleLayout-ViewController.m.md)

# CircleLayout/Cell.m

```objc
/*
Copyright (C) 2015 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Custom collection view cell for a blue dot.
*/

#import "Cell.h"

@implementation Cell

- (instancetype)initWithFrame:(CGRect)frame
{
    self = [super initWithFrame:frame];
    if (self) {
        self.contentView.layer.cornerRadius = 35.0;
        self.contentView.layer.borderWidth = 1.0f;
        self.contentView.layer.borderColor = [UIColor whiteColor].CGColor;
        self.contentView.backgroundColor = [UIColor blueColor];
    }
    return self;
}

@end
```

[Next](CircleLayout-AppDelegate.h.md)[Previous](CircleLayout-ViewController.m.md)

