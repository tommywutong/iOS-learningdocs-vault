---
title: 'PhotoMap: Loading and displaying geotagged photos as MapKit annotations'
apple_id: DTS40011109
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: MapKit
published: '2018-04-26'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoMap/Listings/PhotoMap_PhotosViewController_ModelController_h.html
archived_at: '2026-07-18T03:18:52.545388Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoMap: Loading and displaying geotagged photos as MapKit annotations](PhotoMap-%20Loading%20and%20displaying%20geotagged%20photos%20as%20MapKit%20annotations.md)


[Next](PhotoMap-PhotosViewController-ModelController.m.md)[Previous](PhotoMap-PhotosViewController-DataViewController.h.md)

# PhotoMap/PhotosViewController/ModelController.h

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The model or data source for PhotosViewController.
 */

@import UIKit;

@class DataViewController;

@interface ModelController : NSObject <UIPageViewControllerDataSource>

@property (strong, nonatomic) NSArray *pageData;
@property (assign) NSInteger currentPageIndex;

- (DataViewController *)viewControllerAtIndex:(NSUInteger)index storyboard:(UIStoryboard *)storyboard;
- (NSUInteger)indexOfViewController:(DataViewController *)viewController;

@end
```

[Next](PhotoMap-PhotosViewController-ModelController.m.md)[Previous](PhotoMap-PhotosViewController-DataViewController.h.md)

