---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/CoreLocation.html
archived_at: '2026-07-18T02:52:13.096962Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# CoreLocation Changes

## CoreLocation

Added CLLocationCoordinate2D.init()Added CLLocationCoordinate2D.init(latitude: CLLocationDegrees, longitude: CLLocationDegrees)Modified CLCircularRegion.init(center: CLLocationCoordinate2D, radius: CLLocationDistance, identifier: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(center center: CLLocationCoordinate2D, radius radius: CLLocationDistance, identifier identifier: String!) ``` |
| To | ``` init!(center center: CLLocationCoordinate2D, radius radius: CLLocationDistance, identifier identifier: String!) ``` |

Modified CLGeocoder

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CLHeading

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CLHeading.timestamp

|  | Declaration |
| --- | --- |
| From | ``` var timestamp: NSDate! { get } ``` |
| To | ``` @NSCopying var timestamp: NSDate! { get } ``` |

Modified CLLocation

|  | Protocols | Introduction |
| --- | --- | --- |
| From | AnyObject, NSCoding, NSCopying, NSSecureCoding | OS X 10.10 |
| To | AnyObject, CKRecordValue, NSCoding, NSCopying, NSObjectProtocol, NSSecureCoding | OS X 10.6 |

Modified CLLocation.init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy: CLLocationAccuracy, verticalAccuracy: CLLocationAccuracy, course: CLLocationDirection, speed: CLLocationSpeed, timestamp: NSDate!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(coordinate coordinate: CLLocationCoordinate2D, altitude altitude: CLLocationDistance, horizontalAccuracy hAccuracy: CLLocationAccuracy, verticalAccuracy vAccuracy: CLLocationAccuracy, course course: CLLocationDirection, speed speed: CLLocationSpeed, timestamp timestamp: NSDate!) ``` | OS X 10.10 |
| To | ``` init!(coordinate coordinate: CLLocationCoordinate2D, altitude altitude: CLLocationDistance, horizontalAccuracy hAccuracy: CLLocationAccuracy, verticalAccuracy vAccuracy: CLLocationAccuracy, course course: CLLocationDirection, speed speed: CLLocationSpeed, timestamp timestamp: NSDate!) ``` | OS X 10.7 |

Modified CLLocation.init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy: CLLocationAccuracy, verticalAccuracy: CLLocationAccuracy, timestamp: NSDate!)

|  | Declaration |
| --- | --- |
| From | ``` init(coordinate coordinate: CLLocationCoordinate2D, altitude altitude: CLLocationDistance, horizontalAccuracy hAccuracy: CLLocationAccuracy, verticalAccuracy vAccuracy: CLLocationAccuracy, timestamp timestamp: NSDate!) ``` |
| To | ``` init!(coordinate coordinate: CLLocationCoordinate2D, altitude altitude: CLLocationDistance, horizontalAccuracy hAccuracy: CLLocationAccuracy, verticalAccuracy vAccuracy: CLLocationAccuracy, timestamp timestamp: NSDate!) ``` |

Modified CLLocation.course

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CLLocation.distanceFromLocation(CLLocation!) -> CLLocationDistance

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CLLocation.init(latitude: CLLocationDegrees, longitude: CLLocationDegrees)

|  | Declaration |
| --- | --- |
| From | ``` init(latitude latitude: CLLocationDegrees, longitude longitude: CLLocationDegrees) ``` |
| To | ``` init!(latitude latitude: CLLocationDegrees, longitude longitude: CLLocationDegrees) ``` |

Modified CLLocation.speed

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CLLocation.timestamp

|  | Declaration |
| --- | --- |
| From | ``` var timestamp: NSDate! { get } ``` |
| To | ``` @NSCopying var timestamp: NSDate! { get } ``` |

