---
title: watchOS 2.1 API Diffs
apple_id: TP40016636
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2015-12-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS21APIDiffs/Swift/WatchConnectivity.html
archived_at: '2026-07-18T02:58:09.430852Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 2.1 API Diffs](watchOS%202.0%20to%20watchOS%202.1%20API%20Differences.md)


# WatchConnectivity Changes for Swift

### WatchConnectivity

Modified [WCErrorCode [enum]](https://developer.apple.com/documentation/watchconnectivity/wcerrorcode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [WCSession](https://developer.apple.com/documentation/watchconnectivity/wcsession)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WCSessionFile](https://developer.apple.com/documentation/watchconnectivity/wcsessionfile)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WCSessionFileTransfer](https://developer.apple.com/documentation/watchconnectivity/wcsessionfiletransfer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WCSessionUserInfoTransfer](https://developer.apple.com/documentation/watchconnectivity/wcsessionuserinfotransfer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WCSessionUserInfoTransfer : NSObject, NSSecureCoding, NSCoding {     var currentComplicationInfo: Bool { get }     var userInfo: [String : AnyObject] { get }     var transferring: Bool { get }     func cancel() } ``` | AnyObject, NSCoding, NSSecureCoding |
| To | ``` class WCSessionUserInfoTransfer : NSObject, NSSecureCoding {     var currentComplicationInfo: Bool { get }     var userInfo: [String : AnyObject] { get }     var transferring: Bool { get }     func cancel() } ``` | NSSecureCoding |

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
