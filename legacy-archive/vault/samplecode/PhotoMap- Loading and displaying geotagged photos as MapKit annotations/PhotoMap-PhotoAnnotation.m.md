---
title: 'PhotoMap: Loading and displaying geotagged photos as MapKit annotations'
apple_id: DTS40011109
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: MapKit
published: '2018-04-26'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoMap/Listings/PhotoMap_PhotoAnnotation_m.html
archived_at: '2026-07-18T03:18:52.187037Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoMap: Loading and displaying geotagged photos as MapKit annotations](PhotoMap-%20Loading%20and%20displaying%20geotagged%20photos%20as%20MapKit%20annotations.md)


[Next](PhotoMap-PhotosViewController-PhotosViewController.m.md)[Previous](PhotoMap-PhotoMapViewController.h.md)

# PhotoMap/PhotoAnnotation.m

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A simple model class to display pins representing photos on the map.
 */

#import "PhotoAnnotation.h"
@import CoreLocation;

@implementation PhotoAnnotation

- (id)initWithImagePath:(NSString *)anImagePath title:(NSString *)aTitle coordinate:(CLLocationCoordinate2D)aCoordinate {

    self = [super init];
    if (self != nil) {
        self.imagePath = anImagePath;
        self.title = aTitle;
        self.coordinate = aCoordinate;
    }
    return self;
}

- (NSString *)title {

    if (self.containedAnnotations.count > 0) {
        return [NSString stringWithFormat:@"%zd Photos", self.containedAnnotations.count + 1];
    }

    return _title;
}

- (UIImage *)image {

    if (!_image && self.imagePath) {
        _image = [UIImage imageWithContentsOfFile:self.imagePath];
    }
    return _image;
}

- (NSString *)stringForPlacemark:(CLPlacemark *)placemark {

    NSMutableString *string = [[NSMutableString alloc] init];
    if (placemark.locality) {
        [string appendString:placemark.locality];
    }

    if (placemark.administrativeArea) {
        if (string.length > 0)
            [string appendString:@", "];
        [string appendString:placemark.administrativeArea];
    }

    if (string.length == 0 && placemark.name)
        [string appendString:placemark.name];

    return string;
}

- (void)updateSubtitleIfNeeded {

    if (self.subtitle == nil) {
        // for the subtitle, we reverse geocode the lat/long for a proper location string name
        CLLocation *location = [[CLLocation alloc] initWithLatitude:self.coordinate.latitude longitude:self.coordinate.longitude];
        CLGeocoder *geocoder = [[CLGeocoder alloc] init];
        [geocoder reverseGeocodeLocation:location completionHandler:^(NSArray *placemarks, NSError *error) {
            if (placemarks.count > 0) {
                CLPlacemark *placemark = placemarks[0];
                self.subtitle = [NSString stringWithFormat:@"Near %@", [self stringForPlacemark:placemark]];
            }
        }];
    }
}

@end
```

[Next](PhotoMap-PhotosViewController-PhotosViewController.m.md)[Previous](PhotoMap-PhotoMapViewController.h.md)

