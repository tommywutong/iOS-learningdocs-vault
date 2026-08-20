---
title: 'HelloGoodbye: Using the Accessibility API to Widen Your User Base'
apple_id: TP40014593
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/HelloGoodbye/Listings/HelloGoodbye_AAPLAgeSlider_m.html
archived_at: '2026-07-18T03:11:49.588261Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [HelloGoodbye: Using the Accessibility API to Widen Your User Base](HelloGoodbye-%20Using%20the%20Accessibility%20API%20to%20Widen%20Your%20User%20Base.md)


[Next](HelloGoodbye-AAPLAppDelegate.h.md)[Previous](HelloGoodbye-AAPLMatchesViewController.m.md)

# HelloGoodbye/AAPLAgeSlider.m

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:

  A custom slider that allows users to adjust their age.

 */

#import "AAPLAgeSlider.h"
#import "AAPLStyleUtilities.h"

@implementation AAPLAgeSlider

- (instancetype)initWithFrame:(CGRect)frame {
    self = [super initWithFrame:frame];
    if (self) {
        self.tintColor = [AAPLStyleUtilities foregroundColor];
        self.minimumValue = 18;
        self.maximumValue = 120;
    }
    return self;
}

- (NSString *)accessibilityValue {
    // Return the age as a number, not as a percentage
    return [NSNumberFormatter localizedStringFromNumber:@(self.value) numberStyle:NSNumberFormatterDecimalStyle];
}

- (void)accessibilityIncrement {
    self.value++;
    [self sendActionsForControlEvents:UIControlEventValueChanged];
}

- (void)accessibilityDecrement {
    self.value--;
    [self sendActionsForControlEvents:UIControlEventValueChanged];
}

@end
```

[Next](HelloGoodbye-AAPLAppDelegate.h.md)[Previous](HelloGoodbye-AAPLMatchesViewController.m.md)

