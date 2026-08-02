---
title: 'CloudPhotos : Using CloudKit with iOS and OS X'
apple_id: TP40016061
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: CloudKit
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/CloudPhotos/Listings/CloudPhotos__iOS__CloudPhotos_APLPhotoViewController_m.html
archived_at: '2026-07-18T03:03:33.316345Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudPhotos : Using CloudKit with iOS and OS X](CloudPhotos%20-%20Using%20CloudKit%20with%20iOS%20and%20OS%20X.md)


[Next](CloudPhotos%20%28iOS%29-CloudPhotos-APLPhotoViewController.h.md)[Previous](CloudPhotos%20%28iOS%29-CloudPhotos-PhotoTableCell.h.md)

# CloudPhotos (iOS)/CloudPhotos/APLPhotoViewController.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The view controller responsible for showing the actual CKRecord photo.
 */

#import "APLPhotoViewController.h"

@interface APLPhotoViewController () <UIScrollViewDelegate>

@property (nonatomic, weak) IBOutlet UIImageView *imageView;

@property (nonatomic) CGFloat lastZoomScale;

@property (nonatomic, weak) IBOutlet UIScrollView *scrollView;
@property (nonatomic, weak) IBOutlet NSLayoutConstraint *constraintLeft;
@property (nonatomic, weak) IBOutlet NSLayoutConstraint *constraintRight;
@property (nonatomic, weak) IBOutlet NSLayoutConstraint *constraintTop;
@property (nonatomic, weak) IBOutlet NSLayoutConstraint *constraintBottom;

@end


#pragma mark -

@implementation APLPhotoViewController

- (void)viewDidAppear:(BOOL)animated
{
    [super viewDidAppear:animated];

    self.imageView.image = self.photo;
    self.scrollView.delegate = self;
    [self updateZoom];
}


#pragma mark - UIScrollViewDelegate

- (void)scrollViewDidZoom:(UIScrollView *)scrollView
{
    [self updateConstraints];
}

- (UIView *)viewForZoomingInScrollView:(UIScrollView *)scrollView
{
    return self.imageView;
}


#pragma mark - Updating

- (void)updateConstraints
{
    CGFloat imageWidth = self.imageView.image.size.width;
    CGFloat imageHeight = self.imageView.image.size.height;

    CGFloat viewWidth = self.view.bounds.size.width;
    CGFloat viewHeight = self.view.bounds.size.height;

    // center the photo if it is smaller than screen
    CGFloat hPadding = (viewWidth - self.scrollView.zoomScale * imageWidth) / 2;
    if (hPadding < 0)
    {
        hPadding = 0;
    }
    CGFloat vPadding = (viewHeight - self.scrollView.zoomScale * imageHeight) / 2;
    if (vPadding < 0)
    {
        vPadding = 0;
    }

    self.constraintLeft.constant = self.constraintRight.constant = hPadding;
    self.constraintTop.constant = self.constraintBottom.constant = vPadding;

    [self.view layoutIfNeeded];
}

- (void)updateZoom
{
    CGFloat minZoom = MIN(self.view.bounds.size.width / self.imageView.image.size.width,
                        self.view.bounds.size.height / self.imageView.image.size.height);
    if (minZoom > 1)
    {
        minZoom = 1;
    }

    self.scrollView.minimumZoomScale = minZoom;

    // this will call "scrollViewDidZoom" if zoom did not change
    if (minZoom == self.lastZoomScale)
    {
        minZoom += 0.000001;
    }

    self.lastZoomScale = self.scrollView.zoomScale = minZoom;
}

@end
```

[Next](CloudPhotos%20%28iOS%29-CloudPhotos-APLPhotoViewController.h.md)[Previous](CloudPhotos%20%28iOS%29-CloudPhotos-PhotoTableCell.h.md)

