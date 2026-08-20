---
title: 'Regions: region monitoring, significant location changes, background location
  service, location service authorization'
apple_id: DTS40010726
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2016-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/Regions/Listings/Regions_RegionAnnotationView_m.html
archived_at: '2026-07-18T03:22:05.246312Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Regions: region monitoring, significant location changes, background location service, location service authorization](Regions-%20region%20monitoring%2C%20significant%20location%20changes%2C%20background%20location%20se.md)


[Next](Regions-RegionsAppDelegate.h.md)[Previous](Regions-RegionAnnotation.h.md)

# Regions/RegionAnnotationView.m

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The custom annotation view to display a region that is being monitored.
 */

#import "RegionAnnotationView.h"
#import "RegionAnnotation.h"

@interface RegionAnnotationView() {

}

@property (strong, nonatomic) MKCircle *radiusOverlay;
@property (assign, nonatomic) BOOL isRadiusUpdated;

@end

@implementation RegionAnnotationView

// Initialize the annotation view object. This is the designated initializer.
- (instancetype)initWithAnnotation:(id <MKAnnotation>)annotation {
    self = [super initWithAnnotation:annotation reuseIdentifier:[annotation title]];    

    if (self) {     
        self.canShowCallout = YES;
        self.multipleTouchEnabled = NO;
        self.draggable = YES;
        self.animatesDrop = YES;
        _map = nil;
        _theAnnotation = (RegionAnnotation *)annotation;
        self.pinColor = MKPinAnnotationColorPurple;
        _radiusOverlay = [MKCircle circleWithCenterCoordinate:_theAnnotation.coordinate radius:_theAnnotation.radius];

        [_map addOverlay:self.radiusOverlay];
    }

    return self;    
}


- (void)removeRadiusOverlay {
    // Find the overlay for this annotation view and remove it if it has the same coordinates.
    for (id overlay in [self.map overlays]) {
        if ([overlay isKindOfClass:[MKCircle class]]) {                     
            MKCircle *circleOverlay = (MKCircle *)overlay;          
            CLLocationCoordinate2D coord = circleOverlay.coordinate;

            if (coord.latitude == self.theAnnotation.coordinate.latitude && coord.longitude == self.theAnnotation.coordinate.longitude) {
                [self.map removeOverlay:overlay];
            }           
        }
    }

    self.isRadiusUpdated = NO;
}

// Update the circular overlay if the radius has changed.
- (void)updateRadiusOverlay {
    if (!self.isRadiusUpdated) {
        self.isRadiusUpdated = YES;

        [self removeRadiusOverlay]; 

        self.canShowCallout = NO;

        [self.map addOverlay:[MKCircle circleWithCenterCoordinate:self.theAnnotation.coordinate radius:self.theAnnotation.radius]];

        self.canShowCallout = YES;      
    }
}




@end
```

[Next](Regions-RegionsAppDelegate.h.md)[Previous](Regions-RegionAnnotation.h.md)

