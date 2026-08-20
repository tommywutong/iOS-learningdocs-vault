---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Swift/PassKit.html
archived_at: '2026-07-18T02:57:10.111452Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# PassKit Changes for Swift

### PassKit

Modified [PKAddPassButton](https://developer.apple.com/documentation/passkit/pkaddpassbutton)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PKAddPassButtonStyle [enum]](https://developer.apple.com/documentation/passkit/pkaddpassbuttonstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [PKAddPassesViewController](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PKAddPaymentPassError [enum]](https://developer.apple.com/documentation/passkit/pkaddpaymentpasserror)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [PKAddPaymentPassRequest](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequest)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PKAddPaymentPassRequestConfiguration](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequestconfiguration)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PKAddPaymentPassViewController](https://developer.apple.com/documentation/passkit/pkaddpaymentpassviewcontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PKAutomaticPassPresentationSuppressionResult [enum]](https://developer.apple.com/documentation/passkit/pkautomaticpasspresentationsuppressionresult)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

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

Modified [PKPayment](https://developer.apple.com/documentation/passkit/pkpayment)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PKPaymentAuthorizationStatus [enum]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [PKPaymentAuthorizationViewController](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PKPaymentButton](https://developer.apple.com/documentation/passkit/pkpaymentbutton)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PKPaymentButtonStyle [enum]](https://developer.apple.com/documentation/passkit/pkpaymentbuttonstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [PKPaymentButtonType [enum]](https://developer.apple.com/documentation/passkit/pkpaymentbuttontype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [PKPaymentMethod](https://developer.apple.com/documentation/passkit/pkpaymentmethod)

|  | Protocols |
| --- | --- |
| From | AnyObject |
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

Modified [PKPaymentRequest](https://developer.apple.com/documentation/passkit/pkpaymentrequest)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PKPaymentSummaryItem](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitem)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PKPaymentSummaryItemType [enum]](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitemtype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [PKPaymentToken](https://developer.apple.com/documentation/passkit/pkpaymenttoken)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PKShippingMethod](https://developer.apple.com/documentation/passkit/pkshippingmethod)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [PKShippingType [enum]](https://developer.apple.com/documentation/passkit/pkshippingtype)

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
