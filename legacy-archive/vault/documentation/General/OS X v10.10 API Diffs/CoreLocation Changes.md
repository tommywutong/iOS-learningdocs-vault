---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/CoreLocation.html
archived_at: '2026-07-15T07:34:45.213446Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# CoreLocation Changes

## CoreLocation

CLBeaconRegion.h (Added)Added [CLBeaconMajorValue](https://developer.apple.com/documentation/corelocation/clbeaconmajorvalue)Added [CLBeaconMinorValue](https://developer.apple.com/documentation/corelocation/clbeaconminorvalue)CLCircularRegion.h (Added)Added [CLCircularRegion](https://developer.apple.com/documentation/corelocation/clcircularregion)Added [CLCircularRegion.center](https://developer.apple.com/documentation/corelocation/clcircularregion/1423601-center)Added [-[CLCircularRegion containsCoordinate:]](https://developer.apple.com/documentation/corelocation/clcircularregion/1423697-containscoordinate)Added [-[CLCircularRegion initWithCenter:radius:identifier:]](https://developer.apple.com/documentation/corelocation/clcircularregion/1423761-initwithcenter)Added [CLCircularRegion.radius](https://developer.apple.com/documentation/corelocation/clcircularregion/1423734-radius)CLError.hAdded [kCLErrorRangingFailure](https://developer.apple.com/documentation/corelocation/clerror/kclerrorrangingfailure)Added [kCLErrorRangingUnavailable](https://developer.apple.com/documentation/corelocation/clerror/kclerrorrangingunavailable)CLHeading.hRemoved -[CLHeading description]Added CLHeading.descriptionModified [CLHeading](https://developer.apple.com/documentation/corelocation/clheading)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

Modified [CLHeading.timestamp](https://developer.apple.com/documentation/corelocation/clheading/1423525-timestamp)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) NSDate *timestamp ``` |
| To | ``` @property(readonly, nonatomic, copy) NSDate *timestamp ``` |

CLLocation.hRemoved -[CLLocation description]Removed [CLLocationDistanceMax](https://developer.apple.com/documentation/corelocation/cllocationdistancemax)Removed [CLTimeIntervalMax](https://developer.apple.com/documentation/corelocation/cltimeintervalmax)Added CLLocation.descriptionModified [CLLocation](https://developer.apple.com/documentation/corelocation/cllocation)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

Modified [-[CLLocation initWithCoordinate:altitude:horizontalAccuracy:verticalAccuracy:course:speed:timestamp:]](https://developer.apple.com/documentation/corelocation/cllocation/1423718-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCoordinate:(CLLocationCoordinate2D)coordinate altitude:(CLLocationDistance)altitude horizontalAccuracy:(CLLocationAccuracy)hAccuracy verticalAccuracy:(CLLocationAccuracy)vAccuracy course:(CLLocationDirection)course speed:(CLLocationSpeed)speed timestamp:(NSDate *)timestamp ``` |
| To | ``` - (instancetype)initWithCoordinate:(CLLocationCoordinate2D)coordinate altitude:(CLLocationDistance)altitude horizontalAccuracy:(CLLocationAccuracy)hAccuracy verticalAccuracy:(CLLocationAccuracy)vAccuracy course:(CLLocationDirection)course speed:(CLLocationSpeed)speed timestamp:(NSDate *)timestamp ``` |

Modified [-[CLLocation initWithCoordinate:altitude:horizontalAccuracy:verticalAccuracy:timestamp:]](https://developer.apple.com/documentation/corelocation/cllocation/1423666-initwithcoordinate)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCoordinate:(CLLocationCoordinate2D)coordinate altitude:(CLLocationDistance)altitude horizontalAccuracy:(CLLocationAccuracy)hAccuracy verticalAccuracy:(CLLocationAccuracy)vAccuracy timestamp:(NSDate *)timestamp ``` |
| To | ``` - (instancetype)initWithCoordinate:(CLLocationCoordinate2D)coordinate altitude:(CLLocationDistance)altitude horizontalAccuracy:(CLLocationAccuracy)hAccuracy verticalAccuracy:(CLLocationAccuracy)vAccuracy timestamp:(NSDate *)timestamp ``` |

Modified [-[CLLocation initWithLatitude:longitude:]](https://developer.apple.com/documentation/corelocation/cllocation/1423660-initwithlatitude)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithLatitude:(CLLocationDegrees)latitude longitude:(CLLocationDegrees)longitude ``` |
| To | ``` - (instancetype)initWithLatitude:(CLLocationDegrees)latitude longitude:(CLLocationDegrees)longitude ``` |

Modified [CLLocation.timestamp](https://developer.apple.com/documentation/corelocation/cllocation/1423589-timestamp)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) NSDate *timestamp ``` |
| To | ``` @property(readonly, nonatomic, copy) NSDate *timestamp ``` |

CLLocationManager.hAdded [+[CLLocationManager isMonitoringAvailableForClass:]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423654-ismonitoringavailable)Added [-[CLLocationManager requestStateForRegion:]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423804-requeststate)Modified [CLLocationManager.location](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423687-location)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) CLLocation *location ``` |
| To | ``` @property(readonly, nonatomic, copy) CLLocation *location ``` |

Modified [CLLocationManager.monitoredRegions](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423790-monitoredregions)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) NSSet *monitoredRegions ``` |
| To | ``` @property(readonly, nonatomic, copy) NSSet *monitoredRegions ``` |

Modified [+[CLLocationManager regionMonitoringAvailable]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423564-regionmonitoringavailable)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [+[CLLocationManager regionMonitoringEnabled]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423585-regionmonitoringenabled)

|  | Deprecation |
| --- | --- |
| From | OS X 10.8 |
| To | OS X 10.10 |

CLLocationManagerDelegate.hAdded [-[CLLocationManagerDelegate locationManager:didDetermineState:forRegion:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423570-locationmanager)Modified [-[CLLocationManagerDelegate locationManager:didChangeAuthorizationStatus:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423701-locationmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CLLocationManagerDelegate locationManager:didEnterRegion:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423560-locationmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CLLocationManagerDelegate locationManager:didExitRegion:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423630-locationmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CLLocationManagerDelegate locationManager:didFailWithError:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423786-locationmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CLLocationManagerDelegate locationManager:didFinishDeferredUpdatesWithError:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423537-locationmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CLLocationManagerDelegate locationManager:didStartMonitoringForRegion:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423842-locationmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CLLocationManagerDelegate locationManager:didUpdateLocations:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423615-locationmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CLLocationManagerDelegate locationManager:didUpdateToLocation:fromLocation:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423716-locationmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CLLocationManagerDelegate locationManager:monitoringDidFailForRegion:withError:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423720-locationmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

CLPlacemark.hModified [CLPlacemark](https://developer.apple.com/documentation/corelocation/clplacemark)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

Modified [CLPlacemark.ISOcountryCode](https://developer.apple.com/documentation/corelocation/clplacemark/1423796-isocountrycode)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *ISOcountryCode ``` |
| To | ``` @property(nonatomic, readonly, copy) NSString *ISOcountryCode ``` |

Modified [CLPlacemark.addressDictionary](https://developer.apple.com/documentation/corelocation/clplacemark/1423605-addressdictionary)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSDictionary *addressDictionary ``` |
| To | ``` @property(nonatomic, readonly, copy) NSDictionary *addressDictionary ``` |

Modified [CLPlacemark.administrativeArea](https://developer.apple.com/documentation/corelocation/clplacemark/1423628-administrativearea)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *administrativeArea ``` |
| To | ``` @property(nonatomic, readonly, copy) NSString *administrativeArea ``` |

Modified [CLPlacemark.areasOfInterest](https://developer.apple.com/documentation/corelocation/clplacemark/1423673-areasofinterest)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *areasOfInterest ``` |
| To | ``` @property(nonatomic, readonly, copy) NSArray *areasOfInterest ``` |

Modified [CLPlacemark.country](https://developer.apple.com/documentation/corelocation/clplacemark/1423800-country)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *country ``` |
| To | ``` @property(nonatomic, readonly, copy) NSString *country ``` |

Modified [-[CLPlacemark initWithPlacemark:]](https://developer.apple.com/documentation/corelocation/clplacemark/1423818-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithPlacemark:(CLPlacemark *)placemark ``` |
| To | ``` - (instancetype)initWithPlacemark:(CLPlacemark *)placemark ``` |

Modified [CLPlacemark.inlandWater](https://developer.apple.com/documentation/corelocation/clplacemark/1423738-inlandwater)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *inlandWater ``` |
| To | ``` @property(nonatomic, readonly, copy) NSString *inlandWater ``` |

Modified [CLPlacemark.locality](https://developer.apple.com/documentation/corelocation/clplacemark/1423507-locality)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *locality ``` |
| To | ``` @property(nonatomic, readonly, copy) NSString *locality ``` |

Modified [CLPlacemark.location](https://developer.apple.com/documentation/corelocation/clplacemark/1423603-location)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) CLLocation *location ``` |
| To | ``` @property(nonatomic, readonly, copy) CLLocation *location ``` |

Modified [CLPlacemark.name](https://developer.apple.com/documentation/corelocation/clplacemark/1423634-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *name ``` |
| To | ``` @property(nonatomic, readonly, copy) NSString *name ``` |

Modified [CLPlacemark.ocean](https://developer.apple.com/documentation/corelocation/clplacemark/1423619-ocean)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *ocean ``` |
| To | ``` @property(nonatomic, readonly, copy) NSString *ocean ``` |

Modified [CLPlacemark.postalCode](https://developer.apple.com/documentation/corelocation/clplacemark/1423851-postalcode)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *postalCode ``` |
| To | ``` @property(nonatomic, readonly, copy) NSString *postalCode ``` |

Modified [CLPlacemark.region](https://developer.apple.com/documentation/corelocation/clplacemark/1423808-region)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) CLRegion *region ``` |
| To | ``` @property(nonatomic, readonly, copy) CLRegion *region ``` |

Modified [CLPlacemark.subAdministrativeArea](https://developer.apple.com/documentation/corelocation/clplacemark/1423776-subadministrativearea)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *subAdministrativeArea ``` |
| To | ``` @property(nonatomic, readonly, copy) NSString *subAdministrativeArea ``` |

Modified [CLPlacemark.subLocality](https://developer.apple.com/documentation/corelocation/clplacemark/1423794-sublocality)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *subLocality ``` |
| To | ``` @property(nonatomic, readonly, copy) NSString *subLocality ``` |

Modified [CLPlacemark.subThoroughfare](https://developer.apple.com/documentation/corelocation/clplacemark/1423782-subthoroughfare)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *subThoroughfare ``` |
| To | ``` @property(nonatomic, readonly, copy) NSString *subThoroughfare ``` |

Modified [CLPlacemark.thoroughfare](https://developer.apple.com/documentation/corelocation/clplacemark/1423814-thoroughfare)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *thoroughfare ``` |
| To | ``` @property(nonatomic, readonly, copy) NSString *thoroughfare ``` |

CLRegion.hAdded [CLRegion.notifyOnEntry](https://developer.apple.com/documentation/corelocation/clregion/1423566-notifyonentry)Added [CLRegion.notifyOnExit](https://developer.apple.com/documentation/corelocation/clregion/1423595-notifyonexit)Added [CLProximity](https://developer.apple.com/documentation/corelocation/clproximity)Added [CLRegionState](https://developer.apple.com/documentation/corelocation/clregionstate)Added [CLRegionStateInside](https://developer.apple.com/documentation/corelocation/clregionstate/clregionstateinside)Added [CLRegionStateOutside](https://developer.apple.com/documentation/corelocation/clregionstate/outside)Added [CLRegionStateUnknown](https://developer.apple.com/documentation/corelocation/clregionstate/unknown)Modified [CLRegion](https://developer.apple.com/documentation/corelocation/clregion)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

Modified [CLRegion.center](https://developer.apple.com/documentation/corelocation/clregion/1423691-center)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[CLRegion containsCoordinate:]](https://developer.apple.com/documentation/corelocation/clregion/1423828-contains)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [CLRegion.identifier](https://developer.apple.com/documentation/corelocation/clregion/1423583-identifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) NSString *identifier ``` |
| To | ``` @property(readonly, nonatomic, copy) NSString *identifier ``` |

Modified [-[CLRegion initCircularRegionWithCenter:radius:identifier:]](https://developer.apple.com/documentation/corelocation/clregion/1423681-init)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` - (id)initCircularRegionWithCenter:(CLLocationCoordinate2D)center radius:(CLLocationDistance)radius identifier:(NSString *)identifier ``` | -- |
| To | ``` - (instancetype)initCircularRegionWithCenter:(CLLocationCoordinate2D)center radius:(CLLocationDistance)radius identifier:(NSString *)identifier ``` | OS X 10.10 |

Modified [CLRegion.radius](https://developer.apple.com/documentation/corelocation/clregion/1423730-radius)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

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
