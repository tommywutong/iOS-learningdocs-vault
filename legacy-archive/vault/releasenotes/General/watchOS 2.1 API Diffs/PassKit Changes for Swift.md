---
title: watchOS 2.1 API Diffs
apple_id: TP40016636
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2015-12-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS21APIDiffs/Swift/PassKit.html
archived_at: '2026-07-18T02:58:09.137178Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 2.1 API Diffs](watchOS%202.0%20to%20watchOS%202.1%20API%20Differences.md)


# PassKit Changes for Swift

### PassKit

Modified [PKContact](https://developer.apple.com/documentation/passkit/pkcontact)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PKObject](https://developer.apple.com/documentation/passkit/pkobject)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PKPass](https://developer.apple.com/documentation/passkit/pkpass)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PKPassKitErrorCode [enum]](https://developer.apple.com/documentation/passkit/pkpasskiterrorcode)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` enum PKPassKitErrorCode : Int {     case UnknownError     case InvalidDataError     case UnsupportedVersionError     case InvalidSignature     case NotEntitledError } extension PKPassKitErrorCode : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } extension PKPassKitErrorCode : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } ``` | Equatable, ErrorType, Hashable, RawRepresentable |
| To | ``` enum PKPassKitErrorCode : Int {     case UnknownError     case InvalidDataError     case UnsupportedVersionError     case InvalidSignature     case NotEntitledError } extension PKPassKitErrorCode : _BridgedNSError { } extension PKPassKitErrorCode : _BridgedNSError { } ``` | -- |

Modified [PKPassLibrary](https://developer.apple.com/documentation/passkit/pkpasslibrary)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PKPassLibraryAddPassesStatus [enum]](https://developer.apple.com/documentation/passkit/pkpasslibraryaddpassesstatus)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [PKPassType [enum]](https://developer.apple.com/documentation/passkit/pkpasstype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [PKPaymentPass](https://developer.apple.com/documentation/passkit/pkpaymentpass)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PKPaymentPassActivationState [enum]](https://developer.apple.com/documentation/passkit/pkpaymentpassactivationstate)

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
