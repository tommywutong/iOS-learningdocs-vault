---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Swift/MultipeerConnectivity.html
archived_at: '2026-07-18T02:57:09.769074Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# MultipeerConnectivity Changes for Swift

### MultipeerConnectivity

Modified [MCAdvertiserAssistant](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MCBrowserViewController](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject, MCNearbyServiceBrowserDelegate, NSObjectProtocol |
| To | MCNearbyServiceBrowserDelegate |

Modified [MCEncryptionPreference [enum]](https://developer.apple.com/documentation/multipeerconnectivity/mcencryptionpreference)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MCErrorCode [enum]](https://developer.apple.com/documentation/multipeerconnectivity/mcerrorcode)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` enum MCErrorCode : Int {     case Unknown     case NotConnected     case InvalidParameter     case Unsupported     case TimedOut     case Cancelled     case Unavailable } extension MCErrorCode : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } extension MCErrorCode : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } ``` | Equatable, ErrorType, Hashable, RawRepresentable |
| To | ``` enum MCErrorCode : Int {     case Unknown     case NotConnected     case InvalidParameter     case Unsupported     case TimedOut     case Cancelled     case Unavailable } extension MCErrorCode : _BridgedNSError { } extension MCErrorCode : _BridgedNSError { } ``` | -- |

Modified [MCNearbyServiceAdvertiser](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MCNearbyServiceBrowser](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MCPeerID](https://developer.apple.com/documentation/multipeerconnectivity/mcpeerid)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MCPeerID : NSObject, NSCopying, NSSecureCoding, NSCoding {     init(displayName myDisplayName: String)     var displayName: String { get } } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class MCPeerID : NSObject, NSCopying, NSSecureCoding {     init(displayName myDisplayName: String)     var displayName: String { get } } ``` | NSCopying, NSSecureCoding |

Modified [MCSession](https://developer.apple.com/documentation/multipeerconnectivity/mcsession)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MCSessionSendDataMode [enum]](https://developer.apple.com/documentation/multipeerconnectivity/mcsessionsenddatamode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MCSessionState [enum]](https://developer.apple.com/documentation/multipeerconnectivity/mcsessionstate)

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
