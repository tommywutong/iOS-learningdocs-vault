---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Swift/WatchKit.html
archived_at: '2026-07-18T02:57:11.836950Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# WatchKit Changes for Swift

### WatchKit

Modified [WatchKitErrorCode [enum]](https://developer.apple.com/documentation/watchkit/watchkiterror/code)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` enum WatchKitErrorCode : Int {     case UnknownError     case ApplicationDelegateWatchKitRequestReplyNotCalledError     case InvalidArgumentError     case MediaPlayerError     case DownloadError } extension WatchKitErrorCode : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } extension WatchKitErrorCode : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } ``` | Equatable, ErrorType, Hashable, RawRepresentable |
| To | ``` enum WatchKitErrorCode : Int {     case UnknownError     case ApplicationDelegateWatchKitRequestReplyNotCalledError     case InvalidArgumentError     case MediaPlayerError     case DownloadError } extension WatchKitErrorCode : _BridgedNSError { } extension WatchKitErrorCode : _BridgedNSError { } ``` | -- |

Modified [WKAccessibilityImageRegion](https://developer.apple.com/documentation/watchkit/wkaccessibilityimageregion)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKInterfaceButton](https://developer.apple.com/documentation/watchkit/wkinterfacebutton)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKInterfaceController](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKInterfaceDate](https://developer.apple.com/documentation/watchkit/wkinterfacedate)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKInterfaceDevice](https://developer.apple.com/documentation/watchkit/wkinterfacedevice)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKInterfaceGroup](https://developer.apple.com/documentation/watchkit/wkinterfacegroup)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSObjectProtocol, WKImageAnimatable |
| To | WKImageAnimatable |

Modified [WKInterfaceImage](https://developer.apple.com/documentation/watchkit/wkinterfaceimage)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSObjectProtocol, WKImageAnimatable |
| To | WKImageAnimatable |

Modified [WKInterfaceLabel](https://developer.apple.com/documentation/watchkit/wkinterfacelabel)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKInterfaceMap](https://developer.apple.com/documentation/watchkit/wkinterfacemap)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKInterfaceMapPinColor [enum]](https://developer.apple.com/documentation/watchkit/wkinterfacemappincolor)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [WKInterfaceObject](https://developer.apple.com/documentation/watchkit/wkinterfaceobject)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKInterfaceSeparator](https://developer.apple.com/documentation/watchkit/wkinterfaceseparator)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKInterfaceSlider](https://developer.apple.com/documentation/watchkit/wkinterfaceslider)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKInterfaceSwitch](https://developer.apple.com/documentation/watchkit/wkinterfaceswitch)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKInterfaceTable](https://developer.apple.com/documentation/watchkit/wkinterfacetable)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKInterfaceTimer](https://developer.apple.com/documentation/watchkit/wkinterfacetimer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKMenuItemIcon [enum]](https://developer.apple.com/documentation/watchkit/wkmenuitemicon)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [WKTextInputMode [enum]](https://developer.apple.com/documentation/watchkit/wktextinputmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [WKUserNotificationInterfaceController](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKUserNotificationInterfaceType [enum]](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacetype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

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
