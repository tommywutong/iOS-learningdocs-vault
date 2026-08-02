---
title: 'CloudPhotos : Using CloudKit with iOS and OS X'
apple_id: TP40016061
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: CloudKit
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/CloudPhotos/Listings/CloudPhotos__iOS__CloudPhotos_APLMapViewController_m.html
archived_at: '2026-07-18T03:03:33.229033Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudPhotos : Using CloudKit with iOS and OS X](CloudPhotos%20-%20Using%20CloudKit%20with%20iOS%20and%20OS%20X.md)


[Next](Document%20Revision%20History.md)[Previous](CloudPhotos%20%28iOS%29-CloudPhotos-APLDetailTableViewController.m.md)

# CloudPhotos (iOS)/CloudPhotos/APLMapViewController.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The view controller responsible for showing the location a CKRecord photo was taken.
 */

#import "APLMapViewController.h"

@import MapKit;

@interface APLMapViewController () <MKMapViewDelegate>

@property (nonatomic, weak) IBOutlet MKMapView *mapView;

@end


#pragma mark -

@implementation APLMapViewController

- (void)viewWillAppear:(BOOL)animated
{
    [super viewWillAppear:animated];

    if (self.location != nil)
    {
        MKCoordinateRegion newRegion;
        newRegion.center.latitude = self.location.coordinate.latitude;
        newRegion.center.longitude = self.location.coordinate.longitude;
        newRegion.span.latitudeDelta = 0.008;
        newRegion.span.longitudeDelta = 0.008;
        self.mapView.region = newRegion;

        MKPointAnnotation *myAnnotation = [[MKPointAnnotation alloc] init];
        myAnnotation.coordinate = self.location.coordinate;;

        // get nearby address for our callout
        [UIApplication sharedApplication].networkActivityIndicatorVisible = YES;

        CLGeocoder *geocoder = [[CLGeocoder alloc] init];
        [geocoder reverseGeocodeLocation:self.location completionHandler:^(NSArray *placemarks, NSError *error) {

            dispatch_async(dispatch_get_main_queue(), ^(void) {

                [UIApplication sharedApplication].networkActivityIndicatorVisible = NO;

                if (placemarks != nil && placemarks.count > 0)
                {
                    CLPlacemark *placemark = placemarks[0];
                    if (placemark.locality != nil && placemark.administrativeArea != nil)
                    {
                        myAnnotation.title = self.title;
                        if (placemark.thoroughfare != nil)
                        {
                            myAnnotation.subtitle =
                                [NSString stringWithFormat:@"%@: %@, %@", placemark.thoroughfare, placemark.locality, placemark.administrativeArea];
                        }
                        else
                        {
                            myAnnotation.subtitle =
                                [NSString stringWithFormat:@"%@, %@", placemark.locality, placemark.administrativeArea];
                        }
                        [self.mapView addAnnotation:myAnnotation];
                        [self.mapView selectAnnotation:myAnnotation animated:NO];
                    }
                }
            });
        }];
    }
}

@end
```

[Next](Document%20Revision%20History.md)[Previous](CloudPhotos%20%28iOS%29-CloudPhotos-APLDetailTableViewController.m.md)

