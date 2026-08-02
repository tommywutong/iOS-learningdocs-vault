---
title: 'HelloGoodbye: Using the Accessibility API to Widen Your User Base'
apple_id: TP40014593
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/HelloGoodbye/Listings/HelloGoodbye_AAPLStyleUtilities_h.html
archived_at: '2026-07-18T03:11:50.632203Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [HelloGoodbye: Using the Accessibility API to Widen Your User Base](HelloGoodbye-%20Using%20the%20Accessibility%20API%20to%20Widen%20Your%20User%20Base.md)


[Next](HelloGoodbye-AAPLPhotoBackgroundViewController.m.md)[Previous](HelloGoodbye-AAPLPhotoBackgroundViewController.h.md)

# HelloGoodbye/AAPLStyleUtilities.h

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:

  A collection of methods related to the look and feel of the application.

 */

@import UIKit;

@interface AAPLStyleUtilities : NSObject

+ (UIColor *)foregroundColor;
+ (UIColor *)overlayColor;
+ (UIColor *)cardBorderColor;
+ (UIColor *)cardBackgroundColor;
+ (UIColor *)detailColor;
+ (UIColor *)detailOnOverlayColor;
+ (UIColor *)detailOnOverlayPlaceholderColor;
+ (UIColor *)previewTabLabelColor;
+ (CGFloat)overlayCornerRadius;
+ (CGFloat)overlayMargin;
+ (CGFloat)contentVerticalMargin;
+ (CGFloat)contentHorizontalMargin;
+ (UIImage *)overlayRoundedRectImage;
+ (UIButton *)overlayRoundedRectButton;
+ (UIFont *)standardFont;
+ (UIFont *)largeFont;
+ (UILabel *)standardLabel;
+ (UILabel *)detailLabel;

@end
```

[Next](HelloGoodbye-AAPLPhotoBackgroundViewController.m.md)[Previous](HelloGoodbye-AAPLPhotoBackgroundViewController.h.md)

