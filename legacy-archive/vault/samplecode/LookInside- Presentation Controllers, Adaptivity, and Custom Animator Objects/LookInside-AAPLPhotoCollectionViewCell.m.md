---
title: 'LookInside: Presentation Controllers, Adaptivity, and Custom Animator Objects'
apple_id: TP40014643
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/LookInside/Listings/LookInside_AAPLPhotoCollectionViewCell_m.html
archived_at: '2026-07-18T03:13:49.594239Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LookInside: Presentation Controllers, Adaptivity, and Custom Animator Objects](LookInside-%20Presentation%20Controllers%2C%20Adaptivity%2C%20and%20Custom%20Animator%20Objects.md)


[Next](LookInside-AAPLRootViewController.h.md)[Previous](LookInside-AAPLOverlayViewController.m.md)

# LookInside/AAPLPhotoCollectionViewCell.m

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:

  AAPLPhotoCollectionViewCell implementation.

 */

#import "AAPLPhotoCollectionViewCell.h"

@implementation AAPLPhotoCollectionViewCell

- (instancetype)initWithFrame:(CGRect)frameRect
{
    self = [super initWithFrame:frameRect];
    if (self)
    {
        _imageView = [[UIImageView alloc] init];
        [[self imageView] setContentMode:UIViewContentModeScaleAspectFill];

        [[self contentView] addSubview:[self imageView]];
        [[self contentView] setClipsToBounds:YES];
    }
    return self;
}

- (void)layoutSubviews
{
    [super layoutSubviews];
    [[self imageView] setFrame:[[self contentView] bounds]];
}

- (void)setImage:(UIImage *)image
{
    [[self imageView] setImage:image];
}

- (UIImage *)image
{
    return [[self imageView] image];
}

@end
```

[Next](LookInside-AAPLRootViewController.h.md)[Previous](LookInside-AAPLOverlayViewController.m.md)

