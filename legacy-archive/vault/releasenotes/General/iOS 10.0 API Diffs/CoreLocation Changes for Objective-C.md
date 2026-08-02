---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Objective-C/CoreLocation.html
archived_at: '2026-07-18T02:54:54.889817Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# CoreLocation Changes for Objective-C

### CoreLocation

#### CLBeaconRegion.h

Modified [CLBeacon.major](https://developer.apple.com/documentation/corelocation/clbeacon/1621418-major)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic, strong) NSNumber *major ``` |
| To | ``` @property(readonly, nonatomic, copy) NSNumber *major ``` |

Modified [CLBeacon.minor](https://developer.apple.com/documentation/corelocation/clbeacon/1621558-minor)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic, strong) NSNumber *minor ``` |
| To | ``` @property(readonly, nonatomic, copy) NSNumber *minor ``` |

Modified [CLBeacon.proximityUUID](https://developer.apple.com/documentation/corelocation/clbeacon/1621508-proximityuuid)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic, strong) NSUUID *proximityUUID ``` |
| To | ``` @property(readonly, nonatomic, copy) NSUUID *proximityUUID ``` |

Modified [CLBeaconRegion.major](https://developer.apple.com/documentation/corelocation/clbeaconregion/1621536-major)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic, strong) NSNumber *major ``` |
| To | ``` @property(readonly, nonatomic, copy) NSNumber *major ``` |

Modified [CLBeaconRegion.minor](https://developer.apple.com/documentation/corelocation/clbeaconregion/1621414-minor)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic, strong) NSNumber *minor ``` |
| To | ``` @property(readonly, nonatomic, copy) NSNumber *minor ``` |

Modified [CLBeaconRegion.proximityUUID](https://developer.apple.com/documentation/corelocation/clbeaconregion/1621556-proximityuuid)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic, strong) NSUUID *proximityUUID ``` |
| To | ``` @property(readonly, nonatomic, copy) NSUUID *proximityUUID ``` |

#### CLHeading.h

Removed CLHeading.description

#### CLLocation.h

Removed CLLocation.description

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
