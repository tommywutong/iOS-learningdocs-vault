---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/PassKit.html
archived_at: '2026-07-18T02:56:27.176535Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# PassKit Changes

## PassKit

Added PKAddressField.NameAdded PKPassLibrary.openPaymentSetup()Added PKPaymentAuthorizationViewControllerDelegate.paymentAuthorizationViewControllerWillAuthorizePayment(PKPaymentAuthorizationViewController!)Added PKPaymentButtonAdded PKPaymentButton.init(type: PKPaymentButtonType, style: PKPaymentButtonStyle)Added PKPaymentButtonStyle [enum]Added PKPaymentButtonStyle.BlackAdded PKPaymentButtonStyle.WhiteAdded PKPaymentButtonStyle.WhiteOutlineAdded PKPaymentButtonType [enum]Added PKPaymentButtonType.BuyAdded PKPaymentButtonType.PlainAdded PKPaymentRequest.shippingTypeAdded PKShippingType [enum]Added PKShippingType.DeliveryAdded PKShippingType.ServicePickupAdded PKShippingType.ShippingAdded PKShippingType.StorePickupModified PKAddressField [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PKAddressField : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: PKAddressField { get }     static var PostalAddress: PKAddressField { get }     static var Phone: PKAddressField { get }     static var Email: PKAddressField { get }     static var All: PKAddressField { get } } ``` |
| To | ``` struct PKAddressField : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: PKAddressField { get }     static var PostalAddress: PKAddressField { get }     static var Phone: PKAddressField { get }     static var Email: PKAddressField { get }     static var Name: PKAddressField { get }     static var All: PKAddressField { get } } ``` |

Modified PKPassKitErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let PKPassKitErrorDomain: NSString! ``` |
| To | ``` let PKPassKitErrorDomain: String ``` |

Modified PKPassLibraryAddedPassesUserInfoKey

|  | Declaration |
| --- | --- |
| From | ``` let PKPassLibraryAddedPassesUserInfoKey: NSString! ``` |
| To | ``` let PKPassLibraryAddedPassesUserInfoKey: String ``` |

Modified PKPassLibraryDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let PKPassLibraryDidChangeNotification: NSString! ``` |
| To | ``` let PKPassLibraryDidChangeNotification: String ``` |

Modified PKPassLibraryPassTypeIdentifierUserInfoKey

|  | Declaration |
| --- | --- |
| From | ``` let PKPassLibraryPassTypeIdentifierUserInfoKey: NSString! ``` |
| To | ``` let PKPassLibraryPassTypeIdentifierUserInfoKey: String ``` |

Modified PKPassLibraryRemovedPassInfosUserInfoKey

|  | Declaration |
| --- | --- |
| From | ``` let PKPassLibraryRemovedPassInfosUserInfoKey: NSString! ``` |
| To | ``` let PKPassLibraryRemovedPassInfosUserInfoKey: String ``` |

Modified PKPassLibraryReplacementPassesUserInfoKey

|  | Declaration |
| --- | --- |
| From | ``` let PKPassLibraryReplacementPassesUserInfoKey: NSString! ``` |
| To | ``` let PKPassLibraryReplacementPassesUserInfoKey: String ``` |

Modified PKPassLibrarySerialNumberUserInfoKey

|  | Declaration |
| --- | --- |
| From | ``` let PKPassLibrarySerialNumberUserInfoKey: NSString! ``` |
| To | ``` let PKPassLibrarySerialNumberUserInfoKey: String ``` |

Modified PKPaymentNetworkAmex

|  | Declaration |
| --- | --- |
| From | ``` let PKPaymentNetworkAmex: NSString! ``` |
| To | ``` let PKPaymentNetworkAmex: String ``` |

Modified PKPaymentNetworkMasterCard

|  | Declaration |
| --- | --- |
| From | ``` let PKPaymentNetworkMasterCard: NSString! ``` |
| To | ``` let PKPaymentNetworkMasterCard: String ``` |

Modified PKPaymentNetworkVisa

|  | Declaration |
| --- | --- |
| From | ``` let PKPaymentNetworkVisa: NSString! ``` |
| To | ``` let PKPaymentNetworkVisa: String ``` |

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
