---
title: 'Regions: region monitoring, significant location changes, background location
  service, location service authorization'
apple_id: DTS40010726
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2016-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/Regions/Listings/Regions_RegionsViewController_h.html
archived_at: '2026-07-18T03:22:05.517807Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Regions: region monitoring, significant location changes, background location service, location service authorization](Regions-%20region%20monitoring%2C%20significant%20location%20changes%2C%20background%20location%20se.md)


[Next](Regions-RegionAnnotation.h.md)[Previous](Regions-RegionAnnotationView.h.md)

# Regions/RegionsViewController.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This controller displays the map and allows the user to set regions to monitor.
 */

#import <MapKit/MapKit.h>
#import <CoreLocation/CoreLocation.h>

@interface RegionsViewController : UIViewController {

}

@property (nonatomic, weak) IBOutlet UITableView *updatesTableView;
@property (nonatomic, strong) CLLocationManager *locationManager;

@end
```

[Next](Regions-RegionAnnotation.h.md)[Previous](Regions-RegionAnnotationView.h.md)

