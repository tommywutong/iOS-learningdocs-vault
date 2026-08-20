---
title: OS X v10.8 API Diffs
apple_id: TP40011748
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_8/CoreLocation.html
archived_at: '2026-07-18T02:53:58.419665Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.8 API Diffs](OS%20X%20v10.7%20to%20OS%20X%20v10.8%20API%20Differences.md)


# CoreLocation Changes

## CoreLocation

CLAvailability.hAdded #def CL_EXTERNCLError.hAdded [kCLErrorGeocodeFoundPartialResult](https://developer.apple.com/documentation/corelocation/clerror/kclerrorgeocodefoundpartialresult)Added [kCLErrorRegionMonitoringResponseDelayed](https://developer.apple.com/documentation/corelocation/clerror/code/regionmonitoringresponsedelayed)Added [kCLErrorUserInfoAlternateRegionKey](https://developer.apple.com/documentation/corelocation/kclerroruserinfoalternateregionkey)CLGeocoder.hAdded [CLGeocoder](https://developer.apple.com/documentation/corelocation/clgeocoder)Added [-[CLGeocoder cancelGeocode]](https://developer.apple.com/documentation/corelocation/clgeocoder/1423562-cancelgeocode)Added [-[CLGeocoder geocodeAddressDictionary:completionHandler:]](https://developer.apple.com/documentation/corelocation/clgeocoder/1423693-geocodeaddressdictionary)Added [-[CLGeocoder geocodeAddressString:completionHandler:]](https://developer.apple.com/documentation/corelocation/clgeocoder/1423509-geocodeaddressstring)Added [-[CLGeocoder geocodeAddressString:inRegion:completionHandler:]](https://developer.apple.com/documentation/corelocation/clgeocoder/1423591-geocodeaddressstring)Added [CLGeocoder.geocoding](https://developer.apple.com/documentation/corelocation/clgeocoder/1423765-geocoding)Added [-[CLGeocoder reverseGeocodeLocation:completionHandler:]](https://developer.apple.com/documentation/corelocation/clgeocoder/1423621-reversegeocodelocation)Added [CLGeocodeCompletionHandler](https://developer.apple.com/documentation/corelocation/clgeocodecompletionhandler)CLLocationManager.hRemoved [-[CLLocationManager startMonitoringForRegion:desiredAccuracy:]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1620560-startmonitoringforregion)Added [-[CLLocationManager startMonitoringForRegion:]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423656-startmonitoringforregion)CLLocationManagerDelegate.hAdded [-[CLLocationManagerDelegate locationManager:didStartMonitoringForRegion:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423842-locationmanager)CLPlacemark.hAdded [CLPlacemark](https://developer.apple.com/documentation/corelocation/clplacemark)Added [CLPlacemark.ISOcountryCode](https://developer.apple.com/documentation/corelocation/clplacemark/1423796-isocountrycode)Added [CLPlacemark.addressDictionary](https://developer.apple.com/documentation/corelocation/clplacemark/1423605-addressdictionary)Added [CLPlacemark.administrativeArea](https://developer.apple.com/documentation/corelocation/clplacemark/1423628-administrativearea)Added [CLPlacemark.areasOfInterest](https://developer.apple.com/documentation/corelocation/clplacemark/1423673-areasofinterest)Added [CLPlacemark.country](https://developer.apple.com/documentation/corelocation/clplacemark/1423800-country)Added [-[CLPlacemark initWithPlacemark:]](https://developer.apple.com/documentation/corelocation/clplacemark/1423818-init)Added [CLPlacemark.inlandWater](https://developer.apple.com/documentation/corelocation/clplacemark/1423738-inlandwater)Added [CLPlacemark.locality](https://developer.apple.com/documentation/corelocation/clplacemark/1423507-locality)Added [CLPlacemark.location](https://developer.apple.com/documentation/corelocation/clplacemark/1423603-location)Added [CLPlacemark.name](https://developer.apple.com/documentation/corelocation/clplacemark/1423634-name)Added [CLPlacemark.ocean](https://developer.apple.com/documentation/corelocation/clplacemark/1423619-ocean)Added [CLPlacemark.postalCode](https://developer.apple.com/documentation/corelocation/clplacemark/1423851-postalcode)Added [CLPlacemark.region](https://developer.apple.com/documentation/corelocation/clplacemark/1423808-region)Added [CLPlacemark.subAdministrativeArea](https://developer.apple.com/documentation/corelocation/clplacemark/1423776-subadministrativearea)Added [CLPlacemark.subLocality](https://developer.apple.com/documentation/corelocation/clplacemark/1423794-sublocality)Added [CLPlacemark.subThoroughfare](https://developer.apple.com/documentation/corelocation/clplacemark/1423782-subthoroughfare)Added [CLPlacemark.thoroughfare](https://developer.apple.com/documentation/corelocation/clplacemark/1423814-thoroughfare)

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
