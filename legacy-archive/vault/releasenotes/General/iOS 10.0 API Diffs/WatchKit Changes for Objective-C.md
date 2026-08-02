---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Objective-C/WatchKit.html
archived_at: '2026-07-18T02:55:00.188958Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# WatchKit Changes for Objective-C

### WatchKit

#### WKDefines.h

Added #def WK_DEPRECATED_WATCHOSAdded #def WK_DEPRECATED_WATCHOS_IOS

#### WKGestureRecognizer.h (Added)

Added WKGestureRecognizerStateAdded WKGestureRecognizerStateBeganAdded WKGestureRecognizerStateCancelledAdded WKGestureRecognizerStateChangedAdded WKGestureRecognizerStateEndedAdded WKGestureRecognizerStateFailedAdded WKGestureRecognizerStatePossibleAdded WKGestureRecognizerStateRecognizedAdded WKSwipeGestureRecognizerDirectionAdded WKSwipeGestureRecognizerDirectionDownAdded WKSwipeGestureRecognizerDirectionLeftAdded WKSwipeGestureRecognizerDirectionRightAdded WKSwipeGestureRecognizerDirectionUp

#### WKInterfaceController.h

Added [WKInterfaceController.crownSequencer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1648288-crownsequencer)Added [-[WKInterfaceController handleActionWithIdentifier:forNotification:]](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1648286-handleactionwithidentifier)Added [-[WKUserNotificationInterfaceController didReceiveNotification:withCompletion:]](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/1648287-didreceive)Modified [-[WKInterfaceController handleActionWithIdentifier:forLocalNotification:]](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619516-handleactionwithidentifier)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [-[WKInterfaceController handleActionWithIdentifier:forRemoteNotification:]](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619530-handleactionwithidentifier)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [-[WKUserNotificationInterfaceController didReceiveLocalNotification:withCompletion:]](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/1619534-didreceivelocalnotification)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [-[WKUserNotificationInterfaceController didReceiveRemoteNotification:withCompletion:]](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/1619568-didreceiveremotenotification)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

#### WKInterfaceDevice.h

Added [WKInterfaceDeviceCrownOrientation](https://developer.apple.com/documentation/watchkit/wkinterfacedevicecrownorientation)Added [WKInterfaceDeviceWristLocation](https://developer.apple.com/documentation/watchkit/wkinterfacedevicewristlocation)

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
