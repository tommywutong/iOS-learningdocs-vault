---
title: 'PhotoMap: Loading and displaying geotagged photos as MapKit annotations'
apple_id: DTS40011109
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: MapKit
published: '2018-04-26'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoMap/Listings/PhotoMap_PhotosViewController_DataViewController_h.html
archived_at: '2026-07-18T03:18:52.451409Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoMap: Loading and displaying geotagged photos as MapKit annotations](PhotoMap-%20Loading%20and%20displaying%20geotagged%20photos%20as%20MapKit%20annotations.md)


[Next](PhotoMap-PhotosViewController-ModelController.h.md)[Previous](PhotoMap-PhotosViewController-PhotosViewController.h.md)

# PhotoMap/PhotosViewController/DataViewController.h

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The view controller representing each page in PhotosViewController.
 */

@import UIKit;

@class PhotoAnnotation;

@interface DataViewController : UIViewController

@property (strong, nonatomic) PhotoAnnotation *dataObject;

@end
```

[Next](PhotoMap-PhotosViewController-ModelController.h.md)[Previous](PhotoMap-PhotosViewController-PhotosViewController.h.md)

