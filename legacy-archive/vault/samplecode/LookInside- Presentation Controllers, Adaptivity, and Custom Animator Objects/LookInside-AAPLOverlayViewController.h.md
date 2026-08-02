---
title: 'LookInside: Presentation Controllers, Adaptivity, and Custom Animator Objects'
apple_id: TP40014643
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/LookInside/Listings/LookInside_AAPLOverlayViewController_h.html
archived_at: '2026-07-18T03:13:49.406420Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LookInside: Presentation Controllers, Adaptivity, and Custom Animator Objects](LookInside-%20Presentation%20Controllers%2C%20Adaptivity%2C%20and%20Custom%20Animator%20Objects.md)


[Next](LookInside-AAPLOverlayPresentationController.h.md)[Previous](LookInside-AAPLPhotoCollectionViewCell.h.md)

# LookInside/AAPLOverlayViewController.h

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:

  AAPLOverlayViewController header.

 */

@import UIKit;
#import "AAPLPhotoCollectionViewCell.h"

@interface AAPLOverlayVibrantLabel : UILabel
@end

@interface AAPLOverlayViewController : UIViewController
{
    AAPLPhotoCollectionViewCell* _photoView;
}

@property (nonatomic) UIVisualEffectView *backgroundView;
@property (nonatomic) UIVisualEffectView *foregroundContentView;

@property (nonatomic) UIScrollView *foregroundContentScrollView;

@property (nonatomic) UIBlurEffect *blurEffect;
@property (nonatomic) UIImageView *imageView;

@property (nonatomic) AAPLOverlayVibrantLabel *hueLabel;
@property (nonatomic) UISlider *hueSlider;

@property (nonatomic) AAPLOverlayVibrantLabel *saturationLabel;
@property (nonatomic) UISlider *saturationSlider;

@property (nonatomic) AAPLOverlayVibrantLabel *brightnessLabel;
@property (nonatomic) UISlider *brightnessSlider;

@property (nonatomic) UIButton *saveButton;
@property (nonatomic) AAPLPhotoCollectionViewCell *photoView;

@end
```

[Next](LookInside-AAPLOverlayPresentationController.h.md)[Previous](LookInside-AAPLPhotoCollectionViewCell.h.md)

