---
title: OS X v10.9 API Diffs
apple_id: TP40013007
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_9/CoreLocation.html
archived_at: '2026-07-18T02:54:11.441279Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.9 API Diffs](OS%20X%20v10.8%20to%20OS%20X%20v10.9%20API%20Differences.md)


# CoreLocation Changes

## CoreLocation

CLError.hAdded [kCLErrorDeferredAccuracyTooLow](https://developer.apple.com/documentation/corelocation/clerror/code/deferredaccuracytoolow)Added [kCLErrorDeferredCanceled](https://developer.apple.com/documentation/corelocation/clerror/code/deferredcanceled)Added [kCLErrorDeferredDistanceFiltered](https://developer.apple.com/documentation/corelocation/clerror/kclerrordeferreddistancefiltered)Added [kCLErrorDeferredFailed](https://developer.apple.com/documentation/corelocation/clerror/code/deferredfailed)Added [kCLErrorDeferredNotUpdatingLocation](https://developer.apple.com/documentation/corelocation/clerror/kclerrordeferrednotupdatinglocation)CLLocation.hAdded [CLLocationDistanceMax](https://developer.apple.com/documentation/corelocation/cllocationdistancemax)Added [CLTimeIntervalMax](https://developer.apple.com/documentation/corelocation/cltimeintervalmax)CLLocationManager.hAdded [+[CLLocationManager deferredLocationUpdatesAvailable]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423830-deferredlocationupdatesavailable)Added [CLActivityType](https://developer.apple.com/documentation/corelocation/clactivitytype)Added [CLActivityTypeAutomotiveNavigation](https://developer.apple.com/documentation/corelocation/clactivitytype/clactivitytypeautomotivenavigation)Added [CLActivityTypeFitness](https://developer.apple.com/documentation/corelocation/clactivitytype/clactivitytypefitness)Added [CLActivityTypeOther](https://developer.apple.com/documentation/corelocation/clactivitytype/other)Added [CLActivityTypeOtherNavigation](https://developer.apple.com/documentation/corelocation/clactivitytype/othernavigation)Modified [+[CLLocationManager regionMonitoringEnabled]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423585-regionmonitoringenabled)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

CLLocationManagerDelegate.hAdded [-[CLLocationManagerDelegate locationManager:didFinishDeferredUpdatesWithError:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423537-locationmanager)Added [-[CLLocationManagerDelegate locationManager:didUpdateLocations:]](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423615-locationmanager)

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