Modified CLLocationCoordinate2D [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CLLocationCoordinate2D {     var latitude: CLLocationDegrees     var longitude: CLLocationDegrees } ``` |
| To | ``` struct CLLocationCoordinate2D {     var latitude: CLLocationDegrees     var longitude: CLLocationDegrees     init()     init(latitude latitude: CLLocationDegrees, longitude longitude: CLLocationDegrees) } ``` |

Modified CLLocationManager

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CLLocationManager.authorizationStatus() -> CLAuthorizationStatus [class]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CLLocationManager.deferredLocationUpdatesAvailable() -> Bool [class]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CLLocationManager.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: CLLocationManagerDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: CLLocationManagerDelegate! ``` |

Modified CLLocationManager.headingAvailable() -> Bool [class]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CLLocationManager.location

|  | Declaration |
| --- | --- |
| From | ``` var location: CLLocation! { get } ``` |
| To | ``` @NSCopying var location: CLLocation! { get } ``` |

Modified CLLocationManager.locationServicesEnabled() -> Bool [class]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CLLocationManager.maximumRegionMonitoringDistance

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CLLocationManager.monitoredRegions

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var monitoredRegions: NSSet! { get } ``` | OS X 10.10 |
| To | ``` var monitoredRegions: Set<NSObject>! { get } ``` | OS X 10.8 |

Modified CLLocationManager.purpose

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CLLocationManager.regionMonitoringAvailable() -> Bool [class]

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified CLLocationManager.regionMonitoringEnabled() -> Bool [class]

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified CLLocationManager.significantLocationChangeMonitoringAvailable() -> Bool [class]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CLLocationManager.startMonitoringForRegion(CLRegion!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CLLocationManager.startMonitoringSignificantLocationChanges()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CLLocationManager.stopMonitoringForRegion(CLRegion!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CLLocationManager.stopMonitoringSignificantLocationChanges()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CLLocationManagerDelegate.locationManager(CLLocationManager!, didChangeAuthorizationStatus: CLAuthorizationStatus)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.7 | yes |

Modified CLLocationManagerDelegate.locationManager(CLLocationManager!, didDetermineState: CLRegionState, forRegion: CLRegion!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CLLocationManagerDelegate.locationManager(CLLocationManager!, didEnterRegion: CLRegion!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | yes |

Modified CLLocationManagerDelegate.locationManager(CLLocationManager!, didExitRegion: CLRegion!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | yes |

Modified CLLocationManagerDelegate.locationManager(CLLocationManager!, didFailWithError: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CLLocationManagerDelegate.locationManager(CLLocationManager!, didFinishDeferredUpdatesWithError: NSError!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.9 | yes |

Modified CLLocationManagerDelegate.locationManager(CLLocationManager!, didStartMonitoringForRegion: CLRegion!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | yes |

Modified CLLocationManagerDelegate.locationManager(CLLocationManager!, didUpdateLocations:[AnyObject]!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.9 | yes |

Modified CLLocationManagerDelegate.locationManager(CLLocationManager!, didUpdateToLocation: CLLocation!, fromLocation: CLLocation!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.6 | yes |

Modified CLLocationManagerDelegate.locationManager(CLLocationManager!, monitoringDidFailForRegion: CLRegion!, withError: NSError!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | yes |

Modified CLPlacemark

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CLPlacemark.location

|  | Declaration |
| --- | --- |
| From | ``` var location: CLLocation! { get } ``` |
| To | ``` @NSCopying var location: CLLocation! { get } ``` |

Modified CLPlacemark.init(placemark: CLPlacemark!)

|  | Declaration |
| --- | --- |
| From | ``` init(placemark placemark: CLPlacemark!) ``` |
| To | ``` init!(placemark placemark: CLPlacemark!) ``` |

Modified CLPlacemark.region

|  | Declaration |
| --- | --- |
| From | ``` var region: CLRegion! { get } ``` |
| To | ``` @NSCopying var region: CLRegion! { get } ``` |

Modified CLRegion

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CLRegion.center

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.7 | OS X 10.10 |

Modified CLRegion.init(circularRegionWithCenter: CLLocationCoordinate2D, radius: CLLocationDistance, identifier: String!)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` init(circularRegionWithCenter center: CLLocationCoordinate2D, radius radius: CLLocationDistance, identifier identifier: String!) ``` | OS X 10.10 | -- |
| To | ``` init!(circularRegionWithCenter center: CLLocationCoordinate2D, radius radius: CLLocationDistance, identifier identifier: String!) ``` | OS X 10.7 | OS X 10.10 |

Modified CLRegion.containsCoordinate(CLLocationCoordinate2D) -> Bool

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.7 | OS X 10.10 |

Modified CLRegion.identifier

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CLRegion.radius

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.7 | OS X 10.10 |

Modified CLLocationCoordinate2DIsValid(CLLocationCoordinate2D) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CLLocationCoordinate2DMake(CLLocationDegrees, CLLocationDegrees) -> CLLocationCoordinate2D

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCLErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let kCLErrorDomain: NSString! ``` |
| To | ``` let kCLErrorDomain: String ``` |

Modified kCLErrorUserInfoAlternateRegionKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCLErrorUserInfoAlternateRegionKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCLErrorUserInfoAlternateRegionKey: String ``` | OS X 10.7 |

Modified kCLLocationAccuracyBestForNavigation

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCLLocationCoordinate2DInvalid

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
