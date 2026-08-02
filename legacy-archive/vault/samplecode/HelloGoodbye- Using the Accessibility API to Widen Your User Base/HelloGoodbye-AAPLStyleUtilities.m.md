---
title: 'HelloGoodbye: Using the Accessibility API to Widen Your User Base'
apple_id: TP40014593
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/HelloGoodbye/Listings/HelloGoodbye_AAPLStyleUtilities_m.html
archived_at: '2026-07-18T03:11:50.684184Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [HelloGoodbye: Using the Accessibility API to Widen Your User Base](HelloGoodbye-%20Using%20the%20Accessibility%20API%20to%20Widen%20Your%20User%20Base.md)


[Next](HelloGoodbye-AAPLProfileViewController.m.md)[Previous](HelloGoodbye-AAPLStartViewController.m.md)

# HelloGoodbye/AAPLStyleUtilities.m

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:

  A collection of methods related to the look and feel of the application.

 */

#import "AAPLStyleUtilities.h"

static const CGFloat AAPLOverlayCornerRadius = 10.0;
static const CGFloat AAPLButtonVerticalContentInset = 10.0;
static const CGFloat AAPLButtonHorizontalContentInset = 10.0;
static const CGFloat AAPLOverlayMargin = 20.0;
static const CGFloat AAPLContentVerticalMargin = 50.0;
static const CGFloat AAPLContentHorizontalMargin = 30.0;

@implementation AAPLStyleUtilities

+ (UIColor *)foregroundColor {
    return [UIColor colorWithRed:75.0/255 green:35.0/255 blue:106.0/255 alpha:1.0];
}

+ (UIColor *)overlayColor {
    if (UIAccessibilityIsReduceTransparencyEnabled()) {
        return [UIColor whiteColor];
    }
    return [UIColor colorWithWhite:1.0 alpha:0.8];
}

+ (UIColor *)cardBorderColor {
    return [self foregroundColor];
}

+ (UIColor *)cardBackgroundColor {
    return [UIColor whiteColor];
}

+ (UIColor *)detailColor {
    if (UIAccessibilityDarkerSystemColorsEnabled()) {
        return [UIColor blackColor];
    }
    return [UIColor grayColor];
}

+ (UIColor *)detailOnOverlayColor {
    return [UIColor blackColor];
}

+ (UIColor *)detailOnOverlayPlaceholderColor {
    return [UIColor darkGrayColor];
}

+ (UIColor *)previewTabLabelColor {
    return [UIColor whiteColor];
}

+ (CGFloat)overlayCornerRadius {
    return AAPLOverlayCornerRadius;
}

+ (CGFloat)overlayMargin {
    return AAPLOverlayMargin;
}

+ (CGFloat)contentHorizontalMargin {
    return AAPLContentHorizontalMargin;
}

+ (CGFloat)contentVerticalMargin {
    return AAPLContentVerticalMargin;
}

+ (UIImage *)overlayRoundedRectImage {
    static UIImage *roundedRectImage = nil;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        CGSize imageSize = CGSizeMake(2 * AAPLOverlayCornerRadius, 2 * AAPLOverlayCornerRadius);
        UIGraphicsBeginImageContextWithOptions(imageSize, NO, [[UIScreen mainScreen] scale]);

        UIBezierPath *roundedRect = [UIBezierPath bezierPathWithRoundedRect:CGRectMake(0.0, 0.0, imageSize.width, imageSize.height) cornerRadius:AAPLOverlayCornerRadius];
        [[self overlayColor] set];
        [roundedRect fill];

        roundedRectImage = UIGraphicsGetImageFromCurrentImageContext();
        roundedRectImage = [roundedRectImage resizableImageWithCapInsets:UIEdgeInsetsMake(AAPLOverlayCornerRadius, AAPLOverlayCornerRadius, AAPLOverlayCornerRadius, AAPLOverlayCornerRadius)];
        UIGraphicsEndImageContext();
    });
    return roundedRectImage;
}

+ (UIButton *)overlayRoundedRectButton {
    UIButton *button = [UIButton buttonWithType:UIButtonTypeCustom];
    button.translatesAutoresizingMaskIntoConstraints = NO;
    [button setTitleColor:[self foregroundColor] forState:UIControlStateNormal];
    button.titleLabel.font = [self largeFont];
    [button setBackgroundImage:[self overlayRoundedRectImage] forState:UIControlStateNormal];
    [button setContentEdgeInsets:UIEdgeInsetsMake(AAPLButtonVerticalContentInset, AAPLButtonHorizontalContentInset, AAPLButtonVerticalContentInset, AAPLButtonHorizontalContentInset)];
    return button;
}

+ (NSString *)fontName {
    if (UIAccessibilityIsBoldTextEnabled()) {
        return @"Avenir-Medium";
    }
    return @"Avenir-Light";
}

+ (UIFont *)standardFont {
    return [UIFont fontWithName:[self fontName] size:14.0];
}

+ (UIFont *)largeFont {
    return [UIFont fontWithName:[self fontName] size:18.0];
}

+ (UILabel *)standardLabel {
    UILabel *label = [[UILabel alloc] init];
    label.textColor = [self foregroundColor];
    label.font = [self standardFont];
    label.numberOfLines = 0; // don't force it to be a single line
    label.translatesAutoresizingMaskIntoConstraints = NO;
    return label;
}

+ (UILabel *)detailLabel {
    UILabel *label = [self standardLabel];
    label.textColor = [self detailColor];
    return label;
}

@end
```

[Next](HelloGoodbye-AAPLProfileViewController.m.md)[Previous](HelloGoodbye-AAPLStartViewController.m.md)

