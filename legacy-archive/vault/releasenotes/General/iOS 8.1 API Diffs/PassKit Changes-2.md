---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/PassKit.html
archived_at: '2026-07-18T02:56:15.658722Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# PassKit Changes

## PassKit

Removed PKAddressField.valueRemoved PKMerchantCapability.valueAdded PKAddressField.init(rawValue: UInt)Added PKMerchantCapability.init(rawValue: UInt)Modified PKAddPassesViewController

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified PKAddPassesViewController.init(pass: AnyObject!)

|  | Declaration |
| --- | --- |
| From | ``` init(pass pass: AnyObject!) ``` |
| To | ``` init!(pass pass: AnyObject!) ``` |

Modified PKAddPassesViewController.init(passes: [AnyObject]!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(passes passes: [AnyObject]!) ``` | iOS 8.0 |
| To | ``` init!(passes passes: [AnyObject]!) ``` | iOS 7.0 |

Modified PKAddressField [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PKAddressField : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var None: PKAddressField { get }     static var PostalAddress: PKAddressField { get }     static var Phone: PKAddressField { get }     static var Email: PKAddressField { get }     static var All: PKAddressField { get } } ``` |
| To | ``` struct PKAddressField : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: PKAddressField { get }     static var PostalAddress: PKAddressField { get }     static var Phone: PKAddressField { get }     static var Email: PKAddressField { get }     static var All: PKAddressField { get } } ``` |

Modified PKAddressField.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified PKMerchantCapability [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PKMerchantCapability : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var Capability3DS: PKMerchantCapability { get }     static var CapabilityEMV: PKMerchantCapability { get } } ``` |
| To | ``` struct PKMerchantCapability : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Capability3DS: PKMerchantCapability { get }     static var CapabilityEMV: PKMerchantCapability { get } } ``` |

Modified PKMerchantCapability.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified PKPass.init(data: NSData!, error: NSErrorPointer)

|  | Declaration |
| --- | --- |
| From | ``` init(data data: NSData!, error error: NSErrorPointer) ``` |
| To | ``` init!(data data: NSData!, error error: NSErrorPointer) ``` |

Modified PKPass.userInfo

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified PKPassKitErrorCode [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified PKPassLibrary

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified PKPassLibrary.addPasses([AnyObject]!, withCompletionHandler:((PKPassLibraryAddPassesStatus) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified PKPassLibraryAddPassesStatus [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified PKPaymentAuthorizationViewController.init(paymentRequest: PKPaymentRequest!)

|  | Declaration |
| --- | --- |
| From | ``` init(paymentRequest request: PKPaymentRequest!) ``` |
| To | ``` init!(paymentRequest request: PKPaymentRequest!) ``` |

Modified PKPaymentSummaryItem.init(label: String!, amount: NSDecimalNumber!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(label label: String!, amount amount: NSDecimalNumber!) ``` |
| To | ``` convenience init!(label label: String!, amount amount: NSDecimalNumber!) ``` |

Modified PKPassKitErrorDomain

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified PKPassLibraryAddedPassesUserInfoKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified PKPassLibraryDidChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified PKPassLibraryPassTypeIdentifierUserInfoKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified PKPassLibraryRemovedPassInfosUserInfoKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified PKPassLibraryReplacementPassesUserInfoKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified PKPassLibrarySerialNumberUserInfoKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

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
