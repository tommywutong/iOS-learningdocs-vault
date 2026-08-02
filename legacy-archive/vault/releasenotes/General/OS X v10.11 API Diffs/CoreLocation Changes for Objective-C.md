---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/CoreLocation.html
archived_at: '2026-07-18T02:52:59.755653Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# CoreLocation Changes for Objective-C

### CoreLocation

#### CLCircularRegion.h

Modified [-[CLCircularRegion initWithCenter:radius:identifier:]](https://developer.apple.com/documentation/corelocation/clcircularregion/1423761-initwithcenter)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithCenter:(CLLocationCoordinate2D)center radius:(CLLocationDistance)radius identifier:(NSString *)identifier ``` |
| To | ``` - (instancetype _Nonnull)initWithCenter:(CLLocationCoordinate2D)center radius:(CLLocationDistance)radius identifier:(NSString * _Nonnull)identifier ``` |

#### CLGeocoder.h

Modified [-[CLGeocoder geocodeAddressDictionary:completionHandler:]](https://developer.apple.com/documentation/corelocation/clgeocoder/1423693-geocodeaddressdictionary)

|  | Declaration |
| --- | --- |
| From | ``` - (void)geocodeAddressDictionary:(NSDictionary *)addressDictionary completionHandler:(CLGeocodeCompletionHandler)completionHandler ``` |
| To | ``` - (void)geocodeAddressDictionary:(NSDictionary * _Nonnull)addressDictionary completionHandler:(CLGeocodeCompletionHandler _Nonnull)completionHandler ``` |

Modified [-[CLGeocoder geocodeAddressString:completionHandler:]](https://developer.apple.com/documentation/corelocation/clgeocoder/1423509-geocodeaddressstring)

|  | Declaration |
| --- | --- |
| From | ``` - (void)geocodeAddressString:(NSString *)addressString completionHandler:(CLGeocodeCompletionHandler)completionHandler ``` |
| To | ``` - (void)geocodeAddressString:(NSString * _Nonnull)addressString completionHandler:(CLGeocodeCompletionHandler _Nonnull)completionHandler ``` |

Modified [-[CLGeocoder geocodeAddressString:inRegion:completionHandler:]](https://developer.apple.com/documentation/corelocation/clgeocoder/1423591-geocodeaddressstring)

|  | Declaration |
| --- | --- |
| From | ``` - (void)geocodeAddressString:(NSString *)addressString inRegion:(CLRegion *)region completionHandler:(CLGeocodeCompletionHandler)completionHandler ``` |
| To | ``` - (void)geocodeAddressString:(NSString * _Nonnull)addressString inRegion:(CLRegion * _Nullable)region completionHandler:(CLGeocodeCompletionHandler _Nonnull)completionHandler ``` |

Modified [-[CLGeocoder reverseGeocodeLocation:completionHandler:]](https://developer.apple.com/documentation/corelocation/clgeocoder/1423621-reversegeocodelocation)

|  | Declaration |
| --- | --- |
| From | ``` - (void)reverseGeocodeLocation:(CLLocation *)location completionHandler:(CLGeocodeCompletionHandler)completionHandler ``` |
| To | ``` - (void)reverseGeocodeLocation:(CLLocation * _Nonnull)location completionHandler:(CLGeocodeCompletionHandler _Nonnull)completionHandler ``` |

#### CLHeading.h

Modified CLHeading.description

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSString *description ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) NSString *description ``` |

Modified [CLHeading.timestamp](https://developer.apple.com/documentation/corelocation/clheading/1423525-timestamp)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic, copy) NSDate *timestamp ``` |
| To | ``` @property(readonly, nonatomic, copy, nonnull) NSDate *timestamp ``` |

#### CLLocation.h

Modified CLLocation.description

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSString *description ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) NSString *description ``` |

Modified [-[CLLocation distanceFromLocation:]](https://developer.apple.com/documentation/corelocation/cllocation/1423689-distancefromlocation)

|  | Declaration |
| --- | --- |
| From | ``` - (CLLocationDistance)distanceFromLocation:(const CLLocation *)location ``` |
| To | ``` - (CLLocationDistance)distanceFromLocation:(const CLLocation * _Nonnull)location ``` |

Modified [-[CLLocation initWithCoordinate:altitude:horizontalAccuracy:verticalAccuracy:course:speed:timestamp:]](https://developer.apple.com/documentation/corelocation/cllocation/1423718-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithCoordinate:(CLLocationCoordinate2D)coordinate altitude:(CLLocationDistance)altitude horizontalAccuracy:(CLLocationAccuracy)hAccuracy verticalAccuracy:(CLLocationAccuracy)vAccuracy course:(CLLocationDirection)course speed:(CLLocationSpeed)speed timestamp:(NSDate *)timestamp ``` |
| To | ``` - (instancetype _Nonnull)initWithCoordinate:(CLLocationCoordinate2D)coordinate altitude:(CLLocationDistance)altitude horizontalAccuracy:(CLLocationAccuracy)hAccuracy verticalAccuracy:(CLLocationAccuracy)vAccuracy course:(CLLocationDirection)course speed:(CLLocationSpeed)speed timestamp:(NSDate * _Nonnull)timestamp ``` |

Modified [-[CLLocation initWithCoordinate:altitude:horizontalAccuracy:verticalAccuracy:timestamp:]](https://developer.apple.com/documentation/corelocation/cllocation/1423666-initwithcoordinate)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithCoordinate:(CLLocationCoordinate2D)coordinate altitude:(CLLocationDistance)altitude horizontalAccuracy:(CLLocationAccuracy)hAccuracy verticalAccuracy:(CLLocationAccuracy)vAccuracy timestamp:(NSDate *)timestamp ``` |
| To | ``` - (instancetype _Nonnull)initWithCoordinate:(CLLocationCoordinate2D)coordinate altitude:(CLLocationDistance)altitude horizontalAccuracy:(CLLocationAccuracy)hAccuracy verticalAccuracy:(CLLocationAccuracy)vAccuracy timestamp:(NSDate * _Nonnull)timestamp ``` |

Modified [-[CLLocation initWithLatitude:longitude:]](https://developer.apple.com/documentation/corelocation/cllocation/1423660-initwithlatitude)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithLatitude:(CLLocationDegrees)latitude longitude:(CLLocationDegrees)longitude ``` |
| To | ``` - (instancetype _Nonnull)initWithLatitude:(CLLocationDegrees)latitude longitude:(CLLocationDegrees)longitude ``` |

Modified [CLLocation.timestamp](https://developer.apple.com/documentation/corelocation/cllocation/1423589-timestamp)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic, copy) NSDate *timestamp ``` |
| To | ``` @property(readonly, nonatomic, copy, nonnull) NSDate *timestamp ``` |

#### CLLocationManager.h

Modified [CLLocationManager.delegate](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423792-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, nonatomic) id<CLLocationManagerDelegate> delegate ``` |
| To | ``` @property(assign, nonatomic, nullable) id<CLLocationManagerDelegate> delegate ``` |

Modified [+[CLLocationManager isMonitoringAvailableForClass:]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423654-ismonitoringavailable)

|  | Declaration |
| --- | --- |
| From | ``` + (BOOL)isMonitoringAvailableForClass:(Class)regionClass ``` |
| To | ``` + (BOOL)isMonitoringAvailableForClass:(Class _Nonnull)regionClass ``` |

Modified [CLLocationManager.location](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423687-location)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic, copy) CLLocation *location ``` |
| To | ``` @property(readonly, nonatomic, copy, nullable) CLLocation *location ``` |

Modified [CLLocationManager.monitoredRegions](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423790-monitoredregions)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic, copy) NSSet *monitoredRegions ``` |
| To | ``` @property(readonly, nonatomic, copy, nonnull) NSSet<__kindof CLRegion *> *monitoredRegions ``` |

Modified [CLLocationManager.purpose](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423742-purpose)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, nonatomic) NSString *purpose ``` |
| To | ``` @property(copy, nonatomic, nullable) NSString *purpose ``` |

Modified [-[CLLocationManager requestStateForRegion:]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423804-requeststate)

|  | Declaration |
| --- | --- |
| From | ``` - (void)requestStateForRegion:(CLRegion *)region ``` |
| To | ``` - (void)requestStateForRegion:(CLRegion * _Nonnull)region ``` |

Modified [-[CLLocationManager startMonitoringForRegion:]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423656-startmonitoringforregion)

|  | Declaration |
| --- | --- |
| From | ``` - (void)startMonitoringForRegion:(CLRegion *)region ``` |
| To | ``` - (void)startMonitoringForRegion:(CLRegion * _Nonnull)region ``` |

Modified [-[CLLocationManager stopMonitoringForRegion:]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423840-stopmonitoringforregion)

|  | Declaration |
| --- | --- |
| From | ``` - (void)stopMonitoringForRegion:(CLRegion *)region ``` |
| To | ``` - (void)stopMonitoringForRegion:(CLRegion * _Nonnull)region ``` |

#### CLLocationManagerDelegate.h

Modified [-[CLLocationManagerDelegate locationManager:didChangeAuthorizationStatus:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423701-locationmanager)

|  | Declaration |
| --- | --- |
| From | ``` - (void)locationManager:(CLLocationManager *)manager didChangeAuthorizationStatus:(CLAuthorizationStatus)status ``` |
| To | ``` - (void)locationManager:(CLLocationManager * _Nonnull)manager didChangeAuthorizationStatus:(CLAuthorizationStatus)status ``` |

Modified [-[CLLocationManagerDelegate locationManager:didDetermineState:forRegion:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423570-locationmanager)

|  | Declaration |
| --- | --- |
| From | ``` - (void)locationManager:(CLLocationManager *)manager didDetermineState:(CLRegionState)state forRegion:(CLRegion *)region ``` |
| To | ``` - (void)locationManager:(CLLocationManager * _Nonnull)manager didDetermineState:(CLRegionState)state forRegion:(CLRegion * _Nonnull)region ``` |

Modified [-[CLLocationManagerDelegate locationManager:didEnterRegion:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423560-locationmanager)

|  | Declaration |
| --- | --- |
| From | ``` - (void)locationManager:(CLLocationManager *)manager didEnterRegion:(CLRegion *)region ``` |
| To | ``` - (void)locationManager:(CLLocationManager * _Nonnull)manager didEnterRegion:(CLRegion * _Nonnull)region ``` |

Modified [-[CLLocationManagerDelegate locationManager:didExitRegion:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423630-locationmanager)

|  | Declaration |
| --- | --- |
| From | ``` - (void)locationManager:(CLLocationManager *)manager didExitRegion:(CLRegion *)region ``` |
| To | ``` - (void)locationManager:(CLLocationManager * _Nonnull)manager didExitRegion:(CLRegion * _Nonnull)region ``` |

Modified [-[CLLocationManagerDelegate locationManager:didFailWithError:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423786-locationmanager)

|  | Declaration |
| --- | --- |
| From | ``` - (void)locationManager:(CLLocationManager *)manager didFailWithError:(NSError *)error ``` |
| To | ``` - (void)locationManager:(CLLocationManager * _Nonnull)manager didFailWithError:(NSError * _Nonnull)error ``` |

Modified [-[CLLocationManagerDelegate locationManager:didFinishDeferredUpdatesWithError:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423537-locationmanager)

|  | Declaration |
| --- | --- |
| From | ``` - (void)locationManager:(CLLocationManager *)manager didFinishDeferredUpdatesWithError:(NSError *)error ``` |
| To | ``` - (void)locationManager:(CLLocationManager * _Nonnull)manager didFinishDeferredUpdatesWithError:(NSError * _Nullable)error ``` |

Modified [-[CLLocationManagerDelegate locationManager:didStartMonitoringForRegion:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423842-locationmanager)

|  | Declaration |
| --- | --- |
| From | ``` - (void)locationManager:(CLLocationManager *)manager didStartMonitoringForRegion:(CLRegion *)region ``` |
| To | ``` - (void)locationManager:(CLLocationManager * _Nonnull)manager didStartMonitoringForRegion:(CLRegion * _Nonnull)region ``` |

Modified [-[CLLocationManagerDelegate locationManager:didUpdateLocations:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423615-locationmanager)

|  | Declaration |
| --- | --- |
| From | ``` - (void)locationManager:(CLLocationManager *)manager didUpdateLocations:(NSArray *)locations ``` |
| To | ``` - (void)locationManager:(CLLocationManager * _Nonnull)manager didUpdateLocations:(NSArray * _Nonnull)locations ``` |

Modified [-[CLLocationManagerDelegate locationManager:didUpdateToLocation:fromLocation:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423716-locationmanager)

|  | Declaration |
| --- | --- |
| From | ``` - (void)locationManager:(CLLocationManager *)manager didUpdateToLocation:(CLLocation *)newLocation fromLocation:(CLLocation *)oldLocation ``` |
| To | ``` - (void)locationManager:(CLLocationManager * _Nonnull)manager didUpdateToLocation:(CLLocation * _Nonnull)newLocation fromLocation:(CLLocation * _Nonnull)oldLocation ``` |

Modified [-[CLLocationManagerDelegate locationManager:monitoringDidFailForRegion:withError:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423720-locationmanager)

|  | Declaration |
| --- | --- |
| From | ``` - (void)locationManager:(CLLocationManager *)manager monitoringDidFailForRegion:(CLRegion *)region withError:(NSError *)error ``` |
| To | ``` - (void)locationManager:(CLLocationManager * _Nonnull)manager monitoringDidFailForRegion:(CLRegion * _Nullable)region withError:(NSError * _Nonnull)error ``` |

#### CLPlacemark.h

Added [CLPlacemark.timeZone](https://developer.apple.com/documentation/corelocation/clplacemark/1423707-timezone)Modified [CLPlacemark.addressDictionary](https://developer.apple.com/documentation/corelocation/clplacemark/1423605-addressdictionary)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSDictionary *addressDictionary ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSDictionary *addressDictionary ``` |

Modified [CLPlacemark.administrativeArea](https://developer.apple.com/documentation/corelocation/clplacemark/1423628-administrativearea)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSString *administrativeArea ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSString *administrativeArea ``` |

Modified [CLPlacemark.areasOfInterest](https://developer.apple.com/documentation/corelocation/clplacemark/1423673-areasofinterest)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSArray *areasOfInterest ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSArray<NSString *> *areasOfInterest ``` |

Modified [CLPlacemark.country](https://developer.apple.com/documentation/corelocation/clplacemark/1423800-country)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSString *country ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSString *country ``` |

Modified [-[CLPlacemark initWithPlacemark:]](https://developer.apple.com/documentation/corelocation/clplacemark/1423818-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithPlacemark:(CLPlacemark *)placemark ``` |
| To | ``` - (instancetype _Nonnull)initWithPlacemark:(CLPlacemark * _Nonnull)placemark ``` |

Modified [CLPlacemark.inlandWater](https://developer.apple.com/documentation/corelocation/clplacemark/1423738-inlandwater)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSString *inlandWater ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSString *inlandWater ``` |

Modified [CLPlacemark.ISOcountryCode](https://developer.apple.com/documentation/corelocation/clplacemark/1423796-isocountrycode)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSString *ISOcountryCode ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSString *ISOcountryCode ``` |

Modified [CLPlacemark.locality](https://developer.apple.com/documentation/corelocation/clplacemark/1423507-locality)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSString *locality ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSString *locality ``` |

Modified [CLPlacemark.location](https://developer.apple.com/documentation/corelocation/clplacemark/1423603-location)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) CLLocation *location ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) CLLocation *location ``` |

Modified [CLPlacemark.name](https://developer.apple.com/documentation/corelocation/clplacemark/1423634-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSString *name ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSString *name ``` |

Modified [CLPlacemark.ocean](https://developer.apple.com/documentation/corelocation/clplacemark/1423619-ocean)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSString *ocean ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSString *ocean ``` |

Modified [CLPlacemark.postalCode](https://developer.apple.com/documentation/corelocation/clplacemark/1423851-postalcode)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSString *postalCode ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSString *postalCode ``` |

Modified [CLPlacemark.region](https://developer.apple.com/documentation/corelocation/clplacemark/1423808-region)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) CLRegion *region ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) CLRegion *region ``` |

Modified [CLPlacemark.subAdministrativeArea](https://developer.apple.com/documentation/corelocation/clplacemark/1423776-subadministrativearea)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSString *subAdministrativeArea ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSString *subAdministrativeArea ``` |

Modified [CLPlacemark.subLocality](https://developer.apple.com/documentation/corelocation/clplacemark/1423794-sublocality)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSString *subLocality ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSString *subLocality ``` |

Modified [CLPlacemark.subThoroughfare](https://developer.apple.com/documentation/corelocation/clplacemark/1423782-subthoroughfare)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSString *subThoroughfare ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSString *subThoroughfare ``` |

Modified [CLPlacemark.thoroughfare](https://developer.apple.com/documentation/corelocation/clplacemark/1423814-thoroughfare)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSString *thoroughfare ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSString *thoroughfare ``` |

#### CLRegion.h

Modified [CLRegion.identifier](https://developer.apple.com/documentation/corelocation/clregion/1423583-identifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic, copy) NSString *identifier ``` |
| To | ``` @property(readonly, nonatomic, copy, nonnull) NSString *identifier ``` |

Modified [-[CLRegion initCircularRegionWithCenter:radius:identifier:]](https://developer.apple.com/documentation/corelocation/clregion/1423681-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initCircularRegionWithCenter:(CLLocationCoordinate2D)center radius:(CLLocationDistance)radius identifier:(NSString *)identifier ``` |
| To | ``` - (instancetype _Nonnull)initCircularRegionWithCenter:(CLLocationCoordinate2D)center radius:(CLLocationDistance)radius identifier:(NSString * _Nonnull)identifier ``` |

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
