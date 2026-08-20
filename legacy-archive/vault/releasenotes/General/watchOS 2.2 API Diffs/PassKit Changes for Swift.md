---
title: watchOS 2.2 API Diffs
apple_id: TP40016663
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS22APIDiffs/Swift/PassKit.html
archived_at: '2026-07-18T02:58:12.029463Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 2.2 API Diffs](watchOS%202.1%20to%20watchOS%202.2%20API%20Differences.md)


# PassKit Changes for Swift

### PassKit

Added [PKContact.supplementarySubLocality](https://developer.apple.com/documentation/passkit/pkcontact/1619227-supplementarysublocality)Added [PKPaymentNetworkChinaUnionPay](https://developer.apple.com/documentation/passkit/pkpaymentnetworkchinaunionpay)Modified [PKContact](https://developer.apple.com/documentation/passkit/pkcontact)

|  | Declaration |
| --- | --- |
| From | ``` class PKContact : NSObject {     var name: NSPersonNameComponents?     var postalAddress: CNPostalAddress?     var emailAddress: String?     var phoneNumber: CNPhoneNumber? } ``` |
| To | ``` class PKContact : NSObject {     var name: NSPersonNameComponents?     var postalAddress: CNPostalAddress?     var emailAddress: String?     var phoneNumber: CNPhoneNumber?     var supplementarySubLocality: String? } ``` |

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
