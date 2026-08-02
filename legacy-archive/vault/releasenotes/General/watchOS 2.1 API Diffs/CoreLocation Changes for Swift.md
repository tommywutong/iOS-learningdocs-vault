---
title: watchOS 2.1 API Diffs
apple_id: TP40016636
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2015-12-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS21APIDiffs/Swift/CoreLocation.html
archived_at: '2026-07-18T02:58:08.064417Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 2.1 API Diffs](watchOS%202.0%20to%20watchOS%202.1%20API%20Differences.md)


# CoreLocation Changes for Swift

### CoreLocation

Modified [CLActivityType [enum]](https://developer.apple.com/documentation/corelocation/clactivitytype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CLAuthorizationStatus [enum]](https://developer.apple.com/documentation/corelocation/clauthorizationstatus)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CLCircularRegion](https://developer.apple.com/documentation/corelocation/clcircularregion)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CLDeviceOrientation [enum]](https://developer.apple.com/documentation/corelocation/cldeviceorientation)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CLError [enum]](https://developer.apple.com/documentation/corelocation/clerror/code)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` enum CLError : Int {     case LocationUnknown     case Denied     case Network     case HeadingFailure     case RegionMonitoringDenied     case RegionMonitoringFailure     case RegionMonitoringSetupDelayed     case RegionMonitoringResponseDelayed     case GeocodeFoundNoResult     case GeocodeFoundPartialResult     case GeocodeCanceled     case DeferredFailed     case DeferredNotUpdatingLocation     case DeferredAccuracyTooLow     case DeferredDistanceFiltered     case DeferredCanceled     case RangingUnavailable     case RangingFailure } extension CLError : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } extension CLError : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } ``` | Equatable, ErrorType, Hashable, RawRepresentable |
| To | ``` enum CLError : Int {     case LocationUnknown     case Denied     case Network     case HeadingFailure     case RegionMonitoringDenied     case RegionMonitoringFailure     case RegionMonitoringSetupDelayed     case RegionMonitoringResponseDelayed     case GeocodeFoundNoResult     case GeocodeFoundPartialResult     case GeocodeCanceled     case DeferredFailed     case DeferredNotUpdatingLocation     case DeferredAccuracyTooLow     case DeferredDistanceFiltered     case DeferredCanceled     case RangingUnavailable     case RangingFailure } extension CLError : _BridgedNSError { } extension CLError : _BridgedNSError { } ``` | -- |

Modified [CLFloor](https://developer.apple.com/documentation/corelocation/clfloor)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CLFloor : NSObject, NSCopying, NSSecureCoding, NSCoding {     var level: Int { get } } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class CLFloor : NSObject, NSCopying, NSSecureCoding {     var level: Int { get } } ``` | NSCopying, NSSecureCoding |

Modified [CLGeocoder](https://developer.apple.com/documentation/corelocation/clgeocoder)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CLLocation](https://developer.apple.com/documentation/corelocation/cllocation)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CLLocation : NSObject, NSCopying, NSSecureCoding, NSCoding {     init(latitude latitude: CLLocationDegrees, longitude longitude: CLLocationDegrees)     init(coordinate coordinate: CLLocationCoordinate2D, altitude altitude: CLLocationDistance, horizontalAccuracy hAccuracy: CLLocationAccuracy, verticalAccuracy vAccuracy: CLLocationAccuracy, timestamp timestamp: NSDate)     init(coordinate coordinate: CLLocationCoordinate2D, altitude altitude: CLLocationDistance, horizontalAccuracy hAccuracy: CLLocationAccuracy, verticalAccuracy vAccuracy: CLLocationAccuracy, course course: CLLocationDirection, speed speed: CLLocationSpeed, timestamp timestamp: NSDate)     var coordinate: CLLocationCoordinate2D { get }     var altitude: CLLocationDistance { get }     var horizontalAccuracy: CLLocationAccuracy { get }     var verticalAccuracy: CLLocationAccuracy { get }     var course: CLLocationDirection { get }     var speed: CLLocationSpeed { get }     @NSCopying var timestamp: NSDate { get }     @NSCopying var floor: CLFloor? { get }     var description: String { get }     func getDistanceFrom(_ location: CLLocation) -> CLLocationDistance     func distanceFromLocation(_ location: CLLocation) -> CLLocationDistance } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class CLLocation : NSObject, NSCopying, NSSecureCoding {     init(latitude latitude: CLLocationDegrees, longitude longitude: CLLocationDegrees)     init(coordinate coordinate: CLLocationCoordinate2D, altitude altitude: CLLocationDistance, horizontalAccuracy hAccuracy: CLLocationAccuracy, verticalAccuracy vAccuracy: CLLocationAccuracy, timestamp timestamp: NSDate)     init(coordinate coordinate: CLLocationCoordinate2D, altitude altitude: CLLocationDistance, horizontalAccuracy hAccuracy: CLLocationAccuracy, verticalAccuracy vAccuracy: CLLocationAccuracy, course course: CLLocationDirection, speed speed: CLLocationSpeed, timestamp timestamp: NSDate)     var coordinate: CLLocationCoordinate2D { get }     var altitude: CLLocationDistance { get }     var horizontalAccuracy: CLLocationAccuracy { get }     var verticalAccuracy: CLLocationAccuracy { get }     var course: CLLocationDirection { get }     var speed: CLLocationSpeed { get }     @NSCopying var timestamp: NSDate { get }     @NSCopying var floor: CLFloor? { get }     var description: String { get }     func getDistanceFrom(_ location: CLLocation) -> CLLocationDistance     func distanceFromLocation(_ location: CLLocation) -> CLLocationDistance } ``` | NSCopying, NSSecureCoding |

Modified [CLLocationManager](https://developer.apple.com/documentation/corelocation/cllocationmanager)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CLPlacemark](https://developer.apple.com/documentation/corelocation/clplacemark)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CLPlacemark : NSObject, NSCopying, NSSecureCoding, NSCoding {     init(placemark placemark: CLPlacemark)     @NSCopying var location: CLLocation? { get }     @NSCopying var region: CLRegion? { get }     @NSCopying var timeZone: NSTimeZone? { get }     var addressDictionary: [NSObject : AnyObject]? { get }     var name: String? { get }     var thoroughfare: String? { get }     var subThoroughfare: String? { get }     var locality: String? { get }     var subLocality: String? { get }     var administrativeArea: String? { get }     var subAdministrativeArea: String? { get }     var postalCode: String? { get }     var ISOcountryCode: String? { get }     var country: String? { get }     var inlandWater: String? { get }     var ocean: String? { get }     var areasOfInterest: [String]? { get } } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class CLPlacemark : NSObject, NSCopying, NSSecureCoding {     init(placemark placemark: CLPlacemark)     @NSCopying var location: CLLocation? { get }     @NSCopying var region: CLRegion? { get }     @NSCopying var timeZone: NSTimeZone? { get }     var addressDictionary: [NSObject : AnyObject]? { get }     var name: String? { get }     var thoroughfare: String? { get }     var subThoroughfare: String? { get }     var locality: String? { get }     var subLocality: String? { get }     var administrativeArea: String? { get }     var subAdministrativeArea: String? { get }     var postalCode: String? { get }     var ISOcountryCode: String? { get }     var country: String? { get }     var inlandWater: String? { get }     var ocean: String? { get }     var areasOfInterest: [String]? { get } } ``` | NSCopying, NSSecureCoding |

Modified [CLRegion](https://developer.apple.com/documentation/corelocation/clregion)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CLRegion : NSObject, NSCopying, NSSecureCoding, NSCoding {     init(circularRegionWithCenter center: CLLocationCoordinate2D, radius radius: CLLocationDistance, identifier identifier: String)     var center: CLLocationCoordinate2D { get }     var radius: CLLocationDistance { get }     var identifier: String { get }     var notifyOnEntry: Bool     var notifyOnExit: Bool     func containsCoordinate(_ coordinate: CLLocationCoordinate2D) -> Bool } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class CLRegion : NSObject, NSCopying, NSSecureCoding {     init(circularRegionWithCenter center: CLLocationCoordinate2D, radius radius: CLLocationDistance, identifier identifier: String)     var center: CLLocationCoordinate2D { get }     var radius: CLLocationDistance { get }     var identifier: String { get }     var notifyOnEntry: Bool     var notifyOnExit: Bool     func containsCoordinate(_ coordinate: CLLocationCoordinate2D) -> Bool } ``` | NSCopying, NSSecureCoding |

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
