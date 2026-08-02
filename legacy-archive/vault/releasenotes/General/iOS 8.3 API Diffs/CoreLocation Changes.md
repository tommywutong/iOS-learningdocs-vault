---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/CoreLocation.html
archived_at: '2026-07-18T02:56:22.921811Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# CoreLocation Changes

## CoreLocation

Added CLLocationCoordinate2D.init()Added CLLocationCoordinate2D.init(latitude: CLLocationDegrees, longitude: CLLocationDegrees)Modified CLAuthorizationStatus.AuthorizedAlways

|  | Introduction |
| --- | --- |
| From | iOS 8.2 |
| To | iOS 8.0 |

Modified CLLocationCoordinate2D [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CLLocationCoordinate2D {     var latitude: CLLocationDegrees     var longitude: CLLocationDegrees } ``` |
| To | ``` struct CLLocationCoordinate2D {     var latitude: CLLocationDegrees     var longitude: CLLocationDegrees     init()     init(latitude latitude: CLLocationDegrees, longitude longitude: CLLocationDegrees) } ``` |

Modified CLLocationManager.monitoredRegions

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var monitoredRegions: NSSet! { get } ``` |
| To | ``` var monitoredRegions: Set<NSObject>! { get } ``` |

Modified CLLocationManager.rangedRegions

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var rangedRegions: NSSet! { get } ``` |
| To | ``` var rangedRegions: Set<NSObject>! { get } ``` |

Modified kCLErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let kCLErrorDomain: NSString! ``` |
| To | ``` let kCLErrorDomain: String ``` |

Modified kCLErrorUserInfoAlternateRegionKey

|  | Declaration |
| --- | --- |
| From | ``` let kCLErrorUserInfoAlternateRegionKey: NSString! ``` |
| To | ``` let kCLErrorUserInfoAlternateRegionKey: String ``` |

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
