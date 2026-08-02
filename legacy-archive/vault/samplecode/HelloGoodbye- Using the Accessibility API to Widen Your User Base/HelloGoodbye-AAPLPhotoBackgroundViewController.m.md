---
title: 'HelloGoodbye: Using the Accessibility API to Widen Your User Base'
apple_id: TP40014593
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/HelloGoodbye/Listings/HelloGoodbye_AAPLPhotoBackgroundViewController_m.html
archived_at: '2026-07-18T03:11:50.213086Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [HelloGoodbye: Using the Accessibility API to Widen Your User Base](HelloGoodbye-%20Using%20the%20Accessibility%20API%20to%20Widen%20Your%20User%20Base.md)


[Next](HelloGoodbye-AAPLCardView.m.md)[Previous](HelloGoodbye-AAPLStyleUtilities.h.md)

# HelloGoodbye/AAPLPhotoBackgroundViewController.m

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:

  A view controller that uses a photo as a background image.

 */

#import "AAPLPhotoBackgroundViewController.h"

@interface AAPLPhotoBackgroundViewController ()

@property (nonatomic, strong) UIImageView *backgroundView;

@end

@implementation AAPLPhotoBackgroundViewController

- (void)loadView {
    UIView *containerView = [[UIView alloc] init];
    containerView.clipsToBounds = YES;

    self.backgroundView = [[UIImageView alloc] initWithImage:self.backgroundImage];
    [containerView addSubview:self.backgroundView];

    self.view = containerView;
}

- (void)viewWillLayoutSubviews {
    CGRect bounds = self.view.bounds;
    CGSize imageSize = self.backgroundView.image.size;
    CGFloat imageAspectRatio = imageSize.width / imageSize.height;
    CGFloat viewAspectRatio = CGRectGetWidth(bounds) / CGRectGetHeight(bounds);
    if (viewAspectRatio > imageAspectRatio) {
        // Let the background run off the top and bottom of the screen, so it fills the width
        CGSize scaledSize = CGSizeMake(CGRectGetWidth(bounds), CGRectGetWidth(bounds) / imageAspectRatio);
        self.backgroundView.frame = CGRectMake(0.0, (CGRectGetHeight(bounds) - scaledSize.height) / 2.0, scaledSize.width, scaledSize.height);
    } else {
        // Let the background run off the left and right of the screen, so it fills the height
        CGSize scaledSize = CGSizeMake(imageAspectRatio * CGRectGetHeight(bounds), CGRectGetHeight(bounds));
        self.backgroundView.frame = CGRectMake((CGRectGetWidth(bounds) - scaledSize.width) / 2.0, 0.0, scaledSize.width, scaledSize.height);
    }
}

- (void)setBackgroundImage:(UIImage *)backgroundImage {
    if (_backgroundImage != backgroundImage) {
        _backgroundImage = backgroundImage;
        self.backgroundView.image = backgroundImage;
    }
}

@end
```

[Next](HelloGoodbye-AAPLCardView.m.md)[Previous](HelloGoodbye-AAPLStyleUtilities.h.md)

