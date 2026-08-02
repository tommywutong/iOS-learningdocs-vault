---
title: iOS 8.0 API Diffs
apple_id: TP40014455
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS80APIDiffs/frameworks/CoreLocation.html
archived_at: '2026-07-18T02:55:56.624515Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.0 API Diffs](iOS%207.1%20to%20iOS%208.0%20API%20Differences.md)


# CoreLocation Changes

## CoreLocation

CLBeaconRegion.hModified [CLBeacon.major](https://developer.apple.com/documentation/corelocation/clbeacon/1621418-major)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) NSNumber *major ``` |
| To | ``` @property(readonly, nonatomic, strong) NSNumber *major ``` |

Modified [CLBeacon.minor](https://developer.apple.com/documentation/corelocation/clbeacon/1621558-minor)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) NSNumber *minor ``` |
| To | ``` @property(readonly, nonatomic, strong) NSNumber *minor ``` |

Modified [CLBeacon.proximityUUID](https://developer.apple.com/documentation/corelocation/clbeacon/1621508-proximityuuid)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) NSUUID *proximityUUID ``` |
| To | ``` @property(readonly, nonatomic, strong) NSUUID *proximityUUID ``` |

Modified [-[CLBeaconRegion initWithProximityUUID:identifier:]](https://developer.apple.com/documentation/corelocation/clbeaconregion/1621534-initwithproximityuuid)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithProximityUUID:(NSUUID *)proximityUUID identifier:(NSString *)identifier ``` |
| To | ``` - (instancetype)initWithProximityUUID:(NSUUID *)proximityUUID identifier:(NSString *)identifier ``` |

Modified [-[CLBeaconRegion initWithProximityUUID:major:identifier:]](https://developer.apple.com/documentation/corelocation/clbeaconregion/1621475-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithProximityUUID:(NSUUID *)proximityUUID major:(CLBeaconMajorValue)major identifier:(NSString *)identifier ``` |
| To | ``` - (instancetype)initWithProximityUUID:(NSUUID *)proximityUUID major:(CLBeaconMajorValue)major identifier:(NSString *)identifier ``` |

Modified [-[CLBeaconRegion initWithProximityUUID:major:minor:identifier:]](https://developer.apple.com/documentation/corelocation/clbeaconregion/1621392-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithProximityUUID:(NSUUID *)proximityUUID major:(CLBeaconMajorValue)major minor:(CLBeaconMinorValue)minor identifier:(NSString *)identifier ``` |
| To | ``` - (instancetype)initWithProximityUUID:(NSUUID *)proximityUUID major:(CLBeaconMajorValue)major minor:(CLBeaconMinorValue)minor identifier:(NSString *)identifier ``` |

Modified [CLBeaconRegion.major](https://developer.apple.com/documentation/corelocation/clbeaconregion/1621536-major)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) NSNumber *major ``` |
| To | ``` @property(readonly, nonatomic, strong) NSNumber *major ``` |

Modified [CLBeaconRegion.minor](https://developer.apple.com/documentation/corelocation/clbeaconregion/1621414-minor)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) NSNumber *minor ``` |
| To | ``` @property(readonly, nonatomic, strong) NSNumber *minor ``` |

Modified [CLBeaconRegion.proximityUUID](https://developer.apple.com/documentation/corelocation/clbeaconregion/1621556-proximityuuid)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) NSUUID *proximityUUID ``` |
| To | ``` @property(readonly, nonatomic, strong) NSUUID *proximityUUID ``` |

CLCircularRegion.hModified [-[CLCircularRegion initWithCenter:radius:identifier:]](https://developer.apple.com/documentation/corelocation/clcircularregion/1423761-initwithcenter)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCenter:(CLLocationCoordinate2D)center radius:(CLLocationDistance)radius identifier:(NSString *)identifier ``` |
| To | ``` - (instancetype)initWithCenter:(CLLocationCoordinate2D)center radius:(CLLocationDistance)radius identifier:(NSString *)identifier ``` |

CLHeading.hRemoved -[CLHeading description]Added CLHeading.descriptionModified [CLHeading.timestamp](https://developer.apple.com/documentation/corelocation/clheading/1423525-timestamp)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) NSDate *timestamp ``` |
| To | ``` @property(readonly, nonatomic, copy) NSDate *timestamp ``` |

CLLocation.hRemoved -[CLLocation description]Added [CLFloor](https://developer.apple.com/documentation/corelocation/clfloor)Added [CLFloor.level](https://developer.apple.com/documentation/corelocation/clfloor/1616759-level)Added CLLocation.descriptionAdded [CLLocation.floor](https://developer.apple.com/documentation/corelocation/cllocation/1616762-floor)Modified [-[CLLocation initWithCoordinate:altitude:horizontalAccuracy:verticalAccuracy:course:speed:timestamp:]](https://developer.apple.com/documentation/corelocation/cllocation/1423718-init)

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

CLLocationManager+CLVisitExtensions.h (Added)Added [-[CLLocationManager startMonitoringVisits]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1618692-startmonitoringvisits)Added [-[CLLocationManager stopMonitoringVisits]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1618693-stopmonitoringvisits)Added CLLocationManager(CLVisitExtensions)CLLocationManager.hAdded [-[CLLocationManager requestAlwaysAuthorization]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1620551-requestalwaysauthorization)Added [-[CLLocationManager requestWhenInUseAuthorization]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1620562-requestwheninuseauthorization)Added [kCLAuthorizationStatusAuthorizedAlways](https://developer.apple.com/documentation/corelocation/clauthorizationstatus/kclauthorizationstatusauthorizedalways)Added [kCLAuthorizationStatusAuthorizedWhenInUse](https://developer.apple.com/documentation/corelocation/clauthorizationstatus/authorizedwheninuse)Modified [CLLocationManager.heading](https://developer.apple.com/documentation/corelocation/cllocationmanager/1620555-heading)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) CLHeading *heading ``` |
| To | ``` @property(readonly, nonatomic, copy) CLHeading *heading ``` |

Modified [CLLocationManager.location](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423687-location)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) CLLocation *location ``` |
| To | ``` @property(readonly, nonatomic, copy) CLLocation *location ``` |

Modified [CLLocationManager.monitoredRegions](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423790-monitoredregions)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) NSSet *monitoredRegions ``` |
| To | ``` @property(readonly, nonatomic, copy) NSSet *monitoredRegions ``` |

Modified [CLLocationManager.rangedRegions](https://developer.apple.com/documentation/corelocation/cllocationmanager/1620552-rangedregions)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) NSSet *rangedRegions ``` |
| To | ``` @property(readonly, nonatomic, copy) NSSet *rangedRegions ``` |

Modified [kCLAuthorizationStatusAuthorized](https://developer.apple.com/documentation/corelocation/clauthorizationstatus/kclauthorizationstatusauthorized)

|  | Deprecation | Introduction |
| --- | --- | --- |
| From | -- | iOS 4.2 |
| To | iOS 8.0 | iOS 2.0 |

CLLocationManagerDelegate.hAdded [-[CLLocationManagerDelegate locationManager:didVisit:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1621529-locationmanager)Modified [-[CLLocationManagerDelegate locationManager:didChangeAuthorizationStatus:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423701-locationmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CLLocationManagerDelegate locationManager:didDetermineState:forRegion:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423570-locationmanager)

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

Modified [-[CLLocationManagerDelegate locationManager:didRangeBeacons:inRegion:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1621501-locationmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CLLocationManagerDelegate locationManager:didStartMonitoringForRegion:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423842-locationmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CLLocationManagerDelegate locationManager:didUpdateHeading:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1621555-locationmanager)

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

Modified [-[CLLocationManagerDelegate locationManager:rangingBeaconsDidFailForRegion:withError:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1621483-locationmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CLLocationManagerDelegate locationManagerDidPauseLocationUpdates:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1621553-locationmanagerdidpauselocationu)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CLLocationManagerDelegate locationManagerDidResumeLocationUpdates:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1621512-locationmanagerdidresumelocation)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CLLocationManagerDelegate locationManagerShouldDisplayHeadingCalibration:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1621457-locationmanagershoulddisplayhead)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

CLPlacemark.hModified [CLPlacemark.ISOcountryCode](https://developer.apple.com/documentation/corelocation/clplacemark/1423796-isocountrycode)

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

CLRegion.hModified [CLRegion.identifier](https://developer.apple.com/documentation/corelocation/clregion/1423583-identifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) NSString *identifier ``` |
| To | ``` @property(readonly, nonatomic, copy) NSString *identifier ``` |

Modified [-[CLRegion initCircularRegionWithCenter:radius:identifier:]](https://developer.apple.com/documentation/corelocation/clregion/1423681-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initCircularRegionWithCenter:(CLLocationCoordinate2D)center radius:(CLLocationDistance)radius identifier:(NSString *)identifier ``` |
| To | ``` - (instancetype)initCircularRegionWithCenter:(CLLocationCoordinate2D)center radius:(CLLocationDistance)radius identifier:(NSString *)identifier ``` |

CLVisit.h (Added)Added [CLVisit](https://developer.apple.com/documentation/corelocation/clvisit)Added [CLVisit.arrivalDate](https://developer.apple.com/documentation/corelocation/clvisit/1614681-arrivaldate)Added [CLVisit.coordinate](https://developer.apple.com/documentation/corelocation/clvisit/1614677-coordinate)Added [CLVisit.departureDate](https://developer.apple.com/documentation/corelocation/clvisit/1614685-departuredate)Added [CLVisit.horizontalAccuracy](https://developer.apple.com/documentation/corelocation/clvisit/1614679-horizontalaccuracy)

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
