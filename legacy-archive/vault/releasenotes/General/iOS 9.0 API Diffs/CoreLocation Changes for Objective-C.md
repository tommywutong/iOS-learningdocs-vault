---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/CoreLocation.html
archived_at: '2026-07-18T02:56:32.169953Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# CoreLocation Changes for Objective-C

### CoreLocation

#### CLBeaconRegion.h

Modified [-[CLBeaconRegion peripheralDataWithMeasuredPower:]](https://developer.apple.com/documentation/corelocation/clbeaconregion/1621494-peripheraldatawithmeasuredpower)

|  | Declaration |
| --- | --- |
| From | ``` - (NSMutableDictionary *)peripheralDataWithMeasuredPower:(NSNumber *)measuredPower ``` |
| To | ``` - (NSMutableDictionary<NSString *,id> * _Nonnull)peripheralDataWithMeasuredPower:(NSNumber * _Nullable)measuredPower ``` |

#### CLLocationManager.h

Added [CLLocationManager.allowsBackgroundLocationUpdates](https://developer.apple.com/documentation/corelocation/cllocationmanager/1620568-allowsbackgroundlocationupdates)Added [-[CLLocationManager requestLocation]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1620548-requestlocation)Modified [CLLocationManager.monitoredRegions](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423790-monitoredregions)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic, copy) NSSet *monitoredRegions ``` |
| To | ``` @property(readonly, nonatomic, copy, nonnull) NSSet<__kindof CLRegion *> *monitoredRegions ``` |

Modified [CLLocationManager.rangedRegions](https://developer.apple.com/documentation/corelocation/cllocationmanager/1620552-rangedregions)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic, copy) NSSet *rangedRegions ``` |
| To | ``` @property(readonly, nonatomic, copy, nonnull) NSSet<__kindof CLRegion *> *rangedRegions ``` |

#### CLLocationManagerDelegate.h

Modified [-[CLLocationManagerDelegate locationManager:didRangeBeacons:inRegion:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1621501-locationmanager)

|  | Declaration |
| --- | --- |
| From | ``` - (void)locationManager:(CLLocationManager *)manager didRangeBeacons:(NSArray *)beacons inRegion:(CLBeaconRegion *)region ``` |
| To | ``` - (void)locationManager:(CLLocationManager * _Nonnull)manager didRangeBeacons:(NSArray<CLBeacon *> * _Nonnull)beacons inRegion:(CLBeaconRegion * _Nonnull)region ``` |

Modified [-[CLLocationManagerDelegate locationManager:didUpdateLocations:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423615-locationmanager)

|  | Declaration |
| --- | --- |
| From | ``` - (void)locationManager:(CLLocationManager *)manager didUpdateLocations:(NSArray *)locations ``` |
| To | ``` - (void)locationManager:(CLLocationManager * _Nonnull)manager didUpdateLocations:(NSArray<CLLocation *> * _Nonnull)locations ``` |

#### CLPlacemark.h

Added [CLPlacemark.timeZone](https://developer.apple.com/documentation/corelocation/clplacemark/1423707-timezone)Modified [CLPlacemark.areasOfInterest](https://developer.apple.com/documentation/corelocation/clplacemark/1423673-areasofinterest)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSArray *areasOfInterest ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSArray<NSString *> *areasOfInterest ``` |

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
