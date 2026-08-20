---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/iOS_CloudKitCatalog_CloudKitCatalog_LocationFieldTableViewCell_swift.html
archived_at: '2026-07-18T03:03:28.622176Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](iOS-CloudKitCatalog-CloudKitCatalog-RequestApplicationPermissionSample.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-MarkNotificationsReadSample.swift.md)

# iOS/CloudKitCatalog/CloudKitCatalog/LocationFieldTableViewCell.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A LocationFieldTableViewCell is a FormFieldTableViewCell with controls for inputting a location.
*/

import UIKit
import CoreLocation

class LocationFieldTableViewCell: FormFieldTableViewCell {


    @IBOutlet weak var lookUpButton: UIButton!
    @IBOutlet weak var latitudeField: UITextField!
    @IBOutlet weak var longitudeField: UITextField!
    @IBOutlet weak var spinner: UIActivityIndicatorView!
    @IBOutlet weak var errorLabel: UILabel!

    var locationInput: LocationInput!

    func setCoordinate(coordinate: CLLocationCoordinate2D) {
        let latitude = coordinate.latitude
        let longitude = coordinate.longitude
        locationInput.latitude = Int(latitude)
        locationInput.longitude = Int(longitude)
        latitudeField.text = String(locationInput.latitude!)
        longitudeField.text = String(locationInput.longitude!)
        latitudeField.layoutIfNeeded()
        longitudeField.layoutIfNeeded()
    }

}
```

[Next](iOS-CloudKitCatalog-CloudKitCatalog-RequestApplicationPermissionSample.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-MarkNotificationsReadSample.swift.md)

