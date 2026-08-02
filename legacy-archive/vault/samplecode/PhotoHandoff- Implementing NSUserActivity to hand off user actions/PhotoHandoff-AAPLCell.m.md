---
title: 'PhotoHandoff: Implementing NSUserActivity to hand off user actions'
apple_id: TP40014785
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoHandoff/Listings/PhotoHandoff_AAPLCell_m.html
archived_at: '2026-07-18T03:18:50.249153Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoHandoff: Implementing NSUserActivity to hand off user actions](PhotoHandoff-%20Implementing%20NSUserActivity%20to%20hand%20off%20user%20actions.md)


[Next](Document%20Revision%20History.md)[Previous](PhotoHandoff-AAPLCell.h.md)

# PhotoHandoff/AAPLCell.m

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 */

#import "AAPLCell.h"
#import "AAPLCustomCellBackground.h"

@interface AAPLCell ()
@property (nonatomic, strong) UIColor *labelColor;
@end


#pragma mark -

@implementation AAPLCell

- (instancetype)initWithCoder:(NSCoder *)aDecoder {

    self = [super initWithCoder:aDecoder];
    if (self) {
        self.selectedBackgroundView = [[AAPLCustomCellBackground customCellBackground] init];
    }
    return self;
}

- (void)setSelected:(BOOL)selected {

    [super setSelected:selected];
    if (selected) {
        _labelColor = self.label.textColor;
        self.label.textColor = [UIColor blackColor];
        [self setNeedsDisplay];
    }
    else {
        if (self.labelColor)
            self.label.textColor = self.labelColor;
    }
}

- (void)setHighlighted:(BOOL)highlighted {

    [super setHighlighted:highlighted];
    if (highlighted) {
        _labelColor = self.label.textColor;
        self.label.textColor = [UIColor blackColor];
        [self setNeedsDisplay];
    }
    else {
        if (self.labelColor)
            self.label.textColor = self.labelColor;
    }
}

@end
```

[Next](Document%20Revision%20History.md)[Previous](PhotoHandoff-AAPLCell.h.md)

