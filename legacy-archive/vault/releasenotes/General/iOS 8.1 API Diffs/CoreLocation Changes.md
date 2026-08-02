---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/CoreLocation.html
archived_at: '2026-07-18T02:56:09.627785Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# CoreLocation Changes

## CoreLocation

Modified CLBeacon

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CLBeaconRegion

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CLBeaconRegion.init(proximityUUID: NSUUID!, identifier: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(proximityUUID proximityUUID: NSUUID!, identifier identifier: String!) ``` |
| To | ``` init!(proximityUUID proximityUUID: NSUUID!, identifier identifier: String!) ``` |

Modified CLBeaconRegion.init(proximityUUID: NSUUID!, major: CLBeaconMajorValue, identifier: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(proximityUUID proximityUUID: NSUUID!, major major: CLBeaconMajorValue, identifier identifier: String!) ``` |
| To | ``` init!(proximityUUID proximityUUID: NSUUID!, major major: CLBeaconMajorValue, identifier identifier: String!) ``` |

Modified CLBeaconRegion.init(proximityUUID: NSUUID!, major: CLBeaconMajorValue, minor: CLBeaconMinorValue, identifier: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(proximityUUID proximityUUID: NSUUID!, major major: CLBeaconMajorValue, minor minor: CLBeaconMinorValue, identifier identifier: String!) ``` |
| To | ``` init!(proximityUUID proximityUUID: NSUUID!, major major: CLBeaconMajorValue, minor minor: CLBeaconMinorValue, identifier identifier: String!) ``` |

Modified CLCircularRegion

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CLCircularRegion.init(center: CLLocationCoordinate2D, radius: CLLocationDistance, identifier: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(center center: CLLocationCoordinate2D, radius radius: CLLocationDistance, identifier identifier: String!) ``` |
| To | ``` init!(center center: CLLocationCoordinate2D, radius radius: CLLocationDistance, identifier identifier: String!) ``` |

Modified CLGeocoder

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CLHeading

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified CLLocation

|  | Protocols | Introduction |
| --- | --- | --- |
| From | AnyObject, NSCoding, NSCopying, NSSecureCoding | iOS 8.0 |
| To | AnyObject, CKRecordValue, NSCoding, NSCopying, NSObjectProtocol, NSSecureCoding | iOS 2.0 |

Modified CLLocation.init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy: CLLocationAccuracy, verticalAccuracy: CLLocationAccuracy, course: CLLocationDirection, speed: CLLocationSpeed, timestamp: NSDate!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(coordinate coordinate: CLLocationCoordinate2D, altitude altitude: CLLocationDistance, horizontalAccuracy hAccuracy: CLLocationAccuracy, verticalAccuracy vAccuracy: CLLocationAccuracy, course course: CLLocationDirection, speed speed: CLLocationSpeed, timestamp timestamp: NSDate!) ``` | iOS 8.0 |
| To | ``` init!(coordinate coordinate: CLLocationCoordinate2D, altitude altitude: CLLocationDistance, horizontalAccuracy hAccuracy: CLLocationAccuracy, verticalAccuracy vAccuracy: CLLocationAccuracy, course course: CLLocationDirection, speed speed: CLLocationSpeed, timestamp timestamp: NSDate!) ``` | iOS 4.2 |

Modified CLLocation.init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy: CLLocationAccuracy, verticalAccuracy: CLLocationAccuracy, timestamp: NSDate!)

|  | Declaration |
| --- | --- |
| From | ``` init(coordinate coordinate: CLLocationCoordinate2D, altitude altitude: CLLocationDistance, horizontalAccuracy hAccuracy: CLLocationAccuracy, verticalAccuracy vAccuracy: CLLocationAccuracy, timestamp timestamp: NSDate!) ``` |
| To | ``` init!(coordinate coordinate: CLLocationCoordinate2D, altitude altitude: CLLocationDistance, horizontalAccuracy hAccuracy: CLLocationAccuracy, verticalAccuracy vAccuracy: CLLocationAccuracy, timestamp timestamp: NSDate!) ``` |

Modified CLLocation.course

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.2 |

Modified CLLocation.distanceFromLocation(CLLocation!) -> CLLocationDistance

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified CLLocation.init(latitude: CLLocationDegrees, longitude: CLLocationDegrees)

|  | Declaration |
| --- | --- |
| From | ``` init(latitude latitude: CLLocationDegrees, longitude longitude: CLLocationDegrees) ``` |
| To | ``` init!(latitude latitude: CLLocationDegrees, longitude longitude: CLLocationDegrees) ``` |

Modified CLLocation.speed

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.2 |

Modified CLLocationManager

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CLLocationManager.activityType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CLLocationManager.allowDeferredLocationUpdatesUntilTraveled(CLLocationDistance, timeout: NSTimeInterval)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CLLocationManager.authorizationStatus() -> CLAuthorizationStatus [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified CLLocationManager.deferredLocationUpdatesAvailable() -> Bool [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CLLocationManager.disallowDeferredLocationUpdates()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CLLocationManager.dismissHeadingCalibrationDisplay()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified CLLocationManager.heading

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CLLocationManager.headingAvailable() -> Bool [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CLLocationManager.headingFilter

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified CLLocationManager.headingOrientation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CLLocationManager.isMonitoringAvailableForClass(AnyClass!) -> Bool [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CLLocationManager.isRangingAvailable() -> Bool [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CLLocationManager.locationServicesEnabled() -> Bool [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CLLocationManager.maximumRegionMonitoringDistance

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CLLocationManager.monitoredRegions

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CLLocationManager.pausesLocationUpdatesAutomatically

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CLLocationManager.rangedRegions

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CLLocationManager.requestStateForRegion(CLRegion!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CLLocationManager.significantLocationChangeMonitoringAvailable() -> Bool [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CLLocationManager.startMonitoringForRegion(CLRegion!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CLLocationManager.startMonitoringSignificantLocationChanges()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CLLocationManager.startRangingBeaconsInRegion(CLBeaconRegion!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CLLocationManager.startUpdatingHeading()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified CLLocationManager.stopMonitoringForRegion(CLRegion!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CLLocationManager.stopMonitoringSignificantLocationChanges()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CLLocationManager.stopRangingBeaconsInRegion(CLBeaconRegion!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CLLocationManager.stopUpdatingHeading()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified CLLocationManagerDelegate.locationManager(CLLocationManager!, didChangeAuthorizationStatus: CLAuthorizationStatus)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified CLLocationManagerDelegate.locationManager(CLLocationManager!, didDetermineState: CLRegionState, forRegion: CLRegion!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CLLocationManagerDelegate.locationManager(CLLocationManager!, didEnterRegion: CLRegion!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CLLocationManagerDelegate.locationManager(CLLocationManager!, didExitRegion: CLRegion!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CLLocationManagerDelegate.locationManager(CLLocationManager!, didFinishDeferredUpdatesWithError: NSError!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CLLocationManagerDelegate.locationManager(CLLocationManager!, didRangeBeacons:[AnyObject]!, inRegion: CLBeaconRegion!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CLLocationManagerDelegate.locationManager(CLLocationManager!, didStartMonitoringForRegion: CLRegion!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CLLocationManagerDelegate.locationManager(CLLocationManager!, didUpdateHeading: CLHeading!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified CLLocationManagerDelegate.locationManager(CLLocationManager!, didUpdateLocations:[AnyObject]!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CLLocationManagerDelegate.locationManager(CLLocationManager!, monitoringDidFailForRegion: CLRegion!, withError: NSError!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CLLocationManagerDelegate.locationManager(CLLocationManager!, rangingBeaconsDidFailForRegion: CLBeaconRegion!, withError: NSError!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CLLocationManagerDelegate.locationManagerDidPauseLocationUpdates(CLLocationManager!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CLLocationManagerDelegate.locationManagerDidResumeLocationUpdates(CLLocationManager!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CLLocationManagerDelegate.locationManagerShouldDisplayHeadingCalibration(CLLocationManager!) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified CLPlacemark

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CLPlacemark.init(placemark: CLPlacemark!)

|  | Declaration |
| --- | --- |
| From | ``` init(placemark placemark: CLPlacemark!) ``` |
| To | ``` init!(placemark placemark: CLPlacemark!) ``` |

Modified CLProximity [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CLRegion

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CLRegion.identifier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CLRegion.notifyOnEntry

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CLRegion.notifyOnExit

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CLRegionState [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CLLocationCoordinate2DIsValid(CLLocationCoordinate2D) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CLLocationCoordinate2DMake(CLLocationDegrees, CLLocationDegrees) -> CLLocationCoordinate2D

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CLLocationDistanceMax

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CLTimeIntervalMax

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCLErrorUserInfoAlternateRegionKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCLLocationAccuracyBestForNavigation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCLLocationCoordinate2DInvalid

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

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
