---
title: ZoomingPDFViewer
apple_id: DTS40010281
resource_type: Sample Code
platform: iOS
topic: Graphics & Animation
technology: CoreGraphics
published: '2017-04-27'
source_url: https://developer.apple.com/library/archive/samplecode/ZoomingPDFViewer/Listings/ZoomingPDFViewerCocoa_ZoomingPDFViewer_ModelController_h.html
archived_at: '2026-07-18T03:28:44.570039Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZoomingPDFViewer](ZoomingPDFViewer.md)


[Next](ZoomingPDFViewerCocoa-ZoomingPDFViewer-TiledPDFView.m.md)[Previous](ZoomingPDFViewerCocoa-ZoomingPDFViewer-DataViewController.h.md)

# ZoomingPDFViewerCocoa/ZoomingPDFViewer/ModelController.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This view controller manages the display of a set of view controllers by way of implementing the UIPageViewControllerDataSource protocol.
 */


#import <UIKit/UIKit.h>



@class DataViewController;


@interface ModelController: NSObject <UIPageViewControllerDataSource>


@property CGPDFDocumentRef pdf;

@property int numberOfPages; 


- (id)init;

- (void)dealloc;

- (DataViewController *)viewControllerAtIndex:(NSUInteger)index storyboard:(UIStoryboard *)storyboard;

- (NSUInteger)indexOfViewController:(DataViewController *)viewController;

- (UIViewController *)pageViewController:(UIPageViewController *)pageViewController viewControllerBeforeViewController:(UIViewController *)viewController;

- (UIViewController *)pageViewController:(UIPageViewController *)pageViewController viewControllerAfterViewController:(UIViewController *)viewController;

@end
```

[Next](ZoomingPDFViewerCocoa-ZoomingPDFViewer-TiledPDFView.m.md)[Previous](ZoomingPDFViewerCocoa-ZoomingPDFViewer-DataViewController.h.md)

