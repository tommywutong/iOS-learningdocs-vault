---
title: ZoomingPDFViewer
apple_id: DTS40010281
resource_type: Sample Code
platform: iOS
topic: Graphics & Animation
technology: CoreGraphics
published: '2017-04-27'
source_url: https://developer.apple.com/library/archive/samplecode/ZoomingPDFViewer/Listings/ZoomingPDFViewerCocoa_ZoomingPDFViewer_RootViewController_h.html
archived_at: '2026-07-18T03:28:44.755866Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZoomingPDFViewer](ZoomingPDFViewer.md)


[Next](ZoomingPDFViewerCocoa-ZoomingPDFViewer-RootViewController.m.md)[Previous](ZoomingPDFViewerSwift-ZoomingPDFViewer-TiledPDFScrollView.swift.md)

# ZoomingPDFViewerCocoa/ZoomingPDFViewer/RootViewController.h

```objc
/*
Copyright (C) 2017 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
This view controller manages the display of a set of view controllers by way of implementing the UIPageViewControllerDelegate protocol.
*/



#import <UIKit/UIKit.h>



@class ModelController;



@interface RootViewController: UIViewController <UIPageViewControllerDelegate>


@property (strong, nonatomic) UIPageViewController *pageViewController;

@property (strong, nonatomic) ModelController *modelController;


- (void)viewDidLoad;

- (ModelController *)modelController;

- (UIPageViewControllerSpineLocation)pageViewController:(UIPageViewController *)pageViewController spineLocationForInterfaceOrientation:(UIInterfaceOrientation)orientation;

@end
```

[Next](ZoomingPDFViewerCocoa-ZoomingPDFViewer-RootViewController.m.md)[Previous](ZoomingPDFViewerSwift-ZoomingPDFViewer-TiledPDFScrollView.swift.md)

