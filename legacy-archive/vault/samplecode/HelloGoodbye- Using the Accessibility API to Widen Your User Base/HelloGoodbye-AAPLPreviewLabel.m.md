---
title: 'HelloGoodbye: Using the Accessibility API to Widen Your User Base'
apple_id: TP40014593
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/HelloGoodbye/Listings/HelloGoodbye_AAPLPreviewLabel_m.html
archived_at: '2026-07-18T03:11:50.320345Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [HelloGoodbye: Using the Accessibility API to Widen Your User Base](HelloGoodbye-%20Using%20the%20Accessibility%20API%20to%20Widen%20Your%20User%20Base.md)


[Next](HelloGoodbye-AAPLProfileViewController.h.md)[Previous](LICENSE.txt.md)

# HelloGoodbye/AAPLPreviewLabel.m

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:

  A custom label that appears on the Preview tab in the profile view controller.

 */

#import "AAPLPreviewLabel.h"
#import "AAPLStyleUtilities.h"

@implementation AAPLPreviewLabel

- (instancetype)initWithFrame:(CGRect)frame {
    self = [super initWithFrame:frame];
    if (self) {
        self.text = NSLocalizedString(@"Preview", @"Name of the card preview tab");
        self.font = [AAPLStyleUtilities largeFont];
        self.textColor = [AAPLStyleUtilities previewTabLabelColor];
    }
    return self;
}

- (BOOL)accessibilityActivate {
    [self.delegate didActivatePreviewLabel:self];
    return YES;
}

- (UIAccessibilityTraits)accessibilityTraits {
    return ([super accessibilityTraits] | UIAccessibilityTraitButton);
}

@end
```

[Next](HelloGoodbye-AAPLProfileViewController.h.md)[Previous](LICENSE.txt.md)

