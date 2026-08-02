---
title: LightTable
apple_id: DTS40008927
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2017-08-17'
source_url: https://developer.apple.com/library/archive/samplecode/LightTable/Listings/LightTable_LTMaskLayer_m.html
archived_at: '2026-07-18T03:13:31.090647Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LightTable](LightTable.md)


[Next](LightTable-LTWindowController.h.md)[Previous](LightTable-AppDelegate.h.md)

# LightTable/LTMaskLayer.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The LTMaskLayer is a CALayer that is used by  LTView to draw a single slide in the LTView. It acts as the frame and masking layer for its one child layer that is the image for the slide.
 */

#import "LTMaskLayer.h"
@import ApplicationServices;


@interface LTMaskLayer()

//@property (strong, nonatomic) CALayer * visiblePhoto;

@end

@implementation LTMaskLayer

- (instancetype)init
{
    self = [super init];
    if (self) {

        // Clip to within the photo area.
        CGColorRef borderColor = CGColorCreateGenericRGB(0.85f, 0.85f, 0.85f, 1.0f);
        self.borderColor = borderColor;
        // The CGColorRef has to be released after assignment as described in Technical Q&A QA1565.
        CFRelease(borderColor);
        self.borderWidth = 8;
        self.cornerRadius = 26;
        self.masksToBounds = YES;

        // Add on the visible photo that is masked by the border.
        _photoLayer = [CALayer layer];
        _photoLayer.contents = nil;
        _photoLayer.anchorPoint =  CGPointMake(0, 0);

        [self addSublayer:_photoLayer];
    }

    return self;
}

#pragma mark CALayer

// Overide hitTest so that our sub layers are never considered. LTMaskLayer is the end of the line.
- (CALayer *)hitTest:(CGPoint)hitPoint {
    hitPoint = [self convertPoint:hitPoint fromLayer:self.superlayer];
    return [self containsPoint:hitPoint] ? self : nil;
}


#pragma mark API

- (void)setFrame:(CGRect)frame {
    CGRect oldFrame = self.frame;
    if (!CGSizeEqualToSize(oldFrame.size, frame.size)) {
        CGRect oldPhotoFrame = self.photoLayer.frame;
        if (!(oldFrame.size.width <= 0 || oldFrame.size.height <= 0 || oldPhotoFrame.size.width <= 0 || oldPhotoFrame.size.height <= 0)) {
            CGFloat scaleFactorX = oldPhotoFrame.size.width / oldFrame.size.width;
            CGFloat scaleFactorY = oldPhotoFrame.size.height / oldFrame.size.height;

            CGRect newPhotoFrame;
            newPhotoFrame.size.width = frame.size.width * scaleFactorX;
            newPhotoFrame.size.height = frame.size.height * scaleFactorY;
            newPhotoFrame.origin.x = (oldPhotoFrame.origin.x / oldPhotoFrame.size.width) * newPhotoFrame.size.width;
            newPhotoFrame.origin.y = (oldPhotoFrame.origin.y / oldPhotoFrame.size.height) * newPhotoFrame.size.height;
            self.photoLayer.frame = newPhotoFrame;
        } else {
            self.photoLayer.frame = frame;
        }
    }
    super.frame = frame;
}

- (id)photo {
    return _photoLayer.contents;
}

- (void)setPhoto:(id)newContents {
    _photoLayer.contents = newContents;
}

- (CGRect)photoFrame{
    return [self convertRect:self.photoLayer.frame toLayer:self.superlayer];
}

- (void)setPhotoFrame:(CGRect)frame {
    self.photoLayer.frame = [self convertRect:frame fromLayer:self.superlayer];
}

- (CGPoint)photoPosition{
    return [self convertPoint:self.photoLayer.position toLayer:self.superlayer];
}

- (void)setPhotoPosition:(CGPoint)position {
    self.photoLayer.position = [self convertPoint:position fromLayer:self.superlayer];
}

@end
```

[Next](LightTable-LTWindowController.h.md)[Previous](LightTable-AppDelegate.h.md)

