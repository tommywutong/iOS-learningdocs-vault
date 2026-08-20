---
title: 'PhotoMap: Loading and displaying geotagged photos as MapKit annotations'
apple_id: DTS40011109
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: MapKit
published: '2018-04-26'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoMap/Listings/PhotoMap_PhotosViewController_PhotosViewController_h.html
archived_at: '2026-07-18T03:18:52.644225Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoMap: Loading and displaying geotagged photos as MapKit annotations](PhotoMap-%20Loading%20and%20displaying%20geotagged%20photos%20as%20MapKit%20annotations.md)


[Next](PhotoMap-PhotosViewController-DataViewController.h.md)[Previous](PhotoMap-PhotosViewController-PhotosViewController.m.md)

# PhotoMap/PhotosViewController/PhotosViewController.h

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The secondary view controller used for browing the photos.
 */

@import UIKit;

@interface PhotosViewController : UIViewController <UIPageViewControllerDelegate>

@property (nonatomic, strong) NSArray *photosToShow;
@property BOOL pageAnimationFinished;

@end
```

[Next](PhotoMap-PhotosViewController-DataViewController.h.md)[Previous](PhotoMap-PhotosViewController-PhotosViewController.m.md)

