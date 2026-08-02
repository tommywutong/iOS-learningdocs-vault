---
title: 'BracketStripes: Using the Bracketed Capture API'
apple_id: TP40014579
resource_type: Sample Code
platform: iOS
topic: null
technology: AVFoundation
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/BracketStripes/Listings/BracketStripes_BracketStripesImageViewController_m.html
archived_at: '2026-07-18T03:02:17.099771Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [BracketStripes: Using the Bracketed Capture API](BracketStripes-%20Using%20the%20Bracketed%20Capture%20API.md)


[Next](BracketStripes-BracketStripesCapturePreviewView.h.md)[Previous](BracketStripes-AppDelegate.m.md)

# BracketStripes/BracketStripesImageViewController.m

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Photo view controller
 */

#import "BracketStripesImageViewController.h"
#import "BracketStripesZoomImageView.h"


@implementation BracketStripesImageViewController {

    UIImage *_image;
    BracketStripesZoomImageView *_imageView;
}


- (instancetype)initWithImage:(UIImage *)image
{
    self = [super initWithNibName:nil bundle:nil];
    if (self) {

        _image = image;
    }
    return self;
}


- (void)loadView
{
    [super loadView];

    _imageView = [[BracketStripesZoomImageView alloc] init];
    _imageView.image = _image;
    _imageView.autoresizingMask = UIViewAutoresizingFlexibleWidth | UIViewAutoresizingFlexibleHeight;

    self.automaticallyAdjustsScrollViewInsets = NO;
    self.view = _imageView;

    UIColor *iosBlueColor = [UIColor colorWithRed:0.0 green:122.0/255.0 blue:1.0 alpha:1.0];
    self.navigationController.navigationBar.tintColor = iosBlueColor;

    self.navigationItem.rightBarButtonItem = [[UIBarButtonItem alloc] initWithBarButtonSystemItem:UIBarButtonSystemItemDone target:self action:@selector(_done:)];
}


- (void)_done:(id)sender
{
    [_delegate imageViewControllerDidFinish:self];
}

@end
```

[Next](BracketStripes-BracketStripesCapturePreviewView.h.md)[Previous](BracketStripes-AppDelegate.m.md)

