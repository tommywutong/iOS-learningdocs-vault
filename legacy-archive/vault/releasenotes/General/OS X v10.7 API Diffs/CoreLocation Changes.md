---
title: OS X v10.7 API Diffs
apple_id: TP40010630
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/MacOSXLionAPIDiffs/CoreLocation.html
archived_at: '2026-07-18T02:54:26.686489Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.7 API Diffs](OS%20X%20v10.6%20to%20v10.7%20API%20Diffs.md)


# CoreLocation Changes

## CoreLocation

|  | Framework Architectures |
| --- | --- |
| From | i386,ppc,x86_64 |
| To | i386,x86_64 |

CLError.hAdded [CLError](https://developer.apple.com/documentation/corelocation/clerror/code)Added [kCLErrorGeocodeCanceled](https://developer.apple.com/documentation/corelocation/clerror/kclerrorgeocodecanceled)Added [kCLErrorGeocodeFoundNoResult](https://developer.apple.com/documentation/corelocation/clerror/code/geocodefoundnoresult)Added [kCLErrorHeadingFailure](https://developer.apple.com/documentation/corelocation/clerror/kclerrorheadingfailure)Added [kCLErrorNetwork](https://developer.apple.com/documentation/corelocation/clerror/kclerrornetwork)Added [kCLErrorRegionMonitoringDenied](https://developer.apple.com/documentation/corelocation/clerror/code/regionmonitoringdenied)Added [kCLErrorRegionMonitoringFailure](https://developer.apple.com/documentation/corelocation/clerror/code/regionmonitoringfailure)Added [kCLErrorRegionMonitoringSetupDelayed](https://developer.apple.com/documentation/corelocation/clerror/kclerrorregionmonitoringsetupdelayed)CLErrorDomain.hModified [kCLErrorDomain](https://developer.apple.com/documentation/corelocation/kclerrordomain)

|  | Header |
| --- | --- |
| From | CLError.h |
| To | CLErrorDomain.h |

CLHeading.hAdded [CLHeading](https://developer.apple.com/documentation/corelocation/clheading)Added -[CLHeading description]Added [CLHeading.headingAccuracy](https://developer.apple.com/documentation/corelocation/clheading/1423705-headingaccuracy)Added [CLHeading.magneticHeading](https://developer.apple.com/documentation/corelocation/clheading/1423763-magneticheading)Added [CLHeading.timestamp](https://developer.apple.com/documentation/corelocation/clheading/1423525-timestamp)Added [CLHeading.trueHeading](https://developer.apple.com/documentation/corelocation/clheading/1423568-trueheading)Added [CLHeading.x](https://developer.apple.com/documentation/corelocation/clheading/1423685-x)Added [CLHeading.y](https://developer.apple.com/documentation/corelocation/clheading/1423617-y)Added [CLHeading.z](https://developer.apple.com/documentation/corelocation/clheading/1423609-z)Added [CLHeadingComponentValue](https://developer.apple.com/documentation/corelocation/clheadingcomponentvalue)Added [kCLHeadingFilterNone](https://developer.apple.com/documentation/corelocation/kclheadingfilternone)CLLocation.hRemoved [-[CLLocation getDistanceFrom:]](https://developer.apple.com/documentation/corelocation/cllocation/1616758-getdistancefrom)Added [-[CLLocation initWithCoordinate:altitude:horizontalAccuracy:verticalAccuracy:course:speed:timestamp:]](https://developer.apple.com/documentation/corelocation/cllocation/1423718-init)Added [CLLocationCoordinate2DIsValid()](https://developer.apple.com/documentation/corelocation/1423806-cllocationcoordinate2disvalid)Added [CLLocationCoordinate2DMake()](https://developer.apple.com/documentation/corelocation/1423838-cllocationcoordinate2dmake)Added [kCLLocationAccuracyBestForNavigation](https://developer.apple.com/documentation/corelocation/kcllocationaccuracybestfornavigation)Added [kCLLocationCoordinate2DInvalid](https://developer.apple.com/documentation/corelocation/kcllocationcoordinate2dinvalid)Modified [CLLocation.horizontalAccuracy](https://developer.apple.com/documentation/corelocation/cllocation/1423599-horizontalaccuracy)

|  | Declaration |
| --- | --- |
| From | @property(readonly, ) CLLocationAccuracy horizontalAccuracy |
| To | @property(readonly, nonatomic) CLLocationAccuracy horizontalAccuracy |

Modified [CLLocation.coordinate](https://developer.apple.com/documentation/corelocation/cllocation/1423504-coordinate)

|  | Declaration |
| --- | --- |
| From | @property(readonly, ) CLLocationCoordinate2D coordinate |
| To | @property(readonly, nonatomic) CLLocationCoordinate2D coordinate |

Modified [CLLocation.verticalAccuracy](https://developer.apple.com/documentation/corelocation/cllocation/1423550-verticalaccuracy)

|  | Declaration |
| --- | --- |
| From | @property(readonly, ) CLLocationAccuracy verticalAccuracy |
| To | @property(readonly, nonatomic) CLLocationAccuracy verticalAccuracy |

Modified [CLLocation.altitude](https://developer.apple.com/documentation/corelocation/cllocation/1423820-altitude)

|  | Declaration |
| --- | --- |
| From | @property(readonly, ) CLLocationDistance altitude |
| To | @property(readonly, nonatomic) CLLocationDistance altitude |

Modified [CLLocation.timestamp](https://developer.apple.com/documentation/corelocation/cllocation/1423589-timestamp)

|  | Declaration |
| --- | --- |
| From | @property(readonly, ) NSDate \*timestamp |
| To | @property(readonly, nonatomic) NSDate \*timestamp |

Modified [CLLocation.speed](https://developer.apple.com/documentation/corelocation/cllocation/1423798-speed)

|  | Declaration |
| --- | --- |
| From | @property(readonly, ) CLLocationSpeed speed |
| To | @property(readonly, nonatomic) CLLocationSpeed speed |

Modified [CLLocation.course](https://developer.apple.com/documentation/corelocation/cllocation/1423832-course)

|  | Declaration |
| --- | --- |
| From | @property(readonly, ) CLLocationDirection course |
| To | @property(readonly, nonatomic) CLLocationDirection course |

CLLocationManager.hRemoved [CLLocationManager.locationServicesEnabled](https://developer.apple.com/documentation/corelocation/cllocationmanager/1620566-locationservicesenabled)Added [+[CLLocationManager authorizationStatus]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423523-authorizationstatus)Added [+[CLLocationManager headingAvailable]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423502-headingavailable)Added [CLLocationManager.maximumRegionMonitoringDistance](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423740-maximumregionmonitoringdistance)Added [CLLocationManager.monitoredRegions](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423790-monitoredregions)Added [CLLocationManager.purpose](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423742-purpose)Added [+[CLLocationManager regionMonitoringAvailable]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423564-regionmonitoringavailable)Added [+[CLLocationManager regionMonitoringEnabled]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423585-regionmonitoringenabled)Added [+[CLLocationManager significantLocationChangeMonitoringAvailable]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423677-significantlocationchangemonitor)Added [-[CLLocationManager startMonitoringForRegion:desiredAccuracy:]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1620560-startmonitoringforregion)Added [-[CLLocationManager startMonitoringSignificantLocationChanges]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423531-startmonitoringsignificantlocati)Added [-[CLLocationManager stopMonitoringForRegion:]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423840-stopmonitoringforregion)Added [-[CLLocationManager stopMonitoringSignificantLocationChanges]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423679-stopmonitoringsignificantlocatio)Added [CLAuthorizationStatus](https://developer.apple.com/documentation/corelocation/clauthorizationstatus)Added [CLDeviceOrientation](https://developer.apple.com/documentation/corelocation/cldeviceorientation)Added [CLDeviceOrientationFaceDown](https://developer.apple.com/documentation/corelocation/cldeviceorientation/cldeviceorientationfacedown)Added [CLDeviceOrientationFaceUp](https://developer.apple.com/documentation/corelocation/cldeviceorientation/cldeviceorientationfaceup)Added [CLDeviceOrientationLandscapeLeft](https://developer.apple.com/documentation/corelocation/cldeviceorientation/cldeviceorientationlandscapeleft)Added [CLDeviceOrientationLandscapeRight](https://developer.apple.com/documentation/corelocation/cldeviceorientation/landscaperight)Added [CLDeviceOrientationPortrait](https://developer.apple.com/documentation/corelocation/cldeviceorientation/cldeviceorientationportrait)Added [CLDeviceOrientationPortraitUpsideDown](https://developer.apple.com/documentation/corelocation/cldeviceorientation/cldeviceorientationportraitupsidedown)Added [CLDeviceOrientationUnknown](https://developer.apple.com/documentation/corelocation/cldeviceorientation/cldeviceorientationunknown)Added [kCLAuthorizationStatusAuthorized](https://developer.apple.com/documentation/corelocation/clauthorizationstatus/kclauthorizationstatusauthorized)Added [kCLAuthorizationStatusDenied](https://developer.apple.com/documentation/corelocation/clauthorizationstatus/kclauthorizationstatusdenied)Added [kCLAuthorizationStatusNotDetermined](https://developer.apple.com/documentation/corelocation/clauthorizationstatus/kclauthorizationstatusnotdetermined)Added [kCLAuthorizationStatusRestricted](https://developer.apple.com/documentation/corelocation/clauthorizationstatus/restricted)Modified [CLLocationManager.distanceFilter](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423500-distancefilter)

|  | Declaration |
| --- | --- |
| From | @property(assign, ) CLLocationDistance distanceFilter |
| To | @property(assign, nonatomic) CLLocationDistance distanceFilter |

Modified [CLLocationManager.location](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423687-location)

|  | Declaration |
| --- | --- |
| From | @property(readonly, ) CLLocation \*location |
| To | @property(readonly, nonatomic) CLLocation \*location |

Modified [CLLocationManager.desiredAccuracy](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423836-desiredaccuracy)

|  | Declaration |
| --- | --- |
| From | @property(assign, ) CLLocationAccuracy desiredAccuracy |
| To | @property(assign, nonatomic) CLLocationAccuracy desiredAccuracy |

Modified [CLLocationManager.delegate](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423792-delegate)

|  | Declaration |
| --- | --- |
| From | @property(assign, ) id<CLLocationManagerDelegate> delegate |
| To | @property(assign, nonatomic) id<CLLocationManagerDelegate> delegate |

CLLocationManagerDelegate.hAdded [-[CLLocationManagerDelegate locationManager:didChangeAuthorizationStatus:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423701-locationmanager)Added [-[CLLocationManagerDelegate locationManager:didEnterRegion:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423560-locationmanager)Added [-[CLLocationManagerDelegate locationManager:didExitRegion:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423630-locationmanager)Added [-[CLLocationManagerDelegate locationManager:monitoringDidFailForRegion:withError:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423720-locationmanager)CLRegion.hAdded [CLRegion](https://developer.apple.com/documentation/corelocation/clregion)Added [CLRegion.center](https://developer.apple.com/documentation/corelocation/clregion/1423691-center)Added [-[CLRegion containsCoordinate:]](https://developer.apple.com/documentation/corelocation/clregion/1423828-contains)Added [CLRegion.identifier](https://developer.apple.com/documentation/corelocation/clregion/1423583-identifier)Added [-[CLRegion initCircularRegionWithCenter:radius:identifier:]](https://developer.apple.com/documentation/corelocation/clregion/1423681-init)Added [CLRegion.radius](https://developer.apple.com/documentation/corelocation/clregion/1423730-radius)

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
