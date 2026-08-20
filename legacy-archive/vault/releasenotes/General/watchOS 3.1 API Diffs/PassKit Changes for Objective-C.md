---
title: watchOS 3.1 API Diffs
apple_id: TP40017546
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS31APIDiffs/Objective-C/PassKit.html
archived_at: '2026-07-18T02:58:37.801723Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 3.1 API Diffs](watchOS%203.0%20to%20watchOS%203.1%20API%20Differences.md)


# PassKit Changes for Objective-C

### PassKit

#### PKConstants.h

Added [PKPaymentButtonStyle](https://developer.apple.com/documentation/passkit/pkpaymentbuttonstyle)Added [PKPaymentButtonStyleBlack](https://developer.apple.com/documentation/passkit/pkpaymentbuttonstyle/pkpaymentbuttonstyleblack)Added [PKPaymentButtonStyleWhite](https://developer.apple.com/documentation/passkit/pkpaymentbuttonstyle/pkpaymentbuttonstylewhite)Added [PKPaymentButtonStyleWhiteOutline](https://developer.apple.com/documentation/passkit/pkpaymentbuttonstyle/pkpaymentbuttonstylewhiteoutline)Added [PKPaymentButtonType](https://developer.apple.com/documentation/passkit/pkpaymentbuttontype)Added [PKPaymentButtonTypeBuy](https://developer.apple.com/documentation/passkit/pkpaymentbuttontype/buy)Added [PKPaymentButtonTypeInStore](https://developer.apple.com/documentation/passkit/pkpaymentbuttontype/pkpaymentbuttontypeinstore)Added [PKPaymentButtonTypePlain](https://developer.apple.com/documentation/passkit/pkpaymentbuttontype/pkpaymentbuttontypeplain)Added [PKPaymentButtonTypeSetUp](https://developer.apple.com/documentation/passkit/pkpaymentbuttontype/pkpaymentbuttontypesetup)Added [PKPaymentNetworkJCB](https://developer.apple.com/documentation/passkit/pkpaymentnetworkjcb)Added [PKPaymentNetworkSuica](https://developer.apple.com/documentation/passkit/pkpaymentnetworksuica)

#### PKLabeledValue.h (Added)

Added [PKLabeledValue](https://developer.apple.com/documentation/passkit/pklabeledvalue)Added [-[PKLabeledValue initWithLabel:value:]](https://developer.apple.com/documentation/passkit/pklabeledvalue/2545237-initwithlabel)Added [PKLabeledValue.label](https://developer.apple.com/documentation/passkit/pklabeledvalue/2545240-label)Added [PKLabeledValue.value](https://developer.apple.com/documentation/passkit/pklabeledvalue/2545236-value)

#### PKPassLibrary.h

Added [-[PKPassLibrary canAddFelicaPass]](https://developer.apple.com/documentation/passkit/pkpasslibrary/2544959-canaddfelicapass)

#### PKSuicaPassProperties.h (Added)

Added [PKSuicaPassProperties](https://developer.apple.com/documentation/passkit/pksuicapassproperties)Added [PKSuicaPassProperties.blacklisted](https://developer.apple.com/documentation/passkit/pksuicapassproperties/2545174-isblacklisted)Added [PKSuicaPassProperties.greenCarTicketUsed](https://developer.apple.com/documentation/passkit/pksuicapassproperties/2545172-greencarticketused)Added [PKSuicaPassProperties.inShinkansenStation](https://developer.apple.com/documentation/passkit/pksuicapassproperties/2545170-isinshinkansenstation)Added [PKSuicaPassProperties.inStation](https://developer.apple.com/documentation/passkit/pksuicapassproperties/2545171-isinstation)Added [+[PKSuicaPassProperties passPropertiesForPass:]](https://developer.apple.com/documentation/passkit/pksuicapassproperties/2545173-init)Added [PKSuicaPassProperties.transitBalance](https://developer.apple.com/documentation/passkit/pksuicapassproperties/2545177-transitbalance)Added [PKSuicaPassProperties.transitBalanceCurrencyCode](https://developer.apple.com/documentation/passkit/pksuicapassproperties/2545175-transitbalancecurrencycode)

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
