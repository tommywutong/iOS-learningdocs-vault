---
title: 'CloudPhotos : Using CloudKit with iOS and OS X'
apple_id: TP40016061
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: CloudKit
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/CloudPhotos/Listings/CloudPhotos__OS_X__swift_CloudPhotos_MapViewController_swift.html
archived_at: '2026-07-18T03:03:31.809643Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudPhotos : Using CloudKit with iOS and OS X](CloudPhotos%20-%20Using%20CloudKit%20with%20iOS%20and%20OS%20X.md)


[Next](CloudPhotos%20%28OS%20X%29.swift-CloudPhotos-DetailViewController.swift.md)[Previous](CloudPhotos%20%28OS%20X%29.swift-CloudPhotos-AppDelegate.swift.md)

# CloudPhotos (OS X).swift/CloudPhotos/MapViewController.swift

```swift
/*
Copyright (C) 2017 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
View controller that shows the location of a photo in a popover.
*/

import Cocoa
import Foundation
import MapKit

class MapViewController : NSViewController {
    // MARK: - Properties

    var mapLocation: CLLocation!

    @IBOutlet private weak var mapView: MKMapView!

    // MARK: - View Controller Lifecycle

    override func viewDidAppear() {
        super.viewDidAppear()

        guard mapLocation != nil else { return }

        // Set the location and spanning region to our map view.
        let location: CLLocationCoordinate2D =
            CLLocationCoordinate2D(latitude: mapLocation.coordinate.latitude, longitude: mapLocation.coordinate.longitude)
        let newRegion: MKCoordinateRegion = MKCoordinateRegionMake(location, MKCoordinateSpanMake(0.008, 0.008))
        mapView.region = newRegion

        // Geocode the location for setting the annotation data.
        let geocoder: CLGeocoder = CLGeocoder()
        geocoder.reverseGeocodeLocation(mapLocation, completionHandler: { (placemarks, error) -> Void in

            DispatchQueue.main.async {
                guard let placemarks = placemarks, placemarks.count > 0 else { return }
                self.setMapAnnotation(placemarks)
            }
        })
    }

    /// Adds an annotation (where the CloudPhoto was taken from the camera) to the map.
    private func setMapAnnotation(_ placemarks: [CLPlacemark]) {
        let myAnnotation: MKPointAnnotation = MKPointAnnotation()
        myAnnotation.coordinate = mapLocation.coordinate

        guard (placemarks.count > 0) else { return }

        let placemark: CLPlacemark = placemarks[0]
        if placemark.locality != nil && placemark.administrativeArea != nil
        {
            myAnnotation.title = title
            if placemark.thoroughfare != nil
            {
                myAnnotation.subtitle = String(format: "%@: %@, %@", placemark.thoroughfare!, placemark.locality!, placemark.administrativeArea!)
            }
            else
            {
                myAnnotation.subtitle =
                    String(format:"%@, %@", placemark.locality!, placemark.administrativeArea!)
            }
            mapView.addAnnotation(myAnnotation)
            mapView.selectAnnotation(myAnnotation, animated: false)
        }
    }
}
```

[Next](CloudPhotos%20%28OS%20X%29.swift-CloudPhotos-DetailViewController.swift.md)[Previous](CloudPhotos%20%28OS%20X%29.swift-CloudPhotos-AppDelegate.swift.md)

